# python program to check wether a number is even or odd

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

try:
    num = int(input("Enter a number: "))
    result = check_even_odd(num)
    print(f"The number {num} is {result}.")
except ValueError:
    print("Please enter a valid integer.")
except Exception as e:
    print(f"An error occurred: {e}")



