from abc import ABC, abstractmethod

class ISimulatedAnnelingOperations(ABC):
    @abstractmethod
    def solution(self) -> object:
        pass
    
    @abstractmethod
    def get_solution(self) -> float:
        pass
    
    @abstractmethod
    def best_solution(self) -> object:
        pass
    
    @abstractmethod
    def get_best_solution(self) -> float:
        pass
    
    @abstractmethod
    def generate_neighbor(self) -> None:
        pass
    
    @abstractmethod
    def calcule_delta_solution_with_neighbor(self) -> float:
        pass
    
    @abstractmethod
    def compare_best_solution_with_neighbor(self) -> bool:
        pass
    
    @abstractmethod
    def exchange_solution_for_neighbor(self) -> None:
        pass
    
    @abstractmethod
    def exchange_best_solution_for_neighbor(self) -> None:
        pass