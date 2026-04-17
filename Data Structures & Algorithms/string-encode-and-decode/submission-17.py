class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            delim= len(i)
            s+=str(delim)+"/"+i
        return s
    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        delim = ""
        while i < len(s):
            if s[i] =="/":
                delim = int(delim)+i
                res.append(s[i+1:delim+1])
                i = delim+1
                delim=""
            else:
                delim+=s[i]
                i+=1
           
        return res
