from statsAuxiliary.aggregate import aggregate
from calculator.division import division


def general_mean(a):
    b = division(aggregate(a), len(a))
    return b

