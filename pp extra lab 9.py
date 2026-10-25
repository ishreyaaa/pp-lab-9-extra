import shutil

# Define file paths
source_file = 'source.txt'
destination_file = 'destination.txt'
append_file = 'append_file.txt'

# 1. Open, Write, and Read from a File
try:
    # Open file in write mode to add content
    with open(source_file, 'w') as file:
        file.write('This is the original content.\n')
        file.write('Adding some more text.')
    
    # Open file in read mode to read the content back
    with open(source_file, 'r') as file:
        content = file.read()
        print("Read content from source file:")
        print(content)
        
except IOError as e:
    print(f"Error opening/reading file: {e}")

# 2. Append to a File
try:
    # Open file in append mode to add new text
    with open(source_file, 'a') as file:
        file.write('\nAppending new content.')
        
    # Verify appending by opening the file in read mode
    with open(source_file, 'r') as file:
        updated_content = file.read()
        print("\nUpdated content after appending:")
        print(updated_content)
        
except IOError as e:
    print(f"Error opening/reading file: {e}")
    
    
try:
# Open file in append mode (adds to the end of the
# 2. Append to a File

    # Open file in append mode (adds to the end of the file)
    with open(source_file, 'a') as file:
        file.write('\nAppending new content.')
        
    # Verify appending by reading the file again
    with open(source_file, 'r') as file:
        content = file.read()
        print("\nContent after appending:")
        print(content)
        
except IOError as e:
    print(f"Error opening/reading/appending file: {e}")

# 3. Copy Content from One File to Another
try:
    # Copy the content from source_file to destination_file
    shutil.copy(source_file, destination_file)
    print(f"\nFile copied from {source_file} to {destination_file}.")
    
    # Verify copy by reading the destination file
    with open(destination_file, 'r') as file:
        dest_content = file.read()
        print("\nContent of the destination file:")
        print(dest_content)
        
except IOError as e:
    print(f"Error copying file: {e}")