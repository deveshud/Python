class x:

    def __init__(self,ram,hd):
        self.ram = ram
        self.hd = hd

    def config(self):
        #print ('Config is 1GB RAM, 8 GB Harddisk')
        print ('Config is ',self.ram,' ram ',self.hd,' hardisk ')


obj1 = x(1,8)
obj2 = x(2,16)

obj1.config()
obj2.config()


