a = ''
t = 'y'
out = ''
c = 0
if len(t) == 1:
    out = t
else:

    for i in range(len(a)):

        if a[i] == t[i]:
        # print(f' a[i] is {a[i]} and t[i] is {t[i]}')
            c += 1
            continue

        elif c == len(a):
            out = t[c+1]

        else:
            # print(f' a[i] is {a[i]} and t[i] is {t[i]}')
            test = t[i]
            count = a.count(test)
            countb = t.count(test)
            # print(test)
            # print(f'coundt {countb} counta {count}')
            if countb == count:
                continue
            else:
                out = t[i]
                break



if len(out) == 0:
    out = t[-1]


print(out)
