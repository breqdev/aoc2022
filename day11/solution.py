import queue

with open("input.txt") as f:
    data = f.read()

monkey_data = data.split("\n\n")

items = []
operations = []
tests = []
destinations = []

for chunk in monkey_data:
    lines = chunk.splitlines()

    assert lines[0] == f"Monkey {len(items)}:"

    items.append([int(i) for i in lines[1].strip().removeprefix("Starting items: ").split(",")])

    match lines[2].strip().removeprefix("Operation: new = old ").split(" "):
        case ["+", val] if val.isdigit():
            operations.append(lambda x,val=val: x + int(val))
        case ["*", val] if val.isdigit():
            operations.append(lambda x,val=val: x * int(val))
        case ["+", "old"]:
            operations.append(lambda x: x + x)
        case ["*", "old"]:
            operations.append(lambda x: x * x)
        case [*operation]:
            raise ValueError(f"Unexpected operation: {' '.join(operation)}")

    divisor = int(lines[3].strip().removeprefix("Test: divisible by "))
    tests.append(lambda x,divisor=divisor: x % divisor == 0)

    true_throw = int(lines[4].strip().removeprefix("If true: throw to monkey "))
    false_throw = int(lines[5].strip().removeprefix("If false: throw to monkey "))
    destinations.append((false_throw, true_throw))

inspections = [0 for _ in items]

for round_idx in range(20):
    print(f"Round {round_idx}:")
    for monkey_idx in range(len(items)):
        print(f"  Monkey {monkey_idx}:")
        monkey_items = queue.Queue()
        for item in items[monkey_idx]:
            monkey_items.put(item)

        items[monkey_idx] = []

        while not monkey_items.empty():
            # monkey examines the item
            item = monkey_items.get()
            inspections[monkey_idx] += 1
            print(f"    Monkey inspects an item with a worry level of {item}.")

            # monkey performs its operation to the worry value
            item = operations[monkey_idx](item)
            print(f"      Worry level becomes {item}.")

            # monkey gets bored with the item, worry level // 3
            item = item // 3
            print(f"      Monkey gets bored with item. Worry level is divided by 3 to {item}.")

            # monkey tests the item
            result = tests[monkey_idx](item)
            print(f"      Test returns {result}.")

            # monkey throws the item
            dest_idx = destinations[monkey_idx][result]
            items[dest_idx].append(item)
            print(f"      Item with worry level {item} is thrown to monkey {dest_idx}.")


print(items)
print()
print(inspections)

first, second = sorted(inspections, reverse=True)[:2]
print(first * second)
