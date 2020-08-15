package com.jacektracz.letcode.mergeklists;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.Ignore;
import org.junit.Test;

public class Solution {
	
	
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
		String sErr = checkList(lout, sFun);
		assertEquals(true,sErr.isEmpty());		
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
		assertEquals(2,listLength);		
		String sErr = checkList(lout, sFun);
		assertEquals(true,sErr.isEmpty());		
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
		String sErr = checkList(lout, sFun);
		assertEquals(true,sErr.isEmpty());		
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
		dbgNode(lout,sFun);
		int listLength = dbgList(lout, sFun);
		assertEquals(6,listLength);
		String sErr = checkList(lout, sFun);
		assertEquals(true,sErr.isEmpty());
		dbgInfo(sFun + "-end");
	}

	
	
	
	
	
	@Test	
	public void testWithOneNode_solution() throws Exception {
		String sFun = "testWithOndNode";
		dbgInfo(sFun + "-start");
		
		ListNode ll = getList_OneNodes();
		ListNode[] ll_arr =  new  ListNode[1];
		ll_arr[0] = ll;
		JacekTraczMergeKListNoDebugSolution handler = new JacekTraczMergeKListNoDebugSolution();
		ListNode lout = handler.mergeKLists( ll_arr );
		int listLength = dbgList(lout, sFun);
		assertEquals(1,listLength);				
		String sErr = checkList(lout, sFun);
		assertEquals(true,sErr.isEmpty());		
		dbgInfo(sFun + "-end");
		
	}	
	
	@Test	
	public void testOneListWithTwoNode_solution() throws Exception {
		String sFun = "testOneListWithTwoNode";
		dbgInfo(sFun + "-start");
		ListNode ll = getList_TwoNodes();
		ListNode[] ll_arr =  new  ListNode[1];
		ll_arr[0] = ll;
		JacekTraczMergeKListNoDebugSolution handler = new JacekTraczMergeKListNoDebugSolution();
		ListNode lout = handler.mergeKLists( ll_arr );
		int listLength = dbgList(lout, sFun);
		assertEquals(2,listLength);		
		String sErr = checkList(lout, sFun);
		assertEquals(true,sErr.isEmpty());		
		dbgInfo(sFun + "-end");
	}
	
	@Test
	public void testTwoListWithTwoNode_solution() throws Exception {
		String sFun = "testTwoListWithTwoNode";
		dbgInfo(sFun + "-start");
		ListNode ll = getList_TwoNodes();
		ListNode l2 = getList_TwoNodes();
		ListNode[] ll_arr =  new  ListNode[2];
		ll_arr[0] = ll;
		ll_arr[1] = l2;
		JacekTraczMergeKListNoDebugSolution handler = new JacekTraczMergeKListNoDebugSolution();
		ListNode lout = handler.mergeKLists( ll_arr );
		int listLength = dbgList(lout, sFun);
		assertEquals(4,listLength);
		String sErr = checkList(lout, sFun);
		assertEquals(true,sErr.isEmpty());		
		dbgInfo(sFun + "-end");
	}
	
	@Test
	public void testTwoListWithThreeNodes_solution() throws Exception {
		String sFun = "testTwoListWithThreeNodes";
		dbgInfo(sFun + "-start");
		ListNode ll =  getList_ThreeNodes();
		ListNode l2 =  getList_ThreeNodes();
		ListNode[] ll_arr =  new  ListNode[2];
		ll_arr[0] = ll;
		ll_arr[1] = l2;
		JacekTraczMergeKListNoDebugSolution handler = new JacekTraczMergeKListNoDebugSolution();
		ListNode lout = handler.mergeKLists( ll_arr );
		dbgNode(lout,sFun);
		int listLength = dbgList(lout, sFun);
		assertEquals(6,listLength);
		String sErr = checkList(lout, sFun);
		assertEquals(true,sErr.isEmpty());
		dbgInfo(sFun + "-end");
	}
	
	
	
	
	
	
	
    private void dbgInfo ( String tt){
        dbgInfoSubmitted(tt);
    }
    
    private void dbgInfoSubmitted ( String tt){

        System.out.println( tt );
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
    	
    	int ii = dbgListTxt(p_nl,tt);
    	dbgListShort(p_nl,tt);
    	return ii;
    }    
    
    private int dbgListTxt ( 
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
	
    private int dbgListShort ( 
            ListNode p_nl
            , String tt){
            
        	String sFun =  tt + " -> dbgListShort::";
            dbgInfo(" ");
            dbgInfo(" ");
            dbgInfo("<<<<<");
            dbgInfo(sFun + "-start :");
            String sList = "";
            ListNode nl = p_nl;
            int ii =0;
            while(true){
            	
                if(nl != null){
                    sList = sList +"[";
                    sList = sList + nl.val;
                    sList = sList +"]";                             
                }
                
                if(nl == null){
                	break;
                }                
                nl = nl.next;
                ii++;
            }
            dbgInfo(sFun + " " + sList);
            dbgInfo(sFun + "end :");
            dbgInfo(">>>>");
            dbgInfo(" ");
            dbgInfo(" ");
            return ii;
    }
    
    private  String checkList ( 
            ListNode p_nl
            , String tt
            ){
            
        	String sFun =  tt + " -> checkList::";
            dbgInfo("<<<");        	
            String sOut = "";
            ListNode nl = p_nl;            
            int maxVal = 0;
            int ii = 0;
            while(true){            	
                if(nl != null){                	
                   if( nl.val <= maxVal) {
                	   sOut =  sOut + "[FAILED_VAL:" + nl.val + "][" + ii +"]";  
                   }                                                
                }                
                if(nl == null){
                	break;
                }                
                nl = nl.next;
                ii++;
            }

            dbgInfo(sFun + "ERROR_IN_LIST:" + sOut);
            dbgInfo(sFun + "end :");
            dbgInfo(">>>>");
            dbgInfo(" ");
            dbgInfo(" ");
            return  sOut;
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
