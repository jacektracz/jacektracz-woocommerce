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

class JacekTraczLetCodeMergeSortedKListsVersion3Solution {
    
    private boolean debug_mode_lvl3 = false;
    private boolean debug_mode_lvl0 = true;
    private boolean debug_mode_lvl1 = false;
    
    
    private boolean HANDLE_TAILS = true;
    
    public void setDebugModeLvl3(boolean dbg) {
    	debug_mode_lvl3 = dbg;
    }
    
    public void setDebugModeLvl0(boolean dbg) {
    	debug_mode_lvl0 = dbg;
    }
    
    public void setDebugModeLvl1(boolean dbg) {
    	debug_mode_lvl1 = dbg;
    }
    
    public ListNode mergeKLists( ListNode[] lists ) {
    	
    	String tt = "";
    	String sFun = "> mergeKLists::"; 
    	if(debug_mode_lvl3) dbgInfoLvl3(sFun  + "start :");
    	
    	if(debug_mode_lvl3) {
	    	for(int ii =0;ii< lists.length; ii ++) {
	    		if(debug_mode_lvl3) dbgList(lists[ii], sFun + "in_lis_on_idx:" + ii);		
	    	}
    	}
    	ListNode out_list = mergeKListsInternal(tt,lists);
        if(debug_mode_lvl3) dbgList(out_list, sFun + "out_list::end");
        if(debug_mode_lvl3) dbgInfoLvl3(sFun  + "end :");
        
        return out_list;
    }
    
    public ListNode mergeKListsInternal(String tt, ListNode[] lists) {
    	
        String sFunR = tt + " -> mergeKListsInternal::";
        String lv = "[LVL-0]";
        if(debug_mode_lvl3) dbgInfoLvl3(sFunR  + "start :");
        
        ListNode lout = mergeArrayOfKlistsl(tt, lists);
        
        if(debug_mode_lvl3) dbgInfoLvl3(sFunR  + "end :");
        
        return lout;
    }
    
    public ListNode mergeArrayOfKlistsl(String tt, ListNode[] lists) {
        String sFunR = tt + " -> mergeArrayOfKlistsl::";
        String lv = "[LVL-A]";
        if(debug_mode_lvl3) dbgInfoLvl3(sFunR  + "start :");
    	
    	ListNode[] dividedList = lists;    	
    	
    	while (true) {
    		int[] outListLength = new int[1];
    		outListLength[1] = 0;
    		dividedList = getDividedMergedArray( tt, lists, outListLength);
    		if(outListLength [0] <=1 ) {
    			break;
    		}
    	}
    	if(debug_mode_lvl3) dbgInfoLvl3(sFunR  + "end :");
    	return dividedList[0];
    }    
    
    public ListNode[] getDividedMergedArray(String tt, ListNode[] lists,int[] outListLength) {
    	
        String sFunR = tt + " -> getDividedMergedArray::";
        String lv = "[LVL-0]";
        if(debug_mode_lvl3) dbgInfoLvl3(sFunR  + "start :");
        if(debug_mode_lvl3) dbgHeaderLV0(sFunR  + "start :");
        
        if(debug_mode_lvl1) dbgListsShortLvl1(lists, sFunR);
        if(debug_mode_lvl0) dbgListsShortLvl0(lists, sFunR);
        
        int ii_merged_lists = 0;
        
        ListNode [] l_created_root_current = new ListNode[2];
        ListNode handled_0_root = null;
        
        ListNode[] outList = new ListNode[lists.length];
        int ii_out = 0;
        
        for ( ListNode handled_1_root : lists ){
        	
        	outListLength[0]++;
        	
        	handled_0_root = lists[ ii_merged_lists ];        	        	
        	
        	if(ii_merged_lists == lists.length) {
        		outList[ii_out] = handled_0_root;     
        		break;
        	}
        	
        	handled_1_root = lists[ ii_merged_lists + 1 ];
        	
        	logData( 
        			l_created_root_current
                    ,  handled_0_root
                    ,  handled_1_root
                    , sFunR + lv + "before-merge-two-lists" + "[roots:" + ii_merged_lists + "]");
            
            mergeTwoSortedKLists(
            		l_created_root_current
            		, handled_0_root
            		, handled_1_root
            		, sFunR + "[roots:" + ii_merged_lists + "]");
            
        	logData( 
        			l_created_root_current
                    ,  handled_0_root
                    ,  handled_1_root
                    , sFunR + lv + "after-merge-two-lists" + "[roots:" + ii_merged_lists + "]");
            
            outList[ ii_out ] = l_created_root_current[0];
            ii_out ++;
            
            ii_merged_lists++;      
            
        }
        
        if(debug_mode_lvl3) dbgList(handled_0_root, sFunR+ "handled_out_root::end");
        if(debug_mode_lvl3) dbgHeaderLV0(sFunR  + "end");
        if(debug_mode_lvl3) dbgInfoLvl3(sFunR  + "end :");
        
        return outList;
    }

