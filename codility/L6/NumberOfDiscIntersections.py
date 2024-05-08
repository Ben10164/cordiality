# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    events = []
    for i, radius in enumerate(A):
        events.append((i - radius, "start"))
        events.append((i + radius, "end"))

    events.sort(key=lambda x: (x[0], x[1] == "end"))

    intersections = 0
    active_circles = 0

    for event in events:
        if event[1] == "start":
            # Each new circle intersects with all currently active circles
            intersections += active_circles
            active_circles += 1
        else:
            active_circles -= 1

        # Check for the limit on intersections
        if intersections > 10000000:
            return -1

    return intersections
