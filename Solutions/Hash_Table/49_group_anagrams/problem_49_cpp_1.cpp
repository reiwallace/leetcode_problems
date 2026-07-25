#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        for(string& word : strs) {
            int count[26] = {0};
            for(char letter : word) {
                count[letter - 'a']++;
            }
            string key;
            for(int num : count) {
                key += to_string(num) + "#";
            }
            map[key].push_back(word);
        }

        vector<vector<string>> ans;
        for(auto const& x : map) {
            ans.push_back(x.second);
        }
        return ans;
    }
};