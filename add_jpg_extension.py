import os
import sys


def add_jpg_extension_to_files(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if it's a file and not a directory
        if os.path.isfile(file_path) and not os.path.splitext(file_path)[1]:
            new_filename = f"{file_path}.jpg"
            os.rename(file_path, new_filename)
            print(f"Renamed {file_path} to {new_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python add_jpg_extension.py <relative_directory>")
        sys.exit(1)

    relative_directory = sys.argv[1]
    full_directory_path = os.path.join(os.getcwd(), relative_directory)
    add_jpg_extension_to_files(full_directory_path)
