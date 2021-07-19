#Calculator
from replit import clear
import art
logo = art.logo
print(logo)
def add(n1,n2):
    return n1 + n2

def divide(n1,n2):
    return n1 / n2

def multiply (n1,n2):
    return n1 * n2

def subtract (n1,n2):
    return n1 - n2

def calculator():
    operations = {
        "+":add,
        "-":subtract,
        "/":divide,
        "*":multiply
    }
    q = True
    new_calc = ''
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
            print(symbol)
    while q:
        num2 = int(input("What's the second number?: "))
        operation_symbol = input("Pick an operation from the line above: ")
        hold_answer= operations[operation_symbol]
        answer = hold_answer(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        new_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: \n")
        if new_calc == 'y':
            num1 = answer
        else:
            q = False
            clear
            calculator()


calculator()
