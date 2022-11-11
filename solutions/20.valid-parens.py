class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_dict={
            ')':"(",
            ']':'[',
            '}':'{'
        }
        for paren in s:
            if paren not in valid_dict.keys():
                stack.append(paren)
            else:
                try:
                    if valid_dict[paren]!=stack[-1]:
                        return False
                except IndexError:
                    return False
                stack.pop()
        if len(stack):
            return False
        return True
class Solution:
    def isValid(self, s: str) -> bool:
        sTups={
            ")":"(",
            "}":"{",
            "]":"["
        }
        sList=[]
        if len(s)%2!=0:
            return False
        for item in s:
            if item in sTups.values():
                sList.append(item)
            elif len(sList)==0:
                return False
            else:
                if sTups[item]==sList.pop():
                    pass
                else:
                    return False
        if len(sList)==0:
            return True
        else:
            return False
        """a = "()"
        b = "[]"
        c = "{}"
        valid=["()","[]","{}"]
        t=s
        while a in t or b in t or c in t:
            for i in valid:
                if i in t:
                    t=t.replace(i,"")
        while a in s:
            s.replace(a,"")
        while b in s:
            s.replace(b,"")
        while c in s:
            s.replace(c,"")
        if len(t)==0:
            return True
        else: return False"""