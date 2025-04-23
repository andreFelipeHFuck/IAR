from typing import Callable

from math import e
from random import random

from problems.SAT.Clauses import Clauses
from problems.SAT.Literals import Literals

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

def simulatedAnnealing(problem: ISA, alpha: Callable[[float, float, int, int] ,float], SA_max: int, T0: float, TN: float, N: int) -> tuple[list[int], list[int], list[int]]:
    list_interation = []
    list_values = []
    list_temperature = []
    
    i: int = 0
    
    # best_solution: Literals = s
    
    # best_solution_cache: int = s.get_num_clauses_falses()
        
    inter_T: int = 0
    T: float = T0
    
    # while best_solution.get_num_clauses_falses() > 0 and T > TN:
    
    while i < N:            
        # best_solution_local: int = s.get_num_clauses_falses()
        while inter_T < SA_max:

            inter_T += 1
            
            # n, list_i = s.generate_neighbor()
            problem.generate_neighbor()
            
            # delta: int  = clauses.calcule_delta_between_neighbors(s, n, list_i)
            delta: float = problem.calcule_delta_solution_with_neighbor()
                        
            if delta < 0:
                # s = n                
                problem.exchange_solution_for_neighbor()
                
                # if n.get_num_clauses_falses() < best_solution.get_num_clauses_falses():
                #     best_solution = n
                if problem.compare_best_solution_with_neighbor():
                    problem.exchange_best_solution_for_neighbor()
                    
            else:
                x: float = random()
                               
                if x < e ** (-delta / T):
                    # s = n
                    problem.exchange_solution_for_neighbor()
                
            T = alpha(T0, TN, i, N)
        # print(i, T, problem.get_solution())
        
        list_interation.append(i)
        list_values.append(problem.get_solution())
        list_temperature.append(T)
        
        inter_T = 0
        i += 1
        
        # if best_solution.get_num_clauses_falses() < best_solution_cache:
        #     print(f"T: {T}, i: {i},  Best Solution: {best_solution.get_num_clauses_falses()}")
        #     best_solution_cache = best_solution.get_num_clauses_falses() 
        
        
        
    # print(f"\nBest Solution: {best_solution.get_num_clauses_falses()}\n")  
    
    return problem.best_solution(), list_interation, list_values, list_temperature
    
    