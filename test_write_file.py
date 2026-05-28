from functions.write_file import write_file

# Case 1: Overwrite test on an existing file
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

# Case 2: Nested file creation in a brand new path context
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

# Case 3: Forbidden directory escape test
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
