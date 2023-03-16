import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(list)
    arr = arr.reshape(3, 3)

    # metrics
    mean = [
        arr.mean(axis=0).tolist(),
        arr.mean(axis=1).tolist(),
        arr.mean().tolist()
    ]
    var = [
        arr.var(axis=0).tolist(),
        arr.var(axis=1).tolist(),
        arr.var().tolist()
    ]
    std = [
        arr.std(axis=0).tolist(),
        arr.std(axis=1).tolist(),
        arr.std().tolist()
    ]
    maximum = [
        arr.max(axis=0).tolist(),
        arr.max(axis=1).tolist(),
        arr.max().tolist()
    ]
    minimum = [
        arr.min(axis=0).tolist(),
        arr.min(axis=1).tolist(),
        arr.min().tolist()
    ]
    sum_ = [
        arr.sum(axis=0).tolist(),
        arr.sum(axis=1).tolist(),
        arr.sum().tolist()
    ]

    # dictionary
    calculations = {}
    calculations["mean"] = mean
    calculations["variance"] = var
    calculations["standard deviation"] = std
    calculations["max"] = maximum
    calculations["min"] = minimum
    calculations["sum"] = sum_

    return calculations
