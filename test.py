# import os

# # Set the file path and name
# file_path = "/generated/client/new_file.txt"  # Replace with the desired file path

# # Extract the directory path
# directory = os.path.dirname(file_path)

# # Check if the directory exists
# if not os.path.exists(directory):
#     os.makedirs(directory) # Create the directory if it doesn't exist

# # Open a file in write mode
# with open(file_path, "w") as file:
#     # Write content to the file
#     file.write("This is a new text file.\n")
#     file.write("It contains some text.\n")
#     file.write("Hello, world!")

# print("New file created and written successfully.")


import ast

print(filepaths_string)
# parse the result into a python list
list_actual = []
try:
    print("Eval: "+ filepaths_string)
    list_actual = ast.literal_eval(filepaths_string)

    dir = os.path.dirname(file_path)
    
    # Check if the directory exists
    if not os.path.exists(dir):
        os.makedirs(dir, mode=0o777, exist_ok=True)
        print("dir made:"+ dir)