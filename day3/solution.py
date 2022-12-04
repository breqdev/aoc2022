with open("input.txt") as f:
    sacks = map(
        lambda line: [line[: len(line) // 2], line[len(line) // 2 :]],
        [line.strip() for line in f.readlines()],
    )

duplicates = []

for left, right in sacks:
    for item in left:
        if item in right:
            duplicates.append(item)
            break


def priority(letter):
    if ord("a") <= ord(letter) <= ord("z"):
        return ord(letter) - ord("a") + 1
    elif ord("A") <= ord(letter) <= ord("Z"):
        return ord(letter) - ord("A") + 27


print(sum(priority(item) for item in duplicates))

# Part 2

with open("input.txt") as f:
    sacks = [line.strip() for line in f.readlines()]

badges = []

for i in range(len(sacks) // 3):
    group = sacks[i * 3 : (i + 1) * 3]
    for item in group[0]:
        if item in group[1] and item in group[2]:
            badges.append(item)
            break

print(sum(priority(item) for item in badges))
