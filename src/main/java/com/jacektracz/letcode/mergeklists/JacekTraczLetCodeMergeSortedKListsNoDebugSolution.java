package com.jacektracz.letcode.mergeklists;

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

class JacekTraczLetCodeMergeSortedKListsNoDebugSolution {
	
	static class SolutionStatistics{
		public int dividions_count = 0;
		public int merge_list_count = 0;
		public int merge_nodes_count = 0;
	}	           
    
    private boolean HANDLE_TAILS = false;    
    private boolean MERGE_IN_PLACE = true;
    private boolean MERGE_IMMUTABLE = false;
    
    private int debugLevel = 5;    
    
    public boolean isDebugLevel5() {
    	return debugLevel <= 5;
    }
    
    public boolean isDebugLevel4() {
    	return debugLevel <= 4;
    }
    
    public boolean isDebugLevel3() {
    	return debugLevel <= 3;
    }
    
    public boolean isDebugLevel2() {
    	return debugLevel <= 2;
    }
    
    public boolean isDebugLevel1() {
    	return debugLevel <= 1;
    }
    
    public boolean isDebugLevel0() {
    	return debugLevel == 0;
    }
    
    public void setDebugLevel5(int pdebug) {
    	 debugLevel = pdebug;
    }
    
    
    public void setMergeImmutable(boolean dbg) {
    	MERGE_IMMUTABLE = dbg;
    }
    
    public void setMergeInPlace(boolean dbg) {
    	MERGE_IN_PLACE = dbg;
    }
    
    
    public ListNode mergeKLists( ListNode[] lists ) {
    	
    	String debugInfo = "";
    	String sFun = "> mergeKLists::"; 
    	if(isDebugLevel0()) dbgInfoLvl3(sFun  + "start :");
    	
    	if(isDebugLevel0()) {
	    	for(int ii =0;ii< lists.length; ii ++) {
	    		if(isDebugLevel0()) dbgList(lists[ii], sFun + "in_lis_on_idx:" + ii);		
	    	}
    	}
    	ListNode out_merged_list = mergeKListsInternal(debugInfo,lists);
        if(isDebugLevel0()) dbgList(out_merged_list, sFun + "out_merged_list::end");
        if(isDebugLevel0()) dbgInfoLvl3(sFun  + "end :");
        
        return out_merged_list;
    }
    
    public ListNode mergeKListsInternal(String debugInfo, ListNode[] lists) {
    	
        String sFunR = debugInfo + " -> mergeKListsInternal::";
        String lv = "[LVL-0]";
        if(isDebugLevel0()) dbgInfoLvl3(sFunR  + "start :");
        
        ListNode lout = mergeArrayOfKlistsl(debugInfo, lists);
        
        if(isDebugLevel0()) dbgInfoLvl3(sFunR  + "end :");
        
        return lout;
    }
    
    public ListNode mergeArrayOfKlistsl(String debugInfo, ListNode[] plists) {
        String sFunR = debugInfo + " -> mergeArrayOfKlistsl::";
        String lv = "[LVL-A]";
        if(isDebugLevel0()) dbgInfoLvl3(sFunR  + "start :");
        
        if(isDebugLevel5()) dbgInfoSubmitted(sFunR  + "lists_count :" + plists.length);
        
        ListNode[] lists = new ListNode[plists.length];
		if(isDebugLevel5()) {	
    		dbgInfoSubmitted(sFunR  + "initial_list_length :" + plists.length);
		}
        
        getNotNullArr(sFunR + lv, plists, lists);
        
    	ListNode[] divided_merged_list = lists;    	
    	int[] out_list_lenght = new int[1];
    	
    	SolutionStatistics stats = new SolutionStatistics();
    	while ( true ) {    		
    		out_list_lenght[0] = 0;
    		
    		stats.dividions_count++;
    		SolutionStatistics tmpstats = new SolutionStatistics();
    		divided_merged_list = getDividedMergedArray( 
    				debugInfo
    				, divided_merged_list
    				, out_list_lenght
    				, lists
    				, tmpstats);
    		
    		if(isDebugLevel5()) {	
	    		int dividedLengthTmp = (lists.length/2)+2; 
	    		ListNode[] dividedListTmp =  new ListNode[dividedLengthTmp];
	    		int listLength = getNotNullArr(sFunR + lv, divided_merged_list, dividedListTmp);
	    		dbgInfoSubmitted(sFunR  + "divided_list_length :" + listLength);
    		}
    		
    		stats.merge_list_count += tmpstats.merge_list_count;
    		stats.merge_nodes_count += tmpstats.merge_nodes_count;
    		if(out_list_lenght [0] <=1 ) {
    			break;
    		}    		
    	}
    	
    	if(isDebugLevel5()) dbgInfoSubmitted(sFunR  + "[ii_dividions_count :" + stats.dividions_count + "]");
    	if(isDebugLevel5()) dbgInfoSubmitted(sFunR  + "[m_merge_list_count :" + stats.merge_list_count + "]");
    	if(isDebugLevel5()) dbgInfoSubmitted(sFunR  + "[m_merge_nodes_count :" + stats.merge_nodes_count + "]");
    	
    	if(isDebugLevel0()) dbgInfoLvl3(sFunR  + "end :");
    	return divided_merged_list[0];
    }    

