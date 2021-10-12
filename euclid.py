import sys

a, b = int(sys.argv[1]), int(sys.argv[2])

table = [[a, 1, 0, ''], [b, 0, 1, a // b]]

i = 2
while True:
    if table[i - 2][0] % table[i - 1][0] == 0:
        break
    r = table[i - 2][0] % table[i - 1][0]
    x = table[i - 2][1] - (table[i - 1][1] * table[i - 1][3])
    y = table[i - 2][2] - (table[i - 1][2] * table[i - 1][3])
    q = table[i - 1][0] // r
    table.append([r, x, y, q])
    i += 1

for _ in table:
    print("{:<5}{:>5}{:>5}{:>5}".format(*_))
