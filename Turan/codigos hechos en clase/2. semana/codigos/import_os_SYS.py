import os
import sys
import time

def print_directory_content(directory):
    if os.path.isdir(directory):
        print("Directory is about to be displayed -Please Wait-")
        time.sleep(3)
        print(os.listdir(directory))
        cantidad = len(os.listdir(directory))
        print("Number of existing files :", cantidad)
        return None
    else:
        print("Directory doesn't exist")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: import_os_SYS.py <directorio>")
        sys.exit(1)

    directory = sys.argv[1]
    print(("YOU ARE HERE ->>>>>> "), os.getcwd())
    print_directory_content(directory)
