class Solution {
    public int findNumbers(int[] nums) {
        String a = "";
        int count=0;
        int evenNumbers = 0;
        
        for(int b = 0; b<nums.length; b++)
        {
            a = nums[b] + "";
            count = a.length();
            
            if(count%2==0)
            {
               evenNumbers++;
            }
        }
        return evenNumbers;
    }
}