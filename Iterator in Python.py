#nums = [1,2,3,4,5,6,7,8,9]

#it = iter(nums)
#for i in  nums:
#    print(it.__next__())

# CREATING YOUR OWN ITERATOR

class toptep:
    def __init__(self):
        self.num  = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.num < 10:
            self.num += 1
            return self.num

        else:
            exit()

obj = toptep()

it = obj.__iter__()
print(it.__next__())
while True:
    print(obj.__next__())