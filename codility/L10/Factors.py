# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(N):
    # Implement your solution here
    factors =0
    for i in range(1,math.ceil(math.sqrt(N))):
        if N % i == 0:
            factors += 2
    if math.sqrt(N) == math.ceil(math.sqrt(N)):
        factors += 1
    return factors
print(solution(1))