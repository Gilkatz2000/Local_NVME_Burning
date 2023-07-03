import os
from detect_ssd import check_disk_exists
from directory_view import print_directory_contents, get_user_directory_choice
from burn import burn_image_to_ssd
import math

# Define the main function
def main():
        # Check if the disk exists
        check_disk_exists("/dev/nvme0n1")
        # Print an initial message for the user
        print("This program will allow you to burn your NVME. \nYou may Begin.")
        # Define the path for the directory
        directory_path = "/home/laduser/Desktop/Code/Burning/CI"
        # Change the working directory to the given path
        os.chdir(directory_path)

        # Get the contents of the directory
        directory_contents = print_directory_contents(directory_path)
        # Get user's choice of directory from the given contents
        chosen_directory = get_user_directory_choice(directory_contents)

        # Form the path of the chosen directory
        chosen_directory_path = "/home/laduser/Desktop/Code/Burning/CI/" + chosen_directory
        # Change the working directory to the chosen directory
        os.chdir(chosen_directory_path)
        # Get the contents of the chosen directory
        chosen_directory_path_files = print_directory_contents(chosen_directory_path)
        # Burn the image to SSD
        burn_image_to_ssd(chosen_directory_path_files)

# Call the main function
if __name__ == "__main__":
    main()
