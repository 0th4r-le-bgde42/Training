def cryptic_sorter(strings: list[str]) -> list[str]:
	return sorted(strings, key=lambda s: (len(s), s.lower(), s))

#print(cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]))