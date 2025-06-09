# python program to print fibonacci series up to nth term

def fibonacci(n):
    fib_series = [] # empty list to store the series
    a = 0
    b = 1
    for i in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

try:
    n = int(input("Enter the number of terms: "))
    if n <= 0:
        print("Please enter a number greater than 0.")
    else:
        series = fibonacci(n)
        print(f"Fibonacci series up to the {n}th term: {series}")
        
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except Exception as e:
    print("An error occurred:", str(e))
