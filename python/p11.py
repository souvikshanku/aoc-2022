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


def throw(moneky_idx, round):
    worries = monkey_dict[moneky_idx]["worries"].copy()

    for worry in worries:
        old = worry
        new = eval(monkey_dict[moneky_idx]["op"]) // 3

        if new % monkey_dict[moneky_idx]["div_by"]:
            recv_monkey = monkey_dict[moneky_idx]["false"]
        else:
            recv_monkey = monkey_dict[moneky_idx]["true"]

        monkey_dict[moneky_idx]["worries"].remove(old)
        monkey_dict[recv_monkey]["worries"].append(new)

        if round != 19:
            monkey_dict[recv_monkey]["count"] += 1
        elif recv_monkey > moneky_idx:
            monkey_dict[recv_monkey]["count"] += 1
        else:
            pass


for round in range(20):
    for idx in range(len(monkey_dict)):
        throw(idx, round)
    # print(f"------- round {round + 1} -------")
    # for monkey in monkey_dict:
    #     print(monkey_dict[monkey]["count"])


print("-----------------------------------")
for monkey in monkey_dict:
    print(monkey_dict[monkey]["worries"])

print("-----------------------------------")    
for monkey in monkey_dict:
    print(monkey_dict[monkey]["count"])


counts = sorted([
    monkey_dict[monkey]["count"] for monkey in monkey_dict]
)

print(counts[-1] * counts[-2])