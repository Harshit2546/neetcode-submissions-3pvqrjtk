class Solution:
    def maxProfit(self, arr):
        i,j=0,0
        profit=0
        while i<=j and j<len(arr):
            difference=arr[j]-arr[i]
            if difference >= profit:
                profit=difference
                j=j+1
            elif difference <0:
                i=j
                j=j+1
            else:
                j=j+1
        return profit