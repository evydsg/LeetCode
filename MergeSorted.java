class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) 
    {
        for(int a = 0; a < n; a++)
        {
                nums1[m+a] = nums2[a];
        }
        Arrays.sort(nums1);
    }
}