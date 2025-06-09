# python program to find a factorial of a number entered by user

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Factorial is not Possible.")
    else:
        result = factorial(num)
        print(f"Factorial of {num} is, {result}")
except ValueError:
    print("Please enter a valid integer.")
except Exception as e:
    print("An error occurred: ", str(e))