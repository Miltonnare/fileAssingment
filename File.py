def modification(text):
    return text.upper()


try:
    inputter=input("Which File are you Looking For:   ").strip()
    if inputter=="movie.txt":

        with open("movie.txt", "r") as file:
            rent=file.read()
            if not rent:
                print("movie.txt is empty!")
            else:
                print("Original content:")
                print(rent)
        modify=modification(rent)
        modifiedFileName="modified_" + inputter
        with open(modifiedFileName,"w") as New_file:
            New_file.write(modify)
            print("Modified Content saved.")


    elif inputter=="tumb.txt":
        with open("tumb.txt","w") as file:
            file.write("This is a new File\n")
            file.write("Unknown Dimension\n")
            file.write("Unclaimed error\n")
            print("tumb.txt has been created succesfully!")
    else:
        print("Unknown File!")
except FileNotFoundError:
    print("FileNotFoundError: The file is not available!")
except  PermissionError:
    print("PermissionError: Access to the file Denied!")
except Exception as e:
    print(f"Unexpected Error: {e}")




