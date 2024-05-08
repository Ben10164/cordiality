import codility.L17.MinAbsSum as actual
import pytest
import random

random.seed(0)

# Generate other fixed inputs
fixed_inputs = [
    [1, 5, 2, -2],
    [3, 3, 5, 4, 3],
]

large_random_inputs = []
massive_random_inputs = []

# Generate 1000 different arrays, each with 100 random integers
# large_random_inputs = [[random.randint(-100, 100) for _ in range(random.randint(0, 10000))] for _ in range(5)]
large_random_inputs = [
    [random.randint(-10, 10) for _ in range(random.randint(0, 2))] for _ in range(5)
]
# massive_random_inputs = [[random.randint(-100, 100) for _ in range(random.randint(0, 200000))] for _ in range(2)]

# Combine fixed inputs with random inputs
all_inputs = fixed_inputs + large_random_inputs + massive_random_inputs


@pytest.mark.parametrize("test_input", all_inputs)
def test_solution(test_input):
    assert actual.solution(test_input) == official_solution(test_input)


def official_solution(A):
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
