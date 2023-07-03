import subprocess

# Define a function to burn an image to SSD
def burn_image_to_ssd(chosen_directory_path_files):
    while True:
        user_input2 = input("\nEnter the number of the image you would like to access: ")
        try:
            user_choice2 = int(user_input2)
            # If the choice is invalid
            if user_choice2 < 1 or user_choice2 > len(chosen_directory_path_files):
                print("Invalid image number. Please try again.")
            # If the choice is valid
            else:
                print("\nBurning is in progress!")
                # Get the name of the chosen image
                image_number = chosen_directory_path_files[user_choice2-1]
                # Run the commands to burn the image to SSD
                command1 = ["sudo", "dd", "if=" + image_number, "of=/dev/nvme0n1"]
                command2 = ["echo", "-e", "\\n"]
                subprocess.run(command1)
                subprocess.run(command2)
                print("Thank you for burning")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
