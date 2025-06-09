# python program to count Vowel in a string entered by user

def count_vowels(str):
    vowels = 'aeiou'
    count = 0
    for char in str:
        if char in vowels:
            count += 1
    return count

try:
    str = input("Enter a string: ")
    str = str.replace(" ", "") 
    str = str.lower()
    print("Number of vowels in the string: ", count_vowels(str))
except ValueError:
   print("Please try again by entering a Valid String.")  
except Exception as e:
    print("An error occurred: ", str(e))