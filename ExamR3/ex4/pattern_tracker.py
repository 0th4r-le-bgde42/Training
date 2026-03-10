def pattern_tracker(text: str) -> int:
	count = 0
	prev = None
	for ch in text:
		if ch.isdigit():
			if prev is not None and int(ch) == prev + 1:
				count += 1
			prev = int(ch)
		else:
			prev = None
	return count

# print(pattern_tracker("123"))
# print(pattern_tracker("1293"))
# print(pattern_tracker("a123b45"))