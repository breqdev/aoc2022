with open("input.txt") as f:
    lines = f.readlines()

ranges = [line.strip().split(",") for line in lines]
ranges = [[rang.split("-") for rang in line] for line in ranges]
ranges = [[[int(rang[0]), int(rang[1])] for rang in line] for line in ranges]

fully_contained = 0
for left, right in ranges:
    if left[0] >= right[0] and left[1] <= right[1]:
        fully_contained += 1
    elif right[0] >= left[0] and right[1] <= left[1]:
        fully_contained += 1

print(fully_contained)

# Part 2

overlaps = 0
for left, right in ranges:
    if left[0] <= right[0] and left[1] >= right[0]:
        overlaps += 1
    elif right[0] <= left[0] and right[1] >= left[0]:
        overlaps += 1

print(overlaps)
