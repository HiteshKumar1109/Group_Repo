def division(num1, num2):
    if num2 == 0:
        print("Division by zero is not allowed.")
        return

    print(f"Simple Division results : {num1 / num2}.")
    print(f"Floor Division equals : {num1 // num2}.")
def multiplication(num1, num2):
    print("Multiplication of", num1, "and", num2, "is:", num1 * num2)

def power(num1, num2):
    print(f"{num1} raised to {num2} :",num1 ** num2)

def modulus(num1, num2):
    print(f"{num1} mod {num2} :",num1 % num2)

def subtraction(num1,num2):
    print("Subtraction of", num1, "and", num2, "is:", num1 - num2)

print("""
--------------Calculator Using Python--------------
    """)

num1 = int(input("Enter Number 1:"))
num2 = int(input("Enter Number 2:"))

print("""\nOperations:
1) Addition
2) Subtraction
3) Multiplication
4) Division/Floor Division
5) Power
6) Modulus
      """)


op = int(input("Enter Number For Operation:"))
match(op):
    case 1:
        addition(num1,num2)

    case 2:
        subtraction(num1,num2)

    case 3:
        multiplication(num1,num2)

    case 4:
        division(num1,num2)

    case 5:
        power(num1,num2)

    case 6:
        modulus(num1,num2)

    case _:
        print("Enter Valid Number!")
