#!/usr/bin/env python3

from __future__ import print_function
import subprocess
import os
import argparse
from argparse import RawTextHelpFormatter

# Command line arguments
parser = argparse.ArgumentParser(description="This tool is the easiest way to bulk decrypt all offline Lynda videos to .mp4"
                                             " format with a proper folder structure and naming.",
                                 formatter_class=RawTextHelpFormatter)

parser.add_argument("--id",
                    nargs='+',
                    help="Select which courses from downloaded library to decrypt. Can take one or more arguments.")

parser.add_argument("--all",
                    action="store_true",
                    help="Decrypts all downloaded courses and removes their original encrypted files.")

parser.add_argument("--list",
                    action="store_true",
                    help="Lists out all current courses downloaded and not yet decrypted by ID.")

parser.add_argument("--cached",
                    action="store_true",
                    help="Use the cached paths intead of providing them at startup.")


# Functions
def header_display():
    print()
    print("Welcome to Tony's Python wrapper for h4ck-rOOt's Lynda decryptor!")
    print("This program will help you decrypt offline downloaded Lynda videos to mp4 files in a chosen directory!")
    print()


def variable_setups():
    print("Let's start by setting up some paths...")
    print()
    # Path to offline downloaded videos
    offline_folder = input("Please enter the path where your offline Lynda videos are downloaded."
                           "\nThis should look like C:\\Users\\foobar\\AppData\\Local"
                           "\\lynda.com\\Lynda.com Desktop App\\offline\\ldc_dl_courses\\"
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

    cache_paths(offline_folder, rest_path)

    return offline_folder, rest_path, folders


def cache_paths(offline_folder, rest_path):
    file = open("cached_paths", "w")
    file.writelines([offline_folder + "\n", rest_path])
    file.close()
    print("Cached paths for ease of use next time, just use the --cached switch.\n")


def read_cache():
    file = open("cached_paths", "r")
    offline_folder = file.readline()
    offline_folder = offline_folder.replace("\n", "")
    rest_path = file.readline()
    file.close()

    folders = os.listdir(offline_folder)
    folders.remove("decrypted")

    return offline_folder, rest_path, folders


def decrypt_all(folders):
    # Iterate through all folders and decrypt each
    for name in folders:
        print("Course number: " + name)
        course_path = "\"" + offline_folder + name + "\""
        command = "LyndaDecryptor /D " + course_path + rest_path
        subprocess.call(command, shell=True)

    print("All folders have been successfully decrypted.")


def decrypt_by_id(ids):
    print("A total of", len(ids), "courses will be decrypted.")

    # Iterate through each ID argument and decrypt
    for course_id in ids:
        course_id = course_id + "\""
        course_path = "\"" + offline_folder + course_id

        # Prepare and execute cmd command
        command = "LyndaDecryptor /D " + course_path + rest_path
        subprocess.call(command, shell=True)


# Main
args = parser.parse_args()

# No args selected
if not args.all and not args.id and not args.list:
    print("You did not use any arguments, please read the --help page before running again.")
    exit(1)

# Header display
header_display()

# Determine if reading cache file for paths or not
if args.cached:
    # Read cache file
    offline_folder, rest_path, folders = read_cache()

else:
    # Variable setups if not cached
    offline_folder, rest_path, folders = variable_setups()

# Automatic
if args.all:
    decrypt_all(folders)
    exit(0)

# Decrypting by course ID(s)
if args.id:
    ids = args.id
    decrypt_by_id(ids)
    exit(0)

# List out all downloaded courses (not yet decrypted)
if args.list:
    print("The following course IDs have been downloaded to the application, but not yet decrypted:")
    for name in folders:
        print(name)
    exit(0)
