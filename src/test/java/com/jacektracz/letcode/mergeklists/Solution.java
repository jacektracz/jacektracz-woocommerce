package com.jacektracz.letcode.mergeklists;
import static org.hamcrest.MatcherAssert.assertThat;

import org.junit.Ignore;
import org.junit.Test;

public class Solution {
	
    private void dbgInfo ( String tt){
        System.out.println( tt );
    }
	
	@Test
	@Ignore
	public void testWithOneNode() throws Exception {
		String sFun = "testWithOndNode";
		dbgInfo(sFun + "-start");
		
		ListNode ll = getList_OneNodes();
		ListNode[] ll_arr =  new  ListNode[1];
		ll_arr[0] = ll;
		JacekTraczMergeKListSolution handler = new JacekTraczMergeKListSolution();
		handler.mergeKLists( ll_arr );
		dbgInfo(sFun + "-end");
		
	}	
	
	@Test
	@Ignore
	public void testOneListWithTwoNode() throws Exception {
		String sFun = "testWithTwoNode";
		dbgInfo(sFun + "-start");
		ListNode ll = getList_TwoNodes();
		ListNode[] ll_arr =  new  ListNode[1];
		ll_arr[0] = ll;
		JacekTraczMergeKListSolution handler = new JacekTraczMergeKListSolution();
		handler.mergeKLists( ll_arr );
		dbgInfo(sFun + "-end");
	}
	
	@Test
	public void testTwoListWithTwoNode() throws Exception {
		String sFun = "testWithTwoNode";
		dbgInfo(sFun + "-start");
		ListNode ll = getList_TwoNodes();
		ListNode l2 = getList_TwoNodes();
		ListNode[] ll_arr =  new  ListNode[2];
		ll_arr[0] = ll;
		ll_arr[1] = l2;
		JacekTraczMergeKListSolution handler = new JacekTraczMergeKListSolution();
		handler.mergeKLists( ll_arr );
		dbgInfo(sFun + "-end");
	}
	
	private ListNode getList_OneNodes() {
		ListNode ll = new ListNode(1);
		return ll;
	}
	
	private ListNode getList_TwoNodes() {
		ListNode l1 = new ListNode(1);
		ListNode l2 = new ListNode(2);
		l1.next = l2;
		return l1;
	}
	
	
}
