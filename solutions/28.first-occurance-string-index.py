class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)==0:
            return 0
        else:
            try:
                if isinstance(haystack.index(needle),int):
                    return haystack.index(needle)
            except:
                return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length=len(needle)
        for index in range(len(haystack)):
            if haystack[index:index+length]==needle:
                return index
        return -1