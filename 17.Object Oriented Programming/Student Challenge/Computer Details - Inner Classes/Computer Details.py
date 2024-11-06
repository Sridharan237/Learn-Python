# python program to implement outer class computer and inner classes (CPU, OS)

# class for computer
class Computer:
    
    def __init__(self, name, cpu_make, os_name):
        self.name = name
        self.cpu = self.CPU(cpu_make)
        self.os = self.OS(os_name)
        
    def __str__(self):
        return f'--- Computer Details --- \nName : {self.name} \nCPU : {self.cpu.getMake()} \nOS : {self.os.get_name()}'
    
    # class for CPU
    class CPU:
        
        def __init__(self, make):
            self.__make = make
        
        def getMake(self):
            return self.__make
    
    # class for OS
    class OS:
        
        def __init__(self, name):
            self.__name = name
        
        def get_name(self):
            return self.__name

# creating object for Computer class
computer1 = Computer('Dell', 'Intel', 'Windows')

print(computer1)