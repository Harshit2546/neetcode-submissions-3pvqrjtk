#include<cctype>
class Solution {
public:
    bool isPalindrome(string s) {
        int i=0;
        int j=s.length();
        while(i<j){
            while(!(('a'<=s[i] && 'z'>=s[i])||('A'<=s[i] && 'Z'>=s[i])||('0'<=s[i] && '9'>=s[i]))) i+=1;
            while(!(('a'<=s[j] && 'z'>=s[j])||('A'<=s[j] && 'Z'>=s[j])||('0'<=s[i] && '9'>=s[i]))) j-=1;
            if(tolower(s[i])!=tolower(s[j]) && i<j) return false;
            i++;
            j--;
        }
        return true;
    }
};
