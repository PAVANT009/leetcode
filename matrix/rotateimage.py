def rotate(matrix):
    rnc = len(matrix[0])
    ans = []
    for _ in range(rnc):
        ans.append([0] * rnc)
    for x in range(rnc):
        for y in range(rnc):
            ans[y][rnc - x - 1] = matrix[x][y]
            # print(x, y, y, rnc - x - 1)

    print(ans)


rotate(matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
