class Interpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def execute(self, script):
        tokens = self.tokenize(script)
        for token in tokens:
            self.parse(token)

    def parse(self, token):
        # Using method dispatch instead of large if-elif chain
        # This makes it easier to add more commands in the future
        command = token.split(" ")[0]
        method = getattr(self, command, None)
        if method:
            method(token)
        else:
            raise ValueError(f"Unknown command: {command}")

    def tokenize(self, script):
        return script.split("\n")

    def mvar(self, token):
        var_name, var_value = token[5:].split(" = ")
        self.variables[var_name] = eval(var_value, {}, self.variables)

    def Add(self, token):
        var_name, var_value = token[4:].split(" to ")
        self.variables[var_name] += self.variables[var_value]

    def mprint(self, token):
        print(eval(token[7:], {}, self.variables))

    def mfunc(self, token):
        func_name, func_body = token[7:-1].split(":")
        self.functions[func_name] = func_body.strip()
        print(f"Function {func_name} defined: {self.functions}")

    def mrun(self, token):
        func_name = token[5:]
        print(f"Running function {func_name}: {self.functions}")
        exec(self.functions[func_name], {}, self.variables)


# Create an instance of the interpreter
interpreter = Interpreter()

# Read the script from a file
with open('script.my', 'r') as file:
    script = file.read()

interpreter.execute(script)
