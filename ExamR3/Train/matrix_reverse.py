def matrix_reverse(matrix: list[list[int]]) -> list[list[int]]:
	return [row[::-1] for row in matrix]

print(matrix_reverse([[1,2,3],[4,5,6]]))