from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic=set()
        pacific=set()
        direc = {(0,1),(0,-1),(1,0),(-1,0)}
        for r in range(len(heights)):
            pacific.add((r,0))
            atlantic.add((r,len(heights[0])-1))
        for c in range(len(heights[0])):
            pacific.add((0,c))
            atlantic.add((len(heights)-1,c))
        queue = deque(list(pacific))
        while queue:
            curr_r,curr_c = queue.popleft()
            for dr,dc in direc:
                nr,nc=curr_r+dr,curr_c+dc
                if 0<=nr<len(heights) and 0<=nc<len(heights[0]) and (nr,nc) not in pacific and heights[curr_r][curr_c] <= heights[nr][nc] :
                    pacific.add((nr,nc))
                    queue.append((nr,nc))
        queue = deque(list(atlantic))
        while queue:
            curr_r,curr_c = queue.popleft()
            for dr,dc in direc:
                nr,nc=curr_r+dr,curr_c+dc
                if 0<=nr<len(heights) and 0<=nc<len(heights[0]) and (nr,nc) not in atlantic and heights[curr_r][curr_c] <= heights[nr][nc] :
                    atlantic.add((nr,nc))
                    queue.append((nr,nc))
        ans = [list(i) for i in (atlantic&pacific)]
        return ans
            

