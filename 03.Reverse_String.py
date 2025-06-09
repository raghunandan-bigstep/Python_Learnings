# python program to reverse a given string.
try:
    str = input("Enter a string to reverse: ")
    reversed_string = str[::-1] #To reverse the string
    print("Reversed String:", reversed_string)        
except ValueError:
   print("Please try again by entering a Valid String.")  
except Exception as e:
    print(f"An error occurred: {e}")
    