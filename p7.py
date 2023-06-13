class Directory:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.size = 0

    def add_file_size(self, size):
        self.size += size
        if self.parent is not None:
            self.parent.add_file_size(size)


# root_dir = Directory('/', None)
# dir_a =  Directory('a', root_dir)
# dir_b = Directory('b', dir_a)

# dir_a.add_file_size(12)
# dir_b.add_file_size(10)
# root_dir.add_file_size(1000)

# print(f"{dir_b.size}, {dir_a.size}, {dir_a.parent.size}")


with open('inputs/p7.txt', 'r') as f:
    terminal_output = f.read().split("$ ls")


for i, ls_output in enumerate(terminal_output):
    if i == 0:
        _dir_root_dir = Directory('_root', None)
        root = _dir_root_dir
    else:
        root_name = terminal_output[i-1].split("\n")[-2].split(" ")[-1]
        if root_name == '/':
           root_name = "root_dir"

        exec(f"root = _dir_{root_name}")

    # print(ls_output)

    ls_output = ls_output.split("\n")

    for line in ls_output:
        line_split = line.split(" ")

        # print(line_split)

        if line_split[0] == "dir":
            exec(f"_dir_{line_split[1]} = Directory('{line_split[1]}', root)")
        elif line_split[0] in ["$", ""]:
            pass
        else:
            size = int(line_split[0])
            root.add_file_size(size)

    # print("--------------")



ans = 0

for stuff in dir():
    print(stuff)
    if stuff[:5] == '_dir_':
        # eval(f"print({stuff}.name, {stuff}.size)")
        if eval(f"{stuff}.size") <= 100000:
            exec(f"ans += {stuff}.size")

print(ans)