def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
	merged = list1 + list2

	n = len(merged)
	for i in range(n):
		for j in range(0, n - i - 1):
			if merged[j] > merged[j + 1]:
				merged[j], merged[j + 1] = merged[j + 1], merged[j]
	return merged

# print(shadow_merge([3,1,5], [2,4]))