with open("inputs/p15.txt", "r") as f:
    content = f.read().splitlines()


sensor = []
beacon = []
Y = 2000000
# Y = 10

for line in content:
    x, y = 0, 0  # for making pylint happy
    exec(line.split(":")[0][10:].replace(", ", "\n"))
    sensor.append((x, y))

    exec(line.split("is at ")[1].replace(", ", "\n"))
    beacon.append((x, y))

y_beacons = set([1 for b in beacon if b[1] == Y])


def get_non_beacon_pos(Y):
    ans = set()

    for idx in range(len(sensor)):
        bx, by = beacon[idx]
        sx, sy = sensor[idx]

        dist = abs(sx - bx) + abs(sy - by)
        # print(dist)

        x, y = sx, Y
        while True:
            if (abs(x - sx) + abs(y - sy)) <= dist:
                ans.add((x, y))
                x -= 1
            else:
                break

        x, y = sx, Y
        while True:
            if (abs(x - sx) + abs(y - sy)) <= dist:
                ans.add((x, y))
                x += 1
            else:
                break

    return ans

ans = get_non_beacon_pos(Y)
print(len(ans) - len(y_beacons))  # part 1


imp_points = []
distances = []

for i in range(len(sensor)):
    x1, y1 = sensor[i]
    dist = abs(sensor[i][0] - beacon[i][0]) + abs(sensor[i][1] - beacon[i][1])
    distances.append(dist)

    c1 = [y1 - x1 + dist, y1 - x1 - dist]
    c2 = [y1 + x1 + dist, y1 + x1 - dist]

    for i in range(len(c1)):
        for j in range(len(c1)):
            imp_points.append(((c1[i]-c2[i])/2, (c1[i]+c2[j])/2))

    for j in range(i, len(sensor)):
        x1, y1 = sensor[j]
        dist = abs(sensor[j][0] - beacon[j][0]) + abs(sensor[j][1] - beacon[j][1])
    
        c3 = [y1 - x1 + dist, y1 - x1 - dist]
        c4 = [y1 + x1 + dist, y1 + x1 - dist]

        for i in range(len(c1)):
            for j in range(len(c4)):
                imp_points.append(((c1[i]-c4[i])/2, (c1[i]+c4[j])/2))
        
        for i in range(len(c2)):
            for j in range(len(c3)):
                imp_points.append(((c2[i]-c3[i])/2, (c2[i]+c3[j])/2))



def check_validity(x, y):
    limit = 4000000
    if (x < 0 or x > limit) or (y < 0 or y > limit):
        return False
    for i in range(len(sensor)):
        dist = abs(sensor[i][0] - x) + abs(sensor[i][1] - y)

        if dist <= distances[i]:
            return False

    return True

for point in imp_points:
    x, y = point

    if check_validity(x-1, y):
        ans2 = (x-1 * 4000000 + y)
        break

    if check_validity(x-1, y+1):
        ans2 = (x-1 * 4000000 + y-1)
        break

    elif check_validity(x, y+1):
        ans2 = (x * 4000000 + y+1)
        break

    elif check_validity(x+1, y+1):
        ans2 = (x * 4000000 + y+1)
        break

    elif check_validity(x+1, y):
        ans2 = (x+1 * 4000000 + y)
        break

    elif check_validity(x+1, y-1):
        ans2 = (x+1 * 4000000 + y-1)
        break

    elif check_validity(x, y-1):
        ans2 = (x * 4000000 + y-1)
        break

    elif check_validity(x-1, y-1):
        ans2 = (x-1 * 4000000 + y-1)
        break

print(int(ans2))  # part 2