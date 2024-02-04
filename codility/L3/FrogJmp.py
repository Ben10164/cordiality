# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math


def solution(X, Y, D):
    # Implement your solution here
    delta = Y - X

    jumps = math.ceil(delta / D)
    return jumps
