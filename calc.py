"""
Mini Project: Simple Console Calculator (Beginner Friendly)

Features:
- Class based calculator
- Basic operations
- Loop for repeated use
- History stored in a list
- Save and load history using a text file
- Simple error handling
"""
HISTORY_FILE = "calc_history.txt"

class Calculator:

    def __init__(self):
        self.history = self.load_history()

    def load_history(self):
        data = []
        try:
            with open(HISTORY_FILE, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        data.append(line)
        except FileNotFoundError:
            pass
        return data

    def save_history(self):
        with open(HISTORY_FILE, "w") as f:
            for item in self.history:
                f.write(item + "\n")

    def get_number(self, message):
        while True:
            value = input(message)
            try:
                return float(value)
            except ValueError:
                print("Enter a valid number")
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Cannot divide by zero")
            return None
        
    def show_history(self):
        if not self.history:
            print("No history available.")
            return
        print("\nHistory:")
        for item in self.history:
            print(item)    
    
    
    def run(self):
        while True:
            print("\nSimple Console Calculator")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. View History")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice in ['1', '2', '3', '4']:
                num1 = self.get_number("Enter first number: ")
                num2 = self.get_number("Enter second number: ")

                if choice == '1':
                    result = self.add(num1, num2)
                    operation = f"{num1} + {num2} = {result}"
                elif choice == '2':
                    result = self.subtract(num1, num2)
                    operation = f"{num1} - {num2} = {result}"
                elif choice == '3':
                    result = self.multiply(num1, num2)
                    operation = f"{num1} * {num2} = {result}"
                elif choice == '4':
                    result = self.divide(num1, num2)
                    if result is not None:
                        operation = f"{num1} / {num2} = {result}"
                    else:
                        continue

                print(operation)
                self.history.append(operation)

            elif choice == '5':
                print("\nHistory:")
                for item in self.history:
                    print(item)

            elif choice == '6':
                self.save_history()
                print("Goodbye!")
                break
            else:
                print("Invalid option, try again.") 
                
  
def main():
    calc = Calculator()
    calc.run()
    
    while True:
        print("\nSimple Console Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View History")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice in ['1', '2', '3', '4']:
            num1 = calc.get_number("Enter first number: ")
            num2 = calc.get_number("Enter second number: ")

            if choice == '1':
                result = calc.add(num1, num2)
                operation = f"{num1} + {num2} = {result}"
            elif choice == '2':
                result = calc.subtract(num1, num2)
                operation = f"{num1} - {num2} = {result}"
            elif choice == '3':
                result = calc.multiply(num1, num2)
                operation = f"{num1} * {num2} = {result}"
            elif choice == '4':
                result = calc.divide(num1, num2)
                if result is not None:
                    operation = f"{num1} / {num2} = {result}"
                else:
                    continue

            print(operation)
            calc.history.append(operation)

        elif choice == '5':
            print("\nHistory:")
            for item in calc.history:
                print(item)

        elif choice == '6':
            calc.save_history()
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")       
            
            
            
if __name__ == "__main__":
    main()                     