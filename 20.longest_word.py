#python program to find the longest word in a sentence entered by the user

def find_longest_word(sentence):
    words = sentence.split()
    if not words:
        return None
    longest_word = max(words, key=len)
    return longest_word


try:
    sentence = input("Enter a sentence: ").strip()
    if not sentence:
        print("Invalid input! Please re-enter a sentence")
    else:
       
        longest_word = find_longest_word(sentence)
        if longest_word:
            print("The longest word is:", longest_word)
        else:
            print("No words found in the sentence")
except Exception as e:
    print("An error occurred:", str(e))