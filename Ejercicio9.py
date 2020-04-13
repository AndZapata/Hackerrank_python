def conditions(in_commands, new_list):
    for x in in_commands:
        if x[0] == "insert":
            new_list.insert(int(x[1]), int(x[2]))
        elif x[0] == "append":
            new_list.append(int(x[1]))
        elif x[0] == "remove":
            new_list.remove(int(x[1]))
        elif x[0] == "pop":
            new_list.pop()
        elif x[0] == "reverse":
            new_list.reverse()
        elif x[0] == "sort":
            new_list.sort()
        elif x[0] == "print":
            print(new_list)
        else:
            print("Command incorrect")


if __name__ == '__main__':
    N = int(input())
    in_commands = []
    new_list = []

    for _ in range(N):
        commands = input().split()
        in_commands.append(commands)

    conditions(in_commands, new_list)
