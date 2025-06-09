# python program to check whether a number is prime or not
def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False        
    return True


try:
    num = int(input("Enter a number: "))
    if check_prime(num):
        print(f"The number {num} is prime.")
    else:
        print(f"The number {num} is not prime.")
except ValueError:
    print("Please enter a valid integer.")
except Exception as e:
    print(f"An error occurred: {e}")