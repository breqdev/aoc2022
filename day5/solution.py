import math

with open("input.txt") as f:
    contents = f.read()

initial_stacks, instructions = contents.split("\n\n")

stacks = []

stack_input_lines = initial_stacks.splitlines()
labels, *stack_lines = reversed(stack_input_lines)

stacks = [[] for _ in labels.split()]

for line in stack_lines:
    for i in range(len(stacks)):
        value = line[i * 4 + 1]
        if value != " ":
            stacks[i].append(value)

instructions = instructions.split("\n")

for instr in instructions:
    if not instr:
        break

    _, amount, _, source, _, dest = instr.split()

    # Part 1

    # for i in range(int(amount)):
    #     value = stacks[int(source) - 1].pop()
    #     stacks[int(dest) - 1].append(value)

    # Part 2

    values = stacks[int(source) - 1][-int(amount) :]
    stacks[int(source) - 1] = stacks[int(source) - 1][: -int(amount)]
    stacks[int(dest) - 1].extend(values)

print("".join(stack[-1] for stack in stacks))
