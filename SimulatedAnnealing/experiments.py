

from utils import readCnfFile
from utils import cooling
from utils import graphics


LIST_SA_MAX: list[int] = [1, 5, 10, 15, 20, 25, 30]
LIST_N: list[int] = [1_000, 10_000, 50_000, 100_000]
LIST_LITERALS: list[str] = [
    "uf20-01.cnf",
    "uf100-01.cnf",
    "uf250-01.cnf"
]

TN: int = 0.000_1

