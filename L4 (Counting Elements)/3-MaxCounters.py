# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    counters = [0] * N
    max_numbers = set()
    for i in range(0, len(A)):
        if 1 <= A[i] <= N:
            index = A[i]-1
            counters[index] += 1
            max_numbers.add(counters[A[i]-1])
        elif A[i] == N + 1 and len(max_numbers) > 0:
            counters = [max(max_numbers)] * N
            max_numbers.clear()

    return counters