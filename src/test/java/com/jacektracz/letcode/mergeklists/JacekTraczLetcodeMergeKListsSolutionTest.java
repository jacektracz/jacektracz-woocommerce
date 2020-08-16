package com.jacektracz.letcode.mergeklists;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.Ignore;
import org.junit.Test;

public class JacekTraczLetcodeMergeKListsSolutionTest {

	final static int HANDLER_TYPE =1;
	private boolean TEST_CHOOSEN_TEST_CASE_ONLY = false;
	private boolean TEST_DEBUG_MODE = false;
	private boolean EXEC_DEBUG_MODE = false;
	public ListNode execHandler(int ptype, boolean deb_mode, ListNode [] ll_arr) {
				
		int type = ptype;
		
		if(HANDLER_TYPE >= 0) {
			type = HANDLER_TYPE;
		}
		
		if(type == 0) {
			JacekTraczMergeKListSolution handler = new JacekTraczMergeKListSolution();
			handler.DBG_MODE = false;
			ListNode lout = handler.mergeKLists( ll_arr );
			return lout;
		}
		
		if(type == 1) {
			JacekTraczLetcodeMergeKListsSolution handler = new JacekTraczLetcodeMergeKListsSolution();
			handler.DBG_MODE = false;
			ListNode lout = handler.mergeKLists( ll_arr );
			return lout;
		}
		
		if(type == 2) {
			JacekTraczLetcodeMergeKListsImmutableSolution handler = new JacekTraczLetcodeMergeKListsImmutableSolution();			
			ListNode lout = handler.mergeKLists( ll_arr );
			return lout;
		}
		
		return new ListNode(0);
	}	
	
	public void execTestmanyListsOneNode(int items,int val_step,int start_value,String tt,boolean p_test_debug,boolean p_handler_debug) throws Exception {
		String sFun = "execTestmanyListsOneNode";
		if(p_test_debug) dbgInfo(sFun + "-start");
		if(p_test_debug) dbgInfo(sFun + tt + "-start");
		
		SolutionData handler_data = new SolutionData();
		ListNode[] ll_arr = handler_data.getLists_WithOneNodes(items,val_step,start_value);		
		assertEquals(items,ll_arr.length);
		
		ListNode lout = execHandler(0,p_handler_debug,ll_arr);
		if(TEST_DEBUG_MODE) {
			if(p_test_debug) {
				int listLength = dbgList(lout, sFun);
				assertEquals(items,listLength);
			}
			if(p_test_debug) {
				String sErr = checkList(lout, sFun + "-OUT-LIST");
				assertEquals(true,sErr.isEmpty());
			}
			if(p_test_debug) dbgInfo(sFun + "-end");
		}
	}
	
	@Test	
	//@Ignore
	public void testListsWithOneNode_4() throws Exception {		
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE;
		execTestmanyListsOneNode(4,100,0,"testListsWithOneNode_4",test_debug,handler_debug);		
	}	
	
