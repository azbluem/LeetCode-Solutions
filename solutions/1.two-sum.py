class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = set(nums)
        for ind,num in enumerate(nums):
            diff = target-num
            if diff in num_set and (nums.index(diff))!=(ind):
                return [ind,nums.index(diff)]
        """compare_dict={}
        diff_set = set(nums)
        enumed = enumerate(nums)
        for index,num in enumed:
            diff = target-num
            compare_dict[num] = (diff,index)
        for diff,index in compare_dict.values():
            if diff in diff_set and index!=nums.index(diff):
                return [index,nums.index(diff)]"""

        """for ind,num in enumerate(nums):
            diff=target-num
            if diff in nums and (nums.index(diff),diff)!=(ind,num):
                return [nums.index(diff),ind]"""
            