# Python Import Modules Project

This project aims to teach you how to import functions and variables from another Python file, manage command line arguments, and explore different Python features related to importing modules.

## Learning objectives

At the end of this project, you will be able to explain and implement:

- Why Python programming is great

- How to import functions from another file

- How to use imported functions

- How to create a Python module

- How to use the built-in function `dir()`

- How to prevent the execution of a script when it is imported

- How to use command line arguments with your Python programs

## Resources

Before you start, be sure to read or look at the following resources:

- [Modules](https://docs.python.org/3/tutorial/modules.html)

- [Command line arguments](https://docs.python.org/3/library/sys.html#sys.argv)

- [Pycodestyle - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## Requirements

- You must use an editor like `vi`, `vim` or `emacs` to write your Python files.

- All your files will be interpreted/compiled on Ubuntu 22.04 LTS using Python3 (version 3.10. *).

- The first line of each file must be exactly: `#! /Usr/bin/python3`

- You must respect the PyCodeStyle style conventions (version 2.7.*) for Python code.

- You must make all your files executable.

- You must ensure that all your files end with a new line.

## Structure of the project

### Project files

- `0-add.py`: Program to import the `add` function from the `add_0.py` file and print the result of the addition.

- `1-calculation.py`: Program to import functions from `calculator_1.py` and perform calculations (addition, subtraction, multiplication, division).

- `2-args.py`: Program to print the number of arguments and the list of arguments passed via the command line.

- `3-infinite_add.py`: Program to add all the arguments passed on the command line and print the result.

- `4-hidden_discovery.py`: Program to discover the names defined in the `hidden_4.pyc` module and print them in alphabetical order.

- `5-variable_load.py`: Program to import and print the `a` variable from the `variable_load_5.py` file.

## Program delivery

### 0. Import a simple function

```bash

./0-add.py