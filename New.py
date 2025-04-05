def read_file(file_name):
    """Reads content from a file and returns it."""
    with open(file_name, "r") as file:
        content = file.read()
    return content

def write_file(file_name, content):
    """Writes content to a file."""
    with open(file_name, "w") as file:
        file.write(content)

def modification(text):
    """Converts text to uppercase."""
    return text.upper()

def main():
    try:
        inputter = input("Which File are you Looking For: ").strip()

        if inputter == "movie.txt":
            rent = read_file(inputter)

            if not rent.strip():
                print(" movie.txt is empty!")
            else:
                print("\nOriginal content:")
                print(rent)

                modified_content = modification(rent)
                modified_file_name = "modified_" + inputter

                write_file(modified_file_name, modified_content)
                print(f"\n Modified content saved to '{modified_file_name}'.")

        elif inputter == "tumb.txt":
            default_content = "This is a new File\nUnknown Dimension\nUnclaimed error\n"
            write_file("tumb.txt", default_content)
            print(" tumb.txt has been created successfully!")

        else:
            print(" Unknown File!")

    except FileNotFoundError:
        print(" FileNotFoundError: The file is not available!")
    except PermissionError:
        print(" PermissionError: Access to the file denied!")
    except Exception as e:
        print(f" Unexpected Error: {e}")


if __name__ == "__main__":
    main()
