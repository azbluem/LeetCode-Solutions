class Solution:
    def climbStairs(self, n: int) -> int:
        fib=[1,1]
        for index in range(2,n+1):
            fib.append((fib[index-1]+fib[index-2]))
        return fib[n]