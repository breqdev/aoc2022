with open("input.txt") as f:
    contents = f.readline()

# UNIQUE_SIZE = 4
UNIQUE_SIZE = 14

for i in range(UNIQUE_SIZE, len(contents)):
    window = contents[i - UNIQUE_SIZE : i]

    if len(set(window)) == UNIQUE_SIZE:
        print(i)
        break
