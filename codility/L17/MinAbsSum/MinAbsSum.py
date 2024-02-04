# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # Implement your solution here
    curr_sum = 0
    A_abs = [abs(x) for x in A]
    A_sorted = sorted(A_abs, reverse=True)
    for val in A_sorted:
        if curr_sum <= 0:
            curr_sum += abs(val)
        else:
            curr_sum -= abs(val)
    return abs(curr_sum)


def original_solution(A):  # Correctness: 50%, Performace: 80% (Overall 63%)
    # Implement your solution here
    curr_sum = 0
    A_abs = [abs(x) for x in A]
    A_sorted = sorted(A_abs, reverse=True)
    for val in A_sorted:
        if curr_sum <= 0:
            curr_sum += abs(val)
        else:
            curr_sum -= abs(val)
    return abs(curr_sum)

    # For example, for the input [3, 3, 3, 4, 5] the solution returned a wrong answer (got 2 expected 0).
