# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    # Implement your solution here
    # convert to binary
    # split at 1's
        # xxx1____1 not ___1...
    N_bin = bin(N)
    # N_binary is a string, so lets trim the "0b"
    N_bin = N_bin[2:]
    max_gap = 0
    curr_gap = 0
    for i in range(len(N_bin)):
        if N_bin[i] == '0': 
            # the binary numbers produced by this function never start with 0s, 
            # so we dont need to worry about leading 0s
            curr_gap += 1
        elif N_bin[i] == '1':
            if curr_gap > max_gap:
                max_gap = curr_gap
            curr_gap = 0
        else:
            raise ValueError("No clue how this happened since the `bin` converstion should only output '0b[1|0]*' which we trim down to `[0|1]*`")
    return max_gap