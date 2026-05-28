from functions.get_file_content import get_file_content

# 1. Large file truncation test
result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}\n")

# 2. Valid regular files
print("--- main.py content ---")
print(get_file_content("calculator", "main.py"))

print("\n--- pkg/calculator.py content ---")
print(get_file_content("calculator", "pkg/calculator.py"))

# 3. Rogue boundary breach test
print("\n--- Out of bounds test (/bin/cat) ---")
print(get_file_content("calculator", "/bin/cat"))

# 4. Non-existent file test
print("\n--- Missing file test ---")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
