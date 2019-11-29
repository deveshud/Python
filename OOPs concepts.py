class oops:
    def __init__(self):
        self.age , self.name = 18,'Devesh'

    def update(self):
        self.age = 20

    def compare(self,obj2):
        if self.age > obj2.age:
            print ('Self Greater')
            return True
        else:
            print(' Obj2 is greater')


obj1 = oops()
#oops.update(obj1)
obj1.update()
obj2 = oops()

if obj1.compare(obj2):
    print('Compared')
    print('333333')

if obj1.age < obj2.age:
    print('Greater')
else:
    print('Smaller')

print(obj1.age)
print(obj2.age)
