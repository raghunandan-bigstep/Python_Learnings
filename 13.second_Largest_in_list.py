# python program to find the second largest element in a list

def second_largest(my_list):
    if len(set(my_list)) < 2:
        return None  # Not enough unique elements
    sorted_list = sorted(set(my_list), reverse=True)
    print (f"Sorted list with unique elements: {sorted_list}")
    return sorted_list[1]

try:
    my_list = []

    while True:
        num = input("How many numbers do you want to enter? ").strip()

        if not num.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        num = int(num)

        if num <= 0:
            print("You have to enter a number greater than zero.")
            continue
        else:
            break

    for i in range(num):
        while True:
            number = input(f"Enter number {i+1}: ").strip()
            try:
                number = int(number)
                my_list.append(number)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    result = second_largest(my_list)

    if result is None:
        print("Second largest element not found (not enough unique elements).")
    else:
        print("Second largest element is:", result)

except Exception as e:
    print(f"An error occurred: {e}")

