class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        import collections
        nums_counter=collections.Counter(nums)
        return nums_counter.most_common()[len(nums_counter)-1][0]

# Note: the question asked for linear time, constant space, this is not