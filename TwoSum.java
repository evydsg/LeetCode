class Solution {
    public int[] twoSum(int[] nums, int target)
    {
        int [] indices = new int [2];
        for(int a = 0; a < nums.length-1; a++)
        {
            for(int b = 1; b< nums.length; b++)
            {
                if(nums[a] + nums[b] == target)
                {
                indices[0] = a;
                indices[1] = b;
                }
            }
        }
        
        return indices;
    }
}
