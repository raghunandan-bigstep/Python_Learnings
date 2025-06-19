# write a recursive function in python to compute nth fibonacci number
def fibonacci(n):
    if n <= 0:
        return f"Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
try: 
    user_input = input("Enter number (n) to get the nth Fibonacci number: ").strip()

    if user_input == "":
        print("Input cannot be empty. Please enter a valid positive integer.")
    else:
        try:
            n = int(user_input)
            result = fibonacci(n)
            print(f"The {n}th Fibonacci number is: {result}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
    
