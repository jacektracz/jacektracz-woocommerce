package com.jacektracz.letcode.mergeklists;

import java.util.PriorityQueue;

/**
 * 
 * 
 * 
 * 
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

//class Solution {

class JacekTraczLetCodeMergeSortedKListsPriorityQueueSolution {
    
	public ListNode mergeKLists(ListNode[] lists) {
		if(lists == null || lists.length ==0)
			return null;
		int k = lists.length;
		PriorityQueue<ListNode> pq = new PriorityQueue<>(k, (a,b)-> a.val - b.val);
		ListNode dummy = new ListNode(0);
		ListNode ptr = dummy;
		for(int i=0; i< k; i++){
			if(lists[i]!=null)
				pq.offer(lists[i]);
		}
		while(!pq.isEmpty()){
			ListNode cur = pq.poll();
			ListNode next = cur.next;
			ptr.next = cur;
			ptr = cur;
			if(next!=null)
				pq.offer(next);
		}
		return dummy.next;
	}    
}
