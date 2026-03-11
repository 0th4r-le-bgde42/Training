def number_base_converter(number: str, from_base: int, to_base: int) -> str:
	digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	try:
		decimal = 0
		for ch in numbers:
			index = digits.index(ch)
			if index >= from_base:
				return "ERROR"
			decimal = decimal * from_base + index
		if decimal == 0:
			return "0"	 
		result = ""
		while decimal:
			result = digits[decimal % to_base] + result
			decimal //= to_base
		return result
	except ValueError:
		return "ERROR"

print(f"101, 2, 10 -> {number_base_converter("101", 2, 10)}")
print(f"255, 16, 10 -> {number_base_converter("255", 10, 16)}")