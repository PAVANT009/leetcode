class Solution(object):
    def gameOfLife(self, board):
        rows = len(board)
        cols = len(board[0])

        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        for x in range(rows):
            for y in range(cols):
                live = 0

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < rows and 0 <= ny < cols:
                        if board[nx][ny] == 1 or board[nx][ny] == -1:
                            live += 1

                if board[x][y] == 1:
                    if live < 2 or live > 3:
                        board[x][y] = -1  # alive -> dead

                else:
                    if live == 3:
                        board[x][y] = 2  # dead -> alive

        for x in range(rows):
            for y in range(cols):
                if board[x][y] == -1:
                    board[x][y] = 0
                elif board[x][y] == 2:
                    board[x][y] = 1
