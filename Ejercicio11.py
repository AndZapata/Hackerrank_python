def mutations(in_commands, integer_list):
    for i in in_commands:
        if i[0] == "update":
            integer_list.update(set(i[2]))
        if i[0] == "intersection_update":
            integer_list.intersection_update(set(i[2]))
        if i[0] == "symmetric_difference_update":
            integer_list.symmetric_difference_update(set(i[2]))
        if i[0] == "difference_update":
            integer_list.difference_update(set(i[2]))
    return (sum(integer_list))


if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    N = int(input())
    commands=[]
    in_commands=[]
    for i in range(2 * N):
        if (i % 2) == 0:
            commands = input().split()
        elif (i % 2) == 1:
            partial = list(map(int, input().split()))
            commands.append(partial)
            in_commands.append(commands)
    result = mutations(in_commands, set(integer_list))
    print(result)