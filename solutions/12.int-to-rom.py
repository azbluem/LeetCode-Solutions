class Solution:
    def intToRoman(self, num: int) -> str:
        returnStr=""
        while num>=1000:
            returnStr=returnStr+'M'
            num-=1000
        if num>=900:
            returnStr=returnStr+'CM'
            num-=900
        if num>=500:
            returnStr=returnStr+'D'
            num-=500
        if num>=400:
            returnStr=returnStr+'CD'
            num-=400
        while num>=100:
            returnStr=returnStr+'C'
            num-=100
        if num>=90:
            returnStr=returnStr+'XC'
            num-=90
        if num>=50:
            returnStr=returnStr+'L'
            num-=50
        if num>=40:
            returnStr=returnStr+'XL'
            num-=40
        while num>=10:
            returnStr=returnStr+'X'
            num-=10
        if num>=9:
            returnStr=returnStr+'IX'
            num-=9
        if num>=5:
            returnStr=returnStr+'V'
            num-=5
        if num>=4:
            returnStr=returnStr+'IV'
            num-=4
        while num>=1:
            returnStr=returnStr+'I'
            num-=1
        return returnStr
    
        """romanDict={
            1:I,
            5:V,
            10:X,
            50:L,
            100:C,
            500:D,
            1000:M
        }"""
        