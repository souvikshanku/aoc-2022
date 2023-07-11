with open("inputs/p15.txt", "r") as f:
    content = f.read().splitlines()

# print(content)

sensor = []
beacon = []
Y = 2000000

for line in content:
    x, y = 0, 0  # for making pylint happy
    exec(line.split(":")[0][10:].replace(", ", "\n"))
    sensor.append((x, y))

    exec(line.split("is at ")[1].replace(", ", "\n"))
    beacon.append((x, y))

y_beacons = set([1 for b in beacon if b[1] == Y])


def get_non_beacon_pos(Y):
    ans = []

    for idx in range(len(sensor)):
        bx, by = beacon[idx]
        sx, sy = sensor[idx]

        dist = abs(sx - bx) + abs(sy - by)

        x, y = sx, Y
        while True:
            if (abs(x - sx) + abs(y - sy)) <= dist:
                ans.append((x, y))
                x -= 1
            else:
                break

        x, y = sx, Y
        while True:
            if (abs(x - sx) + abs(y - sy)) <= dist:
                ans.append((x, y))
                x += 1
            else:
                break
    return set(ans)

ans = get_non_beacon_pos(Y)
print(len(ans) - len(y_beacons))


# ans = set(ans)
# for y in range(4000001):
#     non_pos = get_non_beacon_pos(y)
#     if len(non_pos) != 4000000:
#         print(y)

for y in range(4000001):
    for z in range(4000001):
        x = 2