	@Test	
	//@Ignore
	public void testListsWithOneNode_1000() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE;
		execTestmanyListsOneNode(1000,100,0,"testListsWithOneNode_1000",test_debug,handler_debug);		
	}	
	
	@Test
	//@Ignore
	public void testListsWithOneNode_500() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE;
		execTestmanyListsOneNode(500,100,0,"testListsWithOneNode_500",test_debug,handler_debug);				
	}	

	@Test
	//@Ignore
	public void testListsWithOneNode_2000() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE;
		execTestmanyListsOneNode(2000,100,2,"testListsWithOneNode_2000",test_debug,handler_debug);		
	}	
	
	@Test
	//@Ignore
	public void testListsWithOneNode_5000() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE;
		execTestmanyListsOneNode(5000,100,2,"testListsWithOneNode_5000",test_debug,handler_debug);				
	}	
	
	@Test
	//@Ignore
	public void testListsWithOneNode_10000() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE;
		execTestmanyListsOneNode(10000,100,2,"testListsWithOneNode_10000",test_debug,handler_debug);				
	}	
	
	@Test
	//@Ignore
	public void testWitManyListsWithOneNode() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE;
		execTestmanyListsOneNode(2,2,2,"testListsWithOneNode_500",test_debug,handler_debug);				
	}	
	
	@Test
	//@Ignore
	public void testWithNotSortedLists() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		String sFun = "testWithOndNode";
		dbgInfo(sFun + "-start");
		int items =2;
		SolutionData handler_data = new SolutionData();
		ListNode ll = handler_data.getList_Nodes(items,2,2);
		dbgList(ll, sFun+ "-IN-LIST");
		ListNode[] ll_arr =  new  ListNode[1];
		ll_arr[0] = ll;
		
		
		ListNode lout = execHandler(0,true,ll_arr);
		if(TEST_DEBUG_MODE) {
			int listLength = dbgList(lout, sFun);
			assertEquals(items,listLength);				
			String sErr = checkList(lout, sFun + "-OUT-LIST");
			assertEquals(false,sErr.isEmpty());		
			dbgInfo(sFun + "-end");
		}
		
	}	
	
	
	@Test	
	//@Ignore
	public void testWithOneNode() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		String sFun = "testWithOndNode";
		dbgInfo(sFun + "-start");
		
		ListNode ll = getList_OneNodes();
		ListNode[] ll_arr =  new  ListNode[1];
		ll_arr[0] = ll;
		
		ListNode lout = execHandler(0,true,ll_arr);
		if(TEST_DEBUG_MODE) {
			int listLength = dbgList(lout, sFun);
			assertEquals(1,listLength);				
			String sErr = checkList(lout, sFun);
			assertEquals(true,sErr.isEmpty());		
			dbgInfo(sFun + "-end");
		}
		
	}	
	
	@Test
	//@Ignore
	public void testOneListWithTwoNode() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		String sFun = "testOneListWithTwoNode";
		dbgInfo(sFun + "-start");
		ListNode ll = getList_TwoNodes();
		ListNode[] ll_arr =  new  ListNode[1];
		ll_arr[0] = ll;
		ListNode lout = execHandler(0,true,ll_arr);
		
		if(TEST_DEBUG_MODE) {
			int listLength = dbgList(lout, sFun);
			assertEquals(2,listLength);		
			String sErr = checkList(lout, sFun);
			assertEquals(true,sErr.isEmpty());		
			dbgInfo(sFun + "-end");
		}
	}
	
	@Test
	//@Ignore
	public void testTwoListWithTwoNode() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		String sFun = "testTwoListWithTwoNode";
		dbgInfo(sFun + "-start");
		ListNode ll = getList_TwoNodes();
		ListNode l2 = getList_TwoNodes();
		ListNode[] ll_arr =  new  ListNode[2];
		ll_arr[0] = ll;
		ll_arr[1] = l2;
		
		ListNode lout = execHandler(0,true,ll_arr);
		if(TEST_DEBUG_MODE) {
			int listLength = dbgList(lout, sFun);
			assertEquals(4,listLength);
			String sErr = checkList(lout, sFun);
			assertEquals(true,sErr.isEmpty());		
			dbgInfo(sFun + "-end");
		}
	}
	
	@Test
	//@Ignore
	public void testTwoListWithThreeNodes() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		String sFun = "testTwoListWithThreeNodes";
		dbgInfo(sFun + "-start");
		ListNode ll =  getList_ThreeNodes();
		ListNode l2 =  getList_ThreeNodes();
		ListNode[] ll_arr =  new  ListNode[2];
		ll_arr[0] = ll;
		ll_arr[1] = l2;
		
		ListNode lout = execHandler(0,true,ll_arr);
		if(TEST_DEBUG_MODE) {
			dbgNode(lout,sFun);
			int listLength = dbgList(lout, sFun);
			assertEquals(6,listLength);
			String sErr = checkList(lout, sFun);
			assertEquals(true,sErr.isEmpty());
			dbgInfo(sFun + "-end");
		}
	}
	
	@Test	
	//@Ignore
	public void testWithOneNode_solution() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		String sFun = "testWithOndNode";
		dbgInfo(sFun + "-start");
		
		ListNode ll = getList_OneNodes();
		ListNode[] ll_arr =  new  ListNode[1];
		ll_arr[0] = ll;
		boolean handler_debug = EXEC_DEBUG_MODE;
		ListNode lout = execHandler(0,handler_debug,ll_arr);
		
		if(TEST_DEBUG_MODE) {
			int listLength = dbgList(lout, sFun);
			assertEquals(1,listLength);				
			String sErr = checkList(lout, sFun);
			assertEquals(true,sErr.isEmpty());		
			dbgInfo(sFun + "-end");
		}
		
	}	
	
	@Test	
	//@Ignore
	public void testOneListWithTwoNode_solution() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		String sFun = "testOneListWithTwoNode";
		dbgInfo(sFun + "-start");
		ListNode ll = getList_TwoNodes();
		ListNode[] ll_arr =  new  ListNode[1];
		ll_arr[0] = ll;
		boolean handler_debug = EXEC_DEBUG_MODE;
		ListNode lout = execHandler(0,handler_debug,ll_arr);
		if(TEST_DEBUG_MODE) {
			int listLength = dbgList(lout, sFun);
			assertEquals(2,listLength);		
			String sErr = checkList(lout, sFun);
			assertEquals(true,sErr.isEmpty());		
			dbgInfo(sFun + "-end");
		}
	}
	
	@Test
	//@Ignore
	public void testTwoListWithTwoNode_solution() throws Exception {
		
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		String sFun = "testTwoListWithTwoNode";
		dbgInfo(sFun + "-start");
		ListNode ll = getList_TwoNodes();
		ListNode l2 = getList_TwoNodes();
		ListNode[] ll_arr =  new  ListNode[2];
		ll_arr[0] = ll;
		ll_arr[1] = l2;
		boolean handler_debug = EXEC_DEBUG_MODE;
		ListNode lout = execHandler(0,handler_debug,ll_arr);
		
		if(TEST_DEBUG_MODE) {
			int listLength = dbgList(lout, sFun);
			assertEquals(4,listLength);
			String sErr = checkList(lout, sFun);
			assertEquals(true,sErr.isEmpty());		
			dbgInfo(sFun + "-end");
		}
	}
	
	@Test
	//@Ignore
	public void testTwoListWithThreeNodes_solution() throws Exception {
		
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		String sFun = "testTwoListWithThreeNodes";
		dbgInfo(sFun + "-start");
		ListNode ll =  getList_ThreeNodes();
		ListNode l2 =  getList_ThreeNodes();
		ListNode[] ll_arr =  new  ListNode[2];
		ll_arr[0] = ll;
		ll_arr[1] = l2;
		boolean handler_debug = EXEC_DEBUG_MODE;
		ListNode lout = execHandler(0,handler_debug,ll_arr);	
		if(TEST_DEBUG_MODE) {
			dbgNode(lout,sFun);
			int listLength = dbgList(lout, sFun);
			assertEquals(6,listLength);
			String sErr = checkList(lout, sFun);
			assertEquals(true,sErr.isEmpty());
			dbgInfo(sFun + "-end");
		}
	}

	@Test
	//@Ignore
	public void testEmptyList() throws Exception {
		
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			//return;
		}
		
		String sFun = "testTwoListWithThreeNodes";
		dbgInfo(sFun + "-start");
		ListNode ll =  getList_EmptyMode();		
		ListNode[] ll_arr =  new  ListNode[1];
		ll_arr[0] = ll;		
		boolean handler_debug = EXEC_DEBUG_MODE;
		ListNode lout = execHandler(0,handler_debug,ll_arr);
		if(TEST_DEBUG_MODE) {
			dbgNode(lout,sFun);
			int listLength = dbgList(lout, sFun);
			assertEquals(1,listLength);
			String sErr = checkList(lout, sFun);
			assertEquals(true,sErr.isEmpty());
			dbgInfo(sFun + "-end");
		}
	}

    private void dbgInfo ( String tt){
    	if(!TEST_DEBUG_MODE) {
    		return;
    	}
    	
        dbgInfoSubmitted(tt);
    }
    
    private void dbgInfoSubmitted ( String tt){

        System.out.println( tt );
    }
	
    private void dbgNode ( 
            ListNode p_nl
            , String tt){
    	
    	if(!TEST_DEBUG_MODE) {
    		return;
    	}
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
    	
    	if(!TEST_DEBUG_MODE) {
    		return 0;
    	}
    	
    	
    	int ii = dbgListTxt(p_nl,tt);
    	dbgListShort(p_nl,tt);
    	return ii;
    }    
    
    private int dbgListTxt ( 
        ListNode p_nl
        , String tt){
        
    	if(!TEST_DEBUG_MODE) {
    		return 0;
    	}
    	
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
    	
    	if(!TEST_DEBUG_MODE) {
    		return 0;
    	}
            
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
            
    	if(!TEST_DEBUG_MODE) {
    		return "";
    	}
    	
        	String sFun =  tt + " -> checkList::";
            dbgInfo("<<<");        	
            String sOut = "";
            ListNode nl = p_nl;            
            int maxVal = 0;
            int ii = 0;
            while(true){            	
                if(nl != null){                	
                   if( nl.val < maxVal) {
                	   sOut =  sOut + "[FAILED_VAL:" + nl.val + "][" + ii +"]";  
                   }else {
                	   maxVal = nl.val;
                   }
                }                
                if(nl == null){
                	break;
                }                
                nl = nl.next;
                ii++;
            }
            
            if(!sOut.isEmpty()) {
            	dbgInfo(sFun + "ERROR_IN_LIST:" + sOut);
            }
            
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
	
	private ListNode getList_EmptyMode() {
		ListNode l1 = new ListNode();
		return l1;
	}
	
}
