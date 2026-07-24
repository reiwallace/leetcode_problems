#include <string>

using namespace std;

class Solution {
public:
    int compareVersion(string version1, string version2) {
        int pointer1 = -1;
        int pointer2 = -1;

        int numCount1 = 0;
        int numCount2 = 0;

        int curVer1 = 0;
        int curVer2 = 0;

        do {
            if(pointer1 < (int) version1.length() - 1) {
                curVer1 = 0;
                pointer1 ++;
                numCount1 ++;
            }
            if(pointer2 < (int) version2.length() - 1) {
                curVer2 = 0;
                pointer2 ++;
                numCount2 ++;
            }

            while(pointer1 < (int) version1.length() && version1[pointer1] != '.') {
                curVer1 = curVer1 * 10 + (version1[pointer1] - '0');
                pointer1 ++;
            }
            while(pointer2 < (int) version2.length() && version2[pointer2] != '.') {
                curVer2 = curVer2 * 10 + (version2[pointer2] - '0');
                pointer2 ++;
            }

            if(!curVer1 && !curVer2) {
                continue;
            }

            if((curVer1 > curVer2 && numCount1 >= numCount2) || (curVer1 && numCount1 > numCount2)) {
                return 1;
            } 
            else if((curVer2 > curVer1 && numCount2 >= numCount1) || (curVer2 && numCount2 > numCount1)) {
                return -1;
            }

        } while(pointer1 < (int) version1.length() - 1 || pointer2 < (int) version2.length() - 1);

        return 0;
    }
};