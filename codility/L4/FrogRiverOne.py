# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X: int, A: list) -> int:
    # Implement your solution here
    # (X + 1, not X)
    # N = len(A)
    # A: Leaves falling
    # A[K], at second K, position A[K] had a leaf fall on it

    # we want X + 1, not just X
    # create this dictionary
    last_add = 1
    lake = dict.fromkeys([i for i in range(1, X + 1)])  # inits with none
    for time in range(len(A)):
        if lake[A[time]] == None:
            lake[A[time]] = True
            last_add = time
    if None in lake.values():
        return -1
    else:
        return last_add

    pass
