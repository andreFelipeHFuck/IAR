import time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from tqdm import tqdm


import PSO
from utils.graphics import create_con_graph, create_box_plots

def std_func(func):
     if func == PSO.Func.Griewank:
         return "Griewank"
     else:
         return "Ackley"

def experiment_one_PSO(
        problem: str,
        num_iteration: int,
        num_iteration_in_pso:int,
        n: int,
        dim: int,
        func: PSO.Func,
        c: np.float64,
        w: np.float64,
        k: bool,
        show: bool
    ):
        
    solutions_res_func_list = []
    res_func_list: list[np.float64] = []
    
    best_solution = 1_000_000
    
    init = time.perf_counter()
    
    for _ in range(num_iteration):
        _, solutions_res_func, res_func, _ = PSO.pso(
            num_iteration_in_pso,
            n,
            dim,
            func,
            c,
            w,
            k
        )
        
        solutions_res_func_list.append(solutions_res_func)
        
        if solutions_res_func < best_solution:
            best_solution = solutions_res_func
            res_func_list = res_func.copy()
                        
    end = time.perf_counter()
            
    name: str = f"con-F{std_func(func)}-P{n}-DIM{dim}-{time.time_ns()}.png"  
    create_con_graph(
        title="Gráfico de Convergência do PSO",
        xlabel="",
        ylabel="",
        ax_label="",
        name=f"images/PSO/{name}",
        list_x=[i for i in range(0, num_iteration_in_pso)],
        list_y=res_func_list,
        show=show
    )
    
    average = sum(solutions_res_func_list) / len(solutions_res_func_list)
    std = np.std(solutions_res_func_list)
    
    return problem, num_iteration_in_pso, n, dim, std_func(func), c, w, k, best_solution, solutions_res_func_list, average, std, (end - init), name
    
def experiment( problem: str,
        num_iteration: int,
        num_iteration_in_pso:int,
        n: int,
        dim: int,
        func_list: PSO.Func,
        c: np.float64,
        w: np.float64,
        k_list: list[bool],
        show: bool):
    
    pbar = tqdm(total=len(func_list) * len(k_list), desc="Loading")
    
    d = {
        "Problema": [],
        "Melhor Solução": [],
        "Média": [],
        "Desvio Padrão": [],
        "Tempo (s)": [],
        "Imagem": []
    }
    
    print(num_iteration)
    
    for f in func_list:
        box_plots_list = []
        for k in k_list:
            res = experiment_one_PSO(
                problem=problem,
                num_iteration=num_iteration,
                num_iteration_in_pso=num_iteration_in_pso,
                n=n,
                dim=dim,
                func=f,
                c=c,
                w=w,
                k=k,
                show=show
            )
            
            d["Problema"].append(res[0])
            d["Melhor Solução"].append(res[8]),
            d['Média'].append(res[10])
            d["Desvio Padrão"].append(res[11])
            d["Tempo (s)"].append(res[12])
            d["Imagem"].append(res[13])
            
            box_plots_list.append(res[9])
            
            pbar.update(1)
            
        
        name: str = f"box-P{problem}-F{std_func(f)}-P{n}-DIM{dim}-{time.time_ns()}.png"
        
        create_box_plots(
            name=f"images/PSO/{name}",
            ylabel="Solução Mínima Global",
            labels=["Peso de Inércia", "Fator de Constrição"],
            weights=box_plots_list
        )
    
    pbar.close()
    
    df = pd.DataFrame(d)
    df.to_csv(f"logs/result-{problem}-{time.time_ns()}.csv")
    
    return df