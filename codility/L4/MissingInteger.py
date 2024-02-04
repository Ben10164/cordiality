# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A: list):
    # Implement your solution here
    # basic pythonic solution
    A_set = set([val for val in A if val > 0])  # O(N)
    A_sorted = sorted(A_set)  # < O(N)
    # print(A_sorted)
    # A_sorted = sorted(set(A)) # could do some logic to only have it be positive numbers
    search_val = 1
    for val in A_sorted:  # O(N)
        # if val > 0: # since we did the logic on line 7, there is no need to have an if statement
        # print(val)
        if val != search_val:
            # print(val, search_val)
            return search_val
        else:
            search_val += 1
        # else:
        #     # ignore negative numbers
        #     pass
    # at this point, the list (technically set) has been traversed successfully and never ran into
    # any issues reguarding not equalling the number.
    # Therefore, it is then 1 + the largest number in the list, OR it is 1 (in the case of all negatives / 0)
    return search_val
