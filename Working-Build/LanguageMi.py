def tokenize(script):
    return script.split("\n")
def parse(token):
    if token.startswith("mvar"):
        var_name, var_value = token[5:].split(" = ")
        globals()[var_name] = eval(var_value)
    elif token.startswith("Add"):
        var_name, var_value = token[4:].split(" to ")
        globals()[var_name] += globals()[var_value]
    elif token.startswith("Sub"):
        var_name, var_value = token[4:].split(" from ")
        globals()[var_name] -= globals()[var_value]
    elif token.startswith("Multiply"):
        var_name, var_value = token[9:].split(" by ")
        globals()[var_name] *= globals()[var_value]
    elif token.startswith("Divide"):
        var_name, var_value = token[7:].split(" by ")
        globals()[var_name] /= globals()[var_value]
    elif token.startswith("mprint"):
        print(eval(token[7:]))
    elif token.startswith("mfunc"):
        func_name, func_body = token[7:-1].split(":")
        func_body = func_body.strip()
        exec(f"def {func_name}(): {func_body}")
    elif token.startswith("mrun"):
        func_name = token[5:]
        globals()[func_name]()
    elif token.startswith("Create.File"):
        file_name = token.split("(")[1].split(")")[0].strip("'")
        open(file_name, "w").close()  # Create an empty file
    elif token.startswith("file.write"):
        file_name, content = token[10:].split(", ")
        file_name = file_name.strip()
        content = content.strip("'")
        with open(file_name, "a") as file:
            file.write(content + "\n")
    elif token.startswith("AskInput"):
        prompt = token.split('("' )[1].split('")')[0]
        user_input = input(prompt)
        return user_input
    elif token.startswith("if"):
        condition = token.split("if")[1].strip()
        if eval(condition):
            return "if"
        else:
            
            return "else"
    elif token.startswith("elif"):
        condition = token.split("elif")[1].strip()
        if eval(condition):
            return "elif"
    elif token.startswith("else"):
        return "else"
    elif token.startswith("and"):
        return "and"
    else:
        print("Script is empty")
    #0 Add more conditions here for other line types

command_not_found = False
def Error():
    if command_not_found:
        print("This Command is not found")
    elif command_not_found: 
        print("Running the program")
    else:
        print("Command Initiated")
        

def execute(script):
   tokens = tokenize(script)
   for token in tokens:
       parse(token)

# Read the script from a file
with open('script.my', 'r') as file:
   script = file.read()

execute(script)
