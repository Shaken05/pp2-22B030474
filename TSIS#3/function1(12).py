def histogram(List):
    for i in List:
        for j in range(i):
            print('*', end ="")
        print()

list1 = [4, 9, 7]
histogram(list1)
