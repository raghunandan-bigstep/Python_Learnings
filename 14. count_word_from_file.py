# python program to reas a text file and count the numbers of word 

filename = "user_input.txt"

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)            
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

# Write text to the file
try:
    with open(filename, 'w') as file:
        print("Enter text to write to the file (type 'END' to finish):")         
        while True:
            text_value = input()
            if text_value.strip().upper() == 'END':
                break
            file.write(text_value + '\n')         
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

# Count the words in the written file
print(f"\nTotal number of words in '{filename}': {count_words(filename)}")
