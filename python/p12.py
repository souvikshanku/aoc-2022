with open('inputs/p12.txt', 'r') as f:
    map_str = f.read()

letter_dict = {}
for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
    letter_dict[letter] = i+1

letter_dict['S'] = 0
letter_dict['E'] = 100


path_map = []

for path in map_str.splitlines():
    array = map(lambda letter: letter_dict[letter], path)
    path_map.append(list(array))


num_rows = len(path_map)
num_colunms = len(path_map[0])
for r in range(num_rows):
    for c in range(num_colunms):
        if path_map[r][c] == 0:
            start = (r, c)
            path_map[r][c] = 1
        if path_map[r][c] == 100:
            end = (r, c)
            path_map[r][c] = 26


def find_neighbours(i, j):
    neighbours = []

    if i-1 >= 0 and path_map[i-1][j] - path_map[i][j] <= 1:  # left
        neighbours.append((i-1, j))

    if i+1 < num_rows and path_map[i+1][j] - path_map[i][j] <= 1:  # right
        neighbours.append((i+1, j))

    if j-1 >= 0 and path_map[i][j-1] - path_map[i][j] <= 1:  # up
        neighbours.append((i, j-1))

    if j+1 < num_colunms and path_map[i][j+1] - path_map[i][j] <= 1:
        neighbours.append((i, j+1))  # down

    return neighbours


def find_min_steps(start):
    queue = [start]
    done = set()
    path_len = 0
    reached = False

    while len(queue) > 0:
        new_nbrs = []
        for point in queue:
            done.add(point)
            i, j = point
            nbrs = find_neighbours(i, j)

            for nbr in nbrs:
                if nbr not in done:
                    new_nbrs.append(nbr)        

        if end in new_nbrs:
            path_len += 1
            reached = True
            break
        else:
            queue = list(set(new_nbrs))

        path_len += 1

    if not reached:
        path_len = num_rows * num_colunms

    return path_len 


print(find_min_steps(start))  # part 1


starting_points = []
for r in range(num_rows):
    for c in range(num_colunms):
        if path_map[r][c] == 1:
            start = (r, c)
            starting_points.append(start)


steps = []
for point in starting_points:
    min_steps = find_min_steps(point)
    steps.append(min_steps)

print(min(steps))  # part 2
