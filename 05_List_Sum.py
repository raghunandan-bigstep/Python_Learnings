# python program to find the sum of all the elements in a list entered by the user

def sum_of_elements(numbers):
    return sum(numbers)
    
try:
    n = int(input("Enter how many number you want to enter: "))
    my_list = []
    for i in range(n):
        num = int(input(f"Enter element {i+1}: "))
        my_list.append(num)
    print(f"Sum of list is: {sum_of_elements(my_list)}")

except ValueError:
    print("Please enter valid integers only.")
except Exception as e:
    print(f"An error occurred: {e}")
