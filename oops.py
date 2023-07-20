class Computer:

    def __init__(self, cpu , ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("The config is:", self.cpu, self.ram)


comp1 = Computer('i5', 16)
comp2 = Computer('Ryzen 5', 8)
# print(type(comp1))

# Computer.config(comp1)

comp1.config()
comp2.config()
