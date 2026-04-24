def main():
    ascii_tab()
    

def ascii_tab():
    for i in range(32, 127):
        print(f"{i} {chr(i)}")
    


if __name__ == "__main__":
    main()
