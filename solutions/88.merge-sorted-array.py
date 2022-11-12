class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for digit in nums2:
            nums1.append(digit)
        if 0 in nums1:
            for v in range(n):
                nums1.remove(0)
        nums1.sort()
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for pops in range(n):
            nums1.pop()
        for append in range(n):
            nums1.append(nums2[append])
        return nums1.sort()