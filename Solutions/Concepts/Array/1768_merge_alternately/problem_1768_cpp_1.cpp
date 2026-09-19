#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        const char* w1Pointer = word1.c_str();
        const char* w2Pointer = word2.c_str();
        
        vector<char> combined;
        for(int i = 0; i < max(word1.length(), word2.length()); i++) {
            combined.push_back(*w1Pointer);
            w1Pointer++;
            combined.push_back(*w2Pointer);
            w2Pointer++;
        }
    }
};