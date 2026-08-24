try:
    with open("data.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("File does not exist.")

except PermissionError:
    print("You do not have permission to access this file.")