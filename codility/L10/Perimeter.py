# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math
def solution(N):
    # Implement your solution here
    # area is N
    factors_below_sqrt = []
    i = 1
    while i <= math.sqrt(N):
        if N % i == 0:
            factors_below_sqrt.append(i)
        i += 1 

    max_factor_below_sqrt = factors_below_sqrt[-1]
    l = max_factor_below_sqrt
    w = N / l
    return int(2 * (w + l))

print(solution(30))