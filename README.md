# Mii Language Interpreter
Welcome to the Mii Language Interpreter, a Python-based interpreter for a custom scripting language.
![Image](https://github.com/psy-lilulu/Mii-Custom-Language/assets/128460054/11d832b8-5825-41c0-89fa-319fc60c09a8)
## Getting Started

### Prerequisites

- Python 3.x installed
- Basic knowledge of scripting languages

### Installation

1. Clone the repository or download the source code.
2.Clone Mii-Language Folder
3. Ensure Python is installed on your system.

### Usage

#### Running Scripts

- To run a Mii script:
  1. Launch the `shell.py` file in your terminal or command prompt.
  2. Choose the `run` option.
  3. Enter the name of the `.my` script you want to execute when prompted.
  4. Follow the instructions for your script execution.

#### Creating and Editing Scripts

- To create a new script:
  1. Select the `create` option in the shell.
  2. Enter the desired name for your script.
  3. Begin writing your script lines. Use `END` on a new line to finish.

- To edit an existing script:
  1. Choose the `edit` option in the shell.
  2. Select the script you want to edit.
  3. Append or modify the existing script. Use `END` on a new line to finish editing.

#### Language Syntax

- The language supports various commands, including:
  - `mvar` for variable assignment
  - Arithmetic operations like `Add`, `Sub`, `Multiply`, and `Divide`
  - File operations such as `Create.File` and `file.write`
  - Conditional statements (`if`, `elif`, `else`, `and`)
  - Functions (`mfunc`, `mrun`)
  - User input (`AskInput`)

https://carbon.now.sh/?bg=rgba%280%2C0%2C0%2C1%29&t=material&wt=none&l=auto&width=863.75&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=false&pv=56px&ph=56px&ln=false&fl=1&fm=Fira+Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code=Script%25201%253A%2520Simple%2520Math%2520Operations%250Amvar%2520a%2520%253D%252010%250Amvar%2520b%2520%253D%25205%250AAdd%2520a%2520to%2520b%250Amprint%2520a%250A%250AScript%25202%253A%2520File%2520Operations%250ACreate.File%28%27test.txt%27%29%250Afile.write%28%27test.txt%27%252C%2520%27Hello%252C%2520World%21%27%29%250A%250A%250AScript%25203%253A%2520Conditional%2520Statement%250Amvar%2520x%2520%253D%25205%250Amvar%2520y%2520%253D%252010%250Aif%2520x%2520%253C%2520y%253A%250A%2520%2520%2520%2520mprint%2520%2522x%2520is%2520less%2520than%2520y%2522%250Aelse%253A%250A%2520%2520%2520%2520mprint%2520%2522x%2520is%2520greater%2520than%2520or%2520equal%2520to%2520y%2522%250A%250AScript%25204%253A%2520Function%2520Definition%2520and%2520Execution%250Amfunc%2520greet%253A%250A%2520%2520%2520%2520mprint%2520%2522Hello%252C%2520Mii%21%2522%250A%2520%2520%2520%2520%250Amrun%2520greet%250A
