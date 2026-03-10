def py_string_sculptor(text: str) -> str:
	result = ""
	for i, c in enumerate(text):
		if c.isalpha():
			result += c.lower() if i % 2 == 0 else c.upper()
		else:
			result += c
	return result

# print(py_string_sculptor("Hello World"))
# print(py_string_sculptor("BONjoUr A tous LE MondE"))