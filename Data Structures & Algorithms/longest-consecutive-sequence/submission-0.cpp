#include <algorithm>
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int ,int> hash;
        for(int i=0;i<nums.size();i++){
            hash[nums[i]]++;
        }
        int longest=0;
        for(int n:nums){
            if(hash.find(n-1)==hash.end()){
                int current=n;
                int streak=1;
                while(hash.find(current+1)!=hash.end()){
                    current+=1;
                    streak++;
                }
                longest=max(longest,streak);
            }
        }
        return longest;
    }
};
