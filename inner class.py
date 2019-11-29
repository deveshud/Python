
class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        #self.count = 0

    def show(self):
        print(self.name,' ',self.rollno)


    class unique:
        def __init__(self,s1,s2,s3):
            self.s1,self.s2,self.s3 = s1,s2,s3

        def show(self):
            print(self.s1,' ',self.s2,' ',self.s3)

ob1 = student('Devesh',107)
ob2 = student('Abhishek',108)
ob3 = student('Pulkit',109)

lap1 = student.unique(1,2,3)
#lap2 = ob2.unique(self,4,5,6)
#lap3 = ob3.unique(self,7,8,9)

ob1.show()
ob1.lap1.show()
ob2.show()
ob3.show()


