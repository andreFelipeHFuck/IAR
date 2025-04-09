"""
    Read .cnf files and make  representations for Clauses
"""

import csv


from pysat.formula import CNF

def read_cnf_file(path: str) -> tuple[int, list[list[int]]]:
    sat = CNF(from_file=f"./samples/{path}")            
    return sat.nv, list(filter(lambda c: len(c) == 3, sat.clauses))

def write_csv_file(path: str, row: list[str]) -> None:
    with open(path, mode='a', newline='') as file:
        csv_write = csv.writer(file)
        csv_write.writerow(row)
        
def read_csv_file(path: str) -> list[(str, list[int])]:
    res = []
    with open(path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            res.append((row[0], row[1:]))
            
    return res