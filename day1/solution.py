with open("input.txt") as f:
    data = f.readlines()

elves = [0]
for line in data:
    if line.strip():
        elves[-1] += int(line.strip())
    else:
        elves.append(0)

print(max(elves))
print(sum(sorted(elves, reverse=True)[:3]))
