import time
import PSO
import numpy as np

import matplotlib.pyplot as plt 

def create_con_graph(
    name: str,
    title: str,
    xlabel: str,
    ylabel: str,
    ax_label: str,
    list_x,
    list_y,
    show: bool = False
    ):
    
    fig, ax = plt.subplots()
    color_ax = 'tab:blue'

    
    ax.grid(True, linestyle='-.')
    ax.set_title(title, fontsize='10')
    
    ax.plot(list_x, list_y, linewidth=2, color=color_ax, label=ax_label)
    
    ax.set(
            xlim=(0, len(list_x)), 
            ylim=(min(list_y), max(list_y)),
            xlabel=xlabel, 
            ylabel=ylabel,
        )
    ax.set_ylabel(ylabel, color=color_ax)

    plt.savefig(f"{name}", format='png')
    if show:
        plt.show()
    plt.close()
    

def experiment_one_PSO(
        num_iteration: int,
        num_iteration_in_pso:int,
        n: int,
        dim: int,
        func: PSO.Func,
        w: np.float64,
        k: bool,
        show: bool
    ) -> None:
    
    
    dataset: dict = {}
    
    solutions: list[tuple[np.float64, np.float64]] = []
    
    best_solution: tuple[np.float64, np.float64] = (1_000_000, 1_000_000)
    res_func_list: list[np.float64] = []
    get_x_list: list[tuple[np.float64, np.float64]] = []
    
    init = time.perf_counter()
    
    for _ in range(num_iteration):
        solution, res_func, get_x = PSO.pso(
            num_iteration_in_pso,
            n,
            dim,
            func,
            w,
            k
        )
        
        solutions.append(solution)
        
        if solution[0] < best_solution[0] and solution[1] < best_solution[1]:
            best_solution = solution
            res_func_list = res_func.copy()
            get_x_list = get_x.copy()
            
    end = time.perf_counter()
            
    name: str = f"con-P{n}-DIM{dim}-{time.time_ns()}.png"  
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
    
