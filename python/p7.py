with open('inputs/p7.txt', 'r') as f:
    output = f.read()


array = []
stack = [0]
add_upto_pos = -1


for line in output.split("\n"):
    if line.startswith("$ cd .."):
        latest_size = stack[add_upto_pos]
        array.append(latest_size)
        stack.pop(add_upto_pos)
        add_upto_pos -= 1

    elif line.startswith("dir "):
        stack.append(0)

    elif line.startswith("$ cd "):
        add_upto_pos += 1

    elif line.startswith("$ ls") or line == '':
        pass

    else:
        size = int(line.split(" ")[0])
        stack = [
            stack[i] + size if i <= add_upto_pos else stack[i] for i in range(len(stack))
        ]


for elem in stack:
    array.append(elem)

ans = 0

for elem in array:
    if elem <= 100000:
        ans += elem

print(ans)


root_size = max(array)
space_required = 30000000 - (70000000 - root_size)

smallest_so_far = root_size
for elem in array:
    if elem >= space_required and elem <= smallest_so_far:
        smallest_so_far = elem

print(smallest_so_far)

