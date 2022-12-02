with open("input.txt") as f:
    matches = [line.strip().split(" ") for line in f.readlines()]

score = 0

for match in matches:
    if match[0] == "A" and match[1] == "X":  # Rock ties Rock
        score += 3  # Draw
    elif match[0] == "A" and match[1] == "Y":  # Rocks loses to Paper
        score += 6  # Win
    elif match[0] == "A" and match[1] == "Z":  # Rock beats Scissors
        score += 0  # Loss

    elif match[0] == "B" and match[1] == "X":  # Paper beats Rock
        score += 0
    elif match[0] == "B" and match[1] == "Y":  # Paper ties Paper
        score += 3
    elif match[0] == "B" and match[1] == "Z":  # Paper loses to Scissors
        score += 6

    elif match[0] == "C" and match[1] == "X":  # Scissors loses to Rock
        score += 6
    elif match[0] == "C" and match[1] == "Y":  # Scissors beats Paper
        score += 0
    elif match[0] == "C" and match[1] == "Z":  # Scissors ties Scissors
        score += 3

    if match[1] == "X":
        score += 1  # Rock is 1 point
    elif match[1] == "Y":
        score += 2  # Paper is 2 points
    elif match[1] == "Z":
        score += 3  # Scissors is 3 points

print(score)

# Part 2

score = 0

for match in matches:
    if match[0] == "A" and match[1] == "X":
        # Opponent plays rock, we lose by playing scissors
        score += 0  # Loss
        score += 3  # Scissors is 3 points
    elif match[0] == "A" and match[1] == "Y":
        # Opponent plays rock, we draw by playing rock
        score += 3  # Draw
        score += 1  # Rock is 1 point
    elif match[0] == "A" and match[1] == "Z":
        # Opponent plays rock, we win by playing paper
        score += 6  # Win
        score += 2  # Paper is 2 points

    elif match[0] == "B" and match[1] == "X":
        # Opponent plays paper, we lose by playing rock
        score += 0
        score += 1
    elif match[0] == "B" and match[1] == "Y":
        # Opponent plays paper, we draw by playing paper
        score += 3
        score += 2
    elif match[0] == "B" and match[1] == "Z":
        # Opponent plays paper, we win by playing scissors
        score += 6
        score += 3

    elif match[0] == "C" and match[1] == "X":
        # Opponent plays scissors, we lose by playing paper
        score += 0
        score += 2
    elif match[0] == "C" and match[1] == "Y":
        # Opponent plays scissors, we draw by playing scissors
        score += 3
        score += 3
    elif match[0] == "C" and match[1] == "Z":
        # Opponent plays scissors, we win by playing rock
        score += 6
        score += 1

print(score)
