from .cooling import equations

import matplotlib.pyplot as plt 

def create_plot(
        name: str, 
        title: str = 'Gráfico de Convergência do Simulated Annealing para 3-SAT',
        xlabel: str = 'Iterações',
        ylabel: str = 'Número de Cláusulas Falsas',
        ax_label: str = 'Cláusulas Falsas',
        ax2_label: str = 'Temperatura',
        list_interation: list[int] = [], 
        list_values: list[int] = [], 
        list_temperature: list[int] = [], 
        eq: int = 0
        
    ) -> None:    
    fig, ax = plt.subplots()
    ax2 = ax.twinx()
    
    color_ax = 'tab:blue'
    color_ax2 = 'tab:red'
    
    ax.grid(True, linestyle='-.')
    ax.set_title(title, fontsize='10')
    
    ax.plot(list_interation, list_values, linewidth=2, color=color_ax, label=ax_label)
    ax2.plot(list_interation, list_temperature, linewidth=2, color=color_ax2, label='\n'.join(equations[eq].split(',')))
    
    ax.set(
            xlim=(0, len(list_interation)), 
            ylim=(min(list_values), max(list_values)),
            xlabel=xlabel, 
            ylabel=ylabel,
        )
    ax.set_ylabel(ylabel, color=color_ax)
    
    ax.tick_params(labelcolor='black', width=3)
    ax.tick_params(axis='y', labelcolor=color_ax)
    
    lines, labels = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc=0)
    
    
    ax2.set_ylabel(ax2_label, color=color_ax2)
    ax2.tick_params(axis='y', labelcolor=color_ax2)
    
    fig.tight_layout()
    
    plt.savefig(f"{name}", format='png')
    plt.show()
    plt.close()
    
def create_box_plots(
    name: str, 
    ylabel: str = 'Número de Cláusulas Falsas',
    labels: list[str] = [], 
    weights: list[list[int]] = []
    ) -> None:
    
    fig, ax = plt.subplots()
        
    ax.set_ylabel(ylabel)
    
    bplot = ax.boxplot(
        weights,
        patch_artist=True,
        tick_labels=labels
    )
        
    plt.savefig(f"{name}", format='png')
    plt.show()
    plt.close()
