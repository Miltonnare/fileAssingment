def modify_content(content):
    # You can tweak this logic — here we just uppercase it
    return content.upper()

try:
    filename = input("Enter the filename to read from: ").strip()

    with open(filename, "r") as file:
        original_content = file.read()

    modified_content = modify_content(original_content)

    new_filename = "modified_" + filename

    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"✅ File '{filename}' was read successfully.")
    print(f"✍️ Modified content has been written to '{new_filename}'.")

except FileNotFoundError:
    print(f"🚫 Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"🚫 Error: Permission denied for file '{filename}'.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
