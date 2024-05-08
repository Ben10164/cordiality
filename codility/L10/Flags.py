# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def is_valid_distance(peaks, min_distance):
    """Check if the minimum distance can be maintained between peaks."""
    valid_peaks = 1
    previous_peak = peaks[0]
    for peak in peaks:
        if peak >= previous_peak + min_distance:
            valid_peaks += 1
            previous_peak = peak
    return valid_peaks >= min_distance

def find_peaks(heights):
    """Return the indices of peaks in the list of heights."""
    return [
        index for index in range(1, len(heights) - 1)
        if heights[index] > heights[index - 1] and heights[index] > heights[index + 1]
    ]

def solution(heights):
    """Find the optimal number of flags that can be set on the peaks."""
    peaks = find_peaks(heights)
    if not peaks:
        return 0

    max_distance = math.ceil(math.sqrt(len(heights)))
    if is_valid_distance(peaks, max_distance):
        return max_distance

    left, right = 1, max_distance - 1
    while left <= right:
        mid = left + (right - left) // 2
        if is_valid_distance(peaks, mid):
            if not is_valid_distance(peaks, mid + 1):
                return mid
            left = mid + 1
        else:
            right = mid - 1

    return -1
