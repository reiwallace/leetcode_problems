#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string s) {
        int totalPixels = 0;
        int remainder = 0;
        for(char c : s) {
            int toAdd = widths.at(c - 'a');
            if(totalPixels + toAdd - remainder == 100) {
                remainder += 100;
            } else if(totalPixels + toAdd - remainder > 100) {
                 totalPixels += 100 - totalPixels - remainder;
                 remainder += 100;
            }
            totalPixels += toAdd;
        }
        cout << totalPixels << "\n";
        return {(totalPixels / 100) + (totalPixels % 100 > 0), totalPixels % 100};
    }
};