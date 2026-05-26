def setZeroes(matrix):
    rows_nz = set()
    cols_nz = set()
    rows = len(matrix)
    cols = len(matrix[0])
    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == 0:
                rows_nz.add(x)
                cols_nz.add(y)

    for x in range(rows):
        for y in range(cols):
            if x in rows_nz or y in cols_nz:
                matrix[x][y] = 0

    return matrix


setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])
setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
