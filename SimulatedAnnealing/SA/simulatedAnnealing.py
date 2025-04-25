from typing import Callable

from math import e
from random import random

from tqdm import tqdm

from problems.SAT.Clauses import Clauses
from problems.SAT.Literals import Literals

from utils.cooling import cooling_schedule_10

from interfaces.ISimulatedAnnealingOperations import ISimulatedAnnelingOperations as ISA

def generate_T0_simulated(clauses: Clauses, num_literals: int, SA_max: int, T0: float, acceptance_rate: float) -> float:
    num_neighbor_acceptances = 0
    
    l = Literals(num_literals)
    l.generate_random_literals()
    
    clauses.cont_clauses_falses(l, [i for i in range(0, l.get_num_literals())])
    
    while True:
        for i in range(0, SA_max):
            n, list_i = l.generate_neighbor()
            clauses.calcule_delta_between_neighbors(l, n, list_i)
            
            delta: int  = clauses.calcule_delta_between_neighbors(l, n, list_i)

            x: float = random()
            
            print((delta))
            print(T0)
            print(-delta / T0)
            if x < e ** (-delta / T0):
                num_neighbor_acceptances += 1
            
        if (num_neighbor_acceptances / SA_max) >= acceptance_rate:
            break
        else:
            T0 += 0.1 * T0
        
        num_neighbor_acceptances = 0
        
    return T0

def simulatedAnnealing(problem: ISA, 
                       alpha: Callable[[float, float, int, int] ,float] | Callable[[int, int, int], float], 
                       SA_max: int, 
                       T0: float, 
                       TN: float, 
                       N: int, 
                       t: int = 1,
                       bar: bool=False) -> tuple[list[int], list[int], list[int]]:
    if bar:
        pbar = tqdm(total=N, desc="Loading")
    
    list_interation = []
    list_values = []
    list_temperature = []
    
    i: int = 0
        
    inter_T: int = 0
    T: float = T0
        
    while i < N:            
        while inter_T < SA_max:

            inter_T += 1
            
            problem.generate_neighbor()
            
            delta: float = problem.calcule_delta_solution_with_neighbor()
                        
            if delta < 0:
                problem.exchange_solution_for_neighbor()
                
        
                if problem.compare_best_solution_with_neighbor():
                    problem.exchange_best_solution_for_neighbor()
                    
            else:
                x: float = random()
                               
                if x < e ** (-delta / T):
                    problem.exchange_solution_for_neighbor()
            
            if alpha == cooling_schedule_10:
                T = alpha(i, N, t)
            else:
                T = alpha(T0, TN, i, N)
        
        list_interation.append(i)
        list_values.append(problem.get_solution())
        list_temperature.append(T)
        
        inter_T = 0
        i += 1
        
        if bar:
            pbar.update(1)
        
    if bar:    
        pbar.close()
        
        
    return problem.best_solution(), list_interation, list_values, list_temperature
    
    