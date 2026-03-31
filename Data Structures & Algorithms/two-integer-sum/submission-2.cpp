#include<algorithm>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        unordered_map<int,int> hash;
        for(int i=0;i<nums.size();i++){
            hash[nums[i]]=i;
        }
        for(int i=0;i<nums.size();i++){
            int t=target-nums[i];
            if(hash.find(t)!=hash.end()){
                if(hash[t]==i) continue;
                ans.push_back(i);
                ans.push_back(hash[t]);
                std::sort(ans.begin(),ans.end());
                return ans;
            }
        }
        return ans;
    }
};
