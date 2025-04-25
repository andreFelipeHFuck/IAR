import time
import numpy as np
import pandas as pd

from SA.simulatedAnnealing import simulatedAnnealing
from problems.TSP.SimulatedAnnelingOperationsTSP import SimulatedAnnelingOperationsTSP as TSP

from utils.calculations import Point
from utils.manipulationFile import read_txt_file
import utils.cooling as alpha
from utils.graphics import create_plot, create_box_plots

from tqdm import tqdm

def experiment_one_SA(problem: str, 
                      path: str, 
                      num_interation: int, 
                      num_neighbors_mod: int,  
                      num_neighbors: int, 
                      SA_max: int, 
                      eq: int, 
                      TN: int, 
                      N: int, 
                      t: int,
                      show: bool, 
                      bar: bool) -> None:
    
    init = time.perf_counter()
    eq_dict = {
        0: alpha.cooling_schedule_0,
        1: alpha.cooling_schedule_1,
        2: alpha.cooling_schedule_2,
        3: alpha.cooling_schedule_3,
        4: alpha.cooling_schedule_4,
        5: alpha.cooling_schedule_5,
        6: alpha.cooling_schedule_6,
        7: alpha.cooling_schedule_7,
        8: alpha.cooling_schedule_8,
        9: alpha.cooling_schedule_9,
        10: alpha.cooling_schedule_10
    }
    
    solutions: list[int] = []
    
    dataset: dict = {}
    
    best_solution: int = 1_000_000
    best_list_interation: list[int]
    best_list_values: list[int]
    best_list_temperature: list[int]
    
    points: list[Point] = read_txt_file(path)

    tsp_t0: TSP = TSP(points, num_neighbors_mod)
    T0: float = tsp_t0.generate_T0_average(num_neighbors)
    print(T0)
    
    for _ in range(0, num_interation):
        tsp: TSP = TSP(points, num_neighbors_mod)
        
        solution, list_interation, list_values, list_temperature = simulatedAnnealing(
            problem=tsp,
            alpha=eq_dict[eq],
            SA_max=SA_max,
            T0=T0,
            TN=TN,
            N=N,
            t=t,
            bar=bar
        )
        
        solutions.append(solution.get_distance())
                
        if solution.get_distance() < best_solution:
            best_solution = solution.get_distance()
            best_list_interation = list_interation.copy()
            best_list_values = list_values.copy()
            best_list_temperature = list_temperature.copy()
    
    name: str = f"con-P{problem}-SA{SA_max}-EQ{eq}-N{N}-{time.time_ns()}.png"
    create_plot(
            title="Gráfico de Convergência do Simulated Anneling para TSP",
            xlabel="Interações",
            ylabel="Distância Percorrida",
            ax_label="Distância Percorrida",
            name=f"images/TSP/{name}",
            list_interation=best_list_interation,
            list_values=best_list_values,
            list_temperature=best_list_temperature,
            eq=eq,
            show=show
    )
    
    average = sum(solutions) / len(solutions)
    std = np.std(solutions)
    end = time.perf_counter()
    
    print(tsp.best_solution())
    return problem, SA_max, eq, num_neighbors_mod,  N, T0, best_solution, average, std, (end -init), name, solutions
    
def experiment(problem: str, 
               path: str, 
               num_interation: int, 
               num_neighbors_mod_list: list[int],  
               num_neighbors: int, 
               SA_max_list: list[int], 
               eq_list: list[int], 
               TN: int, 
               N: int,
               t: int, 
               show: bool = False, 
               bar: bool = False) -> object:
    
    pbar = tqdm(total=len(num_neighbors_mod_list) * len(eq_list) * len(SA_max_list), desc="Loading")

    d = {
        "Problema": [],
        "SA_max": [],
        "Equação": [],
        "Número de Vizinhos": [],
        "Número de Interações": [],
        "Temperatura Inicial": [],
        "Melhor Solução": [],
        "Média": [],
        "Desvio Padrão": [],
        "Tempo (s)": [],
        "Imagem": []
    }

    for n in num_neighbors_mod_list:
        for eq in eq_list:
            box_plots_list: list[list[int]] = []
            for sa in SA_max_list:
                
                res = experiment_one_SA(
                    problem=problem,
                    path=path,
                    num_interation=num_interation,
                    num_neighbors_mod=n,
                    num_neighbors=num_neighbors,
                    SA_max=sa,
                    eq=eq,
                    TN=TN,
                    N=N,
                    t=t,
                    show=show,
                    bar=bar
                )

                d["Problema"].append(res[0])
                d["SA_max"].append(res[1])
                d["Equação"].append(res[2])
                d["Número de Vizinhos"].append(res[3])
                d["Número de Interações"].append(res[4])
                d["Temperatura Inicial"].append(res[5])
                d["Melhor Solução"].append(res[6])
                d["Média"].append(res[7])
                d["Desvio Padrão"].append(res[8])
                d["Tempo (s)"].append(res[9])
                d["Imagem"].append(res[10])
            
                box_plots_list.append(res[11])
                
                pbar.update(1)

                
            name: str = f"box-P{problem}-SA{sa}-EQ{eq}-N{N}-{time.time_ns()}.png"

            create_box_plots(
                name=f"images/TSP/{name}",
                ylabel="Distância Mínima",
                labels=["SA_1", "SA_5", "SA_10"],
                weights=box_plots_list
            )
            
            
    pbar.close()

    df = pd.DataFrame(d)
    df.to_csv(f"logs/result-{problem}-{time.time_ns()}.csv")
    
    
    return df