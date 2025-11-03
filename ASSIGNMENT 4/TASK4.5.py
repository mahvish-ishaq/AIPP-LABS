# Function to count number of lines in a .txt file
def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()    # Read all lines into a list
            return len(lines)           # Return total number of lines
    except FileNotFoundError:
        print("Error: File not found.")
        return None

# 🔹 Paste your file path here (double backslashes for Windows)
file_path = r"C:\Users\ACER\OneDrive\Documents\MAHVISH M.TECH AIPP LABS\ASSIGNMENT 4\4.5sample.txt"

# Call the function
num_lines = count_lines_in_file(file_path)

# Display output in two lines
if num_lines is not None:
    print(f"File Path: {file_path}")
    print(f"Number of Lines: {num_lines}")


