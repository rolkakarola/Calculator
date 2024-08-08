
print("\n------ Calculator ------\n\n")

class Calculator:
    def __init__(self):
        self.init = float(0) 

    def add(self, number): #number is a user input
        self.init += number 
        print("Added number: ", self.init)
        return self.init

    def substract(self, number):
        self.init -= number
        print("Substracted number: ", self.init)
        return self.init

    def multiply(self, number):
        self.init *= number
        print("Multiplied number: ", self.init)
        return self.init

    def divide(self, number):
        self.init /= number
        print("Divided number: ", self.init)
        return self.init

    def get(self):
        print("Current number: ", self.init)
    
    def reset(self):
        self.init = float(0)
        return self.init 

obj = Calculator()

obj.add(float(5))
obj.substract(float(10))
obj.reset()
obj.multiply(float(-10))
obj.divide(float(5))
obj.get()



