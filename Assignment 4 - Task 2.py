data1 = input("Enter the text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(data1 + "\n")

data2 = input("Enter additional text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(data2 + "\n")

print("\nFinal content of 'output.txt':")
with open("output.txt", "r") as file:
    read = file.read()
    print(read)