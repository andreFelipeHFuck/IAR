"""
    Represents the set of existing literals (variables)
"""

from random import random, sample
from math import ceil

class Literals:
    def __init__(self, num_literals: int) -> None:
        self._num_literals: int = num_literals
        self._num_clauses_falses: int = 0
        self._literals: list[bool] = [True for i in range(0, num_literals)]
        
    def get_index(self, index: int) -> bool:
        return self._literals[index]
    
    def get_num_literals(self) -> int:
        return self._num_literals
    
    def get_num_clauses_falses(self) -> int:
        return self._num_clauses_falses
    
    def get_literals(self) -> list[bool]:
        return self._literals
    
    def set_num_clauses_falses(self, num_clauses_falses: int) -> None:
        self._num_clauses_falses = num_clauses_falses
    
    def set_literals(self, literals: list[bool]) -> None:
        if len(literals) == self._num_literals:
            self._literals = literals
        else:
            raise Exception("The number of array elements must be equal to the number of literals")
            
    def neg_index(self, index: int) -> None:
        self._literals[index] = not self._literals[index]
        
    def generate_random_literals(self) -> None:
        for i in range(0, len(self._literals)):
            if random() > 0.5:
                self._literals[i] = True
            else:
                self._literals[i] = False
                
    def generate_neighbor(self, percen_num_reachead: float = 0.01) -> tuple['Literals', list[int]]:
        neighbor = Literals(self._num_literals)
        neighbor.set_literals(self._literals.copy())
        
        num_elem_reached: int = ceil(self._num_literals * percen_num_reachead)
        
        list_random_index: list[int] = sample([i for i in range(0, self._num_literals - 1,)], num_elem_reached)
                
        for i in list_random_index:        
            neighbor.neg_index(i)
                        
        return neighbor, list_random_index
                
    def __str__(self):
        res = f"num_literals: {self._num_literals}\nnum_clauses_falses: {self._num_clauses_falses}\nliterals: {self._literals}\n"
            
        return res
        
    
        
