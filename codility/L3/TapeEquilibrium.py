# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A: list):
    # Implement your solution here
    left = A[0]
    right = sum(A[1:])
    min_diff = abs(left - right)
    for i in range(1, len(A) - 1):
        left += A[i]
        right -= A[i]
        diff = abs(left - right)
        if diff < min_diff:
            min_diff = diff
    return min_diff
