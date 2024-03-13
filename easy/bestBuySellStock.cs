public class Solution {
    public int MaxProfit(int[] prices) {
        int largest = 0;
        int bought;

        if(prices.Length == 0){
            return 0;
        }
        else{
            bought = prices[0];
        }

        for(int i = 0; i < prices.Length; i++){
            if(largest < prices[i] - bought){
                largest = prices[i] - bought;
            }

            if(prices[i] < bought){
                bought = prices[i];
            }
        }

        return largest;
    }
}