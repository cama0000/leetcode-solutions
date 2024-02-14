class Solution {
    public void reverse(int nums[], int start, int end){
        while(start <= end){
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
    public void rotate(int[] nums, int k) {
        // Method 1 - Circular
        // int[] a = new int[nums.length];

        // for(int i = 0; i < nums.length; i++){
        //     a[(i + k) % nums.length] = nums[i];
        // }

        // for(int i = 0; i < nums.length; i++){
        //     nums[i] = a[i];
        // }

        // Method 2 - REVERSE
        k = k % nums.length;
        reverse(nums, 0, (nums.length - 1) - k);
        reverse(nums, (nums.length) - k, nums.length - 1);
        reverse(nums, 0, nums.length - 1);
    }
}