    private boolean idxOutOfArray(int idx, int length) {
    	return idx == length;
    }
    
    
    public int getNotNullArr(String debugInfo, ListNode[] source_list ,ListNode[] dest_list) {
    
    	int jj = 0;
    	for(int ii = 0; ii<source_list.length;ii++) {
    		if(source_list[ii] != null) {
    			dest_list[jj] = source_list[ii];
    			jj++;
    		}
    	}
    	return jj;
    }
    
    public ListNode[] getDividedMergedArray(
    		String debugInfo
    		, ListNode[] source_divided_list
    		, int[] out_list_lenght
    		, ListNode[] source_lists
    		, SolutionStatistics stats) {
    	
        String sFunR = debugInfo + " -> getDividedMergedArray::";
        String lv = "[LVL-0]";
        if(isDebugLevel0()) dbgInfoLvl3(sFunR  + "start :");
        if(isDebugLevel0()) dbgHeaderLV0(sFunR  + "start :");
        
        if(isDebugLevel1()) dbgListsShortLvl1(source_divided_list, sFunR);
        
        if(isDebugLevel4()) dbgListsShortLvl0(source_divided_list, sFunR);
        
        if(isDebugLevel4() ) {
        	dbgListsShortLvl1(source_lists,  sFunR + lv + "source_lists" );
        	dbgListsShortLvl1(source_divided_list,  sFunR + lv + "source_divided_list" );
        }
        
        int ii_merged_list_current = 0;
        
        int lists_length = source_divided_list.length;
        int divided_length = (lists_length/2)+2; 
        if( isDebugLevel4() ) {
        	dbgInfoSubmitted(  sFunR + lv + "[divided_length:" + divided_length +"]");
        }        
        
        ListNode[] out_list = new ListNode[divided_length];
        int ii_out = 0;
        
        while(true){
        	stats.merge_list_count++;
            ListNode [] l_created_root_current = new ListNode[2];
            ListNode handled_0_root = null;
            ListNode handled_1_root = null;
            
        	int ii_merged_list_0 = ii_merged_list_current;
        	int ii_merged_list_1 = ii_merged_list_current + 1;
        	
        	if(idxOutOfArray(ii_merged_list_0, lists_length)) {        		    
        		break;
        	}
        	
        	handled_0_root = source_divided_list[ ii_merged_list_0 ];        	        	
        	if(handled_0_root == null) {
        		break;
        	}
                	
        	if(idxOutOfArray(ii_merged_list_1, lists_length)) {        		    
        		out_list[ii_out] = handled_0_root;
        		out_list_lenght[0]++;
        		break;
        	}
        	
        	handled_1_root = source_divided_list[ ii_merged_list_1 ];

        	if(handled_1_root == null) {
        		out_list[ii_out] = handled_0_root;
        		out_list_lenght[0]++;
        		break;
        	}
        	        	
        	if(isDebugLevel4() ) {
	        	logData( 
	        			l_created_root_current
	                    ,  handled_0_root
	                    ,  handled_1_root
	                    , sFunR + lv + "before-merge-two-lists" + "[roots:" + ii_merged_list_current + "]");
        	}
            
            if(isDebugLevel4() ) {
            	String phase = ":before-divide-merge:";
            	dbgListsShortLvl1(source_lists,  sFunR + lv + phase + ":source_lists" );
            	dbgListShortLvl1(handled_0_root,  sFunR + lv + phase +  "handled_0_root["  + ii_merged_list_0 + "]");
            	dbgListShortLvl1(handled_1_root,  sFunR + lv + phase +  "handled_1_root["  + ii_merged_list_1 + "]" );
            	dbgListsShortLvl1(source_divided_list,  sFunR + lv + phase +  "source_divided_list" );
            	dbgListsShortLvl1(out_list,  sFunR + lv + phase +  "out_list" );
            }
            
    		SolutionStatistics tmpstats = new SolutionStatistics();
    		
            
            mergeTwoSortedKLists(
            		l_created_root_current
            		, handled_0_root
            		, handled_1_root
            		, sFunR + "[roots:" + ii_merged_list_current + "]"
            		, tmpstats);
            
            stats.merge_nodes_count += tmpstats.merge_nodes_count;
            
            if(isDebugLevel4() ) {
	        	logData( 
	        			l_created_root_current
	                    ,  handled_0_root
	                    ,  handled_1_root
	                    , sFunR + lv + "after-merge-two-lists" + "[roots:" + ii_merged_list_current + "]");
            }
            
        	out_list_lenght[0]++;
            out_list[ ii_out ] = l_created_root_current[0];
            
            if( isDebugLevel4() ) {            
            	String phase = ":after-divide-merge:";
            	String sInfo = sFunR + lv + phase +  "l_created_root_current[0]["  + ii_merged_list_0 + "]";
            	dbgListShortLvl1(l_created_root_current[0],  sInfo);
            }            
            
            if( isDebugLevel4() ) {
            	
            	String phase = ":after-divide-merge:";
            	dbgListShortLvl1(handled_0_root,  sFunR + lv + phase +  "handled_0_root["  + ii_merged_list_0 + "]");
            	dbgListShortLvl1(handled_1_root,  sFunR + lv + phase +  "handled_1_root["  + ii_merged_list_1 + "]" );            	
            	dbgListsShortLvl1(out_list,  sFunR + lv + phase +  "out_list" );
            	
            	dbgListsShortLvl1(source_divided_list,  sFunR + lv + phase +  "source_divided_list" );
            	dbgListsShortLvl1(source_lists,  sFunR + lv + phase + ":source_lists" );            	
            }
            
            ii_out ++;            
            ii_merged_list_current = ii_merged_list_1+1;                              
        }
        
        if( out_list_lenght[0] != ii_out + 1 ) {
        	if(isDebugLevel4()) dbgInfoLvl0(sFunR  + "ALGH-ERR-A1");	
        }
        		
        out_list_lenght[0] = ii_out + 1;        
        
        if(isDebugLevel0()) dbgHeaderLV0(sFunR  + "end");
        if(isDebugLevel0()) dbgInfoLvl3(sFunR  + "end :");
        
        return out_list;
    }

