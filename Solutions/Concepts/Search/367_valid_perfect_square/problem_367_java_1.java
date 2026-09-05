class Solution {
    public boolean isPerfectSquare(int num) {
        int upper = num;
        int lower = 0;
        int mid = num / 2;
        long sq;
        while(upper >= lower) {
            sq = mid * mid;
            if(sq == num) {
                return true;
            } else if(sq > num) {
                upper = mid - 1;
            } else {
                lower = mid + 1;
            }
            mid = lower + (upper - lower) / 2;
        }
        return false;
    }
}