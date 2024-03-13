/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode ReverseList(ListNode head) {
        // FIRST ATTEMPT
        // if(head == null){
        //     return head;
        // }

        // ListNode r = new ListNode();
        // ListNode dummy = r;
        // List<ListNode> a = new List<ListNode>();

        // while(head != null){
        //     a.Add(head);
        //     head = head.next;
        // }

        // a.Reverse();

        // foreach(var l in a){
        //     r.next = l;
        //     r = r.next;
        // }

        // r.next = null;

        // return dummy.next;

       // https://www.youtube.com/watch?v=G0_I-ZF0S38

        // ITERATIVE METHOD
        // ListNode prev = null;
        // ListNode curr = head;

        // while(curr != null){
        //     // to remember the next node to visit
        //     ListNode forward = curr.next;
        //     //reverse the link
        //     curr.next = prev;
        //     prev = curr;
        //     curr = forward;
        // }

        // return prev;

        // RECUSRIVE METHOD
        if(head == null){
            return null;
        }

        ListNode newHead = head;
        
        if(head.next != null){
            newHead = ReverseList(head.next);
            head.next.next = head;
        }
        head.next = null;

        return newHead;
    }
}