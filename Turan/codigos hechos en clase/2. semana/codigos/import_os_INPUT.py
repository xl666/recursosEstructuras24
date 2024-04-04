import os

def print_directory_content(directory):
    print(os.listdir(directory))
    cantidad=len(os.listdir(directory))
    print(cantidad)
    return None

print(("YOU ARE HERE ->>>>>> "), os.getcwd())
directory=(input("Select directory path to list: "))
print_directory_content(directory)
print(os.path.isdir(directory))
