# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A: list):
    # Implement your solution here

    # obvious solution
    A = sorted(A)
    # go until you reach a number that is not its index
    i = 0
    for i in range(1, len(A) + 1):
        # print(i)
        if A[i - 1] != i:
            return i
    return i + 1
