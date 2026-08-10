#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> table;
        for(int i = 0; i < nums.size(); i++) {
            if(table.count(nums[i]) && i - table.at(nums[i]) <= k) {
                return true;
            } else if(table.count(nums[i])) {
                table[nums[i]] = i;
            } else {
                table.insert({nums[i], i});
            }
        }
        return false;
    }
};