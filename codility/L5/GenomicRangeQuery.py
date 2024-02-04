# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# A: 1
# C: 2
# G: 3
# T: 4

# len(S) == N
# len(P) == len(Q) == M
# M is the num queries (0 <= K < M in the loop)

# for the Kth, minimal factor between P[K] and Q[K]

# returns list of length M, corresponding to P and Q


def solution(S: list, P: list, Q: list) -> list:
    # Implement your solution here
    results = []
    for i in range(len(P)):  # could also be Q
        lower_bound = P[i]
        upper_bound = Q[i]
        sequence = S[lower_bound : upper_bound + 1]
        """
        # ooo just realized that the smallest is the highest ASCII number
        # so we can do some conversions/comparisons
        lowest = 'T'
        for nucleotide in sequence:
            if nucleotide < lowest:
                lowest = nucleotide
                if nucleotide == "A":
                    break
        # 3.8 doesnt have switch cases
        values = {"A": 1, "C": 2, "G": 3, "T": 4}
        results.append(values[lowest])
        """  # this had bad performance O(N*M)
        if "A" in sequence:
            results.append(1)
        elif "C" in sequence:
            results.append(2)
        elif "G" in sequence:
            results.append(3)
        elif "T" in sequence:
            results.append(4)

    return results