    private void mergeTwoSortedKLists(
        ListNode[] l_out_created_root_current
        , ListNode l_handled_0_root
        , ListNode l_handled_1_root
        , String debugInfo
        , SolutionStatistics stats){
        
        
        String sFunMN =  debugInfo + "-> mergeTwoSortedKLists::";
        String lv = "[LVL-2]";
        
        if(isDebugLevel0()) dbgHeaderLV1(sFunMN + lv +  "[nodes:" + "start" + "]" + "s-start :");
        
        ListNode l_handled_0_current = l_handled_0_root;
        ListNode l_handled_1_current =   l_handled_1_root;      
        
        
        ListNode[] l_out_handled_0_root_current = new ListNode[2];
        l_out_handled_0_root_current[0] = l_handled_0_root;
        
        
        ListNode[] l_out_handled_1_root_current = new ListNode[2];
        l_out_handled_1_root_current[0] = l_handled_1_root;
        
        int ii_merged_nodes = 0;
        while( true )                
        {
        	stats.merge_nodes_count++;
        	if(isDebugLevel1()) dbgInfoLvl1("");        	
        	
        	if(isDebugLevel4()) dbgInfoLvl0(sFunMN + lv +  "[nodes_iteration:" + ii_merged_nodes + "]");
        	
        	if(isDebugLevel2()) {
	        	logData( 
	        			l_out_created_root_current
	                    ,  l_handled_0_current
	                    ,  l_handled_1_current
	                    ,  sFunMN + lv +  "[nodes:" + ii_merged_nodes + "]-before-merge-nodes");
        	}
        	SolutionStatistics tmpstats = new SolutionStatistics();        	
        	mergeTwoNodes( 
        		l_handled_0_current
                , l_handled_1_current
                , l_out_created_root_current
                , l_out_handled_0_root_current
                , l_out_handled_1_root_current
                , sFunMN +  "[ii_merged_nodes:" + ii_merged_nodes + "]"
                , tmpstats);
        
        	if( isDebugLevel4() ) {
        		
            	String ph = ":after-merge-two-nodes:";
            	dbgListShortLvl1(
            			l_out_created_root_current[0]
            			, sFunMN + lv +  "[nodes:" + ii_merged_nodes + "]" + ph );
            	
        	}
        	
        	if(isDebugLevel2()) {
	        	logData( 
	        			l_out_created_root_current
	                    ,  l_handled_0_current
	                    ,  l_handled_1_current
	                    ,  sFunMN + lv +  "[nodes:" + ii_merged_nodes + "]-after-merge-nodes");
        	}
        	l_handled_0_current = l_out_handled_0_root_current[1];
        	l_handled_1_current = l_out_handled_1_root_current[1];            
            
            if( l_handled_0_current == null   && HANDLE_TAILS ){
            	if(isDebugLevel0()) dbgInfoLvl3(sFunMN + lv +  "[nodes:" + ii_merged_nodes + "]" + "l_handled_0_current-is-empty");            	
            	if(l_out_created_root_current[1] != null ) {
            		l_out_created_root_current[1].next = l_handled_1_current;
            	}            	
                break;
            }
            
            if( l_handled_1_current == null   && HANDLE_TAILS){
            	if(isDebugLevel0()) dbgInfoLvl3(sFunMN + lv +  "[nodes:" + ii_merged_nodes + "]" + "l_handled_1_current-is-empty");            	
            	if( l_out_created_root_current[1]!= null ) {
            		l_out_created_root_current[1].next = l_handled_0_current;
            	}            	
                break;                
            }
        	
            if( l_handled_0_current == null  && l_handled_1_current == null ){
            	if(isDebugLevel0()) dbgInfoLvl3(sFunMN + lv +  "[nodes:" + ii_merged_nodes + "]" + "-ater=merge-break-on-empty-");            	
                break;
            }                                   
            ii_merged_nodes ++;                        
        }
        
        if(isDebugLevel0()) dbgHeaderLV1(sFunMN + lv +  "end :");
    }    

