class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest=""
        i=1
        j=0
        if strs==[""]:
            return ""
        elif strs==["a"]:
            return "a"
        shortestword=10000
        for word in strs:
            if len(word) < shortestword:
                shortestword = len(word)
        while j < shortestword:
            while i < len(strs):
                if strs[i]=="" or strs[i-1]=="":
                    return longest
                elif strs[i][j]==strs[i-1][j]:
                    i+=1
                else: return longest
            longest=longest+strs[i-1][j]
            j+=1
            i=1
        return longest
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(min(strs)) or len(strs)<2:
            return min(strs)
        return_string = self.comparator(strs[1],strs[0])
        for string in strs:
            return_string=self.comparator(return_string,string)
        return return_string
    
    def comparator(self,str1,str2):
        if not str1 or not str2:
            return ""
        index=0
        return_string=[]
        while index<len(min(str1,str2)):
            if str1[index]==str2[index]:
                return_string.append(str1[index])
                index+=1
            else:
                break
        return "".join(return_string)