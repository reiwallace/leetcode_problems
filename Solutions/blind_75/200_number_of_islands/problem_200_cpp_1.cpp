#include <vector>
using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for(int x = 0; x < grid.size(); x++) {
            for(int y = 0; y < grid[x].size(); y++) {
                if(grid[x][y] != '1') continue;
                markLand(grid, x, y);
                count++;
            }
        }
        return count;
    }

    void markLand(vector<vector<char>>& grid, int x, int y) {
            if(grid[x][y] != '1') return;

            grid[x][y] = NULL;
            if(x + 1 < grid.size()) markLand(grid, x + 1, y);
            if(y + 1 < grid[x].size()) markLand(grid, x, y + 1);
            if(x - 1 >= 0) markLand(grid, x - 1, y);
            if(y - 1 >= 0) markLand(grid, x, y - 1);
    }
};

