class oops:

    standard = 12

    def __init__(self):
        self.age , self.name = 18,'Devesh'

    @classmethod
    def returnclas(cls):
        return cls.standard

    @staticmethod
    def info():
        print ('Static method')

obj1 = oops()
obj2 = oops()

obj1.standard = 11
oops.standard = 13
obj2.standard = 14


#print(obj1.age,obj1.name,obj1.returnclas())
#print(obj2.age,obj2.name,obj2.standard)


print(oops.returnclas())
#print(obj2.standard)

obj2.info()