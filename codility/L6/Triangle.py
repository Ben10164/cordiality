# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A: list) -> int:
    # Implement your solution here
    # p, q, r are in order of appearance (doesnt have to be consecutive)
    # (the sum of any 2 items must be greater than the other)
    # a[p] + a[q] > a[r]
    # a[q] + a[r] > a[p]
    # a[r] + a[p] > a[q]

    # trick is that we want the two smallest numbers to be greater than the larger number
    # there are negative numbers

    if len(A) < 3:
        return 0

    a = sorted(A)

    # [10,2,5,1,8,20]
    # [1,2,5,8,10,20]
    # [1,2,*5,8,10*,20]
    for i in range(len(a) - 2):  # [0, index of the 3rd to last]:
        if is_triangular(a[i], a[i + 1], a[i + 2]):
            return 1
    return 0


def is_triangular(p: int, q: int, r: int) -> bool:
    if (p + q) > r and (p + r) > q and (q + r) > p:
        return True
    return False
