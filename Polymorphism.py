# Duck Typing


class pycharm:
    def execute(self):
        print('EXECUTE')
        print('COMPILING')

class Conda:
    def execute(self):
        print('CONDA')
        print('EXECUTE')
        print('COMPILING')

class basic:
    def editor(self,ide):
        print('The ide is of class',type(ide))
        ide.execute()

obj = basic()
py = pycharm()
co = Conda()
obj.editor(py)
obj.editor(co)


# OPERATOR OVERLOADING

a,b = '1','2'
#print(int.__add__(a,b))
print(str.__add__(a,b))


class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        #self.m1 = int(input('Enter marks 1'))
        #self.m2 = int(input('Enter marks 2'))

    def __add__(self, other):

        s3 = Student(self.m1, self.m2)
        s3.m1 = s3.m1 + other.m1
        s3.m2 = s3.m2 + other.m2
        s3 = Student(s3.m1,s3.m2)
        return s3

    def display(self):
        print(self.m1 , ' ', self.m2)

    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)

s1  = Student(10,20)
s2  = Student(30,40)
s3 = s1 + s2
s3.display()
print(s1.m1,' ',s2.m1,' ',s3.m1)
print(s1.m2,' ',s2.m2,' ',s3.m2)

#print(s1)
# This thing prints the address of the object s1

# Now I have overridden the str method which is called by default , therefore calling the print method using the class obejct will call the overridden
# method of the class __str__ that is
print(s1)
print(s2)
print(s3)