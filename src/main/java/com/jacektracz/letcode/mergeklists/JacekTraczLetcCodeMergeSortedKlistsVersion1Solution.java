package com.jacektracz.letcode.mergeklists;

public class JacekTraczLetcCodeMergeSortedKlistsVersion1Solution {
	
	 public ListNode mergeKLists(ListNode[] lists) {
	        if(lists == null || lists.length == 0){
	            return null;
	        }
	        
	        if(lists.length == 1){
	            return lists[0];
	        }
	        
	        return mergeKSortedLists(lists,lists.length - 1);
	    }
	    
	    public ListNode mergeKSortedLists(ListNode[] lists,int last){
	        while(last != 0){
	            int i = 0;
	            int j = last;
	            
	            while(i < j){
	                lists[i] = mergeTwoSortedLinkedLists(lists[i],lists[j]);
	                i++;
	                j--;
	                
	                if(i >= j) {
	                  last = j;
	                  break;
	                }
	            }
	        }
	        
	        return lists[0];
	    }
	    
	    public ListNode mergeTwoSortedLinkedLists(ListNode l1, ListNode l2){
	        if(l1 == null && l2 == null){
	            return null;
	        }
	        
	        if(l1 == null || l2 == null){
	            return l1 != null ? l1 : l2;
	        }
	        
	        return mergeLists(l1, l2);
	    }
	    
	    public ListNode mergeLists(ListNode l1, ListNode l2){
	        if(l1 == null && l2 == null){
	            return null;
	        }
	        
	        ListNode temp = new ListNode();
	        ListNode resultList = temp;
	        
	        while(l1 != null && l2 != null){
	            if(l1.val < l2.val){
	               temp.next = l1;
	                l1 = l1.next;
	            } else {
	                temp.next = l2;
	                l2 = l2.next;
	            }
	            
	            temp = temp.next;
	        }
	        
	        temp.next = l1 == null ? l2 : l1;
	        
	        return resultList.next;
	    }
}
