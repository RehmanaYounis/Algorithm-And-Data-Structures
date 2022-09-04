class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[[p,s] for p,s in zip(position, speed)]
        stack=[]
        for pos, sp in sorted(cars)[::-1]:
            time=(target-pos)/sp
            stack.append(time)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)