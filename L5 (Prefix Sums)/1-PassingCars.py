# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A: list):
    # Implement your solution here

    # ohhhh i see now
    # car 1 is driving east,
    # cars 2 through 4 are driving west
    # there will be 3 instances where there is a "drive by"
    # 1 drives by 2
    # 1 drives by 3
    # 1 drives by 4
    # the trick is that it is only cars that are in the direction of the car
    # i.e. A[1] = 1 will never pass A[2] = 0 because they are already passed each other
    # at the moment of observation
    passes = 0
    num_ones_left = A.count(1)

    for i in range(len(A)):
        # if it is a 0, we check for 1's that are in the positive index direction
        if A[i] == 0:
            passes += num_ones_left
        else:
            num_ones_left -= 1

        if passes > 1000000000:
            return -1
        # if it is a 1, we check for 0s that are in the negative index direction
        # this is actually already taken care of (0,2) == (2,0)
    return passes