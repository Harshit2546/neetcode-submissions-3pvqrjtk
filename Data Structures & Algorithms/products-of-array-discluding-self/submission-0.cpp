class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int l0=0;
        int mul=1;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==0){
                l0++;
                continue;
            }
            mul*=nums[i];
        }
        vector<int> ans;
        for(int i=0;i<nums.size();i++){
            if(l0>=2){
                ans.push_back(0);
            }
            else if(l0==1){
                if(nums[i]==0){
                    ans.push_back(mul);
                }
                else{
                    ans.push_back(0);
                }
            }
            else{
                ans.push_back(mul/nums[i]);
            }
        }
        return ans;
    }
};
