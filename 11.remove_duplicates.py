# python program to remove duplicates from a list entered by user 
# sets is best data structure to remove duplicates in python

def remove_duplicates(user_list):
    return list(set(user_list))

user_list = []

try:
    while True:
        num = input("How many elements do you want to enter to check program execution? ").strip()

        if num == "":
            print("You entered empty string. you need to enter a valid integer")            
        elif not num.isdigit() or int(num) <= 0:
            print("sorry! you need to enter a positive integer which should be greater than zero")
        else:
            num = int(num)
            break 

    for i in range(num):
        while True:
            input_element = input(f"Enter element {i+1}: ").strip()

            if input_element == "":
                print("Invalid String . Please enter a valid string.")               
            else:
                user_list.append(input_element)
                break

    print("\n Original List:", user_list)
    print("List after removing duplicates:", remove_duplicates(user_list))

except ValueError :
    print ("Invalid Input. Please enter a valid integer for number of elements and a valid string for each element")             
except Exception as e:
    print("An error occurred:", str(e))
