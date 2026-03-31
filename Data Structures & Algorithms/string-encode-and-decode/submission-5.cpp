#include<cctype>
class Solution {
public:

    string encode(vector<string>& strs) {
        string s="";
        int i=0;
        for(string str : strs){
            int len = str.length();
            s += to_string(len) + "#" + str;
        }
        return s;
    }

    vector<string> decode(string s) {
        vector<string> ans;
        int i = 0;
        while (i < s.length()) {
            int sharpPos = s.find('#', i);
            int len = stoi(s.substr(i, sharpPos - i));
            ans.push_back(s.substr(sharpPos + 1, len));
            i = sharpPos + 1 + len;
        }
        return ans;
    }

};
