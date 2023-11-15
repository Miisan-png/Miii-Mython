# Custom language emulator in Python

# Dictionary to store variables
variables = {}
# Dictionary to store functions
functions = {}

# Custom language emulator in Python

# Dictionary to store variables
variables = {}
# Dictionary to store functions
functions = {}

def run_command(command):
    # Split the command into words
    words = command.split()

    # Handle each command
    if words[0] == 'mvar':
        # Variable assignment
        variables[words[1]] = eval(words[3])  # 'eval' is used to convert the string number to an integer
    elif words[0] == 'mprint':
        # Print command
        to_print = ' '.join(words[1:])
        print(variables[to_print]) if to_print in variables else print(to_print)
    elif words[0] in ['Add', 'Sub', 'Multiply', 'Divide']:
        # Arithmetic operations
        var1 = variables[words[1]]
        var2 = variables[words[3]]
        if words[0] == 'Add':
            variables[words[1]] = var1 + var2
        elif words[0] == 'Sub':
            variables[words[1]] = var1 - var2
        elif words[0] == 'Multiply':
            variables[words[1]] = var1 * var2
        elif words[0] == 'Divide':
            variables[words[1]] = var1 / var2
    elif words[0] == 'mfunc':
        # Function definition
        func_name = words[1]
        func_body = ' '.join(words[2:])
        functions[func_name] = func_body
    elif words[0] == 'mrun':
        # Function call
        func_name = words[1]
        func_body = functions[func_name]
        run_command(func_body)
    elif words[0] == 'AskInput':
        # User input
        variables[words[1]] = input()
    elif words[0] == 'Loop':
        # Loop
        loop_count = int(variables[words[1]])
        loop_body = ' '.join(words[2:])
        for _ in range(loop_count):
            run_command(loop_body)
    elif words[0] == 'If':
        # If statement
        var1 = variables[words[1]]
        operator = words[2]
        var2 = variables[words[3]]
        if_body = ' '.join(words[4:])
        if eval(f"{var1} {operator} {var2}"):
            run_command(if_body)


# Read the script file
with open('script.my', 'r') as script:
    for line in script:
        # Remove newline character and any trailing spaces
        line = line.strip()

        # Ignore empty lines and comments
        if line == '' or line.startswith('#'):
            continue

        # Run the command
        run_command(line)
