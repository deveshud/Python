class oops:

    standard = 12

    def __init__(self):
        self.age , self.name = 18,'Devesh'



obj1 = oops()
obj2 = oops()

#obj1.standard = 11
oops.standard = 13


print(obj1.age,obj1.name,obj1.standard)
print(obj2.age,obj2.name,obj2.standard)


