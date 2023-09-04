import java.util.Arrays;
class Solution {
    public int[] sortedSquares(int[] nums) 
    {
        int square =0;
        int [] newArray = new int[nums.length];
        
        for(int a = 0; a < nums.length; a++)
        {
            square = nums[a]*nums[a];
            newArray[a] = square;
        }
       

        Arrays.sort(newArray);
        return newArray;
    }
}
