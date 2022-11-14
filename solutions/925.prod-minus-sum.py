class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        import math
        Nlist=[]
        while n>0:
            Nlist.append(n%10)
            n=n//10
        return math.prod(Nlist)-sum(Nlist)