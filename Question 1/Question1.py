ops = ['5', '-2', '4', 'C', 'D', '9', '+', '+']

new_list = []
for i in range(len(ops)):
    if ops[i] == 'C':
        el = i-1
        new_list.pops(el)
    elif ops[i] == 'D':

        if ops[i-1].isdigit():
            el = i - 1
        else:
            el = i-2

        new_list.append(new_list[-1] * 2)
    elif ops[i] == '+':
        total = len(new_list)
        # print(f"first is {new_list[f]} and second is {new_list[s]}")
        new_list.append(new_list[-1] + new_list[-2])
    else:

        new_list.append(int(ops[i]))
print(sum(new_list))