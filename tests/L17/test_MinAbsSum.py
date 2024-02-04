import codility.L17.MinAbsSum.MinAbsSum_Official_Solution as expected
import codility.L17.MinAbsSum.MinAbsSum as actual
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
# large_random_inputs = [[random.randint(-100, 100) for _ in range(random.randint(0, 10000))] for _ in range(100)]
# massive_random_inputs = [[random.randint(-100, 100) for _ in range(random.randint(0, 200000))] for _ in range(2)]

# Combine fixed inputs with random inputs
all_inputs = fixed_inputs + large_random_inputs + massive_random_inputs


@pytest.mark.parametrize("test_input", all_inputs)
def test_solution(test_input):
    assert expected.solution(test_input) == actual.solution(test_input)
