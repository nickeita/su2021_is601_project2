from generalStatistics.generalMean import general_mean
from statsAuxiliary.aggregate import aggregate


def variance_input(a):
    b = []
    c = []
    for i in range(len(a)):
        b.append(a[i] - general_mean(a))
        c.append(b[i] ** 2)
    d = aggregate(c)
    return d
