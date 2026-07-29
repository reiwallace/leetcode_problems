#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int numsSize = nums.size();
        int halfway = numsSize / 2;
        int previous = -1;
        while(true) {
            int temp = halfway;
            if(nums.at(halfway) == target) {
                return halfway;
            }
            else if(nums.at(halfway) > target) {
                temp -= (halfway + 1) / 2;
            } else {
                temp += (halfway + 1) / 2;
            }
            cout << temp << "\n";
            if(temp == previous || temp > numsSize - 1) return -1;
            else {
                previous = halfway = temp;
                
            }
        }
    }
};