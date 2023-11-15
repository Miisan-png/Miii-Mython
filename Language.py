# Import the interpret function from the Mii interpreter script
from mii_interpreter import interpret

def create_new_file():
    filename = input("Enter the name for the new file: ")
    filename += ".my"  # Add the .my extension
    with open(filename, 'w') as file:
        print(f"New script {filename} created.")

def run_existing_file():
    filename = input("Enter the name of the file to run: ")
    if not filename.endswith('.my'):
        print("File must have a '.my' extension")
        return
    # Run the interpreter on the file
    interpret(filename)

def main():
    action = input("Do you want to (c)reate a new script or (r)un an existing script? ")
    if action.lower() == 'c':
        create_new_file()
    elif action.lower() == 'r':
        run_existing_file()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
