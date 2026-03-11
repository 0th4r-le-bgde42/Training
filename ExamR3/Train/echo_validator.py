def echo_validator(text: str) -> bool:
	formated = ''.join(ch.lower() for ch in text if ch.isalpha())
	return formated == formated[::-1]

print(f"Radar -> {echo_validator("Radar")}")
print(f"Hello -> {echo_validator("Hello")}")