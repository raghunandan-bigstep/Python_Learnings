#python program to count the freq of char in a string using dictionary
# Take string input from the user

s = input("Enter a string: ")

# Initialize empty dictionary to store frequencies
d = {}

# Count frequency of each character
for char in s:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1

# Print the final dictionary
print("Character frequencies:", d)
