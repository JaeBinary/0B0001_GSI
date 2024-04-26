for i in range(1, 10, 1) :
    if i % 2 == 0 :
        print()
        continue
    for j in range(2, 10, 1) :
        print(j, 'x', i, '=', (j * i), '\t', end = '')
    print()
