import math

def square_root(x: float) -> float:
    # TODO - you fill in here.
    start, end = (0, 1.0) if x < 1.0 else (1.0, x)
    while not math.isclose(start, end):
        mid = start + (end - start)/2.0
        mid_squared = mid*mid
        if mid_squared > x:
            end = mid
        else:
            start = mid
    return start