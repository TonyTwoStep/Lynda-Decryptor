from __future__ import print_function
import subprocess
import os


def header_display():
    print()
    print("Welcome to Tony's Python wrapper for h4ck-rOOt's Lynda decryptor!")
    print("This program will help you decrypt offline downloaded Lynda videos to mp4 files in a chosen directory!")
    print()
    print("Let's start by setting up some paths...")
    print()


def variable_setups():
    # Path to offline downloaded videos
    offline_folder = input("Please enter the path where your offline Lynda videos are downloaded."
                           "\nThis should look like C:\\...\\lynda.com\\Lynda.com Desktop App\\offline\\ldc_dl_courses\\"
                           "\nYour path: ")
    print()

    # Db.sqlite path
    db_path = input("Please enter the full path to your db.sqlite file."
                    "\nThis should look like  C:\\...\\lynda.com\\Lynda.com Desktop App\\db.sqlite"
                    "\nYour file path: ")
    print()

    # Specified Destination Path
    dest_path = "\"" + input("Enter a destination path for your decrypted video files: ") + "\""
    print()

    # Concatenating a full path
    rest_path = " /RM /DB \"" + db_path + "\" /OUT " + dest_path

    # List of all folders in lynda path minus decrypted folder
    folders = os.listdir(offline_folder)
    folders.remove("decrypted")

    return offline_folder, rest_path, folders


def menu_loop(offline_folder, rest_path, folders):
    while True:
        print()
        print("Options")
        print("A - automatically decrypt all courses currently downloaded (recommended)")
        print("L - list out all current courses downloaded (by number ID)")
        print("D - decrypt a known course by it's number ID")
        print("X - exit the program")
        print()
        user_input = str(input("Your choice: ")).lower()

        # Automatic
        if user_input == "a":
            # Iterate through all folders and decrypt each
            for name in folders:
                print("Course number: " + name)
                course_path = "\"" + offline_folder + name + "\""
                command = "LyndaDecryptor /D " + course_path + rest_path
                subprocess.call(command, shell=True)

            print("All folders have been successfully decrypted.")

        # Decrypting
        if user_input == "d":
            decrypting = True

            # Repeated decrypting loop
            while decrypting:
                user_input = str(input("Enter the course ID: ")) + "\""
                course_path = "\"" + offline_folder + user_input

                # Prepare and execute cmd command
                command = "LyndaDecryptor /D " + course_path + rest_path
                subprocess.call(command, shell=True)

                user_input = str(input("Decrypt another course?(y/n): ")).lower()

                if user_input == "n":
                    decrypting = False

        # List option
        if user_input == "l":
            for name in folders:
                print(name)

        # Exit
        if user_input == "x":
            break


# Header display
header_display()

# Variable setups
offline_folder, rest_path, folders = variable_setups()

# Main Loop
menu_loop(offline_folder, rest_path, folders)






