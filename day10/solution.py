with open("input.txt") as f:
    instructions = [line.strip() for line in f.readlines()]

strengths = 0
clock = 0
x = 1
value = None

i = 0
while i < len(instructions):
    # print(f"cycle {clock}: x {x}")
    if value is not None:
        # print(f"still executing add {value}")
        clock += 1
        new_value = None

    elif instructions[i] == "noop":
        # print("executing noop")
        clock += 1
        i += 1
        new_value = None

    elif instructions[i].startswith("addx"):
        new_value = int(instructions[i].split(" ")[1])
        # print(f"begin executing add {new_value}")
        clock += 1
        i += 1


    # if clock % 40 == 20:
    #     print(f"cycle {clock} x {x} = {clock * x}")
    #     strengths += clock * x

    # print(f"\nclock pos {(clock % 40) - 1} x {x}")
    screen_pos = (clock % 40) - 1 if clock % 40 > 0 else 39
    if abs(x - screen_pos) <= 1:
        print("#", end="")
    else:
        print(" ", end="")

    if clock % 40 == 0:
        print()

    if value is not None:
        # print(f"finish executing add {value}")
        x += value
        value = None

    value = new_value

# print(strengths)
