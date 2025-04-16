import numpy as np
import numpy.typing as npt

from calculations import Point, euclidean_distance

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
    
    
        
        
    def __str__(self) -> str:
        pass
    
if __name__ == "__main__":
    m: MatrixTSP = MatrixTSP([(1, 2), (4, 5)])
