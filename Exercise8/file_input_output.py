def main():
#    filename = input("Enter a filename: (txt) ")
#    text = input("Enter a text to write to the file: ")
#    write_to_file(filename, text)
#    append_to_file(filename, "This is a new line.")
#    read_to_file(filename)
    write_to_file('greet.txt', 'Hello!\n')
    append_to_file('greet.txt', 'Goodbye!\n')
    assert read_to_file('greet.txt') == 'Hello!\nGoodbye!\n'


def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)
#        file.write(text + '\n')


def append_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text)
#        file.write(text + '\n')


def read_to_file(filename):
    with open(filename, 'r') as file:
        return file.read()


if __name__ == "__main__":
    main()
