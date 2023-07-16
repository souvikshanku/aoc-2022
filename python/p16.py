with open("inputs/p16.txt", "r") as f:
    content = f.read()

tunnel = {}
rate = {}

for line in content.split("\n"):
    key = line[6:8]
    if "tunnel leads to valve" in line:
        value = [line[-2:]]
    else:
        value = line.replace(" ", "").split("valves")[1].split(",")
    
    tunnel[key] = value
    rate[key] = int(line.split(";")[0].split("=")[-1])

print(tunnel)
print(rate)

pressure_list = []
max_p = 0
done = {key: 0 for key in rate}


def traverse(key, pressure, path, time):
    global max_p
    time += 1
    if time >= 30:
        # pressure_list.append(pressure)
        if pressure > max_p:
            max_p = pressure
        # print(path, pressure, time)
        return

    if rate[key] > 0 and key not in path:
        time += 1  # open the valve
        pressure += rate[key] * (30 - time)

    path.add(key)
    nbrs = tunnel[key]

    for nbr in nbrs:
        nbr_path = path.copy()
        nbr_time  = time
        nbr_pressure = pressure
        traverse(nbr, nbr_pressure, nbr_path, nbr_time)



traverse("DD", pressure=0, path=set(), time=0)
print(max_p)
