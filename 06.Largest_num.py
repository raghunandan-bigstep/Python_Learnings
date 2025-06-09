# python program to find largest number from three numbers entered by user

def find_largest(a, b, c):
    if a == b == c:
        return "All three numbers are equal."
    elif a == b and c != a:
        if c > a:
            return (f"{c} is the largest. {a} and {b} are equal")
        else:
            return (f"{a} and {b} are equal and larger than {c}")
    elif a == c and b != a:
        if b > a:
           return (f"{b} is the largest. {a} and {c} are equal")
        else:
            return (f"{a} and {c} are equal and larger than {b}")
    elif b == c and a != b:
        if a > b:
            return (f"{a} is the largest. {b} and {c} are equal")
        else:
            return (f"{b} and {c} are equal and larger than {a}")
    else:        
        largest = max(a, b, c)
        return (f"The largest amonge three numbers is: {largest}")


try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    result = find_largest(a, b, c)
    print(result)

except ValueError:
    print("Please enter valid integers.")
except Exception as e:
    print(f"An error occurred: {e}")
