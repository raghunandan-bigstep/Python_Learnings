# write a python program to check weather a string entered by user is palindrome or not

try:
    Str = input("Enter a string to check weather it is palindrome or not: ")
    Str = Str.replace(" ", "")  # remove spaces from the string
    Str = Str.lower()  # convert the string to lowercase
    if Str == Str[::-1]:  # check if the string is equal to its reverse
        print("Congrats ! string  entered by you is a palindrome")
    else:
        print("Sorry ! string entered by you is not a palindrome")
except ValueError :
    print("Invalid input") 
except Exception as e:
    print(f"An error occurred: {e}")
    


