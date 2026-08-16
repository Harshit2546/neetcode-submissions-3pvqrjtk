from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque()
        freshCnt = 0
        row,column = len(grid),len(grid[0])
        direc = [(-1,0),(1,0),(0,1),(0,-1)]
        for curr_r in range(row):
            for curr_c in range(column):
                if grid[curr_r][curr_c] == 2:
                    que.append((curr_r,curr_c,0))
                elif grid[curr_r][curr_c] ==1:
                    freshCnt +=1
        cnt = 0
        ans =0
        while que:
            curr_r,curr_c,time=que.popleft()
            for dirx,diry in direc:
                nx,ny=curr_r+dirx,curr_c+diry
                if 0<=nx<row and 0<=ny<column and grid[nx][ny]==1:
                    cnt +=1
                    grid[nx][ny] = 2
                    que.append((nx,ny,time+1))
            ans = max(ans,time)
        if cnt != freshCnt :
            return -1
        return ans
