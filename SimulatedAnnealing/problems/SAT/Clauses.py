
"""
    Data structure representing all conjectures present in Conjunctive Normal Form
"""

from typing import Dict
 
from .Literals import Literals

class Clause:
    def __init__(self, values: list[int]) -> None: 
        self._clause: list[tuple[int, bool]] = [(abs(i) - 1, i < 0) for i in values]
        
    def __calcule_literal(self, literals: Literals, index: int) -> bool:
        i: int = self._clause[index][0]
                
        if self._clause[index][1]:
            return not literals.get_index(i)
        return literals.get_index(i)
    
    def get_value(self, index) -> int:
        return self._clause[index][0]
    
    def calcule_clause(self, literals: Literals) -> bool:
        return self.__calcule_literal(literals, 0) or self.__calcule_literal(literals, 1) or self.__calcule_literal(literals, 2)
    
    def __str__(self):
        res: str = ""
        for k, v in self._clause:
            res += f"{k} -> {v} \n"
            
        return res
    
class Clauses:
    def __init__(self, num_literal: int, clauses: list[list[int]]) -> None:
        self._clauses = [Clause(i) for i in clauses]
        self._num_literal: int = num_literal
        self._dict_clauses = self.__make_dict()
    
    def __make_dict(self) -> Dict[int, list[int]]:
        d: Dict[int, int] = {i:[] for i in range(self._num_literal)}
        
        for i in range(0, len(self._clauses)):     
                       
                d[abs(self._clauses[i].get_value(0))].append(i)
                d[abs(self._clauses[i].get_value(1))].append(i)
                d[abs(self._clauses[i].get_value(2))].append(i)

        return d
    
    def __get_all_clauses_from_index(self, index: int) -> list[Clause]:
        return self._dict_clauses[index]
    
    def get_all_clauses_from_list_index(self, list_indexs: list[int]) -> list[Clause]:
        res_set: set[Clause] = set()
        
        for i in list_indexs:            
            for c in self.__get_all_clauses_from_index(i):
                res_set.add(c)
            
        return list(res_set)
    
    def calcule_all_clauses_falses(self, literals: Literals) -> None:
        num_clauses_falses = 0
        
        for c in self._clauses:
            if not c.calcule_clause(literals):
                num_clauses_falses += 1
                
        literals.set_num_clauses_falses(num_clauses_falses)
                 
    def cont_clauses_falses(self, literals: Literals, list_index: list[int]) -> None:
        cont: int = 0
        list_clauses = self.get_all_clauses_from_list_index(list_index)
                
        for c in list_clauses:
            if not self._clauses[c].calcule_clause(literals):
                cont += 1
                
        literals.set_num_clauses_falses(cont)
        
    def calcule_delta_between_neighbors(self, literals: Literals, literals_neighbors: Literals, literals_neighbors_list_index: list[int]) -> int:
        literals_neighbors_cont: int = 0
                
        literals_list_neighbors_clauses = self.get_all_clauses_from_list_index(literals_neighbors_list_index)
        
        for c in literals_list_neighbors_clauses:
            if self._clauses[c].calcule_clause(literals) and not self._clauses[c].calcule_clause(literals_neighbors):
                literals_neighbors_cont += 1
            elif not self._clauses[c].calcule_clause(literals) and self._clauses[c].calcule_clause(literals_neighbors):
                literals_neighbors_cont -= 1

        literals_neighbors.set_num_clauses_falses(literals.get_num_clauses_falses() + literals_neighbors_cont)
        
        return literals_neighbors.get_num_clauses_falses() - literals.get_num_clauses_falses()
        
    def __str__(self):
        res: str = ""
        
        for k, v in self._dict_clauses.items():
            res += f"{k} -> {v} \n"
            
        return res
    
    
if __name__ == "__main__":
    literals = Literals(4)
    literals.set_literals([True, False, True, True])
    
    print(literals)
    
    clauses = Clauses(4, [[1, -2, 3], [2, -3, 4], [-4, 2, -1]])
    
    clauses.cont_clauses_falses(literals, [2])
    
    print(literals.get_num_clauses_falses())
    