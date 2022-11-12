class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        index=0
        while index < len(nums):
            if nums[index]==val:
                print(nums.pop(index))
                print(nums)
                count+=1
            else:
                index+=1
        return len(nums)