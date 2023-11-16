# shell.py
## Importing the language
import LanguageMi

print("Welcome to Mii Language Command Panel")
print("Version 0.01")

while True:
    action = input('Would you like to run a script or create a new script? (run/create): ')
    if action.lower() == 'run':
        filename = input('Enter the name of the script to run: ')
        with open(filename, 'r') as file:
            script = file.read()
        tokens = LanguageMi.tokenize(script)
        for token in tokens:
            result = LanguageMi.parse(token)
            print(result)
    elif action.lower() == 'create':
        filename = input('Enter the name for the new script (will be created if it does not exist): ')
        with open(filename, 'w+') as file:
            print(f'Start writing your script. Write "END" on a new line when you are done.\n')
            while True:
                line = input()
                if line == 'END':
                    break
                file.write(line + '\n')
        print(f'Script {filename} created successfully.')
    else:
        print('Invalid action. Please enter "run" or "create".')