    private void mergeTwoNodes(
        ListNode l_in_handled_0_current        
        , ListNode l_in_handled_1_current
        , ListNode[] l_out_created_root_current
        , ListNode[] l_out_handled_0_root_current
        , ListNode[] l_out_handled_1_root_current
        , String debugInfo
        , SolutionStatistics stats){
        
        String sFun2N =  debugInfo + " -> * mergeTwoNode-LV-4s::";
        String lv = "[LVL-4]";
        if(isDebugLevel0()) dbgHeaderLV2(sFun2N  + lv + "-2N-start :");
                
        if(isDebugLevel0()) dbgInfoLvl3(sFun2N  + lv + "-initialize-out-current-pointers-start");        
        l_out_handled_0_root_current[1] = l_in_handled_0_current;
        l_out_handled_1_root_current[1] = l_in_handled_1_current;
        if(isDebugLevel0()) dbgInfoLvl3(sFun2N  + lv + "-initialize-out-current-pointers-end");
        
        ListNode l_created_left = null;                        
        
        int cases_check = 0;
        if(cases_check == 0) {
        	
        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-1-check-start") ;
        	
	        if(l_in_handled_0_current == null && l_in_handled_1_current == null){
	            if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + "case-1-exec-start") ;
	            if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + "no-nodes-to-handle") ;
	            
	            if(MERGE_IN_PLACE) {
	            	l_created_left = null;
	            }
	            
	            if(MERGE_IMMUTABLE) {
	            	l_created_left = null;
	            }
	            
	            l_out_handled_0_root_current[1] = null;
	            l_out_handled_1_root_current[1] = null;
	            
	            cases_check = 1;
	            if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + "case 1-exec-end") ;
	        }
	        
	        if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-1-check-end") ;
	        
        }
        
        if(cases_check == 0) {
        	
        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-2-check-start") ;
        	
	        if(l_in_handled_0_current == null && l_in_handled_1_current != null){
	            if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-2-exec-start") ;
	            if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " item-from-list-1-was-taken") ;
	            
	            if(MERGE_IN_PLACE) {
	            	l_created_left = l_in_handled_1_current;	
	            }
	            	            
	            if(MERGE_IMMUTABLE) {
	            	l_created_left = new ListNode(l_in_handled_1_current.val);
	            	l_created_left.next = null;
	            }
	            
	            l_out_handled_1_root_current[1] = l_in_handled_1_current.next;
	            
	            if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-2-exec-end") ;
	            cases_check = 2;
	        }
	        
	        if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-2-check-end") ;
	        
        }
        
        if(cases_check == 0) {
        	
        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-3-check-start") ;
        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current == null){
	        	
	            if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-3-exec-start") ;
	            if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " item-from-list-0-was-taken") ;
	            if(isDebugLevel4()) dbgInfoLvl0(sFun2N + lv + " item-from-list-0-was-taken") ;
	            
	            if(MERGE_IN_PLACE) {
	            	l_created_left = l_in_handled_0_current;	
	            }
	            
	            if(MERGE_IMMUTABLE) {
	            	l_created_left = new ListNode(l_in_handled_0_current.val);   
	            	l_created_left.next = null;
	            }
	            
	            l_out_handled_0_root_current[1] = l_in_handled_0_current.next;
	            l_out_handled_1_root_current[1] = l_in_handled_1_current;
	            		
	            cases_check = 3;
	            if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-3-exec-end") ;
	            
	        }
	        
	        if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-3-check-end") ;
	        
        }
        
        if(cases_check == 0) {
        	
        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-4-check-start") ;
        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current != null){
	        	
	        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-4-check-vals-start");	        
	        	
	            if( l_in_handled_0_current.val < l_in_handled_1_current.val ){
	            	
	            	if(isDebugLevel0()) {
		            	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-4-exec-start") ;
		            	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " item-from-list-0-was-taken");	            	
		            	if(isDebugLevel4()) dbgInfoLvl0(sFun2N + lv + " item-from-list-0-was-taken");
	            	}
	            	if(MERGE_IN_PLACE) {
	            		l_created_left = l_in_handled_0_current;	            		
	            	}
	            	
	            	if(MERGE_IMMUTABLE) {
	            		l_created_left = new ListNode(l_in_handled_0_current.val);
	            	}
	            	
	            	l_out_handled_0_root_current[1] = l_in_handled_0_current.next;
	            	l_out_handled_1_root_current[1] = l_in_handled_1_current;
	            	
	                cases_check = 4;
	                if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-4-exec-end") ;	                
	            }	            
	            if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-4-check-vals-end") ;
	        }	        
	        if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-4-check-end") ;	        
        }
        
        if(cases_check == 0) {        	
        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-7-check-start") ;        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current != null){	        	
	        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-7-check-vals-start") ;
	        	
	            if(l_in_handled_0_current.val == l_in_handled_1_current.val){
	            	if(isDebugLevel0()) {
		            	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-7-exec-start") ;
		            	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " item-from-list-1-was-taken") ;
		            	if(isDebugLevel4()) dbgInfoLvl0(sFun2N + lv + " item-from-list-1-was-taken") ;
	            	}
	            	
	            	if(MERGE_IN_PLACE) {
	            		l_created_left = l_in_handled_1_current;
	            	}	            	
	            	
	            	if(MERGE_IMMUTABLE) {
	            		l_created_left = new ListNode(l_in_handled_1_current.val);
	            		l_created_left.next = null;
	            	}
	            	
	            	l_out_handled_0_root_current[1] = l_in_handled_0_current;
	            	l_out_handled_1_root_current[1] = l_in_handled_1_current.next;
	            	
	                cases_check = 7;
	                if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-7-exec-end") ;
	                
	            }	            
	            if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-7-check-vals-end") ;	            
	        }	        
	        if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-7-check-end") ;
	        
        }
        
        if(cases_check == 0) {
        	
        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-5-check-start") ;        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current != null){
	        	
	        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-5-check-vals-start") ;
	        	
	            if(l_in_handled_0_current.val == l_in_handled_1_current.val){
	            	
	            	if(isDebugLevel0()) {
		            	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-5-exec-start") ;
		            	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " item-from-list-0-was-taken") ;	    
		            	if(isDebugLevel4()) dbgInfoLvl0(sFun2N + lv + " item-from-list-0-was-taken") ;
	            	}
	            	
	            	if(MERGE_IN_PLACE) {
	            		l_created_left = l_in_handled_0_current;
	            	}
	            	
	            	if(MERGE_IMMUTABLE) {
	            		l_created_left = new ListNode(l_in_handled_0_current.val);
	            		l_created_left.next = null;
	            	}
	            	
	            	l_out_handled_0_root_current[1] = l_in_handled_0_current.next;
	            	l_out_handled_1_root_current[1] = l_in_handled_1_current;
	            	
	                cases_check = 5;
	                
	                if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-5-exec-end") ;	                
	            }	            
	            if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-5-check-vals-end") ;	            
	        }	        
	        if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-5-check-end") ;	        
        }
        
        if(cases_check == 0) {
        	
        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-6-check-start") ;
        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current != null){
	        	
	        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-6-check-vals-start") ;
	        	
	            if(l_in_handled_0_current.val > l_in_handled_1_current.val){     
	            	
	                if(isDebugLevel0()) dbgInfoLvl3(debugInfo + " case-6-start") ;
	                if(isDebugLevel4()) dbgInfoLvl0(sFun2N + lv + " item-from-list-1-was-taken") ;
	                
	                if(MERGE_IN_PLACE) {
	                	l_created_left = l_in_handled_1_current;
	                }
	                
	                if(MERGE_IMMUTABLE) {
	                	l_created_left = new ListNode(l_in_handled_1_current.val);
	                	l_created_left.next = null;
	                }
	                
	                l_out_handled_0_root_current[1] = l_in_handled_0_current;
	                l_out_handled_1_root_current[1] = l_in_handled_1_current.next;
	                
	                
	                cases_check = 6;
	                if(isDebugLevel0()) dbgInfoLvl3(debugInfo + " case-6-end") ;	                
	            }	            
	            if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-6-check-vals-end") ;	            
	        }	        
	        if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " case-6-check-end") ;
	        
        }
        
        if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-cases-end-" + cases_check);
        
        if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-cases-end-" + cases_check);
        
        if(isDebugLevel0()) dbgInfoLvl3("") ;
        
        int resolved_items = 0;
        if( resolved_items == 0 ) {        	
        	
        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-4-start");
        	
	        if( l_created_left == null ){
	        	
	        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-4-exec-start");
	        	
	        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + "no-items-to-handle-work-finished-current-out-pinter-to-null:");
	        	
	            l_out_created_root_current[1] = null;
	            resolved_items = 4;
	            
	            if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-4-exec-end");
	            
	        }else {
	        	
	        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-4-no-check");
	        	
	        }
	        
	        if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-4-end");
	        
        }
        
        if( resolved_items == 0 ) {
        	
        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-1-start");
        	
	        if( l_out_created_root_current[0] == null ){
	        	
	        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-1-exec-start");
	        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + "fill-root-first-time-set-current-as-root");
	        	
	        	l_created_left.next = null;
	            l_out_created_root_current[0] = l_created_left;
	            l_out_created_root_current[1] = l_created_left;
	            resolved_items = 1;
	            
	            if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-1-exec-end");
	            
	        }else {
	        	
	        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-1-no-check");
	        	
	        }
	        
	        if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-1-end");
	        
        }
        
        if( resolved_items == 0 ) {
        	
        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-2-start");
        	
	        if( l_out_created_root_current[0] != null && l_out_created_root_current[1] == null){
	        	
	        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-2-exec-start :");
	        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " should-not-exists:ERROR-OCCURED");
	        	
	        	ListNode last_created_node = l_out_created_root_current[1];	        	
	        	last_created_node.next = l_created_left;	        	
	            l_out_created_root_current[1] = l_created_left;	            
	            resolved_items = 2;
	            
	            if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-2-exec-end :");
	            
	        }else {
	        	
	        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-2-no-check :");
	        	
	        }
	        
	        if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-2-end");
        }
        
        if( resolved_items == 0 ) {
        	
        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-3-start");
        	
	        if( l_out_created_root_current[0] != null && l_out_created_root_current[1] != null){
	        	
	        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-3-exec-start :");
	        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-2-move-current-to-right :");
	        	
	        	ListNode last_created_node = l_out_created_root_current[1];	        	
	        	last_created_node.next = l_created_left;	        	
	            l_out_created_root_current[1] = l_created_left;	            
	            resolved_items = 3;
	            
	            if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-3-exec-end");
	            
	        }else {	        	
	        	if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-3-no-check");	        	
	        }
	        
	        if(isDebugLevel0()) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-3-end");
	        
        }
                        
        if(isDebugLevel0()) dbgHeaderLV2(sFun2N + lv + "-2N-end :");
        
        return ;
        
    }
    
    private void dbgNode ( 
            ListNode par_list
            , String debugInfo){
    	
    	String sFun =  debugInfo + " -> dbgNode::";
    	
		if(isDebugLevel0()) dbgInfoLvl3(" ");
		if(isDebugLevel0()) dbgInfoLvl3(">>");
        if(isDebugLevel0()) dbgInfoLvl3(sFun + " -> dbgNode-start :");
        if(par_list != null) {
        	if(isDebugLevel0()) dbgInfoLvl3(sFun + " value :" + par_list.val) ;
        }else {
        	if(isDebugLevel0()) dbgInfoLvl3(sFun + " value :" + "NULL") ;
        }
        if(par_list != null && par_list.next != null) {
        	if(isDebugLevel0()) dbgInfoLvl3(sFun + " -> :" + par_list.next.val) ;
        }
        
        if(isDebugLevel0()) dbgInfoLvl3(sFun + " dbgNode-end :");
        if(isDebugLevel0()) dbgInfoLvl3("");
        if(isDebugLevel0()) dbgInfoLvl3("");
        
    }

    
    private int dbgList ( 
            ListNode par_list
            , String debugInfo){
    	if(!isDebugLevel0()) {
    		return 0;
    	}
    	int ii = dbgListTxt(par_list,debugInfo);
    	dbgListShortLvl1(par_list,debugInfo);
    	checkList(par_list,debugInfo);
    	return ii;
    }
    
    
    private int dbgListTxt ( 
        ListNode par_list
        , String debugInfo){
    	if(!isDebugLevel0()) {
    		return 0;
    	}
        
    	String sFun =  debugInfo + " -> dbgList::";
        if(isDebugLevel0()) dbgInfoLvl3(" ");
        if(isDebugLevel0()) dbgInfoLvl3(" ");
        if(isDebugLevel0()) dbgInfoLvl3("<<<<<");
        if(isDebugLevel0()) dbgInfoLvl3(sFun + "-start :");
        
        ListNode nl = par_list;
        int ii =0;
        while(true){
        	
            if(nl == null){
                if(isDebugLevel0()) dbgInfoLvl3(sFun + " node is null:") ;
                break;                   
            }
            if(isDebugLevel0()) dbgInfoLvl3(sFun + " value: " + nl.val) ;
            nl = nl.next;
            ii++;
        }
        
        if(isDebugLevel0()) dbgInfoLvl3(sFun + "end :");
        if(isDebugLevel0()) dbgInfoLvl3(">>>>");
        if(isDebugLevel0()) dbgInfoLvl3(" ");
        if(isDebugLevel0()) dbgInfoLvl3(" ");
        return ii;
    }
    
    private int dbgListsShortLvl0 ( 
            ListNode []par_list
            , String debugInfo){
    	
    	if(!isDebugLevel4()) {
    		return 0;
    	}
    	
	    for (int ii = 0;ii<par_list.length;ii++) {
	    	
	    	dbgListShortLvl0(par_list[ii],debugInfo);	
	    }
	    return 0;
    }
    
    private int dbgListsShortLvl1 ( 
            ListNode []par_list
            , String debugInfo){
    	
    	boolean proceed = false;
    	if(isDebugLevel1()) {
    		proceed = true;
    	}    	
    	
    	if(isDebugLevel4()) {
    		proceed = true;
    	}    	
    	
    	if(isDebugLevel4()) {
    		proceed = true;
    	}    	
    	if(!proceed) {
    		return 0;
    	}
	    for (int ii = 0;ii<par_list.length;ii++) {	    	
	    	if(par_list[ii] != null) {	    		
	    		dbgInfoSubmitted(debugInfo + "list-idx:" + ii);
	    		dbgListShortLvl1(par_list[ii],debugInfo);	    		
	    	}else {	    		
	    		dbgInfoSubmitted(debugInfo + "list-idx:" + ii +" -> null");	    		
	    	}
	    }
	    return 0;
    }
    
    private int dbgListShortLvl0 ( 
            ListNode par_list
            , String debugInfo){
    	
    	boolean proceed = false;
    	if(isDebugLevel1()) {
    		proceed = true;
    	}    	
    	
    	if(isDebugLevel4()) {
    		proceed = true;
    	}    	
    	
    	if(isDebugLevel4()) {
    		proceed = true;
    	}
    	
    	if(!proceed) {
    		return 0;
    	}
    	
	    return dbgListShorInternal(par_list,debugInfo);	    	
    }	
    
    private int dbgListShortLvl1 ( 
            ListNode par_list
            , String debugInfo){
    	
    	if(!isDebugLevel1()) {
    		return 0;
    	}
    	
	    return dbgListShorInternal(par_list,debugInfo);	    	
    }	
    
    private int dbgListShorInternal ( 
            ListNode par_list
            , String debugInfo){
    	            
        	String sFun =  debugInfo + " -> dbgListShort::";
            if(isDebugLevel0()) dbgInfoLvl3(" ");
            if(isDebugLevel0()) dbgInfoLvl3(" ");
            if(isDebugLevel0()) dbgInfoLvl3("<<<<<");
            if(isDebugLevel0()) dbgInfoLvl3(sFun + "-start :");
            
            String sList = "";
            int ii = 0;
            boolean to_count = false;
            
            if(isDebugLevel4()) {
            	to_count = true;
            }
            
            if(isDebugLevel4()) {
            	to_count = true;
            }
            
            if(isDebugLevel1()) {
            	to_count = true;
            }
            
            if(to_count) {
            	
	            ListNode nl = par_list;
	            
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
            }
            
            int printed = 0;
            if(printed == 0) {
            	if(isDebugLevel4()) dbgInfoSubmitted(sFun + " " + sList);
            	printed = 1;
            }
            if(printed == 0) {
            	if(isDebugLevel1()) dbgInfoSubmitted(sFun + " " + sList);
            	printed = 1;
            }            
            if(printed == 0) {
            	if(isDebugLevel4()) dbgInfoSubmitted(sFun + " " + sList);
            	printed = 1;
            }
            
            if(isDebugLevel0()) dbgInfoLvl3(sFun + " " + sList);
            if(isDebugLevel0()) dbgInfoLvl3(sFun + "end :");
            if(isDebugLevel0()) dbgInfoLvl3(">>>>");
            if(isDebugLevel0()) dbgInfoLvl3(" ");
            if(isDebugLevel0()) dbgInfoLvl3(" ");
            return ii;
    }

    
    private void dbgHeaderLV0 (String debugInfo) {
    	if(!isDebugLevel0()) {
    		return ;
    	}
    	
    	dbgN5();
    	if(isDebugLevel0()) dbgInfoLvl3("");
    	if(isDebugLevel0()) dbgInfoLvl3("");
        if(isDebugLevel0()) dbgInfoLvl3("================================================================");
        if(isDebugLevel0()) dbgInfoLvl3("=");
        if(isDebugLevel0()) dbgInfoLvl3("=");
        if(isDebugLevel0()) dbgInfoLvl3("=" + debugInfo);
        if(isDebugLevel0()) dbgInfoLvl3("=");
        if(isDebugLevel0()) dbgInfoLvl3("=");
        if(isDebugLevel0()) dbgInfoLvl3("================================================================");
        if(isDebugLevel0()) dbgInfoLvl3("");
        if(isDebugLevel0()) dbgInfoLvl3("");
        dbgN5();
    	
    }
    
    private void dbgHeaderLV1 (String debugInfo) {
    	if(!isDebugLevel0()) {
    		return ;
    	}
    	
    	dbgN5();
    	if(isDebugLevel0()) dbgInfoLvl3("");
        if(isDebugLevel0()) dbgInfoLvl3("****************************************************************");
        if(isDebugLevel0()) dbgInfoLvl3("*");
        if(isDebugLevel0()) dbgInfoLvl3("**" + debugInfo);
        if(isDebugLevel0()) dbgInfoLvl3("*");        
        if(isDebugLevel0()) dbgInfoLvl3("****************************************************************");
        if(isDebugLevel0()) dbgInfoLvl3("");
        dbgN5();
    	
    }
    
    private void dbgHeaderLV2 (String debugInfo) {
    	if(!isDebugLevel0()) {
    		return ;
    	}
    	
    	dbgN5();
    	if(isDebugLevel0()) dbgInfoLvl3("");
        if(isDebugLevel0()) dbgInfoLvl3("--------------------------------------------------------------");                
        if(isDebugLevel0()) dbgInfoLvl3("-" + debugInfo);               
        if(isDebugLevel0()) dbgInfoLvl3("---------------------------------------------------------------");
        if(isDebugLevel0()) dbgInfoLvl3("");
        dbgN5();
    	
    }
    
    private void dbgN5 () {
    	if(!isDebugLevel0()) {
    		return ;
    	}
    	
    	if(isDebugLevel0()) dbgInfoLvl3("");
    	if(isDebugLevel0()) dbgInfoLvl3("");
    	if(isDebugLevel0()) dbgInfoLvl3("");
    	if(isDebugLevel0()) dbgInfoLvl3("");
    	if(isDebugLevel0()) dbgInfoLvl3("");
    }
    
    private  String checkList ( 
            ListNode par_list
            , String debugInfo
            ){
    	if(!isDebugLevel0()) {
    		return "";
    	}
            
        	String sFun =  debugInfo + " -> checkList::";
            if(isDebugLevel0()) dbgInfoLvl3("<<<");        	
            String sOut = "";
            ListNode nl = par_list;            
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
            	dbgInfoLvl3(sFun + "ERROR_IN_LIST:" + sOut);
            }

            if(isDebugLevel0()) dbgInfoLvl3(sFun + "end :");
            if(isDebugLevel0()) dbgInfoLvl3(">>>>");
            if(isDebugLevel0()) dbgInfoLvl3(" ");
            if(isDebugLevel0()) dbgInfoLvl3(" ");
            return  sOut;
    }
    
    
    private void dbgInfoLvl3 ( String debugInfo ){
    	if(!isDebugLevel0()) {
    		return ;
    	}
    	    	
        dbgInfoSubmitted(debugInfo);
        
    }
    
    private void dbgInfoLvl0 ( String debugInfo ){
    	
    	
    	if(!isDebugLevel4()) {
    		return ;
    	}
    	    	
        dbgInfoSubmitted(debugInfo);
        
    }
    
    private void dbgInfoLvl1 ( String debugInfo ){
    	
    	if(!isDebugLevel1()) {
    		return ;
    	}
    	    	
        dbgInfoSubmitted(debugInfo);
        
    }
    
    private void dbgInfoSubmitted ( String debugInfo ){    	
    	
    	String needle = "";
    	//needle ="LV-0";
    	
    	if(needle.isEmpty()) {
    		System.out.println( debugInfo );
    	}
    	
    	if(!needle.isEmpty()) {
    		if(debugInfo.indexOf(needle) >= 0) {
    			System.out.println( debugInfo );
    		}
    	}
    	
    }
    
    public void logData(
    		
    		ListNode[] l_created_root_current
            , ListNode handled_0_root
            , ListNode handled_1_root
            , String postfix
            ) {
    	
    	if(isDebugLevel1()) dbgInfoLvl1("");
    	if(isDebugLevel1()) dbgInfoLvl1("");

        if(isDebugLevel4()) dbgListShortLvl0(handled_1_root,  "handled_1_root::" + postfix);
        if(isDebugLevel4()) dbgListShortLvl0(handled_0_root,  "handled_0_root::" + postfix);
    	
        if(isDebugLevel1()) dbgListShortLvl1(handled_1_root,  "handled_1_root::" + postfix);
        if(isDebugLevel1()) dbgListShortLvl1(handled_0_root,  "handled_0_root::" + postfix);
    	
    	if(isDebugLevel0()) dbgList(handled_0_root, "handled_0_root-" + postfix);
        if(isDebugLevel0()) dbgList(handled_1_root, "handled_1_root-" + postfix);
    	if(isDebugLevel0()) dbgList(l_created_root_current[0],  "l_created_root_current[0]-" + postfix);
        if(isDebugLevel0()) dbgList(l_created_root_current[1],  "l_created_root_current[1]-" + postfix);                
    	
    }
    
    
}
