class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """res = set(nums)
        nums.clear()
        for n in res:
            nums.append(n)
        nums.sort()
        return(len(nums))"""
        n=0
        while n<len(nums)-1:
            if nums[n]==nums[n+1]:
                nums.remove(nums[n+1])
            else:
                n+=1
        return len(nums)