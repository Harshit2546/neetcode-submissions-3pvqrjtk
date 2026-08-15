from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        que = deque()
        direc = [(-1,0),(1,0),(0,-1),(0,1)]
        ans = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if (row,column) not in visited and grid[row][column] == 1:
                    area = 1
                    visited.add((row,column))
                    que.append((row,column))
                    while que:
                        curr_r,curr_c = que.popleft()
                        for dirR,dirC in direc:
                            nR,nC=curr_r+dirR,curr_c+dirC
                            if (0<= nR <len(grid)) and (0<=nC<len(grid[0])):
                                if (nR,nC) not in visited and grid[nR][nC] == 1:
                                    area+=1
                                    visited.add((nR,nC))
                                    que.append((nR,nC))
                    ans = max(ans,area)
                continue
        return ans


