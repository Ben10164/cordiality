# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # returns the value of the number odd amount of times
    # (not just only occuring once)
    # be efficient
    # first thing that comes to mind is mapping
    #   like how in R you can use `table`
    # lets start off with a dictionary
    occurances = dict()
    for val in A:
        occurances[val] = occurances.get(val, 0) + 1
    # now we just need to find an index with an odd number
    for val in occurances:
        if occurances[val] % 2 != 0:
            return val