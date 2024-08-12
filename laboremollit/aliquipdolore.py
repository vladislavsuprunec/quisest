# Proposal with the corresponding dimension of the specified size.
# Creates a 2D list with the given number of rows and columns, initialized to the specified value.
def create_matrix(rows: int, cols: int, value: int):
    return [[value for _ in range(cols)] for _ in range(rows)]

matrix = create_matrix(3, 4, 7)
for row in matrix:
    print(row)
