#python program that use list comprehension to square all even numbers in a list 

def square_even_numbers(my_list):
    even_squares = [num ** 2 for num in my_list if num % 2 == 0]
    if even_squares: 
     return even_squares 
    else :
        return "No even numbers in the list"

# test the function
try:
    my_list = []
    while True:
        num = input("How many numbers do you want to enter?\n ").strip()
        if not num.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        num = int(num)
        if num <= 0:
            print("You have to enter a number greater than zero.")
            continue
        else:
            break

    for i in range(num):
        while True:
            number = input(f"Enter number {i+1}: ").strip()
            try:
                number = int(number)
                my_list.append(number)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
except Exception as e:
    print(f"An error occurred: {e}")
    
                
result = square_even_numbers(my_list)
print(f"Result is: {result}")
