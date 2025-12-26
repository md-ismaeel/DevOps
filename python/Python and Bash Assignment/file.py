# file = open("data.txt", "w")
# file.write("This file is created using Python.\n")
# file.write("File handling is simple and useful.")
# file.close()

# print("Data written to file successfully.")


file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
