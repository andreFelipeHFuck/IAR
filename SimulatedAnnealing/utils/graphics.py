from .cooling import equations

import matplotlib.pyplot as plt 

def create_plot(name: str, list_interation: list[int], list_values: list[int], list_temperature: list[int], eq: int = 0) -> None:    
    fig, ax = plt.subplots()
    
    color = 'tab:blue'
    
    ax.plot(list_interation, list_values, linewidth=2, label='\n'.join(equations[eq].split(',')))
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
    
    plt.savefig(f"images/{name}", format='png')
    plt.close()
    
def create_box_plots(name: str, labels: list[str], weights: list[list[int]]) -> None:
    fig, ax = plt.subplots()
    
    colors = ['peachpuff', 'orange', 'tomato']
    
    ax.set_ylabel('Número de Cláusulas Falsas')
    
    bplot = ax.boxplot(
        weights,
        patch_artist=True,
        tick_labels=labels
    )
    
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
        
    plt.savefig(f"images/{name}", format='png')
    plt.close()
