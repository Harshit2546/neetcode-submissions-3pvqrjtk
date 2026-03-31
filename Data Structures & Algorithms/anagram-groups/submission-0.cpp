#include<algorithm>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> hash;
        for(int i =0;i<strs.size();i++){
            string s=strs[i];
            std::sort(s.begin(),s.end());
            hash[s].push_back(strs[i]);
        }
        vector<vector<string>> strings;
        for(auto const& i:hash){
            strings.push_back(i.second);
        }
        return strings;
    }
};
