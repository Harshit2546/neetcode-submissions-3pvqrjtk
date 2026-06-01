class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j=strs[0]
        mini=10000000
        for i in strs:
            k=0
            while k<=len(i)-1 and k<=len(j)-1 and i[k]==j[k]:
                k=k+1
            mini=min(k,mini)
        return i[:mini]