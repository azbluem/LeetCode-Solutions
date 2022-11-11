class Solution:
    
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        count = 1
        return_list = []
        for word in words:
            return_list.append(self.worder(word,count))
            count+=1
        return " ".join(return_list)

    def worder(self,word,count):
        VOWEL_SET=set("aeiou")
        end = "a" * count
        ah = "ma"
        if word[0].lower() in VOWEL_SET:
            return word+ah+end
        return word[1:]+word[0]+ah+end