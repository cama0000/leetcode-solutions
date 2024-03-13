public class Solution {
  // VISUAL:  https://www.youtube.com/watch?v=K-RYzDZkzCI
    public int SearchInsert(int[] nums, int target) {
        int l = 0;
        int r = nums.Length - 1;

        // on the iteration where it cannot find target, left will become greater than right
        while(l <= r){
            int m = (l + r) / 2;

            // if target found
            if(target == nums[m]){
                return m;
            }

            // if target not found, change search positions
            if(target < nums[m]){
                // left stays same, right moves
                r = m - 1;
            }
            else{
                // right stays same, left moves
                l = m + 1;
            }
        }

        // return left, watch video for visual
        return l;
    }
}