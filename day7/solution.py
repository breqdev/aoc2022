with open("input.txt") as f:
    contents = [line.strip() for line in f.readlines()]

tree = {}
pwd = []

for line in contents:
    if line == "$ cd ..":
        pwd.pop()
    elif line == "$ cd /":
        pwd = []
    elif line.startswith("$ cd "):
        pwd.append(line.removeprefix("$ cd "))
    elif line.startswith("$ ls"):
        pass
    elif line.startswith("dir "):
        parent = tree
        for part in pwd:
            parent = parent[part]
        parent[line.removeprefix("dir ")] = {}
    elif line:
        size, name = line.split(" ", 1)
        parent = tree
        for part in pwd:
            parent = parent[part]
        parent[name] = (name, int(size))

def find_dir_sizes(tree):
    result = {}
    total_size = 0
    for key, value in tree.items():
        if isinstance(value, dict):
            sub_result, sub_size = find_dir_sizes(value)
            result[key] = (sub_result, sub_size)
            total_size += sub_size
        else:
            result[key] = value
            total_size += value[1]
    return result, total_size

sized = find_dir_sizes(tree)

def sum_small_dirs(tree):
    value, size = tree
    if size < 100000:
        total = size
    else:
        total = 0

    for key, value in value.items():
        if isinstance(value[0], dict):
            total += sum_small_dirs(value)
    return total

print(sum_small_dirs(sized))

# Part 2

free = 70000000 - sized[1]
needed = 30000000 - free

def find_smallest_dir(tree):
    value, size = tree
    if size > needed:
        smallest = []
        smallestVal = size
    else:
        smallest = None
        smallestVal = float("inf")

    for key, value in value.items():
        if isinstance(value[0], dict):
            candidate, candidateVal = find_smallest_dir(value)
            if candidateVal < smallestVal:
                smallest = [key, *candidate]
                smallestVal = candidateVal

    return smallest, smallestVal

print(find_smallest_dir(sized))
