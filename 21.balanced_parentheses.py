#write a function in python to check if a string has balanced parantheses
def balanced_parentheses(s):
    stack = []
    result = False  

    for char in s:
        if char == '(':
            stack.append(char)
            result = True
        elif char == ')':
            result = True
            if not stack:
                return False
            stack.pop()

    return result and not stack  

try:
    while True:
        user_input = input("Enter a string with parentheses (or type q to quit):\n").strip()

        if user_input.lower() in ("q"):
            print("program exit! thanks have a nice day.")
            break

        if not user_input:
            print("Please enter a string with parentheses.")
            continue

        if balanced_parentheses(user_input):
            print("The parentheses are balanced.")
        else:
            print("The parentheses are not balanced.")
except Exception as e:
    print(f"An error occurred: {e}")
