with open("input.txt") as f:
    lines = f.readlines()

moves = []
for line in lines:
    direction, distance = line.split(" ", 1)
    for _ in range(int(distance)):
        moves.append(direction)

head_position = (0, 0)
tail_position = (0, 0)

positions = set()
positions.add(tail_position)

for direction in moves:
    if direction == "U":
        head_position = (head_position[0], head_position[1] + 1)
    elif direction == "D":
        head_position = (head_position[0], head_position[1] - 1)
    elif direction == "L":
        head_position = (head_position[0] - 1, head_position[1])
    elif direction == "R":
        head_position = (head_position[0] + 1, head_position[1])
    else:
        raise ValueError("invalid direction " + direction)

    if abs(tail_position[0] - head_position[0]) <= 1 and abs(tail_position[1] - head_position[1]) <= 1:
        continue  # tail is within range

    if tail_position[0] == head_position[0]:
        # tail needs to move vertically
        if tail_position[1] < head_position[1]:
            tail_position = (tail_position[0], tail_position[1] + 1)
        elif tail_position[1] > head_position[1]:
            tail_position = (tail_position[0], tail_position[1] - 1)
    elif tail_position[1] == head_position[1]:
        # tail needs to move horizontally
        if tail_position[0] < head_position[0]:
            tail_position = (tail_position[0] + 1, tail_position[1])
        elif tail_position[0] > head_position[0]:
            tail_position = (tail_position[0] - 1, tail_position[1])
    else:
        # tail needs to move diagonally
        if tail_position[0] < head_position[0] and tail_position[1] < head_position[1]:
            tail_position = (tail_position[0] + 1, tail_position[1] + 1)
        elif tail_position[0] < head_position[0] and tail_position[1] > head_position[1]:
            tail_position = (tail_position[0] + 1, tail_position[1] - 1)
        elif tail_position[0] > head_position[0] and tail_position[1] < head_position[1]:
            tail_position = (tail_position[0] - 1, tail_position[1] + 1)
        elif tail_position[0] > head_position[0] and tail_position[1] > head_position[1]:
            tail_position = (tail_position[0] - 1, tail_position[1] - 1)

    positions.add(tail_position)

print(len(positions))
