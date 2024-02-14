class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> l = new ArrayList<>();

        if(nums.length == 0){
            return l;
        }
        
        if(nums.length == 1){
            l.add(Integer.toString(nums[0]));
        }

        int begin = nums[0];
        int begIndex = 0;

        for(int i = 0; i < nums.length; i++){
            if(i != 0){
                if(nums[i] != nums[i - 1] + 1){
                    String s = Integer.toString(begin);

                    if(i != begIndex + 1){
                        s += "->" + Integer.toString(nums[i - 1]);
                    }

                    l.add(s);
                    begin = nums[i];
                    begIndex = i;

                    if(begIndex == nums.length - 1){
                        l.add(Integer.toString(begin));
                    }
                }
                else if(i == nums.length - 1){
                    l.add(Integer.toString(begin) + "->" + nums[i]);
                }
            }
        }

        return l;
    }
}