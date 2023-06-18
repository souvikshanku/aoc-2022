with open('inputs/p9.txt', 'r') as f:
    movements = f.read()

move_str = ""
for movement in movements.split("\n"):
    move_str += movement[0] * int(movement[2:])

# print(move_str)

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

# print(len(tail_set))

# heads = [(0, 0)] * 10
heads = [(0, 0), (-1, 0), (-2, 0), (-3, 0), (-4, 0)] + [(-5, 0)] * 5
print(heads)
print("____________________________")

tail_set2 = set({})

for move in move_str:
    if move == 'L':
        heads[0] = (heads[0][0] - 1, heads[0][1])
        for i in range(9):
            x_diff = heads[i+1][0] - heads[i][0]
            y_diff = heads[i+1][1] - heads[i][1]
            if abs(x_diff) == 1 and abs(y_diff) == 1:
                pass
            if abs(x_diff) == 2 and abs(y_diff) == 0:
                heads[i+1] = (heads[i+1][0] - 1, heads[i+1][1])
            elif x_diff == 2 and abs(y_diff) == 1:
                heads[i+1] = (heads[i+1][0] - 1, heads[i+1][1] - y_diff)
            elif x_diff == 1 and y_diff == 2:
                heads[i+1] = (heads[i+1][0] - 1, heads[i+1][1] - 1)
            elif x_diff == 1 and y_diff == - 2:
                heads[i+1] = (heads[i+1][0] - 1, heads[i+1][1] + 1)
            elif abs(x_diff) == 2 and abs(y_diff) == 2:
                heads[i+1] = (heads[i+1][0] - 1, heads[i+1][1] + (y_diff / abs(y_diff) ) )
            

        print(heads)
        tail_set2.add(heads[-1])

    elif move == 'R':
        heads[0] = (heads[0][0] + 1, heads[0][1])
        for i in range(9):
            x_diff = heads[i+1][0] - heads[i][0]
            y_diff = heads[i+1][1] - heads[i][1]
            if abs(x_diff) == 1 and abs(y_diff) == 1:
                pass
            if abs(x_diff) == 2 and y_diff == 0:
                heads[i+1] = (heads[i+1][0] + 1, heads[i+1][1])
            elif x_diff == -2 and abs(y_diff) == 1:
                heads[i+1] = (heads[i+1][0] + 1, heads[i+1][1] - y_diff)
            elif x_diff == -1 and y_diff == 2:
                heads[i+1] = (heads[i+1][0] + 1, heads[i+1][1] - 1)
            elif x_diff == -1 and y_diff == - 2:
                heads[i+1] = (heads[i+1][0] + 1, heads[i+1][1] + 1)
            elif abs(x_diff) == 2 and abs(y_diff) == 2:
                heads[i+1] = (heads[i+1][0] + 1, heads[i+1][1] + (y_diff / abs(y_diff) ) )

        print(heads)
        tail_set2.add(heads[-1])
 
    elif move == 'U':
        heads[0] = (heads[0][0], heads[0][1] + 1)
        for i in range(9):
            x_diff = heads[i+1][0] - heads[i][0]
            y_diff = heads[i+1][1] - heads[i][1]
            if abs(x_diff) == 1 and abs(y_diff) == 1:
                pass
            if abs(y_diff) == 2 and x_diff == 0:
                heads[i+1] = (heads[i+1][0], heads[i+1][1] + 1)
            elif y_diff == -2 and abs(x_diff) == 1:
                heads[i+1] = (heads[i+1][0] - x_diff, heads[i+1][1] + 1)
            elif y_diff == 1 and x_diff == 2:
                heads[i+1] = (heads[i+1][0] - 1, heads[i+1][1] + 1)
            elif y_diff == -1 and x_diff == - 2:
                heads[i+1] = (heads[i+1][0] + 1, heads[i+1][1] + 1)
            elif abs(x_diff) == 2 and abs(y_diff) == 2:
                heads[i+1] = (heads[i+1][0] + (x_diff / abs(x_diff)), heads[i+1][1] + 1)

        print(heads)
        tail_set2.add(heads[-1])

    else:
        heads[0] = (heads[0][0], heads[0][1] - 1)
        for i in range(9):
            x_diff = heads[i+1][0] - heads[i][0]
            y_diff = heads[i+1][1] - heads[i][1]
            if abs(x_diff) == 1 and abs(y_diff) == 1:
                pass
            if abs(y_diff) == 2 and x_diff == 0:
                heads[i+1] = (heads[i+1][0], heads[i+1][1] - 1)
            elif y_diff == -2 and abs(x_diff) == 1:
                heads[i+1] = (heads[i+1][0] - x_diff, heads[i+1][1] - 1)
            elif y_diff == 1 and x_diff == 2:
                heads[i+1] = (heads[i+1][0] - 1, heads[i+1][1] - 1)
            elif y_diff == -1 and x_diff == - 2:
                heads[i+1] = (heads[i+1][0] + 1, heads[i+1][1] - 1)
            elif abs(x_diff) == 2 and abs(y_diff) == 2:
                heads[i+1] = (heads[i+1][0] + (x_diff / abs(x_diff)), heads[i+1][1] - 1)

        print(heads)
        tail_set2.add(heads[-1])

print(len(tail_set2))