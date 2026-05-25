def spiralOrder(matrix):
    ans = []

    endc = len(matrix[0])
    endr = len(matrix)

    startc = 0
    startr = 0

    while startc < endc and startr < endr:
        # left -> right
        for col in range(startc, endc):
            ans.append(matrix[startr][col])

        # top -> bottom
        for row in range(startr + 1, endr):
            ans.append(matrix[row][endc - 1])

        # right -> left
        if startr < endr - 1:
            for col in range(endc - 2, startc - 1, -1):
                ans.append(matrix[endr - 1][col])

        # bottom -> top
        if startc < endc - 1:
            for row in range(endr - 2, startr, -1):
                ans.append(matrix[row][startc])

        startc += 1
        startr += 1
        endc -= 1
        endr -= 1

    return ans


print(spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
