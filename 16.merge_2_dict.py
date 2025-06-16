# python program to merge two dictionary into one 

# function to create a dictionary
def get_dict_by_user(dict_num):
    user_dict = {} # declare a dictionary
    while True:
        num = input(f"\nHow many key-value pairs do you want to enter for dictionary {dict_num}? ").strip()
        if not num.isdigit() or int(num) <= 0: # check if the input is a positive integer
            print("Please enter a valid positive integer.") 
            continue 
        num = int(num) # convert the input to integer
        break   
    
        # loop to get the key-value pairs
    for i in range(num): 
        
        while True: 
            key = input(f"Enter key {i+1} for dictionary {dict_num}: ").strip()
            if not key: # check if the key is not empty
                print("Key cannot be empty. Please enter a valid key.")
                continue
            if key in user_dict: # check if the key already exists
                print(f"The key '{key}' already exists. Please enter a unique key.")
                continue
            
            
            value = input(f"Enter value for key '{key}': ").strip()          
            if not value: # check if the value is not empty
                print("Value cannot be empty. Please enter a valid value.")
                continue

            user_dict[key] = value # add the key-value pair to the dictionary
            break  
    return user_dict            

 # function to merge two dictionaries
def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2} # use the dictionary unpacking operator to merge the two dictionaries

#-------Main Program-----------
try:
    print("Enter data for the first dictionary:")
    dict1 = get_dict_by_user(1)

    print("\nEnter data for the second dictionary:")
    dict2 = get_dict_by_user(2)

    merged_dict = merge_dictionaries(dict1, dict2)

    print("\nMerged Dictionary:")
    print(merged_dict)

except Exception as e:
    print(f"An error occurred: {e}")
