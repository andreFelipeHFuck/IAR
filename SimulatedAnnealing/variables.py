from utils import cooling
from simulatedAnnealing import generate_T0_average


RESULTS_CSV: str = "logs/results.csv"
RESULTS_BLOX_PLOTS_CSV: str = "logs/results_box_plots"
RESULTS_BLOX_AVERAGE_STANDARD_DERIVATION = "logs/results_average_standard_deviation" 


LIST_SA_MAX: list[int] = [1, 5, 10]
LIST_N: list[int] = [1_000, 10_000, 500_000]

LIST_T0 = [100.0, generate_T0_average]
LIST_TN: int = [0.1, 0.001, 5]

LIST_ALPHA = [
    cooling.cooling_schedule_0,
    cooling.cooling_schedule_1,
    cooling.cooling_schedule_2,
    cooling.cooling_schedule_3,
    cooling.cooling_schedule_4,
    cooling.cooling_schedule_5,
    cooling.cooling_schedule_6,
    cooling.cooling_schedule_7,
    cooling.cooling_schedule_8,
    cooling.cooling_schedule_9
]

LIST_LITERALS: list[str] = [
    "uf20-01.cnf",
    "uf100-01.cnf",
    "uf250-01.cnf"
]

DICT_LITERALS: dict[str, int] = {
    20: "uf20-01.cnf",
    100: "uf100-01.cnf",
    250: "uf250-01.cnf"
}