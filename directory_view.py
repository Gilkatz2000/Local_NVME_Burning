import os
import time

# Define a function to print the contents of a directory
def print_directory_contents(directory_path):
    # List the contents of the directory
    directory_contents = os.listdir(directory_path)
    # Print the names and dates of the directory's contents
    print('{:>25} {:>38}'.format("Name", "Date"))
    for num, item_name in enumerate(directory_contents, start=1):
        creation_time = time.ctime(os.path.getctime(item_name))
        print('{:<5} {:<40} | {:>25}'.format(num, item_name, creation_time))
    return directory_contents

# Define a function to get the user's choice of directory
def get_user_directory_choice(directory_contents):
    while True:
        user_input = input("\nEnter the number of the directory you would like to access: ")
        try:
            user_choice = int(user_input)
            # If the choice is invalid
            if user_choice < 1 or user_choice > len(directory_contents):
                print("Invalid directory number. Please try again.")
            # If the choice is valid
            else:
                chosen_directory = directory_contents[user_choice - 1]
                print("You chose directory '{}'.\n".format(chosen_directory))
                return chosen_directory
        except ValueError:
            print("Invalid input. Please enter a number.")

