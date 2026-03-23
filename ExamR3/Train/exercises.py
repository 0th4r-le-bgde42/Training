def brackets(text: str) -> bool:
	stack = []
	bra = {"]": "[", "}": "{", ")": "("}
	for c in text:
		if c in "{[(":
			stack.append(c)
		elif c in "}])":
			if not stack or stack[-1] != bra[c]:
				return False
			stack.pop()
	return len(stack) == 0


def echo_validator(text: str) -> bool:
	formatted = ''.join(c.lower() for c in text if c.isalpha())
	return formatted == formatted[::-1]


def matrix_reverse(matrix: list[list[int]]) -> list[list[int]]:
	return [row[::-1] for row in matrix]


def pattern_tracker(text: str) -> int:
	count = 0
	prev = None
	for c in text:
		if c.isdigit():
			if prev is not None and int(c) == prev + 1:
				count += 1
			prev = int(c)
		else:
			prev = None
	return count


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
	digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	try:
		nb = int(number, from_base)
		if nb == 0:
			return "0"
		res = ""
		while nb:
			res = digits[nb % to_base] + res
			nb //= to_base
		return res
	except Exception:
		return "ERROR"


def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
	return sorted(list1 + list2)


def string_permutation_checker(s1: str, s2: str) -> bool:
	if len(s1) != len(s2):
		return False
	return sorted(s1) == sorted(s2)


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


def twist_sequence(arr: list[int], k: int) -> list[int]:
	if not arr:
		return arr
	k = k % len(arr)
	return arr[-k:] + arr[:-k] if k else arr[:]


def whisper_cipher(text: str, shift: int) -> str:
	res = ""
	for c in text:
		if c.isalpha():
			base = ord("A") if c.isupper() else ord("a")
			res += chr((ord(c) - base + shift) % 26 + base)
		else:
			res += c
	return res


def cryptic_sorter(strings: list[str]) -> list[str]:
	return sorted(strings, key=lambda s: (len(s), s.lower(), s)) 


print("\n--- Brackets ---"
	  f"\n{brackets("()")}"
	  f"\n{brackets("(]")}")
print("\n\n--- ECHO ---"
	  f"\n{echo_validator("racecar")}"
	  f"\n{echo_validator("race a car")}")
print("\n\n--- MATRIX ---"
	  f"\n{matrix_reverse([[1,2,3],[4,5,6]])}"
	  f"\n{matrix_reverse([[1]])}")
print("\n\n--- PATTERN ---"
	  f"\n{pattern_tracker("123")}"
	  f"\n{pattern_tracker("01234567")}")
print("\n\n--- BASE ---"
	  f"\n{number_base_converter("1010", 2, 10)}"
	  f"\n{number_base_converter("G", 16, 10)}")
print("\n\n--- SHADOW ---"
	  f"\n{shadow_merge([1,3,5], [2,4,6])}"
	  f"\n{shadow_merge([], [1,2,3])}")
print("\n\n--- PERMUTATION ---"
	  f"\n{string_permutation_checker("abc", "cab")}"
	  f"\n{string_permutation_checker("abc", "abcc")}")
print("\n\n--- SCULPTOR ---"
	  f"\n{py_string_sculptor("Hello")}"
	  f"\n{py_string_sculptor("Hello! World!")}")
print("\n\n--- TWIST ---"
	  f"\n{twist_sequence([1,2,3,4], 1)}"
	  f"\n{twist_sequence([1,2,3,4], 5)}")
print("\n\n--- WHISPER ---"
	  f"\n{whisper_cipher("hello", 3)}"
	  f"\n{whisper_cipher("Hello World!", 1)}")
print(f"\n\n--- CYPTIC ---"
	  f"\n{cryptic_sorter(["apple", "cat", "banana"])}"
	  f"\n{cryptic_sorter(["aaa", "AAA"])}")