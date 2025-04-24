import logging
from sys import exit
from random import sample, randint

from utils.calculations import Point
from .PermutedList import *

class SolutionTSP:
    def __init__(self, num_elements: int) -> None:
        self._num_elements: int = num_elements
        self._distance: float = 0
        self._elements: PermutedList = None
        
        self._log: logging = logging.basicConfig(level=logging.INFO)
    
    def get_index(self, index: int) -> int:
        return self._elements.get_element(index)
    
    def get_num_elements(self) -> int:
        return self._num_elements
    
    def get_distance(self) -> float:
        return float(self._distance)
    
    def get_elements(self) -> PermutedList:
        return self._elements
    
    def set_distance(self, distance: int) -> None:
        self._distance = distance
    
    def set_elements(self, elements: PermutedList) -> None:
        if self._num_elements == elements.get_num_elements():
            self._elements = elements
        else: 
            raise Exception("The number of PermutedLis elements must be equal to the number of elements")

    def get_list_pair_elems(self) -> list[Point]:
        return self._elements.list_pair_elems()

    def generate_random_elements(self) -> None:
        self._elements = PermutedList.generate_random_list(self._num_elements)
        
    def swap_element(self, index: int) -> None:
        self._elements.swap_elems(index)
    
    def generate_neighbor(self, num_neighbors=1) -> 'SolutionTSP':
        neighbor: SolutionTSP = SolutionTSP(self._num_elements)
        neighbor.set_elements(PermutedList(self._elements.list_elems()))
        
        num_random_index_changed:int = randint(1, num_neighbors)
        
        for i in sample([k for k in range(0, self._num_elements)], num_random_index_changed):
            try:
                neighbor.swap_element(i)
            except PermutedListSwapIndexException as e:
                self._log.error(F"Error: {str(e)}")
                exit(1)
            
        return neighbor
                
    def __str__(self) -> str:
         return  f"num_elements: {self._num_elements}\ndistance: {self._distance}\nelements: {self._elements}\n"
    
    def __repr__(self):
        return  f"num_elements: {self._num_elements}\ndistance: {self._distance}\nelements: {self._elements}\n"

    
if __name__ == "__main__":
    s: SolutionTSP = SolutionTSP(10)
    s.generate_random_elements()
    
    print(s)