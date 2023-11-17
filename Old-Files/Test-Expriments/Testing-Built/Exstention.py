import os
import re

def change_logo_file(file_path, new_logo_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            updated_content = re.sub(r'Logo\.png', new_logo_path.replace('\\', r'\\'), content)
        
        with open(file_path, 'w') as file:
            file.write(updated_content)
        print(f"Logo file path in '{file_path}' has been updated.")
    else:
        print(f"'{file_path}' does not exist.")

# Path to the script.my file
script_file_path = 'script.my'

# New logo file path
new_logo_path = 'C:\\Users\\ssaya\\OneDrive\\Desktop\\Miico\\Mii-Custom-Language\\Info\\Logo.png'

# Call the function to change the logo file path in script.my
change_logo_file(script_file_path, new_logo_path)
