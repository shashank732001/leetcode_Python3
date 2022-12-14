class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = []
        n = len(position)
        stack = []
        
        for i in range(n):
            pair.append([position[i],speed[i]])
        
        pair.sort(key=lambda i:i[0],reverse=True)
        for p,s in pair:
        # for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)        