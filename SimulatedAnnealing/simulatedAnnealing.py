from typing import Callable

from math import e
from random import random


from utils import Literals
from utils import Clauses


def generate_T0_average(clauses: Clauses, num_literals: int, num_neighbors: int) -> float:
    l = Literals(num_literals)
    l.generate_random_literals()
    
    clauses.cont_clauses_falses(l, [i for i in range(0, l.get_num_literals())])
    
    best_neighbor = 0
    list_neighbor = [l.generate_neighbor() for i in range(0, num_neighbors)]
    
    for n in list_neighbor:
        clauses.calcule_delta_between_neighbors(l, n[0], n[1])
        
        if n[0].get_num_clauses_falses() > best_neighbor:
            best_neighbor = n[0].get_num_clauses_falses()
            
    return float(best_neighbor)

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

def simulatedAnnealing(clauses: Clauses, alpha: Callable[[float, float, int, int] ,float], SA_max: int, T0: float, TN: float, N: int, s: Literals) -> tuple[Literals, list[int], list[int], list[int]]:
    list_interation = []
    list_values = []
    list_temperature = []
    
    i: int = 0
    
    best_solution: Literals = s
    
    best_solution_cache: int = s.get_num_clauses_falses()
        
    inter_T: int = 0
    T: float = T0
    
    # while best_solution.get_num_clauses_falses() > 0 and T > TN:
    
    while i < N:
            
        best_solution_local: int = s.get_num_clauses_falses()
        while inter_T < SA_max:

            inter_T += 1
            
            n, list_i = s.generate_neighbor()
            
            delta: int  = clauses.calcule_delta_between_neighbors(s, n, list_i)
                        
            if delta < 0:
                s = n
                
                if n.get_num_clauses_falses() < best_solution.get_num_clauses_falses():
                    best_solution = n
                    
            else:
                x: float = random()
                               
                if x < e ** (-delta / T):
                    s = n
                    
            if s.get_num_clauses_falses() < best_solution_local:
                best_solution_local = s.get_num_clauses_falses()
                T = alpha(T0, TN, i, N)
        
        list_interation.append(i)
        list_values.append(best_solution_local)
        list_temperature.append(T)
        
        inter_T = 0
        i += 1
        
        if best_solution.get_num_clauses_falses() < best_solution_cache:
            print(f"T: {T}, i: {i},  Best Solution: {best_solution.get_num_clauses_falses()}")
            best_solution_cache = best_solution.get_num_clauses_falses() 
        
        
        
    print(f"\nBest Solution: {best_solution.get_num_clauses_falses()}\n")  
    
    return best_solution, list_interation, list_values, list_temperature
    
    