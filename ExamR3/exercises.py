def brackets(text: str) -> bool:
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    for ch in text:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()
    return len(stack) == 0

def echo_validator(text: str) -> bool:
	format = ''.join(c.lower() for c in text if c.isalpha())
	return format == format[::-1]