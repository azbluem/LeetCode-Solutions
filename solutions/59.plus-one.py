class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for n in digits:
            s=s+str(n)
        num=int(s)
        num=num+1
        s=str(num)
        rlist=[]
        for l in s:
            rlist.append(l)
        return rlist
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(digit) for digit in digits]
        string="".join(digits)
        return list(str(int(string)+1))