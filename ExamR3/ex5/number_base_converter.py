def number_base_converter(number: str, from_base: int, to_base: int) -> str:
	digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	try:
		decimal = 0
		for ch in number.upper():
			val = digits.index(ch)
			if val >= from_base:
				return "ERROR"
			decimal = decimal * from_base + val

		if decimal == 0:
			return "0"
		result = ""
		while decimal:
			result = digits[decimal % to_base] + result
			decimal //= to_base
		return result
	except ValueError:
		return "ERROR"

# print(number_base_comverter("101", 2, 10))
# print(number_base_comverter("FF", 16, 10))
# print(number_base_comverter("255", 10, 16))
# print(number_base_comverter("XYZ", 10, 2))