def interpret(filename):
    # Create a dictionary to store variable values
    variables = {}

    # Open the Mii script file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Process each line in the file
    for line in lines:
        # Split the line into words
        words = line.split()

        # Skip empty lines and comments
        if len(words) == 0 or words[0].startswith('#'):
            continue

        # Process Mii commands
        elif words[0] == 'mvar':
            # This is a variable assignment
            variables[words[1]] = eval(words[3])
        elif words[0] in ['Add', 'Sub', 'Multiply', 'Divide']:
            # This is an arithmetic operation
            if words[0] == 'Add':
                variables[words[1]] = variables[words[1]] + variables[words[3]]
            elif words[0] == 'Sub':
                variables[words[1]] = variables[words[1]] - variables[words[3]]
            elif words[0] == 'Multiply':
                variables[words[1]] = variables[words[1]] * variables[words[3]]
            elif words[0] == 'Divide':
                variables[words[1]] = variables[words[1]] / variables[words[3]]
        elif words[0] == 'mprint':
            # This is a print statement
            print(eval(words[1], variables))

        else:
            print(f"Unknown command: {words[0]}")

if __name__ == "__main__":
    interpret('test.my')
