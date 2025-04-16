import itertools

import numpy as np

from utils import cooling
from utils import graphics

from utils.manipulationFile import read_cnf_file, write_csv_file, read_csv_file
from utils.Clauses import Clauses
from utils.Literals import Literals

from simulatedAnnealing import simulatedAnnealing, generate_T0_average, generate_T0_simulated

from variables import *

def generate_literal(n_lit: int) -> Literals:
    l: Literals = Literals(n_lit)
    l.generate_random_literals()

    return l

def generate_T0(t0: int, sa_max: int, n: int,  clauses: Clauses, n_lit: int) -> float:
    T0: float
    if LIST_T0[t0] is generate_T0_average:
        T0 = generate_T0_average(clauses, n_lit, LIST_N[n])
        print(T0)
    elif LIST_T0[t0] is generate_T0_simulated:
        T0 = generate_T0_simulated(clauses, n_lit, LIST_SA_MAX[sa_max], 0.01, 0.95)
        print(T0)
    else:
        T0 = LIST_T0[t0]
        
    if type(T0) == float:
        return T0
    
    print(T0)
    print(f"T0 não é um número, é um {type(T0)}")

def experiment(formula: int=20, sa_max: int=0, n: int=0, t0:int=0, tn:int=0, alpha:int=0) -> None:
    solutions: list[int] = []
    best_solution: int = 1_000
    best_list_interation: list[int]
    best_list_values: list[int]
    best_list_temperature: list[int]
    
    n_lit: int
    c_list: list[int] 
    T0: float
    
    n_lit, c_list = read_cnf_file(path=DICT_LITERALS[formula])
    clauses: Clauses = Clauses(n_lit, c_list)
    T0 = generate_T0(t0, sa_max, n, clauses, n_lit)
    
    for _ in range(0, 30):
        l: Literals = generate_literal(n_lit)
        clauses.calcule_all_clauses_falses(l)
        
        
        solution, list_interation, list_values, list_temperature = simulatedAnnealing(clauses, LIST_ALPHA[alpha], LIST_SA_MAX[sa_max], T0, LIST_TN[tn], LIST_N[n], l)

        solutions.append(solution.get_num_clauses_falses())
        
        if solution.get_num_clauses_falses() < best_solution:
            best_solution = solution.get_num_clauses_falses()
            best_list_interation = list_interation.copy()
            best_list_values = list_values.copy()
            best_list_temperature = list_temperature.copy()
            
    image_name: str = f"result-form{formula}-saMax{LIST_SA_MAX[sa_max]}-N{LIST_N[n]}-T0{T0}-TN{LIST_TN[tn]}-EQ{alpha}.png"
    
    average = sum(solutions) / len(solutions)
    std = np.std(solutions)
    
    write_csv_file(RESULTS_CSV, [formula, LIST_SA_MAX[sa_max], LIST_N[n], T0, LIST_TN[tn],alpha, cooling.equations[alpha], average, std ,best_solution ])

    blox_plot_file: str = f"{RESULTS_BLOX_PLOTS_CSV}-form{formula}.csv"
    write_csv_file(blox_plot_file, [f"SA_MAX {LIST_SA_MAX[sa_max]}"] + solutions)    
    
        
    graphics.create_plot(image_name, best_list_interation, best_list_values, best_list_temperature, alpha)
    
    return blox_plot_file
    