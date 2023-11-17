# Mii Language Interpreter
Welcome to the Mii Language Interpreter, a Python-based interpreter for a custom scripting language.
![Marta](https://github.com/psy-lilulu/Mii-Custom-Language/assets/128460054/1490dfc0-8b36-4713-96ac-7c1025747cd9) 
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

### Examples
# Example Script
mvar x = 10
mvar y = 5
Add x to y
mprint x
mfunc greet:
    mprint "Hello, World!"

mrun greet()
