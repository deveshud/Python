def topten():

    n = 1

    while n<=10:
        yield n**2
        n+=1


it = topten()

for i in it:
    print(i)
    print(it.__next__())