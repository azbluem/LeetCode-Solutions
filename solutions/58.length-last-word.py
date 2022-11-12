class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sList=s.strip().split()
        return len(sList[-1])