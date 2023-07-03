# NVMe Image Burner

## Overview
This project, written in Python, provides a command-line interface for burning disk images onto a NVMe chip. The scripts utilize a variety of built-in Python libraries to interact with the user, list directories, and perform the actual image burning process.

## Functionality
1. The application begins by verifying the presence of a specific NVMe disk on the system using `fdisk`.
2. Once the disk is confirmed, the program presents the user with a list of directories from a predetermined location.
3. The user is then prompted to choose a sub-directory from this list.
4. After the sub-directory is chosen, its contents are displayed, enabling the user to select a disk image file to be burned onto the NVMe SSD.
5. With a valid image selection, the `dd` command is invoked to burn the selected disk image onto the NVMe SSD.

**Please note:** This program requires superuser permissions (sudo) as it needs to access system disks and perform write operations.

## Usage
To run the project:

1. Navigate to the project directory in your terminal.
2. Execute the command: `sudo python3 main.py` or create a bash file with that command.
    To do that, you can create a file called burning.sh . 
    In the file write the following bash lines. 
        1) clear
        2) sudo python3 main.py   *** You should write the absolute file path where you store the directory and execute the file.
3. Follow the on-screen prompts to select a directory and an image to burn.

## Purpose
This project was developed to simplify and automate the process of burning disk images onto NVMe disks. It's especially useful for users who frequently need to write disk images to NVMe's and prefer a guided process to doing so manually. A basic understanding of directories and file navigation on Unix-like systems is required to effectively use this program.
