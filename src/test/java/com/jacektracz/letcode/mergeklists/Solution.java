package com.jacektracz.letcode.mergeklists;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.Ignore;
import org.junit.Test;

public class Solution {
	
    private void dbgInfo ( String tt){
        System.out.println( tt );
    }
	
	@Test	
	public void testWithOneNode() throws Exception {
		String sFun = "testWithOndNode";
		dbgInfo(sFun + "-start");
		
		ListNode ll = getList_OneNodes();
		ListNode[] ll_arr =  new  ListNode[1];
		ll_arr[0] = ll;
		JacekTraczMergeKListSolution handler = new JacekTraczMergeKListSolution();
		ListNode lout = handler.mergeKLists( ll_arr );
		int listLength = dbgList(lout, sFun);
		assertEquals(1,listLength);				
		dbgInfo(sFun + "-end");
		
	}	
	
	@Test	
	public void testOneListWithTwoNode() throws Exception {
		String sFun = "testOneListWithTwoNode";
		dbgInfo(sFun + "-start");
		ListNode ll = getList_TwoNodes();
		ListNode[] ll_arr =  new  ListNode[1];
		ll_arr[0] = ll;
		JacekTraczMergeKListSolution handler = new JacekTraczMergeKListSolution();
		ListNode lout = handler.mergeKLists( ll_arr );
		int listLength = dbgList(lout, sFun);
		assertEquals(4,listLength);		
		dbgInfo(sFun + "-end");
	}
	
	@Test
	public void testTwoListWithTwoNode() throws Exception {
		String sFun = "testTwoListWithTwoNode";
		dbgInfo(sFun + "-start");
		ListNode ll = getList_TwoNodes();
		ListNode l2 = getList_TwoNodes();
		ListNode[] ll_arr =  new  ListNode[2];
		ll_arr[0] = ll;
		ll_arr[1] = l2;
		JacekTraczMergeKListSolution handler = new JacekTraczMergeKListSolution();
		ListNode lout = handler.mergeKLists( ll_arr );
		int listLength = dbgList(lout, sFun);
		assertEquals(4,listLength);
		
		dbgInfo(sFun + "-end");
	}
	
	@Test
	public void testTwoListWithThreeNodes() throws Exception {
		String sFun = "testTwoListWithThreeNodes";
		dbgInfo(sFun + "-start");
		ListNode ll =  getList_ThreeNodes();
		ListNode l2 =  getList_ThreeNodes();
		ListNode[] ll_arr =  new  ListNode[2];
		ll_arr[0] = ll;
		ll_arr[1] = l2;
		JacekTraczMergeKListSolution handler = new JacekTraczMergeKListSolution();
		ListNode lout = handler.mergeKLists( ll_arr );
		int listLength = dbgList(lout, sFun);
		assertEquals(6,listLength);
		dbgInfo(sFun + "-end");
	}
	
	
    private void dbgNode ( 
            ListNode p_nl
            , String tt){
    	
    	String sFun =  tt + " -> dbgNode::";
    	
		dbgInfo(" ");
		dbgInfo(">>");
        dbgInfo(sFun + " -> dbgNode-start :");
        if(p_nl != null) {
        	dbgInfo(sFun + " value :" + p_nl.val) ;
        }else {
        	dbgInfo(sFun + " value :" + "NULL") ;
        }
        if(p_nl != null && p_nl.next != null) {
        	dbgInfo(sFun + " -> :" + p_nl.next.val) ;
        }
        
        dbgInfo(sFun + " dbgNode-end :");
        dbgInfo("<<");
        dbgInfo(" ");
    }

    
    private int dbgList ( 
        ListNode p_nl
        , String tt){
        
    	String sFun =  tt + " -> dbgList::";
        dbgInfo(" ");
        dbgInfo(" ");
        dbgInfo("<<<<<");
        dbgInfo(sFun + "-start :");
        
        ListNode nl = p_nl;
        int ii =0;
        while(true){
        	
            if(nl == null){
                dbgInfo(sFun + " node is null:") ;
                break;                   
            }
            dbgInfo(sFun + " value: " + nl.val) ;
            nl = nl.next;
            ii++;
        }
        
        dbgInfo(sFun + "end :");
        dbgInfo(">>>>");
        dbgInfo(" ");
        dbgInfo(" ");
        return ii;
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
	
	private ListNode getList_ThreeNodes() {
		ListNode l1 = new ListNode(1);
		ListNode l2 = new ListNode(1);
		l1.next = l2;
		ListNode l3 = new ListNode(2);
		l2.next = l3;		
		return l1;
	}
	
}
