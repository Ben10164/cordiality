# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # Implement your solution here
    A_set = set(A)
    if len(A) == len(A_set):
        # no dupes
        if max(A_set) == len(A_set):
            return 1
        else:
            return 0
    else:
        return 0
