import queue

with open("input.txt") as f:
    data = f.readlines()

grid = []
start = None
end = None

# build the heightmap grid
for line in data:
    if not line:
        continue

    row = []
    for char in line:
        if char == "S":
            start = (len(row), len(grid))
            row.append(0)
        elif char == "E":
            end = (len(row), len(grid))
            row.append(25)
        else:
            row.append(ord(char) - ord("a"))
    grid.append(row)

# build the graph
adjacency = {}

for y, row in enumerate(grid):
    for x, height in enumerate(row):
        adjacency[(x, y)] = set()

        if x > 0:
            if grid[y][x - 1] - height <= 1:
                adjacency[(x, y)].add((x - 1, y))

        if x < len(row) - 1:
            if grid[y][x + 1] - height <= 1:
                adjacency[(x, y)].add((x + 1, y))

        if y > 0:
            if grid[y - 1][x] - height <= 1:
                adjacency[(x, y)].add((x, y - 1))

        if y < len(grid) - 1:
            if grid[y + 1][x] - height <= 1:
                adjacency[(x, y)].add((x, y + 1))

# use BFS
parents = {}
visited = set()
worklist = queue.Queue()

parents[start] = None
visited.add(start)
worklist.put(start)

while not worklist.empty():
    node = worklist.get()

    if node == end:
        break

    for neighbor in adjacency[node]:
        if neighbor in visited:
            continue

        parents[neighbor] = node
        visited.add(neighbor)
        worklist.put(neighbor)

# reconstruct the path from the parent table
path = [end]
while True:
    parent = parents[path[-1]]
    if parent:
        path.append(parent)
    else:
        break

# print(path)
# get the length
print(len(path) - 1)
