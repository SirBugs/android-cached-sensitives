import os
import json
import argparse
import sys

# Set up argument parsing
parser = argparse.ArgumentParser(description='Search for values in files.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-c', '--config', help='Path to the JSON configuration file')
group.add_argument('-t', '--text', help='A single text string to search for in all files')

args = parser.parse_args()

# Prepare the search values
if args.config:
    with open(args.config, 'r') as file:
        data = json.load(file)
    search_values = list(data.values())
elif args.text:
    search_values = [args.text]

current_directory = os.getcwd()

def search_in_file(file_path, search_values):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        for value in search_values:
            if value in content:
                print(f"Found '{value}' in file: {file_path}")

for root, dirs, files in os.walk(current_directory):
    if root == current_directory:
        for directory in dirs:
            subdirectory_path = os.path.join(current_directory, directory)
            print(f"Searching in '{directory}':")
            for sub_root, sub_dirs, sub_files in os.walk(subdirectory_path):
                for file_name in sub_files:
                    file_path = os.path.join(sub_root, file_name)
                    search_in_file(file_path, search_values)
            print()
