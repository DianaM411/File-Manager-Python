import os

def create_file(filename):
    try:
        with open(filename, 'w') as file:
            file.write('')
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating file '{filename}': {e}")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting file '{filename}': {e}")

def update_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write(content)
        print(f"File '{filename}' updated successfully.")
    except Exception as e:
        print(f"Error updating file '{filename}': {e}")

def modify_data(filename, search, replacement):
    try:
        with open(filename, 'r') as file:
            file_data = file.read()
        
        modified_data = file_data.replace(search, replacement)
        
        with open(filename, 'w') as file:
            file.write(modified_data)
        print(f"Data modified successfully in file '{filename}'.")
    except Exception as e:
        print(f"Error modifying data in file '{filename}': {e}")

def batch_process_files(directory, search, replacement):
    try:
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                file_path = os.path.join(directory, filename)
                modify_data(file_path, search, replacement)
    except Exception as e:
        print(f"Error during batch processing: {e}")

# Example Usage:

# Create a new file
create_file('example1.txt')
create_file('example2.txt')

# Update the files with content
update_file('example1.txt', 'Hello, World!')
update_file('example2.txt', 'Hello, OpenAI!')

# Batch process files in a directory
batch_process_files('.', 'Hello', 'Hi')

# Delete the files
delete_file('example1.txt')
delete_file('example2.txt')
