class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        numDict=collections.defaultdict(lambda : 0)
        for num in nums:
            numDict[num]+=1
        numList=[(k,v) for k,v in numDict.items()]
        return max(numList, key=lambda x:x[1])[0]