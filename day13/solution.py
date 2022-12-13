import json
from functools import cmp_to_key

with open("input.txt") as f:
    data = f.read()

pairs = []
for line_pair in data.split("\n\n"):
    first, second = line_pair.strip().split("\n")
    first_val = json.loads(first)
    second_val = json.loads(second)
    pairs.append((first_val, second_val))


def compare(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        if left > right:
            return 1
        if left == right:
            return 0

    if isinstance(left, list) and isinstance(right, list):
        for subleft, subright in zip(left, right):
            result = compare(subleft, subright)
            if result != 0:
                return result

        if len(left) < len(right):
            return -1
        if len(left) > len(right):
            return 1
        if len(left) == len(right):
            return 0

    if isinstance(left, int) and isinstance(right, list):
        return compare([left], right)

    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])


indices = 0
for i, (left, right) in enumerate(pairs):
    result = compare(left, right)
    # print(f"Comparison {i} between {left} and {right} gave {result}")
    if result == -1:
        indices += i + 1

print(indices)

# part 2

all_packets = [packet for pair in pairs for packet in pair]

dividers = ([[2]], [[6]])
all_packets.extend(dividers)

sorted_packets = sorted(all_packets, key=cmp_to_key(compare))

indices = [sorted_packets.index(divider) for divider in dividers]
print((indices[0] + 1) * (indices[1] + 1))
