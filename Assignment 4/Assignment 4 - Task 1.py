m1 = "sample1.txt"
try:
    print("Reading file content:")
    with open(m1, "r") as file:
        read = file.read()
        print(read)
except FileNotFoundError:
    print("Error: The file " + m1 + " was not found.")
