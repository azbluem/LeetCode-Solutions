class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        return_list=[]
        for n in range(0,len(nums)+1):
            iterlist = [list(i) for i in combinations(nums, n)]
            return_list.extend(iterlist)
        return return_list