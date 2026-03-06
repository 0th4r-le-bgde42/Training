def echo_validator(text: str) -> bool:
	format = ''.join(c.lower() for c in text if c.isalpha())
	return format == format[::-1]

print(echo_validator("Radar"))
print(echo_validator("A man, a plan, a canal: Panama"))
print(echo_validator("Hello"))
print(echo_validator("K351635413Ay@#$%^&*a[}K]"))