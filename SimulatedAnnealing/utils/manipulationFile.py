"""


    Read .cnf files and make representations for Clauses
"""

import csv

from pysat.formula import CNF

from calculations import Point

def read_cnf_file(path: str) -> tuple[int, list[list[int]]]:
    sat = CNF(from_file=f"./samples/{path}")            
    return sat.nv, list(filter(lambda c: len(c) == 3, sat.clauses))

        
def read_csv_file(path: str) -> list[(str, list[int])]:
    res = []
    with open(path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            res.append((row[0], row[1:]))
            
    return res

def write_csv_file(path: str, row: list[str]) -> None:
    with open(path, mode='a', newline='') as file:
        csv_write = csv.writer(file)
        csv_write.writerow(row)
        
def read_txt_file(path: str) -> list[Point]:
    res: list[Point] = []
    
    with open(path, mode='r') as file:
        while True:
            line = file.readline()
            
            if "EOF" in line:
                break
            
            values = line.split("\n")[0].split(" ")
            res.append((int(values[1]), int(values[2])))
    
    return res
     

if __name__ == "__main__":
    PATH: str = "../samples/eil100.txt"
    print(read_txt_file(PATH))