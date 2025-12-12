# 100 Awesome Days Of Python.
Learning and solving all exercises from the python programming exercise book by AL Sweigart

From Exercise 1 to 42 plus more exercises

# Project structure

```cpp
project_folder/
    |
    |--Exercise1/
    |	   |--Helloworld.py
    |
    |--Exercise2/
    |	   |--temperature_conversion.py
    |
    |-- ...
    |--README.md
    |--.gitattribute
    |--.gitignore
    
    


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

