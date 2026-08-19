class Solution {
    public int[] numberOfLines(int[] widths, String s) {
        int ans[] = {1,0};
        for(int i = 0; i < s.length(); i++) {
            int width = widths[s.charAt(i) - 'a'];
            if(ans[1] + width > 100) {
                ans[0]++;
                ans[1] = 0;
            }
            ans[1] += width;
        }
        return ans;
    }
}