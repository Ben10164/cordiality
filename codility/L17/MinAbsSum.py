# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    N = len(A)
    M = 0
    for i in range(N):
        A[i] = abs(A[i])
        M = max(A[i], M)
    S = sum(A)
    count = [0] * (M + 1)
    for i in range(N):
        count[A[i]] += 1
    dp = [-1] * (S + 1)
    dp[0] = 0
    for a in range(1, M + 1):
        if count[a] > 0:
            for j in range(S):
                if dp[j] >= 0:
                    dp[j] = count[a]
                elif j >= a and dp[j - a] > 0:
                    dp[j] = dp[j - a] - 1
    result = S
    for i in range(S // 2 + 1):
        if dp[i] >= 0:
            result = min(result, S - 2 * i)
    return result


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
