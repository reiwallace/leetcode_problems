#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;   
        int right = numbers.size() - 1;
        while(left < right) {
            int total = numbers.at(left) + numbers.at(right);
            if(total > target) {
                right--;
            } else if(total < target) {
                left++;
            } else {
                break;
            }
        }
        return {left + 1, right + 1};
    }
};