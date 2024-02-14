class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int[] nums3 = new int[m + n];
        int index = 0;
        int i = 0, j = 0;
        int mIndex;

        while(i < m || j < n){
            if(i < m && j < n){
                if(nums1[i] <= nums2[j]){
                    nums3[index] = nums1[i];
                    i++;
                }
                else{
                    nums3[index] = nums2[j];
                    j++;
                }
            }
            else{
                if(j >= n){
                    nums3[index] = nums1[i];
                    i++;
                }
                else{
                    nums3[index] = nums2[j];
                    j++;
                }
            }

            index++;
        }

        /*for(int v : nums3){
                System.out.println(v);
            }*/

        if((m + n) % 2 == 0){
            return (nums3[((m+n) / 2) - 1] + nums3[((m+n) / 2)]) / 2.0;
        }
        else{
            return nums3[(m + n) / 2];
        }
    }
}