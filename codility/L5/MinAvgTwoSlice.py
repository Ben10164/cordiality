# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://www.youtube.com/watch?v=Xu_hTjFAauk


def solution(A):
    mn = max(A) * 2
    mi = 0
    for i in range(0, len(A) - 2):
        v1 = (A[i] + A[i + 1] + A[i + 2]) / 3
        v2 = (A[i] + A[i + 1]) / 2
        if mn > v1 or mn > v2:
            mn = min(v1, v2)
            mi = i
    if mn > (A[-1] + A[-2]) / 2:
        return len(A) - 2
    return mi
