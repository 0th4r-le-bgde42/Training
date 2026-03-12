def py_string_sculptor(text: str) -> str:
	res = ""
	i = 0
	for c in text:
		if c.isalpha():
			res += c.lower() if i % 2 == 0 else c.upper()
			i += 1
		else:
			res += c
	return res

print(py_string_sculptor("Hello World"))
print(py_string_sculptor("BONjoUr A tous LE MondE"))