class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed),reverse=True)
        stack=[]
        for i,s in cars:
            time=(target-i)/s
            if stack and time>stack[-1]  :
                stack.append(time)
            elif not stack:
                stack.append(time)
        return len(stack)
        