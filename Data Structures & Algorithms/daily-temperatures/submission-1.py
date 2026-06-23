class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        sol=temperatures.copy()
        for i in range(0,len(sol)):
            sol[i]=0
        for i in range(0,len(temperatures)): 
            while len(stack)>0 and temperatures[i]>temperatures[stack[-1]]:
                    sol[stack[-1]]=i-stack[-1]
                    stack.pop(-1)
            stack.append(i)
        return sol