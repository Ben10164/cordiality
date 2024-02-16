# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # make A_abs (the abs value of all A)
    A_abs = [abs(i) for i in A]
    # find the sum of A_abs (S)
    S = sum(A_abs)
    # divide sum by 2 (M)
    M = S // 2 # should always be an int-compatible number
    # print("M:",M)
    # create array [0..M] full of 0s (N)
    N = [0] * (M + 1)
    # print(N)
    # set N[0] to 1
    N[0] = 1
    # for each value in A_abs:
    for value in A_abs:
        # make a new N, N_temp
        N_temp = N.copy()
        # for i in range(len(N)):
        for i in range(len(N)):
            # if N[i] == 1:
            if N[i] == 1 and i + value <= M:
                # check to make sure i + value is not out of bounds
                # N_temp[i+value] = 1
                N_temp[i+value] = 1
        # N = N_temp
        N = N_temp
    # now we can find the index of the furthest 1 (L)
    # print("N:",N)
    for i in range(1,len(N)+1):
        if (N[-i] == 1):
            # print(i)
            # now perform (M - L) * 2
            L = ((len(N)) - i)- 1 # needs the -1 because we are finding the index
            # return sol
            return (M - L) * 2


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

test = [5]
print(solution(test))
import MinAbsSum_Official_Solution
print(MinAbsSum_Official_Solution.solution(test))