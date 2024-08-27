
# mypy - checks the consitency of the type, static type check

class Calculator:

    # expecting start_value to be float
    # expecting that the function returns None (setting up inital state)
    
    def __init__(self, start_value: float = 0) -> None: # Initializes the calculator
        self.current_value = start_value

    def add(self, number: float) -> None: # not returning any value, modyfing the iternal state
        self.current_value += number

    def substract(self, number: float) -> None: 
        self.current_value -= number

    def multiply(self, number: float) -> None:
        self.current_value *= number

    def divide(self, number: float) -> None:
        self.current_value /= number
        if number == 0:
            raise ValueError("Error, you can't divide by 0") # expection

    def get(self) -> float:
        return self.current_value
    
    def reset(self) -> None:
        self.current_value = 0 
    
'''
obj = Calculator()

obj.add(5)

obj.substract(10)

obj.multiply(-10)

obj.divide(5)

obj.get()
obj.reset()
'''