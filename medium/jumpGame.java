class Solution {
    public boolean canJump(int[] nums) {
        // greedy algorithm will naturally find shortest path

        // first attempt
        // if(nums.length == 1){
        //     return true;
        // }

        // int largest = 0;
        // int jumpIndex = 0;

        // for(int i = 0; i < nums.length; i++){
        //     for(int j = 0; j < nums[i]; j++){
        //         if(largest < nums[jumpIndex]){
        //             largest = nums[jumpIndex];
        //             jumpIndex = i + j;
        //         }
        //     }

        //     if(nums.length <= jumpIndex){
        //         return false;
        //     }
        //     else if(nums.length - 1 == jumpIndex){
        //         return true;
        //     }
        //     else{
        //         i = jumpIndex;
        //     }
        // }

        // return false;

        // max index that you can make it
        int maxIndex = nums[0];

        for(int i = 0; i < nums.length; i++){
            if(maxIndex >= nums.length - 1){
                return true;
            }
            
            // cant jump anymore
            if(nums[i] == 0 && maxIndex == i){
                return false;
            }
            
            // update maxIndex jumped
            if(i + nums[i] > maxIndex){
                maxIndex = i + nums[i];
            }
        }

        return false;
    }
}