#include <climits>
class Solution {
public:
    int getSum(int a, int b) {
        int carry = 0;
        int ans = 0;
        int i = 1;
        while(true) {
            int binA = a & i;
            int binB = b & i;
            if(carry && binA && binB) {
                ans |= binA;
                carry <<= 1;
            } else if(carry && !(binA || binB)) {
                ans |= carry;
                carry = 0;
            } else if(carry && (binA || binB)){
                carry <<= 1;
            } else if(binA && binB) {
                carry = binA << 1;
            } else if(binA || binB) {
                if(binA) {
                    ans |= binA;
                } else {
                    ans |= binB;
                }
            }
            if(i == -2147483648) break;
            i <<= 1;
        }
        return ans;
    }
};