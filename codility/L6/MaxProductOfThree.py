# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


# O(N * log(N))
def solution(A):
    # Implement your solution here
    A.sort()
    pos_max = A[-3] * A[-2] * A[-1]
    # in the event that there are negatives
    neg_max = A[0] * A[1] * A[-1]
    return max(pos_max, neg_max)
