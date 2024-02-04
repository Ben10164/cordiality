# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A: list, K: int) -> list:
    # rotate A, K times to the right
    # Implement your solution here
    if A == []:
        return A
    for i in range(K):
        # save the end
        end = A[-1]
        # trim A
        A = A[:-1]
        A.insert(0, end)
    return A
