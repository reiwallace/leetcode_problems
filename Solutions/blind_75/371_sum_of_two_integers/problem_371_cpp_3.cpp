#include <stack>

class Solution {
private:
    bool carry = false;

public:
    int getSum(int a, int b) {
        unsigned int ua = a;
        unsigned int ub = b;

        int sum = 0;
        std::stack<bool> bits;

        while(a || b) {
            bool bitA = ua & 1;
            bool bitB = ub & 1;
            bool bit = false;

            if(bitA && bitB) {
                if(carry) {
                    bit = true;
                } else {
                    carry = true;
                }
            } else if((bitA || bitB) && !carry) {
                bit = true;
            } else if(carry && (!bitA && !bitB)) {
                bit = true;
                carry = false;
            }

            ua >>= 1;
            ub >>= 1;
            bits.push(bit);
        }

        if(carry) {
            bits.push(true);
        }


        while(!bits.empty()) {
            sum <<= 1;
            sum |= bits.top();
            bits.pop();
        }

        return sum;
    }
};