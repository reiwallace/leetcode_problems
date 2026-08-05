#include <string>
#include <sstream>
#include <iostream>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        if(s.length() < 1) return 0;
        if(s.length() == 1) return 1;
        int firstChar = 0;
        int lastChar = 0;
        for(int i = 1; i < s.length(); i++) {
            if(s[i] == ' ' && s[i-1] != ' ') {
                lastChar = i;
            }
            if(s[i-1] == ' ' && s[i] != ' ') {
                firstChar = i;
            }
        }
        if(lastChar <= firstChar) return s.length() - firstChar;
        return lastChar - firstChar;
    }
};