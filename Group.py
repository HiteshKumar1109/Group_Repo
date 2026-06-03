def power(num1, num2):
    print(f"{num1} raised to {num2} :",num1 ** num2)

def modulus(ans, num):
    print(f"{num1} mod {num2} :",num1 % num2)


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


while(1):
    op = int(input("Enter Number For Operation:"))
    match(op):
        case 1:
            addition(num1,num2)   
            break

        case 2:
            subtraction(num1,num2)
            break

        case 3:
            multiplication(num1,num2)
            break

        case 4:
            division(num1,num2)
            break

        case 5:
            modulus(num1,num2)
            break

        case 6:
            power(num1,num2)

        case _:
            print("Enter Valid Number!")