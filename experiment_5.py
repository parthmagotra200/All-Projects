#AIM: WRITE A PROGRAM TO REVERSE EVERY KTH ROW IN MATRIX.
def reverse_kth_row(matrix, k):
    if k < 0 or k >= len(matrix):
        return "Invalid row index"

    matrix[k] = matrix[k][::-1]  # Reverse the kth row in the matrix
    return matrix

# Example matrix
example_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

k_row_to_reverse = 1  # Change this value to reverse a different row

result = reverse_kth_row(example_matrix, k_row_to_reverse)
if result != "Invalid row index":
    print(f"Matrix after reversing {k_row_to_reverse}th row:")
    for row in result:
        print(row)
else:
    print(result)