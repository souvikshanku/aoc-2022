import math

with open('inputs/p11.txt', 'r') as f:
    start = f.read()

monkeys = start.split("\n\n")

monkey_dict = {}

for i in range(len(monkeys)):
    info = monkeys[i].split("\n")
    items = list(map(int, info[1].split(":")[-1].split(",")))

    monkey_dict[i] = {
        "worries": items,
        "count": len(items),
        "div_by": int(info[3].split(" ")[-1]),
        "true": int(info[4].split(" ")[-1]),
        "false": int(info[5].split(" ")[-1]),
        "op": info[2].split("= ")[-1]
    }

num_rounds = 20

def throw(moneky_idx, round):
    worries = monkey_dict[moneky_idx]["worries"].copy()

    for worry in worries:
        to_div_by = monkey_dict[moneky_idx]["div_by"]
        old = worry
        
        new = eval(monkey_dict[moneky_idx]["op"])
        new = new // 3

        if new % to_div_by:
            recv_monkey = monkey_dict[moneky_idx]["false"]
        else:
            recv_monkey = monkey_dict[moneky_idx]["true"]

        monkey_dict[moneky_idx]["worries"].remove(old)
        monkey_dict[recv_monkey]["worries"].append(new)

        if round != num_rounds - 1:
            monkey_dict[recv_monkey]["count"] += 1
        elif recv_monkey > moneky_idx:
            monkey_dict[recv_monkey]["count"] += 1
        else:
            pass


for round in range(num_rounds):
    for idx in range(len(monkey_dict)):
        throw(idx, round)


counts = sorted([monkey_dict[monkey]["count"] for monkey in monkey_dict])
print(counts[-1] * counts[-2])


monkey_dict = {}

for i in range(len(monkeys)):
    info = monkeys[i].split("\n")
    items = list(map(int, info[1].split(":")[-1].split(",")))

    monkey_dict[i] = {
        "worries": items,
        "count": len(items),
        "div_by": int(info[3].split(" ")[-1]),
        "true": int(info[4].split(" ")[-1]),
        "false": int(info[5].split(" ")[-1]),
        "op": info[2].split("= ")[-1]
    }

num_rounds_v2 = 10000
div_by_list = [monkey_dict[monkey]["div_by"] for monkey in monkey_dict]
product = math.prod(div_by_list)


def throw_v2(moneky_idx, round):
    worries = monkey_dict[moneky_idx]["worries"].copy()

    for worry in worries:
        monkey_dict[moneky_idx]["worries"].remove(worry)

        div_by = monkey_dict[moneky_idx]["div_by"]
        old = worry % product
        new = eval(monkey_dict[moneky_idx]["op"])

        if new % div_by:
            recv_monkey = monkey_dict[moneky_idx]["false"]
        else:
            recv_monkey = monkey_dict[moneky_idx]["true"]


        monkey_dict[recv_monkey]["worries"].append(new)

        if round != num_rounds_v2 - 1:
            monkey_dict[recv_monkey]["count"] += 1
        elif recv_monkey > moneky_idx:
            monkey_dict[recv_monkey]["count"] += 1
        else:
            pass


for round in range(num_rounds_v2):
    for idx in range(len(monkey_dict)):
        throw_v2(idx, round)


counts = sorted([monkey_dict[monkey]["count"] for monkey in monkey_dict])
print(counts[-1] * counts[-2])
