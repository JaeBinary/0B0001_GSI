for i in range(3) : #range(0, 3, 1)
    for j in range(2) : #range(0, 2, 1)
        print("난생처음은 쉽습니다.^^ (i값 : %d, j값 : %d)" %(i, j))
print("")

for i in range(2, 10, 1) :
    for j in range(1, 10, 1) :
        print("%d x %d = %d" %(i, j, i*j))
print("")

for i in range(2, 10, 1) :
    print("%d단 : " %(i), end='')
    for j in range(1, 10, 1) :
        print("\t%d x %d = %2d" %(i, j, i*j), end='')
    print("")
print("")

for i in range(1, 10, 1) :
    for j in range(2, 10, 1) :
        print("%d x %d = %d" %(j, i, j*i), end = '\t')
    print("")
