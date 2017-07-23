
def doWhatISay(input_command, list):
    split_it = input_command.split(" ")

    if(split_it[0] == 'print'):
        print(list)
    elif(split_it[0] == 'sort'):
        list.sort()
    elif(split_it[0] == 'reverse'):
        list.reverse()
    elif(split_it[0] == 'pop'):
        if len(list) != 0:
            del list[len(list) - 1]
    elif(split_it[0] == 'append'):
        list.append(int(split_it[1]))
    elif(split_it[0] == 'remove'):
        del list[list.index(int(split_it[1]))]
    elif(split_it[0] == 'insert'):
        print(list)
        position = int(split_it[1])
        value = int(split_it[2])
        print(position)
        print(value)
        l1 = list[:position]
        l2 = list[position:]
        print(l1)
        print(l2)
        # print(l2)
        # l1 = list[:position]
        # l1.append(value)
        # list = list[:position]
        # print(list)
        l1.append(value)
        print(l1)
        print(l2)
        # print(list)

        # list = list + l2
        # print(list)
        # list.append(int(split_it[2]))

i = int(input().strip())
list = []

for i in range(i):
    doWhatISay(input(), list)

# a = [1, 3, 5, 6, 7]
#
# def doIt(yes):
#     if(yes == 'yes'):
#         a.append(67)
#         print(a)
#
# doIt('yes')