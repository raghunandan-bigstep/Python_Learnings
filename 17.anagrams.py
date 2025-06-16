# python Program to check if two strings are anagrams:

def check_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

try:
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")
    
    if check_anagrams(string1, string2):
        print(f'"{string1}" and "{string2}" are anagrams.')
    else:
        print(f'"{string1}" and "{string2}" are NOT anagrams.')

except KeyboardInterrupt:
    print("\nInput interrupted by user.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
