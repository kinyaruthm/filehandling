def modify_line(line):
    return "Hello, Python! " + line

def process_file():
    filename = input("Enter the filename to read from: ")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            print("📄 Original File Content:\n")
            print("".join(lines))

        new_filename = "modified_" + filename
        with open(new_filename, "w") as newfile:
            for line in lines:
                modified = modify_line(line)
                newfile.write(modified)

        print(f"\n✅ Modified content written to '{new_filename}' successfully!")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except IOError:
        print("❌ Error: Unable to read/write the file. Check permissions or file state.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

process_file()
