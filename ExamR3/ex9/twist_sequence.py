def twist_sequence(arr: list[int], k: int) -> list[int]:
	if not arr:
		return arr
	k = k % len(arr)
	return arr[-k:] + arr[:-k] if k else arr[:]

# print(twist_sequence([1,2,3,4], 1))
# print(twist_sequence([1,2,3,4], 2))
# print(twist_sequence([1,2,3,4], 3))
# print(twist_sequence([1,2,3,4], 4))