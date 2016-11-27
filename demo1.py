list = []

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
        position = int(split_it[1])
        value = int(split_it[2])
        l2 = list[position:]
        # l1 = list[:position]
        # l1.append(value)
        list = list[:position]
        list.append(value)
        list = list + l2
        # list.append(int(split_it[2]))

i = int(input().strip())

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