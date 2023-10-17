# UCID: SV925
# Date: 10/16/23 08:35

class MyCalc:
    def __init__(self):
        self.ans = 0  # Initialize the answer to 0

    def addition(self, num1, num2):
        try:
            result = num1 + num2
            self.ans = result
            return result
        except TypeError:
            return "Invalid input. Please provide valid numbers."
# UCID: SV925
# Date: 10/16/23 09:01
# This describes the addition function of the two numbers will be popped up on Result for example 2 + 3 Result: 5.0   

    def subtract(self, num1, num2):
        try:
            result = num1 - num2
            self.ans = result
            return result
        except TypeError:
            return "Invalid input. Please provide valid numbers."
# UCID: SV925
# Date: 10/16/23 09:10
# This describes the Subtraction function of the two numbers will be popped up on Result for example 5 - 3 Result: 2.0 

    def multiply(self, num1, num2):
        try:
            result = num1 * num2
            self.ans = result
            return result
        except TypeError:
            return "Invalid input. Please provide valid numbers."
# UCID: SV925
# Date: 10/16/23 09:14
# This describes the Multiplication function of the two numbers will be popped up on Result for example 5 * 3 Result: 15.0 

    def divide(self, num1, num2):
        try:
            if num2 == 0:
                return "Cannot divide by zero."
            result = num1 / num2
            self.ans = result
            return result
        except (TypeError, ZeroDivisionError):
            return "Invalid input or division by zero. Please provide valid numbers."
# UCID: SV925
# Date: 10/16/23 09:17
# This describes the Division function of the two numbers will be popped up on Result for example 6 / 3 Result: 2.0 

def main():
    calculator = MyCalc()
    while True:
        user_input = input("Enter an expression (e.g., '2 + 2' or 'ans * 2'): ")
        if user_input.lower() == "quit":
            break

        try:
            if "ans" in user_input:
                parts = user_input.split()
                operator = parts[1]
                num2 = float(parts[2])
                if operator == "+":
                    print("Result:", calculator.addition(calculator.ans, num2))
                elif operator == "-":
                    print("Result:", calculator.subtract(calculator.ans, num2))
                elif operator == "*":
                    print("Result:", calculator.multiply(calculator.ans, num2))
                elif operator == "/":
                    print("Result:", calculator.divide(calculator.ans, num2))
                else:
                    print("Invalid operator. Please use +, -, *, or /.")
            else:
                parts = user_input.split()
                num1 = float(parts[0])
                operator = parts[1]
                num2 = float(parts[2])
                if operator == "+":
                    print("Result:", calculator.addition(num1, num2))
                elif operator == "-":
                    print("Result:", calculator.subtract(num1, num2))
                elif operator == "*":
                    print("Result:", calculator.multiply(num1, num2))
                elif operator == "/":
                    print("Result:", calculator.divide(num1, num2))
                else:
                    print("Invalid operator. Please use +, -, *, or /.")
        except (ValueError, IndexError):
            print("Invalid input format. Please use 'number operator number'.")

if __name__ == "__main__":
    main()
