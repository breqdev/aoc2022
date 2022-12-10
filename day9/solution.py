with open("input.txt") as f:
    lines = f.readlines()

moves = []
for line in lines:
    direction, distance = line.split(" ", 1)
    for _ in range(int(distance)):
        moves.append(direction)

joints = [(0, 0) for _ in range(10)]

positions = set()
positions.add(joints[-1])

for direction in moves:
    # move the head
    head = joints[0]
    if direction == "U":
        joints[0] = (head[0], head[1] + 1)
    elif direction == "D":
        joints[0] = (head[0], head[1] - 1)
    elif direction == "L":
        joints[0] = (head[0] - 1, head[1])
    elif direction == "R":
        joints[0] = (head[0] + 1, head[1])
    else:
        raise ValueError("invalid direction " + direction)

    for i in range(1, len(joints)):
        leading = joints[i - 1]
        lagging = joints[i]

        if abs(lagging[0] - leading[0]) <= 1 and abs(lagging[1] - leading[1]) <= 1:
            continue  # tail is within range

        if lagging[0] == leading[0]:
            # tail needs to move vertically
            if lagging[1] < leading[1]:
                joints[i] = (lagging[0], lagging[1] + 1)
            elif lagging[1] > leading[1]:
                joints[i] = (lagging[0], lagging[1] - 1)
        elif lagging[1] == leading[1]:
            # tail needs to move horizontally
            if lagging[0] < leading[0]:
                joints[i] = (lagging[0] + 1, lagging[1])
            elif lagging[0] > leading[0]:
                joints[i] = (lagging[0] - 1, lagging[1])
        else:
            # tail needs to move diagonally
            if lagging[0] < leading[0] and lagging[1] < leading[1]:
                joints[i] = (lagging[0] + 1, lagging[1] + 1)
            elif lagging[0] < leading[0] and lagging[1] > leading[1]:
                joints[i] = (lagging[0] + 1, lagging[1] - 1)
            elif lagging[0] > leading[0] and lagging[1] < leading[1]:
                joints[i] = (lagging[0] - 1, lagging[1] + 1)
            elif lagging[0] > leading[0] and lagging[1] > leading[1]:
                joints[i] = (lagging[0] - 1, lagging[1] - 1)

    positions.add(joints[-1])

print(len(positions))
