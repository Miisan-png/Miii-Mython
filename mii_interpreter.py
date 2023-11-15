def tokenize(script):
   return script.split("\n")

def parse(token):
   if token.startswith("mvar"):
       var_name, var_value = token[5:].split(" = ")
       globals()[var_name] = eval(var_value)
   elif token.startswith("Add"):
       var_name, var_value = token[4:].split(" to ")
       globals()[var_name] += globals()[var_value]
   elif token.startswith("mprint"):
       print(eval(token[7:]))
   elif token.startswith("mfunc"):
       func_name, func_body = token[7:-1].split(":")
       func_body = func_body.strip()
       exec(f"def {func_name}(): {func_body}")
   elif token.startswith("mrun"):
       func_name = token[5:]
       globals()[func_name]()
   # Add more conditions here for other line types

def execute(script):
   tokens = tokenize(script)
   for token in tokens:
       parse(token)

# Read the script from a file
with open('script.my', 'r') as file:
   script = file.read()

execute(script)
