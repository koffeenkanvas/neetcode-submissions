class Solution:

    def encode(self, strs: List[str]) -> str:
       parts = []
       for word in strs:
        parts.append(str(len(word))+"#"+word)
       return "".join(parts)

    def decode(self, s: str) -> List[str]:
        i=0
        result=[]
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            word_start = j+1
            word_end = word_start+ length
            result.append(s[word_start:word_end])
            i = word_end
        return result

