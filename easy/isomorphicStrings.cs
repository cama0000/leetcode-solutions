public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> d = new Dictionary<int, int>();
        int[] ans = new int[2];

        for(int i = 0; i < nums.Length; i++){
            int complement = target - nums[i];
            if(d.ContainsKey(complement)){
                ans[0] = d[complement];
                ans[1] = i;
            }

            d[nums[i]] = i;
        }

        return ans;

    }
}