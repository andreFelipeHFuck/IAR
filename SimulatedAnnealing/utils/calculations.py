from math import sqrt
from typing import Tuple 

Point = Tuple[int, int]

def euclidean_distance(a: Point, b: Point) -> float:
    return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)