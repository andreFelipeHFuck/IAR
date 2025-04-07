from .cooling import equations

import matplotlib.pyplot as plt 

def create_plot(list_interation: list[int], list_values: list[int], list_temperature: list[int], eq: int = 0) -> None:    
    fig, ax = plt.subplots()
    
    color = 'tab:blue'
    
    ax.plot(list_interation, list_values, linewidth=2, label=equations[eq])
    ax.set(
            xlim=(0, len(list_interation)), 
            ylim=(0, max(list_values)),
            xlabel="Iterações", 
            ylabel="Número de Cláusulas Falsas",
        )
    ax.set_ylabel("Número de Cláusulas Falsas", color=color)
    
    
    ax.grid(True, linestyle='-.')
    ax.set_title("Gráfico de Convergência do Simulated Annealing para 3-SAT", fontsize="10")
    
    ax.tick_params(labelcolor='black', width=3)
    ax.tick_params(axis='y', labelcolor=color)
    ax.legend(fontsize=14)
    
    ax2 = ax.twinx()
    
    color = 'tab:red'
    
    ax2.set_ylabel("Temperatura", color=color)
    ax2.plot(list_interation, list_temperature, linewidth=2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    
    fig.tight_layout()
    
    plt.show()