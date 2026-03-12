def shadow_merge_1(list1: list[int], list2: list[int]) -> list[int]:
	list1.extend(list2)
	list1.sort()
	return list1

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
	return sorted(list1 + list2)

# print(shadow_merge([3,1,5], [2,4]))
# print(shadow_merge_2([3,1,5], [2,4]))