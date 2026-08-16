from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        border_set = set()
        direc = {(0,1),(0,-1),(1,0),(-1,0)}
        for row in range(len(board)):
            if board[row][0] == "O":
                border_set.add((row,0))
            if board[row][len(board[0])-1] == "O":
                border_set.add((row,len(board[0])-1))
        for col in range(len(board[0])):
            if board[0][col] =="O":
                border_set.add((0,col))
            if board[len(board)-1][col] == "O":
                border_set.add((len(board)-1,col))      
        que = deque(list(border_set))
        while que:
            curr_r,curr_c = que.popleft()
            for dr,dc in direc:
                nr,nc=curr_r+dr,curr_c+dc
                if (0<=nr<len(board)) and (0<=nc<len(board[0])) and (nr,nc) not in border_set and board[nr][nc]=="O":
                    border_set.add((nr,nc))
                    que.append((nr,nc))
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row,col) not in border_set:
                    board[row][col] = "X"
        return 
