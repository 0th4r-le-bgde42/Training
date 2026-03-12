def number_base_converter(number: str, from_base: int, to_base: int) -> str:
	digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	try:
		nb = int(number, from_base)
		if nb == 0:
			return "0"
		result = ""
		while nb:
			result = digits[nb % to_base] + result
			nb //= to_base
		return result
	except ValueError:
		return "ERROR"

# print(number_base_comverter("101", 2, 10))
# print(number_base_comverter("FF", 16, 10))
# print(number_base_comverter("255", 10, 16))
# print(number_base_comverter("XYZ", 10, 2))