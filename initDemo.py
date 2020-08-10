class Computer:

    def __init__(self, cpu, ram): #construct in python
        print("In Init method")
        self.cpu =cpu
        self.ram = ram
        
    def config(self):
        print("Config: ", self.cpu, self.ram)

'''
com1 = Computer()
print(type(com1))

Computer.config(com1)
'''
com1 = Computer("i5",8)
com2 = Computer("i7",4)
com1.config()
com2.config()
