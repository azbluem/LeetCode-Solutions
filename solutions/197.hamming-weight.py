class Solution:
    def hammingWeight(self, n: int) -> int:
        check = str(n)
        return bin(int(check)).count("1")