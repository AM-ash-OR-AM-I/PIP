f = open("f3", "w+")
print(f'{f.write("Hello World") = }')  # returns number of characters written

print(f"{f.tell() = }")  # returns the current position of the cursor
print(f"{f.seek(0) = }")  # moves the cursor to the beginning of the file
print(f.read())  # reads the entire file
print(f"{f.seek(2) = }")  # moves the cursor to the 3rd character
print(f.tell())  # returns 2
