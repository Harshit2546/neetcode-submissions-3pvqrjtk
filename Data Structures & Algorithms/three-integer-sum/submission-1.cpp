#include<algorithm>
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        std::sort(nums.begin(),nums.end());
        for(int i=0;i< nums.size();i++){
            int target=-nums[i];
            int j=0;
            int k=nums.size()-1;
            while(j<k){
                int sum=nums[j]+nums[k];
                if(sum==target && i!=j && i!=k){
                    vector<int> ans1;
                    ans1.push_back(nums[j]);
                    ans1.push_back(nums[k]);
                    ans1.push_back(nums[i]);
                    std::sort(ans1.begin(),ans1.end());
                    if(find(ans.begin(),ans.end(),ans1)==ans.end()){
                        ans.push_back(ans1);
                    }
                    j++;
                    k--;
                }
                else if(sum<target){
                    j++;
                }
                else{
                    k--;
                }
            }

        }
        return ans;
    }
};
