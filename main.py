
class Calculator:
    def __init__(self):
        self.init: float = 0.

    def add(self, number: float): #number is a user input
        self.init += number 
        return self.init

    def substract(self, number: float):
        self.init -= number
        return self.init

    def multiply(self, number: float):
        self.init *= number
        return self.init

    def divide(self, number: float):
        self.init /= number
        if number == 0:
            print("Error, you can't divide by 0")
        return self.init

    def get(self):
        print("Current number: ", self.init)
    
    def reset(self):
        self.init: float = 0.
        return self.init 
    


''''
obj = Calculator()

obj.add(float(5))
print("Added number: ", self.init)

obj.substract(float(10))
print("Substracted number: ", self.init)

obj.reset()
obj.multiply(float(-10))
print("Multiplied number: ", self.init)

obj.divide(float(5))
print("Divided number: ", self.init)

obj.get()
'''

