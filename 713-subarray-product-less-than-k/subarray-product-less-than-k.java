class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k<=1)
            return 0;
        int l=0;
        int r=0;
        int p=1;
        int c=0;
        while (r<nums.length){
            p=p*nums[r];
            while (p>=k){
            p=p/nums[l];
            l++;
            }
        c=c+1+r-l;
        r++;
        }
    return c;
    }
}