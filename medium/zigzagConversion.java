class Solution {
    public String convert(String s, int numRows) {
    //     int inc = numRows + (numRows / 2);
    //     int firstInc = inc;
    //     int i = 0;
    //     int j = 0;
    //     StringBuilder sb = new StringBuilder();

    //     while(i < s.length()){
    //         if(j < s.length()){
    //             sb.append(s.charAt(j));
    //             System.out.println(s.charAt(j));
    //             j += inc;
    //         }
    //         else{
    //             i++;
    //             j = i;

    //             if(i >= numRows){
    //                 System.out.println("HERE");
    //                 break;
    //             }

    //             if(i != numRows - 1){
    //                 inc -= 2;
    //             }
    //             else{
    //                 inc = firstInc;
    //             }
    //         }
    //     }

    //     return sb.toString();

    if(numRows == 1){
        return s;
    }

    int inc = (numRows - 1) * 2;
    StringBuilder sb = new StringBuilder();

    for(int i = 0; i < numRows; i++){
        for(int j = i; j < s.length(); j += inc){
            sb.append(s.charAt(j));
            if(i < numRows - 1 && i > 0 && (j + inc - (2 * i)) < s.length()){
                sb.append(s.charAt(j + inc - (2 * i)));
            }
        }
    }

    return sb.toString();
    }


}