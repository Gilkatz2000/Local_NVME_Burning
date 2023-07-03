import subprocess
import sys

# Define a function to check if a disk exists
def check_disk_exists(disk_name):
    # Run a subprocess to check the disk
    check_disk = subprocess.run(["fdisk", "-l"], capture_output=True, text=True)
    
    # If the subprocess run successfully
    if check_disk.returncode == 0:
        # If the disk is found
        if disk_name in check_disk.stdout:
            print(f"\nNVMe is detected!\n")
            return True
        # If the disk is not found
        else:
            print(f"\nNVMe is not detected!\n")
            sys.exit()
    # If the subprocess did not run successfully
    else:
        print("\nError running fdisk -l\n")
        return False
