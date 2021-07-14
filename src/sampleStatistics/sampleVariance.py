from statsAuxiliary.varianceInput import variance_input


def sample_variance(a):
    return variance_input(a) / (len(a) - 1)


