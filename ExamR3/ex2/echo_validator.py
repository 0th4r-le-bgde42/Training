def echo_validator(text: str) -> bool:
	format = ''.join(c.lower() for c in text if c.isalpha())
	return format == format[::-1]

# print(f"{echo_validator('Radar')}\n"
# 	  f"{echo_validator("A man, a plan, a canal: Panama")}\n"
# 	  f"{echo_validator("Hello")}\n"
# 	  f"{echo_validator("K351635413Ay@#$%^&*a[}K]")}\n")