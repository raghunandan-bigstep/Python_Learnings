# python program to print the multiplication table of a given number
try:
    num = int(input("Enter a number to print its multiplication table: "))
    for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
except ValueError:
    print("Please enter a valid integer.")
except Exception as e:
    print(f"An error occurred: {e}")