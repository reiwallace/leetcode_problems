#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string s) {
        vector<int> ans = {1, 0};
        for(char c : s) {
            int width = widths[c - 'a'];
            if(ans[1] + width > 100) {
                ans[1] = 0;
                ans[0] ++;
            }
            ans[1] += width;
        }
        return ans;
    }
};