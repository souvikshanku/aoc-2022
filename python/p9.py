with open('inputs/p9.txt', 'r') as f:
    movements = f.read()

move_str = ""
for movement in movements.split("\n"):
    move_str += movement[0] * int(movement[2:])

head = (0, 0)
tail = (0, 0)

tail_set = set({})
tail_set.add(tail)

def move_left(head, tail):
    head = (head[0] - 1, head[1])
    if abs(tail[0] - head[0]) > 1:
        tail = (head[0] + 1, head[1])
        tail_set.add(tail)
    return head, tail

def move_right(head, tail):
    head = (head[0] + 1, head[1])
    if abs(tail[0] - head[0]) > 1:
        tail = (head[0] - 1, head[1])
        tail_set.add(tail)
    
    return head, tail

def move_up(head, tail):
    head = (head[0], head[1] + 1)
    if abs(tail[1] - head[1]) > 1:
        tail = (head[0], head[1] - 1)
        tail_set.add(tail)

    return head, tail

def move_down(head, tail):
    head = (head[0], head[1] - 1)
    if abs(tail[1] - head[1]) > 1:
        tail = (head[0], head[1] + 1)
        tail_set.add(tail)

    return head, tail

for move in move_str:
    if move == 'L':
        head, tail = move_left(head, tail)
    elif move == 'R':
        head, tail = move_right(head, tail)
    elif move == 'U':
        head, tail = move_up(head, tail)
    else:
        head, tail = move_down(head, tail)

print(len(tail_set))

diff_dict = {
    '-2 -2': [1, 1],
    '-2 -1': [1, 1],
    '-2 0': [1, 0],
    '-2 1': [1, -1],
    '-2 2': [1, -1],
    '-1 2': [1, -1],
    '0 2': [0, -1],
    '1 2': [-1, -1],
    '2 2': [-1, -1],
    '2 1': [-1, -1],
    '2 0': [-1, 0],
    '2 -1': [-1, 1],
    '2 -2': [-1, 1],
    '1 -2': [-1, 1],
    '0 -2': [0, 1],
    '-1 -2': [1, 1]
}


heads = [(0, 0)] * 10

tail_set = set({})
tail_set.add(heads[-1])

for move in move_str:
    if move == 'L':
        heads[0] = (heads[0][0] - 1, heads[0][1])
    if move == 'R':
        heads[0] = (heads[0][0] + 1, heads[0][1])
    if move == 'U':
        heads[0] = (heads[0][0], heads[0][1] + 1)
    if move == 'D':
        heads[0] = (heads[0][0], heads[0][1] - 1)
    
    for i in range(1, 10):
        x_diff = heads[i][0] - heads[i-1][0]
        y_diff = heads[i][1] - heads[i-1][1]
        if abs(x_diff) <= 1 and abs(y_diff) <= 1:
            pass
        else:
            diff_str = f"{x_diff} {y_diff}"
            dx, dy = diff_dict[diff_str]
            heads[i] = heads[i][0] + dx, heads[i][1] + dy

    tail_set.add(heads[-1])

print(len(tail_set))