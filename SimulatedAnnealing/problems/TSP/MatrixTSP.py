import numpy as np
import numpy.typing as npt
import pandas as pd

from .SolutionTSP import SolutionTSP

from utils.calculations import Point, euclidean_distance

class MatrixTSP:
    def __init__(self, points: list[Point]):
        self._num_instances: int = len(points)
        self._points: list[Point] = points
        self._matrix: npt.NDArray[np.float64] = self.__make_matrix()
        
    def __make_matrix(self) ->  npt.NDArray[np.float64]:
        matrix: npt.NDArray[np.float64] = np.zeros((self._num_instances, self._num_instances))

        for i in range(0, self._num_instances):
            for j in range(0, self._num_instances):     
                if i <= j:
                    continue
                
                matrix[i][j] = euclidean_distance(self._points[i], self._points[j])
                
        return matrix
    
    def __get_value_matrix(self, point: tuple[int, int]) -> int:
        i, j = point
        
        if j == i:
            return 0
        elif j > i:
            return self._matrix[j][i]
        else:
            return self._matrix[i][j]
    
    def calcule_distance(self, solutionTSP: SolutionTSP) -> None:
        list_pair_elems: list[(int, int)] = solutionTSP.get_list_pair_elems()
                
        distance: int = sum([self.__get_value_matrix(i) for i in list_pair_elems])
        
        solutionTSP.set_distance(distance)
    
    def calcule_delta_between_neighbors(self, solutionTSP: SolutionTSP, solutionTSP_neighbors: SolutionTSP) -> float:
        
        self.calcule_distance(solutionTSP_neighbors)
        
        return solutionTSP_neighbors.get_distance() - solutionTSP.get_distance()
    
    def print_matrix(self) -> pd.DataFrame:
        return pd.DataFrame(self._matrix)

    
    def __str__(self) -> str:
        df = pd.DataFrame(self._matrix)
        return f"Número de Instâncias: {self._num_instances}\nMatriz: {self._matrix}"
        
    def __repr__(self):
        df = pd.DataFrame(self._matrix)
        return f"Número de Instâncias: {self._num_instances}\nMatrix: {self._matrix}"
            
        
if __name__ == "__main__":
    from manipulationFile import read_txt_file
    
    file: str = read_txt_file("../samples/eil51.txt")
    
    m: MatrixTSP = MatrixTSP([(1, 2), (4, 5)])
    print(m)