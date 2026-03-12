def string_permutation_checker_2(s1: str, s2: str) -> bool:
	if len(s1) != len(s2):
		return False
	count = {}
	for c in s1.lower():
		count[c] = count.get(c, 0) + 1
	for c in s2.lower():
		count[c] = count.get(c, 0) - 1
		if count[c] < 0:
			return False
	return True

def string_permutation_checker(s1: str, s2: str) -> bool:
	if len(s1) != len(s2):
		return False
	return sorted(s1) == sorted(s2)

# print(string_permutation_checker("abc", "cab"))
# print(string_permutation_checker("hello", "olleh"))
# print(string_permutation_checker("abc", "abcc"))
# print(string_permutation_checker("Tom Marvolo Riddle ", "I am Lord Voldemort"))