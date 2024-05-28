def file_handling():
    try:
         with open("my_file.txt", mode='w') as my_file:
          my_file.write("Today we're learning about file handling. \n")
          my_file.write("When you want to write you have to open first. \n")
          my_file.write("Happy coding! \n")
    except (FileNotFoundError, PermissionError) as e:
        print(f'When you were creating or writing the file an error occured: {e}')
    finally:
        print("Done attempting to create and write to the file")

def read_and_display_file():
    try:
        with open("my_file.txt", "r") as my_file:
          contents = my_file.read()
          print(contents)
    except (FileNotFoundError, PermissionError) as e:
        print(f'Found an error when displaying the file: {e}')

    finally:
        print('Finished trying to read and display to the file.')


def file_appending():
    try:
        with open("my_file.txt", mode='a') as my_file:
            my_file.write("Js is the language for me. \n")
            my_file.write("Python is an OOP. \n")
            my_file.write("SQL does it! \n")
    except (FileNotFoundError, PermissionError) as e:
        print(f'found an error when trying to append to the file: {e}')

    finally:
        print('Finished attempting to append to the file')

file_handling()
file_appending()
read_and_display_file()
