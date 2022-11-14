class Solution:
    def reverseWords(self, s: str) -> str:
        rs = [word.strip() for word in list(s.split())]
        return " ".join(rs[::-1])
        #return " ".join(s.split()[::-1])