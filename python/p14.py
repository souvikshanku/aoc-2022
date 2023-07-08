with open("inputs/p14.txt", "r") as f:
    content = f.read().splitlines()

block = {}
sand = {}

for line in content:
    xy_list = line.split("->")
    _paths = [(eval(xy)) for xy in xy_list]
    for i in range(len(_paths)-1):
        x1, y1 = _paths[i]
        x2, y2 = _paths[i+1]
        _range1 = range(min(x1, x2), max(x1, x2) + 1)
        _range2 = range(min(y1, y2), max(y1, y2) + 1)

        for x in _range1:
            block[(x, y1)] = 1
        for y in _range2:
            block[(x1, y)] = 1


y_limit = max(block, key=lambda x: x[1])[1]

start = (500, 0)

def sand_descend(sand_pos):
    x, y = sand_pos
    if (x, y + 1) not in block and (x, y + 1) not in sand and y + 1 <= y_limit:
        return sand_descend((x, y + 1))
    elif (x - 1, y + 1) not in block and (x - 1, y + 1) not in sand and y + 1 <= y_limit:
        return sand_descend((x - 1, y + 1))
    elif (x + 1, y + 1) not in block and (x + 1, y + 1) not in sand and y + 1 <= y_limit:
        return sand_descend((x + 1, y + 1))
    elif y + 1 > y_limit:
        return None
    else:
        return sand_pos


def sand_descend2(sand_pos):
    x, y = sand_pos
    if (x, y + 1) not in block and (x, y + 1) not in sand and y + 1 <= y_limit:
        return sand_descend2((x, y + 1))
    elif (x - 1, y + 1) not in block and (x - 1, y + 1) not in sand and y + 1 <= y_limit:
        return sand_descend2((x - 1, y + 1))
    elif (x + 1, y + 1) not in block and (x + 1, y + 1) not in sand and y + 1 <= y_limit:
        return sand_descend2((x + 1, y + 1))
    else:
        return sand_pos


while True:
    prev_length = len(sand)
    pos = sand_descend(start)
    sand[pos] = 1
    later_length  = len(sand)

    if later_length == prev_length:
        break

print(len(sand) - 1)  # part 1

y_limit += 1


while True:
    prev_length = len(sand)
    pos = sand_descend2(start)
    sand[pos] = 1
    later_length  = len(sand)

    if later_length == prev_length:
        break

print(len(sand) - 1)  # part 2
