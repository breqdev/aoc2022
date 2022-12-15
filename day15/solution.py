with open("input.txt") as f:
    lines = f.readlines()

beacons = {}

for line in lines:
    sensor_part, beacon_part = line.strip().split(":")

    sensor_x, sensor_y = sensor_part.strip().removeprefix("Sensor at ").split(",")
    beacon_x, beacon_y = (
        beacon_part.strip().removeprefix("closest beacon is at ").split(",")
    )

    sensor_x, sensor_y = (
        int(sensor_x.strip().removeprefix("x=")),
        int(sensor_y.strip().removeprefix("y=")),
    )
    beacon_x, beacon_y = (
        int(beacon_x.strip().removeprefix("x=")),
        int(beacon_y.strip().removeprefix("y=")),
    )

    beacons[(sensor_x, sensor_y)] = (beacon_x, beacon_y)

covered = set()
TARGET_ROW = 2000000
# TARGET_ROW = 10

for sensor, beacon in beacons.items():
    # find the distance covered
    distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

    width_at_y = distance - abs(sensor[1] - TARGET_ROW)
    for x in range(sensor[0] - width_at_y, sensor[0] + width_at_y):
        covered.add(x)

print(len(covered))
print()

# Part 2

# RANGE = 21
RANGE = 4000001

edges = {}
candidates = set()

for sensor, beacon in beacons.items():
    distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

    for x in range(sensor[0] - distance - 1, sensor[0] + distance + 2):
        if x < 0 or x > RANGE:
            continue

        height = distance - abs(x - sensor[0]) + 1
        y_up = sensor[1] + height
        y_down = sensor[1] - height

        if y_up >= 0 and y_up <= RANGE:
            edges[(x, y_up)] = edges.get((x, y_up), 0) + 1
            if edges[(x, y_up)] == 4:
                candidates.add((x, y_up))
        if y_down >= 0 and y_down <= RANGE:
            edges[(x, y_down)] = edges.get((x, y_down), 0) + 1
            if edges[(x, y_down)] == 4:
                candidates.add((x, y_down))

    print(f"sensor {sensor} analyzed")

# print(edges[(14, 11)])
print(f"{len(candidates)} candidates identified")

for (x, y) in candidates:
    for sensor, beacon in beacons.items():
        # find the distance covered
        sensor_range = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        our_distance = abs(sensor[0] - x) + abs(sensor[1] - y)
        if our_distance <= sensor_range:
            break
    else:
        print(f"Found point: {(x, y)}")
        print(f"Code: {x * 4000000 + y}")
