/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode[] a = new ListNode[30];
        int count = 0;

        while(head != null){
            a[count] = head;
            head = head.next;
            count++;
        }

        if(count-n-1 >= 0 && count-n+1 < count){
            a[count-n-1].next = a[count-n+1];
        }
        else if(count-n-1 < 0 && count-n+1 >= count){
            a[0] = null;
        }
        else if(count-n-1 < 0 && count-n+1 < count){
            a[0] = a[1];
        }
        else{
            a[count-n-1].next = null;
        }

        return a[0];
    }
}