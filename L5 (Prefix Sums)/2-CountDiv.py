# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A: int, B: int, K: int) -> int:
    # Implement your solution here
    # basic sol
    num_div = 0
    starting = A
    # find first occurrence
    for i in range(A, B+1): # needs to be inclusive
        if i % K == 0:
            num_div = 1
            starting = i
            break
    num_div += ((B - starting) // K)
    
    return num_div