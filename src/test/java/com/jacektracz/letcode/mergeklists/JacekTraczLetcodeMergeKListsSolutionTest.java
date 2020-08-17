package com.jacektracz.letcode.mergeklists;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.Test;

public class JacekTraczLetcodeMergeKListsSolutionTest {

	final static int HANDLER_TYPE =1;
	private int EXEC_HANDLER_VERSION = 3;
	private boolean TEST_CHOOSEN_TEST_CASE_ONLY =false;
	
	private int TEST_CHOOSEN_TEST_FOR_ONE_EXEC = 10000;
	
	private boolean TEST_DEBUG_MODE = false;
	private boolean EXEC_DEBUG_MODE_LVL3 = false;
	
	private boolean  EXEC_DEBUG_MODE_LVL0 = false;
	private boolean  EXEC_DEBUG_MODE_LVL1 = false;
	private boolean  EXEC_DEBUG_MODE_LVC0 = false;
	
	@Test	
	//@Ignore
	public void testListsWithOneNode_4() throws Exception {		
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE_LVL3;
		execTestmanyListsOneNode(4,100,0,"testListsWithOneNode_4",test_debug,handler_debug);		
	}
	
	@Test
	//@Ignore
	public void testListsWithOneNode_10() throws Exception {
		
		if(TEST_CHOOSEN_TEST_CASE_ONLY && (TEST_CHOOSEN_TEST_FOR_ONE_EXEC != 10)) {			
			return;			
		}
		
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE_LVL3;
		execTestmanyListsOneNode(10,3,2,"testListsWithOneNode_10",test_debug,handler_debug);				
	}	
	