    private void mergeTwoSortedKLists(
        ListNode[] l_out_created_root_current
        , ListNode l_handled_0_root
        , ListNode l_handled_1_root
        , String tt){
        
        
        String sFunMN =  tt + "-> mergeTwoSortedKLists::";
        String lv = "[LVL-2]";
        
        if(debug_mode_lvl3) dbgHeaderLV1(sFunMN + lv +  "[nodes:" + "start" + "]" + "s-start :");
        
        ListNode l_handled_0_current = l_handled_0_root;
        ListNode l_handled_1_current =   l_handled_1_root;      
        
        
        ListNode[] l_out_handled_0_root_current = new ListNode[2];
        l_out_handled_0_root_current[0] = l_handled_0_root;
        
        
        ListNode[] l_out_handled_1_root_current = new ListNode[2];
        l_out_handled_1_root_current[0] = l_handled_1_root;
        
        int ii_merged_nodes = 0;
        while( true )                
        {
        	
        	if(debug_mode_lvl1) dbgInfoLvl1("");        	
        	
        	if(debug_mode_lvl0) dbgInfoLvl0(sFunMN + lv +  "[nodes_iteration:" + ii_merged_nodes + "]");
        	
        	logData( 
        			l_out_created_root_current
                    ,  l_handled_0_current
                    ,  l_handled_1_current
                    ,  sFunMN + lv +  "[nodes:" + ii_merged_nodes + "]-before-merge-nodes");
        	        	
        	mergeTwoNodes( 
        		l_handled_0_current
                , l_handled_1_current
                , l_out_created_root_current
                , l_out_handled_0_root_current
                , l_out_handled_1_root_current
                , sFunMN +  "[ii_merged_nodes:" + ii_merged_nodes + "]");
        	
        	logData( 
        			l_out_created_root_current
                    ,  l_handled_0_current
                    ,  l_handled_1_current
                    ,  sFunMN + lv +  "[nodes:" + ii_merged_nodes + "]-after-merge-nodes");
        	
        	l_handled_0_current = l_out_handled_0_root_current[1];
        	l_handled_1_current = l_out_handled_1_root_current[1];            
            
            if( l_handled_0_current == null   && HANDLE_TAILS ){
            	if(debug_mode_lvl3) dbgInfoLvl3(sFunMN + lv +  "[nodes:" + ii_merged_nodes + "]" + "l_handled_0_current-is-empty");            	
            	if(l_out_created_root_current[1] != null ) {
            		l_out_created_root_current[1].next = l_handled_1_current;
            	}            	
                break;
            }
            
            if( l_handled_1_current == null   && HANDLE_TAILS){
            	if(debug_mode_lvl3) dbgInfoLvl3(sFunMN + lv +  "[nodes:" + ii_merged_nodes + "]" + "l_handled_1_current-is-empty");            	
            	if( l_out_created_root_current[1]!= null ) {
            		l_out_created_root_current[1].next = l_handled_0_current;
            	}            	
                break;                
            }
        	
            if( l_handled_0_current == null  && l_handled_1_current == null ){
            	if(debug_mode_lvl3) dbgInfoLvl3(sFunMN + lv +  "[nodes:" + ii_merged_nodes + "]" + "-ater=merge-break-on-empty-");            	
                break;
            }                                   
            ii_merged_nodes ++;                        
        }
        
        if(debug_mode_lvl3) dbgHeaderLV1(sFunMN + lv +  "end :");
    }    

