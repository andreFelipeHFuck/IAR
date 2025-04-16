from experiments import experiment
from utils.manipulationFile import read_csv_file
from utils.graphics import create_box_plots

from variables import *

if __name__ == '__main__':
    
    # for v in [20]:
    #     results_box_plots = experiment(v, sa_max=0, n=0, t0=1, tn=2, alpha=1)
    #     experiment(v, sa_max=1, n=0, t0=1, tn=2, alpha=1)
    #     experiment(v, sa_max=2, n=0, t0=1, tn=2, alpha=1)

    #     res = read_csv_file(results_box_plots)
        
    #     labels = [i[0] for i in res]
    #     weights = [[int(j) for j  in i[1]] for i in res]
        
    #     create_box_plots(f"results_box_plots-form{v}", labels, weights)
            

    for v in [20]:
    
            # experiment(v, sa_max=0, n=0, t0=1, tn=2, alpha=1)
            # # results_box_plots = experiment(v, sa_max=1, n=2, t0=1, tn=2, alpha=1)
            # #experiment(v, sa_max=2, n=2, t0=1, tn=2, alpha=1)

            res = read_csv_file("logs/results_box_plots-form100.csv")
        
            labels = [i[0] for i in res]
            weights = [[int(j) for j  in i[1]] for i in res]
        
            create_box_plots(f"results_box_plots-form{v}", labels, weights)
