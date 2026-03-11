def brackets(text: str) -> bool:
	stack = []
	bracks = {"]": "[", ")": "(", "}": "{"}
	for ch in text:
		if ch in "({[":
			stack.append(ch)
		elif ch in ")}]":
			if not stack or stack[-1] != bracks[ch]:
				return False
			stack.pop()
	return len(stack) == 0 

print(f"() -> {brackets("()")}")
print(f"(] -> {brackets("(]")}")