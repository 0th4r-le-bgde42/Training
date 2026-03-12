def brackets(text: str) -> bool:
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    for c in text:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or stack[-1] != matching[c]:
                return False
            stack.pop()
    return len(stack) == 0

#print(brackets("{({"))