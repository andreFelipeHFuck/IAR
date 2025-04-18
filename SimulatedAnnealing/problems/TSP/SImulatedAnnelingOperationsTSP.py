from utils.calculations import Point

from MatrixTSP import MatrixTSP
from SolutionTSP import SolutionTSP
from interfaces.ISimulatedAnnealingOperations import ISimulatedAnnelingOperations

class SImulatedAnnelingOperationsTSP(ISimulatedAnnelingOperations):
    def __init__(self, points: list[Point] ):
        self._matrix: MatrixTSP = MatrixTSP(points)
        self._solution: SolutionTSP = SolutionTSP(len(points))
        self._best_solution: SolutionTSP = self._solution
        self._neighbor: SolutionTSP = None
        
        self._solution.generate_random_elements()
        self._matrix.calcule_distance(self._solution)
        
        super().__init__()
    def best_solution(self) -> SolutionTSP:
        return self._solution
    
    def get_best_solution(self) -> float:
        return self._solution.get_distance()
    
    def generate_neighbor(self) -> None:
        self._neighbor = self._solution.generate_neighbor()
        
    def calcule_delta_solution_with_neighbor(self) -> float:
        return self._matrix.calcule_delta_between_neighbors(self._solution, self._neighbor)
    
    def compare_solution_compare_best_solution_with_neighbor(self) -> bool:
        return self._neighbor.get_distance() < self._best_solution.get_distance()
    
    def exchange_solution_for_neighbor(self) -> None:
        self._solution = self._neighbor
        self._neighbor = None
        
    def exchange_best_solution_for_neighbor(self) -> None:
        self._best_solution = self._neighbor
        self._neighbor = None