class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """ABC = string.ascii_uppercase
        print(ord("A"))
        refDict={}
        for let in range(len(ABC)):
            refDict[ABC[let]]=let+1
        print(refDict)
        charList=[c for c in columnTitle]"""
        tProd=0
        counter=len(columnTitle)
        for c in columnTitle:
            tProd+=(ord(c)-64)*(26**(counter-1))
            counter-=1
        return tProd