"""
    Read .cnf files and make  representations for Clauses
"""

import os 

from pysat.formula import CNF

def readCnfFile(path: str) -> tuple[int, list[list[int]]]:
    sat = CNF(from_file=f"./samples/{path}")            
    return sat.nv, list(filter(lambda c: len(c) == 3, sat.clauses))