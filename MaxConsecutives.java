class MaxConsecutives {
    public int findMaxConsecutiveOnes(int[] nums) {
        int count=0;
        int max =0;
        
        for(int a = 0; a < nums.length; a++)
        {
                if(nums[a]==1)
                {
                    count++;
        
                }
                else
                {
                    count =0;
                 
                }
            max = Math.max(count, max);
                
        }
        return max;
    }
}