    private void mergeTwoNodes(
        ListNode l_in_handled_0_current        
        , ListNode l_in_handled_1_current
        , ListNode[] l_out_created_root_current
        , ListNode[] l_out_handled_0_root_current
        , ListNode[] l_out_handled_1_root_current
        , String tt){
        
        String sFun2N =  tt + " -> * mergeTwoNode-LV-4s::";
        String lv = "[LVL-4]";
        if(debug_mode_lvl3) dbgHeaderLV2(sFun2N  + lv + "-2N-start :");
                
        if(debug_mode_lvl3) dbgInfoLvl3(sFun2N  + lv + "-initialize-out-current-pointers-start");        
        l_out_handled_0_root_current[1] = l_in_handled_0_current;
        l_out_handled_1_root_current[1] = l_in_handled_1_current;
        if(debug_mode_lvl3) dbgInfoLvl3(sFun2N  + lv + "-initialize-out-current-pointers-end");
        
                
        
        ListNode l_created_left = null;                        
        
        int cases_check = 0;
        if(cases_check == 0) {
        	
        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-1-check-start") ;
        	
	        if(l_in_handled_0_current == null && l_in_handled_1_current == null){
	            if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + "case-1-exec-start") ;
	            if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + "no-nodes-to-handle") ;
	            l_created_left = null;
	            cases_check = 1;
	            if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + "case 1-exec-end") ;
	        }
	        
	        if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-1-check-end") ;
	        
        }
        
        if(cases_check == 0) {
        	
        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-2-check-start") ;
        	
	        if(l_in_handled_0_current == null && l_in_handled_1_current != null){
	            if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-2-exec-start") ;
	            if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " item-from-list-1-was-taken") ;
	            l_out_handled_1_root_current[1] = l_in_handled_1_current.next;
	            l_created_left = new ListNode(l_in_handled_1_current.val);
	            l_created_left.next = null;
	            if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-2-exec-end") ;
	            cases_check = 2;
	        }
	        
	        if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-2-check-end") ;
	        
        }
        
        if(cases_check == 0) {
        	
        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-3-check-start") ;
        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current == null){
	        	
	            if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-3-exec-start") ;
	            if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " item-from-list-0-was-taken") ;
	            if(debug_mode_lvl0) dbgInfoLvl0(sFun2N + lv + " item-from-list-0-was-taken") ;
	            l_out_handled_0_root_current[1] = l_in_handled_0_current.next;
	            //l_created_left = new ListNode(l_in_handled_0_current.val);   
	            //l_created_left.next = null;
	            
	            l_created_left = l_in_handled_0_current;
	            		
	            cases_check = 3;
	            if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-3-exec-end") ;
	            
	        }
	        
	        if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-3-check-end") ;
	        
        }
        
        if(cases_check == 0) {        	
        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-4-check-start") ;        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current != null){	        	
	        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-4-check-vals-start");	        	
	            if( l_in_handled_0_current.val < l_in_handled_1_current.val ){
	            	
	            	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-4-exec-start") ;
	            	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " item-from-list-0-was-taken");	            	
	            	if(debug_mode_lvl0) dbgInfoLvl0(sFun2N + lv + " item-from-list-0-was-taken");	            	
	            	l_out_handled_0_root_current[1] = l_in_handled_0_current.next;	            	
	                //l_created_left = new ListNode(l_in_handled_0_current.val);	                
	            	l_created_left = l_in_handled_0_current;	            	
	                cases_check = 4;
	                if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-4-exec-end") ;	                
	            }	            
	            if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-4-check-vals-end") ;
	        }	        
	        if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-4-check-end") ;	        
        }
        
        if(cases_check == 0) {        	
        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-7-check-start") ;        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current != null){	        	
	        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-7-check-vals-start") ;	        	
	            if(l_in_handled_0_current.val == l_in_handled_1_current.val){	            
	            	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-7-exec-start") ;
	            	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " item-from-list-1-was-taken") ;
	            	if(debug_mode_lvl0) dbgInfoLvl0(sFun2N + lv + " item-from-list-1-was-taken") ;
	            	l_out_handled_1_root_current[1] = l_in_handled_1_current.next;	                
	                //l_created_left = new ListNode(l_in_handled_0_current.val);	            	
	            	l_created_left = l_in_handled_1_current;	            	
	                cases_check = 7;
	                if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-7-exec-end") ;
	                
	            }	            
	            if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-7-check-vals-end") ;	            
	        }	        
	        if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-7-check-end") ;
	        
        }
        
        if(cases_check == 0) {
        	
        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-5-check-start") ;        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current != null){	        	
	        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-5-check-vals-start") ;	        	
	            if(l_in_handled_0_current.val == l_in_handled_1_current.val){	            	
	            	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-5-exec-start") ;
	            	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " item-from-list-0-was-taken") ;	    
	            	if(debug_mode_lvl0) dbgInfoLvl0(sFun2N + lv + " item-from-list-0-was-taken") ;
	            	
	            	l_out_handled_0_root_current[1] = l_in_handled_0_current.next;	     
	            	
	                //l_created_left = new ListNode(l_in_handled_0_current.val);	            	
	            	l_created_left = l_in_handled_0_current;	            	
	                cases_check = 5;
	                if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-5-exec-end") ;	                
	            }	            
	            if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-5-check-vals-end") ;	            
	        }	        
	        if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-5-check-end") ;	        
        }
        
        if(cases_check == 0) {
        	
        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-6-check-start") ;
        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current != null){
	        	
	        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-6-check-vals-start") ;
	        	
	            if(l_in_handled_0_current.val > l_in_handled_1_current.val){     
	            	
	                if(debug_mode_lvl3) dbgInfoLvl3(tt + " case-6-start") ;
	                if(debug_mode_lvl0) dbgInfoLvl0(sFun2N + lv + " item-from-list-1-was-taken") ;
	                
	                l_out_handled_1_root_current[1] = l_in_handled_1_current.next;
	                //l_created_left = new ListNode(l_in_handled_1_current.val);
	                
	                l_created_left = l_in_handled_1_current;
	                
	                cases_check = 6;
	                if(debug_mode_lvl3) dbgInfoLvl3(tt + " case-6-end") ;	                
	            }	            
	            if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-6-check-vals-end") ;	            
	        }	        
	        if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " case-6-check-end") ;
	        
        }
        
        if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-cases-end-" + cases_check);
        
        if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-cases-end-" + cases_check);
        
        if(debug_mode_lvl3) dbgInfoLvl3("") ;
        
        int resolved_items = 0;
        if( resolved_items == 0 ) {        	
        	
        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-4-start");
        	
	        if( l_created_left == null ){
	        	
	        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-4-exec-start");
	        	
	        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + "no-items-to-handle-work-finished-current-out-pinter-to-null:");	        		            
	            l_out_created_root_current[1] = null;
	            resolved_items = 4;
	            if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-4-exec-end");
	            
	        }else {
	        	
	        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-4-no-check");
	        	
	        }
	        
	        if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-4-end");
	        
        }
        
        if( resolved_items == 0 ) {
        	
        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-1-start");
        	
	        if( l_out_created_root_current[0] == null ){
	        	
	        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-1-exec-start");
	        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + "fill-root-first-time-set-current-as-root");
	        	l_created_left.next = null;
	            l_out_created_root_current[0] = l_created_left;
	            l_out_created_root_current[1] = l_created_left;
	            resolved_items = 1;
	            if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-1-exec-end");
	            
	        }else {
	        	
	        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-1-no-check");
	        	
	        }
	        
	        if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-1-end");
	        
        }
        
        if( resolved_items == 0 ) {
        	
        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-2-start");
        	
	        if( l_out_created_root_current[0] != null && l_out_created_root_current[1] == null){
	        	
	        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-2-exec-start :");
	        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " should-not-exists:ERROR-OCCURED");
	            l_out_created_root_current[1].next = l_created_left;
	            l_out_created_root_current[1] = l_created_left;
	            resolved_items = 2;
	            if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-2-exec-end :");
	            
	        }else {
	        	
	        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-2-no-check :");
	        	
	        }
	        
	        if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-2-end");
        }
        
        if( resolved_items == 0 ) {
        	
        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-3-start");
        	
	        if( l_out_created_root_current[0] != null && l_out_created_root_current[1] != null){
	        	
	        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-3-exec-start :");
	        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-2-move-current-to-right :");
	            l_out_created_root_current[1].next = l_created_left;
	            l_out_created_root_current[1] = l_created_left;
	            resolved_items = 3;
	            if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-3-exec-end");
	            
	        }else {
	        	
	        	if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-3-no-check");
	        	
	        }
	        
	        if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-resolve-3-end");
	        
        }
                
        if(debug_mode_lvl3) dbgInfoLvl3(sFun2N + lv + " nodes-cases-resolves-end:" + "[cases_check:" + cases_check + "]" + "[resolved_items:" + resolved_items + "]");
        
        if(debug_mode_lvl3) dbgHeaderLV2(sFun2N + lv + "-2N-end :");
        
        return ;
        
    }
    
    private void dbgNode ( 
            ListNode p_nl
            , String tt){
    	
    	String sFun =  tt + " -> dbgNode::";
    	
		if(debug_mode_lvl3) dbgInfoLvl3(" ");
		if(debug_mode_lvl3) dbgInfoLvl3(">>");
        if(debug_mode_lvl3) dbgInfoLvl3(sFun + " -> dbgNode-start :");
        if(p_nl != null) {
        	if(debug_mode_lvl3) dbgInfoLvl3(sFun + " value :" + p_nl.val) ;
        }else {
        	if(debug_mode_lvl3) dbgInfoLvl3(sFun + " value :" + "NULL") ;
        }
        if(p_nl != null && p_nl.next != null) {
        	if(debug_mode_lvl3) dbgInfoLvl3(sFun + " -> :" + p_nl.next.val) ;
        }
        
        if(debug_mode_lvl3) dbgInfoLvl3(sFun + " dbgNode-end :");
        if(debug_mode_lvl3) dbgInfoLvl3("");
        if(debug_mode_lvl3) dbgInfoLvl3("");
        
    }

    
    private int dbgList ( 
            ListNode p_nl
            , String tt){
    	if(!debug_mode_lvl3) {
    		return 0;
    	}
    	int ii = dbgListTxt(p_nl,tt);
    	dbgListShortLvl1(p_nl,tt);
    	checkList(p_nl,tt);
    	return ii;
    }
    
    
    private int dbgListTxt ( 
        ListNode p_nl
        , String tt){
    	if(!debug_mode_lvl3) {
    		return 0;
    	}
        
    	String sFun =  tt + " -> dbgList::";
        if(debug_mode_lvl3) dbgInfoLvl3(" ");
        if(debug_mode_lvl3) dbgInfoLvl3(" ");
        if(debug_mode_lvl3) dbgInfoLvl3("<<<<<");
        if(debug_mode_lvl3) dbgInfoLvl3(sFun + "-start :");
        
        ListNode nl = p_nl;
        int ii =0;
        while(true){
        	
            if(nl == null){
                if(debug_mode_lvl3) dbgInfoLvl3(sFun + " node is null:") ;
                break;                   
            }
            if(debug_mode_lvl3) dbgInfoLvl3(sFun + " value: " + nl.val) ;
            nl = nl.next;
            ii++;
        }
        
        if(debug_mode_lvl3) dbgInfoLvl3(sFun + "end :");
        if(debug_mode_lvl3) dbgInfoLvl3(">>>>");
        if(debug_mode_lvl3) dbgInfoLvl3(" ");
        if(debug_mode_lvl3) dbgInfoLvl3(" ");
        return ii;
    }
    
    private int dbgListsShortLvl0 ( 
            ListNode []p_nl
            , String tt){
    	
    	if(!debug_mode_lvl0) {
    		return 0;
    	}
    	
	    for (int ii = 0;ii<p_nl.length;ii++) {
	    	dbgListShortLvl0(p_nl[ii],tt);	
	    }
	    return 0;
    }
    
    private int dbgListsShortLvl1 ( 
            ListNode []p_nl
            , String tt){
    	
    	if(!debug_mode_lvl1) {
    		return 0;
    	}
    	
	    for (int ii = 0;ii<p_nl.length;ii++) {
	    	dbgListShortLvl1(p_nl[ii],tt);	
	    }
	    return 0;
    }
    
    private int dbgListShortLvl0 ( 
            ListNode p_nl
            , String tt){
    	
    	if(!debug_mode_lvl0) {
    		return 0;
    	}
    	
	    return dbgListShorInternal(p_nl,tt);	    	
    }	
    
    private int dbgListShortLvl1 ( 
            ListNode p_nl
            , String tt){
    	
    	if(!debug_mode_lvl1) {
    		return 0;
    	}
    	
	    return dbgListShorInternal(p_nl,tt);	    	
    }	
    
    private int dbgListShorInternal ( 
            ListNode p_nl
            , String tt){
    	            
        	String sFun =  tt + " -> dbgListShort::";
            if(debug_mode_lvl3) dbgInfoLvl3(" ");
            if(debug_mode_lvl3) dbgInfoLvl3(" ");
            if(debug_mode_lvl3) dbgInfoLvl3("<<<<<");
            if(debug_mode_lvl3) dbgInfoLvl3(sFun + "-start :");
            
            String sList = "";
            int ii = 0;
            if(debug_mode_lvl1||debug_mode_lvl0) {
	            ListNode nl = p_nl;
	            
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
            if(debug_mode_lvl0) dbgInfoLvl0(sFun + " " + sList);
            if(debug_mode_lvl1) dbgInfoLvl1(sFun + " " + sList);
            
            if(debug_mode_lvl3) dbgInfoLvl3(sFun + " " + sList);
            if(debug_mode_lvl3) dbgInfoLvl3(sFun + "end :");
            if(debug_mode_lvl3) dbgInfoLvl3(">>>>");
            if(debug_mode_lvl3) dbgInfoLvl3(" ");
            if(debug_mode_lvl3) dbgInfoLvl3(" ");
            return ii;
    }

    
    private void dbgHeaderLV0 (String tt) {
    	if(!debug_mode_lvl3) {
    		return ;
    	}
    	
    	dbgN5();
    	if(debug_mode_lvl3) dbgInfoLvl3("");
    	if(debug_mode_lvl3) dbgInfoLvl3("");
        if(debug_mode_lvl3) dbgInfoLvl3("================================================================");
        if(debug_mode_lvl3) dbgInfoLvl3("=");
        if(debug_mode_lvl3) dbgInfoLvl3("=");
        if(debug_mode_lvl3) dbgInfoLvl3("=" + tt);
        if(debug_mode_lvl3) dbgInfoLvl3("=");
        if(debug_mode_lvl3) dbgInfoLvl3("=");
        if(debug_mode_lvl3) dbgInfoLvl3("================================================================");
        if(debug_mode_lvl3) dbgInfoLvl3("");
        if(debug_mode_lvl3) dbgInfoLvl3("");
        dbgN5();
    	
    }
    
    private void dbgHeaderLV1 (String tt) {
    	if(!debug_mode_lvl3) {
    		return ;
    	}
    	
    	dbgN5();
    	if(debug_mode_lvl3) dbgInfoLvl3("");
        if(debug_mode_lvl3) dbgInfoLvl3("****************************************************************");
        if(debug_mode_lvl3) dbgInfoLvl3("*");
        if(debug_mode_lvl3) dbgInfoLvl3("**" + tt);
        if(debug_mode_lvl3) dbgInfoLvl3("*");        
        if(debug_mode_lvl3) dbgInfoLvl3("****************************************************************");
        if(debug_mode_lvl3) dbgInfoLvl3("");
        dbgN5();
    	
    }
    
    private void dbgHeaderLV2 (String tt) {
    	if(!debug_mode_lvl3) {
    		return ;
    	}
    	
    	dbgN5();
    	if(debug_mode_lvl3) dbgInfoLvl3("");
        if(debug_mode_lvl3) dbgInfoLvl3("--------------------------------------------------------------");                
        if(debug_mode_lvl3) dbgInfoLvl3("-" + tt);               
        if(debug_mode_lvl3) dbgInfoLvl3("---------------------------------------------------------------");
        if(debug_mode_lvl3) dbgInfoLvl3("");
        dbgN5();
    	
    }
    
    private void dbgN5 () {
    	if(!debug_mode_lvl3) {
    		return ;
    	}
    	
    	if(debug_mode_lvl3) dbgInfoLvl3("");
    	if(debug_mode_lvl3) dbgInfoLvl3("");
    	if(debug_mode_lvl3) dbgInfoLvl3("");
    	if(debug_mode_lvl3) dbgInfoLvl3("");
    	if(debug_mode_lvl3) dbgInfoLvl3("");
    }
    
    private  String checkList ( 
            ListNode p_nl
            , String tt
            ){
    	if(!debug_mode_lvl3) {
    		return "";
    	}
            
        	String sFun =  tt + " -> checkList::";
            if(debug_mode_lvl3) dbgInfoLvl3("<<<");        	
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
            	dbgInfoLvl3(sFun + "ERROR_IN_LIST:" + sOut);
            }

            if(debug_mode_lvl3) dbgInfoLvl3(sFun + "end :");
            if(debug_mode_lvl3) dbgInfoLvl3(">>>>");
            if(debug_mode_lvl3) dbgInfoLvl3(" ");
            if(debug_mode_lvl3) dbgInfoLvl3(" ");
            return  sOut;
    }
    
    
    private void dbgInfoLvl3 ( String tt ){
    	if(!debug_mode_lvl3) {
    		return ;
    	}
    	    	
        dbgInfoSubmitted(tt);
        
    }
    
    private void dbgInfoLvl0 ( String tt ){
    	
    	
    	if(!debug_mode_lvl0) {
    		return ;
    	}
    	    	
        dbgInfoSubmitted(tt);
        
    }
    
    private void dbgInfoLvl1 ( String tt ){
    	
    	if(!debug_mode_lvl1) {
    		return ;
    	}
    	    	
        dbgInfoSubmitted(tt);
        
    }
    
    private void dbgInfoSubmitted ( String tt ){    	
    	
    	String needle = "";
    	//needle ="LV-0";
    	
    	if(needle.isEmpty()) {
    		System.out.println( tt );
    	}
    	
    	if(!needle.isEmpty()) {
    		if(tt.indexOf(needle) >= 0) {
    			System.out.println( tt );
    		}
    	}
    	
    }
    
    public void logData(
    		
    		ListNode[] l_created_root_current
            , ListNode handled_0_root
            , ListNode handled_1_root
            , String postfix
            ) {
    	
    	if(debug_mode_lvl1) dbgInfoLvl1("");
    	if(debug_mode_lvl1) dbgInfoLvl1("");

        if(debug_mode_lvl0) dbgListShortLvl0(handled_1_root,  "handled_1_root::" + postfix);
        if(debug_mode_lvl0) dbgListShortLvl0(handled_0_root,  "handled_0_root::" + postfix);
    	
        if(debug_mode_lvl1) dbgListShortLvl1(handled_1_root,  "handled_1_root::" + postfix);
        if(debug_mode_lvl1) dbgListShortLvl1(handled_0_root,  "handled_0_root::" + postfix);
    	
    	if(debug_mode_lvl3) dbgList(handled_0_root, "handled_0_root-" + postfix);
        if(debug_mode_lvl3) dbgList(handled_1_root, "handled_1_root-" + postfix);
    	if(debug_mode_lvl3) dbgList(l_created_root_current[0],  "l_created_root_current[0]-" + postfix);
        if(debug_mode_lvl3) dbgList(l_created_root_current[1],  "l_created_root_current[1]-" + postfix);                
    	
    }
    
    
}
