from experiments import experiment
from utils.manipulationFile import read_csv_file
from utils.graphics import create_box_plots


    
if __name__ == '__main__':
    # experiment(20, 0, 0, 2, 2, 2)
    # experiment(20, 1, 0, 2, 2, 2)
    # experiment(20, 2, 0, 2, 2, 2)

    res = read_csv_file("results_box_plots.csv")
    
    labels = [i[0] for i in res]
    weights = [[int(j) for j  in i[1]] for i in res]
    
    create_box_plots("teste_box_plots", labels, weights)
