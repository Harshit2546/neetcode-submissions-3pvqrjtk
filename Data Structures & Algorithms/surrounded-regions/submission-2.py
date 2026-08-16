class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()

        def add(r, c):
            if (
                0 <= r < ROWS and
                0 <= c < COLS and
                board[r][c] == "O"
            ):
                board[r][c] = "T"
                q.append((r, c))

        for r in range(ROWS):
            add(r, 0)
            add(r, COLS - 1)

        for c in range(COLS):
            add(0, c)
            add(ROWS - 1, c)

        while q:
            r, c = q.popleft()
            add(r + 1, c)
            add(r - 1, c)
            add(r, c + 1)
            add(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"


