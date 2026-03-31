class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        hash={}
        i=0
        j=1
        hash[s[i]]=i
        count=1
        res=1
        while(j<len(s)):
            if(s[j] not in hash):
                count+=1
                hash[s[j]]=j
                j+=1
            else:
                count-=1
                del hash[s[i]]
                i+=1
            res=max(count,res)
        return res
