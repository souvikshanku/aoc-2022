with open("inputs/p13.txt", "r") as f:
    content = f.read()


def check(a, b):
    if a == b:
        return 0
    elif a < b:
        return 1
    return -1


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return check(left, right)
    elif isinstance(left, int) and isinstance(right, list):
        left = [left]
        return compare(left, right)
    elif isinstance(left, list) and isinstance(right, int):
        right = [right]
        return compare(left, right)
    else:
        try:
            for i in range(len(left)):
                if compare(left[i], right[i]) == -1:
                    return -1
                elif compare(left[i], right[i]) == 1:
                    return 1

            if len(left) == 0 and len(right) == 0:
                return 0
            elif len(left) < len(right):
                return 1
            else:
                return 0
        except IndexError:
            return -1


result = 0
for j, pair in enumerate(content.split("\n\n")):
    pair = pair.split("\n")
    list1 = eval(pair[0])
    list2 = eval(pair[1])
    if compare(list1, list2) != -1:
        result += j + 1

print(result)  # part 1


pos_1 = 1
pos_2 = 1
a = [[2]]
b = [[6]]


for j, pair in enumerate(content.split("\n\n")):
    pair = pair.split("\n")
    list1 = eval(pair[0])
    list2 = eval(pair[1])

    if compare(list1, a) == 1:
        pos_1 += 1
    if compare(list2, a) == 1:
        pos_1 += 1

    if compare(list1, b) == 1:
        pos_2 += 1
    if compare(list2, b) == 1:
        pos_2 += 1

print(pos_1 * (pos_2+1))  # part 2
