#include <unordered_set>
#include <vector>

class Solution {
public:
    int distributeCandies(std::vector<int>& candyType) {
        // Initialise candySet and put candies into the candy set
        std::unordered_set<int> candySet;
        for(int candy : candyType) {
            candySet.insert(candy);
        } 

        // Compare number of candies in the set to the max amount of candies 
        int maxSize = candyType.size() / 2;

        if(candySet.size() < maxSize) {
            return candySet.size();
        } else {
            return maxSize;
        }
    }
};