	@Test	
	//@Ignore
	public void testListsWithOneNode_1000() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY && (TEST_CHOOSEN_TEST_FOR_ONE_EXEC != 1000)) {
			return;
		}
		
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE_LVL3;
		execTestmanyListsOneNode(1000,100,0,"testListsWithOneNode_1000",test_debug,handler_debug);		
	}	
	
	@Test
	//@Ignore
	public void testListsWithOneNode_500() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY && (TEST_CHOOSEN_TEST_FOR_ONE_EXEC != 500)) {
			return;
		}
		
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE_LVL3;
		execTestmanyListsOneNode(500,100,2,"testListsWithOneNode_500",test_debug,handler_debug);				
	}
	
	@Test
	//@Ignore
	public void testListsWithOneNode_20() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY && (TEST_CHOOSEN_TEST_FOR_ONE_EXEC != 20)) {
			return;
		}
		
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE_LVL3;
		execTestmanyListsOneNode(20,100,2,"testListsWithOneNode_2000",test_debug,handler_debug);		
	}	
	
	@Test
	//@Ignore
	public void testListsWithOneNode_100() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY && (TEST_CHOOSEN_TEST_FOR_ONE_EXEC != 100)) {
			return;
		}
		
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE_LVL3;
		execTestmanyListsOneNode(100,100,2,"testListsWithOneNode_500",test_debug,handler_debug);				
	}	
	

	@Test
	//@Ignore
	public void testListsWithOneNode_2000() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE_LVL3;
		execTestmanyListsOneNode(2000,100,2,"testListsWithOneNode_2000",test_debug,handler_debug);		
	}	
	
	@Test
	//@Ignore
	public void testListsWithOneNode_5000() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY&& (TEST_CHOOSEN_TEST_FOR_ONE_EXEC != 5000)) {
			return;
		}
		
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE_LVL3;
		execTestmanyListsOneNode(5000,100,2,"testListsWithOneNode_5000",test_debug,handler_debug);				
	}
	
	@Test
	//@Ignore
	public void testListsWithOneNode_8000() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY&& (TEST_CHOOSEN_TEST_FOR_ONE_EXEC != 8000)) {
			return;
		}
		
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE_LVL3;
		execTestmanyListsOneNode(8000,100,2,"testListsWithOneNode_8000",test_debug,handler_debug);				
	}	
	
	@Test
	//@Ignore
	public void testListsWithOneNode_10000() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY && (TEST_CHOOSEN_TEST_FOR_ONE_EXEC != 10000)) {
			return;
		}
		
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE_LVL3;
		execTestmanyListsOneNode(10000,100,2,"testListsWithOneNode_10000",test_debug,handler_debug);				
	}
	
	
	@Test
	//@Ignore
	public void testWitManyListsWithOneNode() throws Exception {
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		boolean test_debug = TEST_DEBUG_MODE;
		boolean handler_debug = EXEC_DEBUG_MODE_LVL3;
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
		validateList(lout,sFun,items);

		
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
		validateList(lout,sFun,1);

		
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
		
		validateList(lout,sFun,2);

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
		
		validateList(lout,sFun,4);
		
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
		
		validateList(lout,sFun,6);
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
		boolean handler_debug = EXEC_DEBUG_MODE_LVL3;
		ListNode lout = execHandler(0,handler_debug,ll_arr);
		
		validateList(lout,sFun,1);
		
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
		boolean handler_debug = EXEC_DEBUG_MODE_LVL3;
		ListNode lout = execHandler(0,handler_debug,ll_arr);
		
		validateList(lout,sFun,2);
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
		boolean handler_debug = EXEC_DEBUG_MODE_LVL3;
		ListNode lout = execHandler(0,handler_debug,ll_arr);
		
		validateList(lout,sFun,4);
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
		boolean handler_debug = EXEC_DEBUG_MODE_LVL3;
		ListNode lout = execHandler(0,handler_debug,ll_arr);	
		validateList(lout,sFun,6);
	}

	@Test
	//@Ignore
	public void testEmptyList() throws Exception {
		
		if(TEST_CHOOSEN_TEST_CASE_ONLY) {
			return;
		}
		
		String sFun = "testTwoListWithThreeNodes";
		dbgInfo(sFun + "-start");
		ListNode ll =  getList_EmptyMode();		
		ListNode[] ll_arr =  new  ListNode[1];
		ll_arr[0] = ll;		
		boolean handler_debug = EXEC_DEBUG_MODE_LVL3;
		ListNode lout = execHandler(EXEC_HANDLER_VERSION,handler_debug,ll_arr);
		validateList(lout,sFun,1);
	}
	
    private void validateList (ListNode lout,String sFun,int expected_length){
    	
    	if(TEST_DEBUG_MODE) {
    		
    		String sFunV =  "::validateList::";
    		
			dbgNode(lout,sFun);
			
			dbgList(lout,  sFun + sFunV );
			int listLength = dbgList(lout, sFun + sFunV);
			if(expected_length >= 0) {
				assertEquals(expected_length,listLength);
			}
			checkList(lout, sFun);
			//assertEquals(true,sErr.isEmpty());
			dbgInfo(sFun + "-end");
		}
	}
    
	public ListNode execHandler(int ptype, boolean deb_mode, ListNode [] ll_arr) {
		
		int type = EXEC_HANDLER_VERSION;
		if(type == 1){
			JacekTraczLetcCodeMergeSortedKlistsVersion1Solution handler = new JacekTraczLetcCodeMergeSortedKlistsVersion1Solution();
			ListNode lout = handler.mergeKLists( ll_arr );
			return lout;
		}
		
		if(type == 2) {
			JacekTraczLetCodeMergeSortedKListsVersion2Solution handler = new JacekTraczLetCodeMergeSortedKListsVersion2Solution();
			handler.setDebugModeLvl3(  EXEC_DEBUG_MODE_LVL3 );
			handler.setDebugModeLvl0( EXEC_DEBUG_MODE_LVL0  );
			handler.setDebugModeLvl1( EXEC_DEBUG_MODE_LVL1  );
			ListNode lout = handler.mergeKLists( ll_arr );
			return lout;
		}
		if(type == 3) {
			JacekTraczLetCodeMergeSortedKListsVersion3Solution handler = new JacekTraczLetCodeMergeSortedKListsVersion3Solution();
			handler.setDebugModeLvl3(  EXEC_DEBUG_MODE_LVL3 );
			handler.setDebugModeLvl0( EXEC_DEBUG_MODE_LVL0  );
			handler.setDebugModeLvl1( EXEC_DEBUG_MODE_LVL1  );			
			handler.setDebugModeLvc0( EXEC_DEBUG_MODE_LVC0  );
			ListNode lout = handler.mergeKLists( ll_arr );
			return lout;
		}
		
		return null;	
	}	
		
	public void execTestmanyListsOneNode(int items,int val_step,int start_value,String tt,boolean p_test_debug,boolean p_handler_debug) throws Exception {
		String sFun = "execTestmanyListsOneNode";
		if(p_test_debug) dbgInfo(sFun + "-start");
		if(p_test_debug) dbgInfo(sFun + tt + "-start");
		
		SolutionData handler_data = new SolutionData();
		ListNode[] ll_arr = handler_data.getLists_WithOneNodes(items,val_step,start_value);		
		assertEquals(items,ll_arr.length);
		
		ListNode lout = execHandler(EXEC_HANDLER_VERSION,p_handler_debug,ll_arr);
		
		validateList(lout,sFun,items);
	
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
