import csv
import itertools

import numpy as np

from utils import cooling
from utils import graphics

from utils.manipulationFile import read_cnf_file, write_csv_file
from utils.Clauses import Clauses
from utils.Literals import Literals

from simulatedAnnealing import simulatedAnnealing, generate_T0_average, generate_T0_simulated

RESULTS_CSV: str = "log/results.csv"
RESULTS_BLOX_PLOTS_CSV: str = "log/results_box_plots.csv"
RESULTS_BLOX_AVERAGE_STANDARD_DERIVATION = "log/results_average_standard_deviation.csv" 


LIST_SA_MAX: list[int] = [1, 5, 10]
LIST_N: list[int] = [1_000, 10_000, 100_000]

LIST_T0 = [100.0, 200.0, generate_T0_average, generate_T0_simulated]
LIST_TN: int = [0.1, 0.001, 0.000_1]

LIST_ALPHA = [
    cooling.cooling_schedule_0,
    cooling.cooling_schedule_1,
    cooling.cooling_schedule_2,
    cooling.cooling_schedule_3,
    cooling.cooling_schedule_4,
    cooling.cooling_schedule_5,
    cooling.cooling_schedule_6,
    cooling.cooling_schedule_7,
    cooling.cooling_schedule_8,
    cooling.cooling_schedule_9
]

LIST_LITERALS: list[str] = [
    "uf20-01.cnf",
    "uf100-01.cnf",
    "uf250-01.cnf"
]

DICT_LITERALS: dict[str, int] = {
    20: "uf20-01.cnf",
    100: "uf100-01.cnf",
    250: "uf250-01.cnf"
}

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
    
    write_csv_file(RESULTS_CSV, [formula, LIST_SA_MAX[sa_max], LIST_N[n], T0, LIST_TN[tn],alpha, cooling.equations[alpha], best_solution ])

    write_csv_file(RESULTS_BLOX_PLOTS_CSV, [f"SA_MAX {LIST_SA_MAX[sa_max]}"] + solutions)    
    
    average = sum(solutions) / len(solutions)
    std = np.std(solutions)
    
    write_csv_file(RESULTS_BLOX_AVERAGE_STANDARD_DERIVATION, [f"SA_MAX {LIST_SA_MAX[sa_max]}"] + [average, std])
    
    graphics.create_plot(image_name, best_list_interation, best_list_values, best_list_temperature, alpha)
    
    
def execute_experiments() -> None:
    experiments = list(itertools.product(
        [i for i in range(0, len(LIST_SA_MAX))], 
        [i for i in range(0, len(LIST_N))], 
        [i for i in range(0, len(LIST_T0))], 
        [i for i in range(0, len(LIST_TN))], 
        [i for i in range(0, len(LIST_ALPHA))]
    ))
    
    for i in experiments:
        experiment(20, i[0], i[1], i[2], i[3], i[4])