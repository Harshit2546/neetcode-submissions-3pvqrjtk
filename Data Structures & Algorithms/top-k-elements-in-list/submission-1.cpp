class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> hash;
        for(int i:nums){
            if(!hash[i]) {
                hash[i]=1;
                continue;
            }
            hash[i]++;
        }
        vector<pair<int, int>> freqVec;
        for(auto &i: hash){
            freqVec.push_back({i.second, i.first});
        }
        sort(freqVec.rbegin(), freqVec.rend());
        vector<int> ans;
        for(int i = 0; i < k; i++) {
            ans.push_back(freqVec[i].second);
        }
        return ans;
    }
};