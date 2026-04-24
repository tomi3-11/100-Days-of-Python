# 100 Awesome Days Of Python.
Learning and solving all exercises from the python programming exercise book by AL Sweigart

From Exercise 1 to 42 plus more exercises

# Project structure

```sh
.
├── C-implementation
│   ├── Exercise10
│   │   ├── find
│   │   └── findAndReplace.c
│   ├── Exercise7
│   │   ├── ascii
│   │   └── ascii_table.c
│   ├── Exercise8
│   │   ├── file
│   │   ├── fileHandling.c
│   │   └── greet.txt
│   └── Exercise9
│       ├── chess
│       └── chess_colors.c
├── Exercise1
│   └── hello.py
├── Exercise10
│   └── find_and_replace.py
├── Exercise11
│   └── get_hours_minutes_seconds.py
├── Exercise12
│   ├── get_smallest.py
│   ├── __pycache__
│   │   └── get_smallest.cpython-314.pyc
│   └── test_get_smallest.py
├── Exercise13
│   └── get_sum_and_product.py
├── Exercise2
│   └── temperature_conservation.py
├── Exercise3
│   ├── is_even_or_odd.py
│   └── is_even_or_odd.py~
├── Exercise4
│   └── area_volume.py
├── Exercise5
│   └── fizz_buzz_exercise.py
├── Exercise6
│   └── ordinal_numbers.py
├── Exercise7
│   └── ascii_table.py
├── Exercise8
│   ├── file_input_output.py
│   └── greet.txt
├── Exercise9
│   └── chess_square_colors.py
├── main.py
├── pyproject.toml
├── PythonProgrammingExercisesGentlyExplained.pdf
├── README.md
└── uv.lock

20 directories, 31 files

```

# What to contribute
- Anything related to the topic
- Code documentation
- Code refactoring
- Naming convention
- README.md documention
- Better solutions

# How to contribute

### 1. Fork The repo
```sh
git fork https://github.com/tomi3-11/100-Days-of-Python.git
```

### 2. Clone from ur end
```sh
git clone https://github.com/<yourusername>/100-Days-of-Python.git
```

### 3. project setup
```sh
# Use uv
uv init

# Create a virtual environment
uv venv

# Activate the virtual environment
venv\Scripts\activate # for windows
source venv/bin/activate # for linux or MacOs
```

### 4. Run the application particular files
```sh
# Change directory to the specific folder that you need to work on
cd Exercise1
uv run helloworld.py

```

> Make Appropriate changes

### 5. Add changes
```sh
# create a  branch
git checkout -b <branchname>

# add changes
git add <filename.py>
git commit -m "Update <filename.py> with changes ..."

# push changes to github
git push origin <branchname>
```

### 6. Open a pull request on github
Open a pull request with good and clear explanation of the changes that you made

### 7. Done


# Happy coding ❤️

