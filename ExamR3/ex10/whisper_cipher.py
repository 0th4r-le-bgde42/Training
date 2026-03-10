def whisper_cipher(text: str, shift: int) -> str:
	result = ""
	for c in text:
		if c.isalpha():
			base = ord('A') if c.isupper() else ord('a')
			result += chr((ord(c) - base + shift) % 26 + base)
		else:
			result += c
	return result

# print(whisper_cipher("Hello", 3))
# print(whisper_cipher("abc", 1))