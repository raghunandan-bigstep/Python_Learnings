# Python program to sort a list of tuples based on the second element of each tuple.
   
def sorting_in_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

try:
    tuples_list = []

    while True:
        num = input("How many tuples do you want to enter? ").strip()

        if not num.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        num = int(num)  # ✅ Convert to integer here

        if num == 0:
            print("You have to enter a number greater than zero.")
            continue
        else:
            break

    for i in range(num):  # ✅ Now num is an integer
        while True:
            element = input(f"Enter tuple {i+1} as two numbers separated by space: ").strip().split()

            if len(element) != 2:
                print("Please enter exactly two numbers.")
                continue

            try:
                tuple_pair = (int(element[0]), int(element[1]))
                tuples_list.append(tuple_pair)
                break
            except ValueError:
                print("Please enter valid integers.")

    sorted_list = sorting_in_tuples(tuples_list)
    print("Sorted list:", sorted_list)

except Exception as e:
    print(f"An error occurred: {e}")
