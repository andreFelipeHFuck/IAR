""""
    Cooling Schedule 
"""

from math import log, e, pi, cos, tanh, cosh

equations = {
    0: r"$T_i =  T_0 - i \frac{T_0 - T_N}{N}$",   
    1: r"$T_i =  T_0 \left( \frac{T_N}{T_0}  \right) ^\frac{i}{N}$",
    2: r'''
        $T_i = \frac{A}{i + 1} + B$
        $A = \frac{(T_0 - T_N) (N + 1)}{N}$
        $B = T_0 - A$
    ''',
    3: r'''
        $T_i = T_0 - i ^ A$
        $A = \frac{\ln(T_0 - T_N)}{\ln(N)}$
    ''',
    4: r'''
        $T_i = \frac{T_0 - T_N}{1 + e ^ {3(i - \frac{N}{2})}} + T_N$
    ''',
    5: r'''
        $T_i = \frac{1}{2}(T_0 - T_N)(1 + \cos(\frac{i\pi}{N})) + T_N $
    ''',
    6: r'''
        $T_i = \frac{1}{2}(T_0 - T_N)(1 - \tanh(\frac{10i}{N} - 5)) + T_N$
    ''',
    7: r'''
        $T_i = \frac{(T_0 - T_N)}{\cosh(\frac{10i}{N})} + T_N$ 
    ''',
    8: r'''
        $T_i = T_0e ^{-Ai}$
        $A = \frac{1}{N} + \ln(\frac{T_0}{T_N})$
    ''',
    9: r'''
    $T_i = T_0e ^{-Ai^2}$
    $A = (\frac{1}{N ^ 2})\ln(\frac{T_0}{T_N})$
    '''
}

def cooling_schedule_0(T0: float, TN: float, i: int, N: int) -> float:
    Ti = T0 - i * ((T0 - TN) / N)
    
    if Ti == 0:
        return TN
    return Ti

def cooling_schedule_1(T0: float, TN: float, i: int, N: int) -> float:
    return T0 * (TN / T0) ** (i / N)

def cooling_schedule_2(T0: float, TN: float, i: int, N: int) -> float:
    A = ((T0 - TN) * (N + 1)) / N
    B = T0 - A
    
    return A / (i + 1) + B

def cooling_schedule_3(T0: float, TN: float, i: int, N: int) -> float:
    A = log(T0 - TN) / log(N)
    
    return T0 - i ** A

def cooling_schedule_4(T0: float, TN: float, i: int, N: int) -> float:
    return ((T0 - TN) / (1 + e ** (3 * (i - N / 2)))) + TN

def cooling_schedule_5(T0: float, TN: float, i: int, N: int) -> float:
    return 0.5 * (T0 - TN) * (1 + cos((i * pi) / N)) + TN

def cooling_schedule_6(T0: float, TN: float, i: int, N: int) -> float:
    return 1/2 * (T0 - TN) * (1 - tanh((10 * i) / N) - 5) + TN

def cooling_schedule_7(T0: float, TN: float, i: int, N: int) -> float:
    return ((T0 - TN) / cosh((10 * i) / N)) + TN

def cooling_schedule_8(T0: float, TN: float, i: int, N: int) -> float:
    A = (1 / N) * log(T0 / TN)
    
    return T0 * e ** (-A * i)

def cooling_schedule_9(T0: float, TN: float, i: int, N: int) -> float:
    A = (1 / (N ** 2)) * log(T0 / TN)
    
    return T0 * e ** (-A * i ** 2) 