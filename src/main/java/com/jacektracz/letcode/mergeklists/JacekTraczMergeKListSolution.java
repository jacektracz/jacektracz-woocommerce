package com.jacektracz.letcode.mergeklists;

/**
 * 
 * 
 * Darek 792 636 939
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
class JacekTraczMergeKListSolution {
    
    public boolean DBG_MODE = true;
    
    public ListNode mergeKLists( ListNode[] lists ) {
    	
    	String tt = "";
    	String sFun = "> mergeKLists::"; 
    	if(DBG_MODE) dbgInfo(sFun  + "start :");
    	
    	if(DBG_MODE) {
	    	for(int ii =0;ii< lists.length; ii ++) {
	    		if(DBG_MODE) dbgList(lists[ii], sFun + "in_lis_on_idx:" + ii);		
	    	}
    	}
    	ListNode out_list = mergeKListsInternal(tt,lists);
        if(DBG_MODE) dbgList(out_list, sFun + "out_list::end");
        if(DBG_MODE) dbgInfo(sFun  + "end :");
        
        return out_list;
    }
    
    public ListNode mergeKListsInternal(String tt, ListNode[] lists) {
    	
        String sFunR = tt + " -> mergeKListsInternal::";
        String lv = "[LVL-0]";
        if(DBG_MODE) dbgInfo(sFunR  + "start :");
        if(DBG_MODE) dbgHeaderLV0(sFunR  + "start :");
        int ii = 0;        
        ListNode [] l_created_root_current = new ListNode[2];
        ListNode handled_0_root = null;
        
        for (ListNode handled_1_root : lists){
        	
        	if(DBG_MODE) dbgInfo(sFunR   + "-" + ii + "merge-list-start");	
        	
        	if(DBG_MODE) dbgList(handled_0_root, sFunR + lv + "[roots:" + ii + "]" + "handled_0_root-before-merge-roots");
            if(DBG_MODE) dbgList(handled_1_root, sFunR + lv + "[roots:" + ii + "]" + "handled_1_root-before-merge-roots");
        	if(DBG_MODE) dbgList(l_created_root_current[0], sFunR + lv + "[roots:" + ii + "]" + "l_created_root_current[0]-before-merge-roots");
            if(DBG_MODE) dbgList(l_created_root_current[1], sFunR + lv + "[roots:" + ii + "]" + "l_created_root_current[1]-before-merge-roots");
            
            mergeTwoRoots(
            		l_created_root_current
            		, handled_0_root
            		, handled_1_root
            		, sFunR + "[roots:" + ii + "]");

        	if(DBG_MODE) dbgList(l_created_root_current[0], sFunR + lv + "[roots:" + ii + "]" + "l_created_root_current[0]-after-merge-roots");
        	if(DBG_MODE) dbgList(l_created_root_current[1], sFunR + lv + "[roots:" + ii + "]" + "l_created_root_current[1]-after-merge-roots");
            
            handled_0_root = l_created_root_current[0];
            
            l_created_root_current[0] = null;
            l_created_root_current[1] = null;
            
            if(DBG_MODE) dbgList(handled_1_root, sFunR + lv + "[roots:" + ii + "]" + "handled_1_root::after-merge-after-merge-roots");
            if(DBG_MODE) dbgList(handled_0_root, sFunR + lv + "[roots:" + ii + "]" + "handled_0_root::after-merge-after-merge-roots");
            
            if(DBG_MODE) dbgInfo(sFunR   + "[" + ii + "]" +  "merge-list-end :");
            
            ii++;
            
        }
        
        if(DBG_MODE) dbgList(handled_0_root, sFunR+ "handled_out_root::end");
        if(DBG_MODE) dbgHeaderLV0(sFunR  + "end");
        if(DBG_MODE) dbgInfo(sFunR  + "end :");
        
        return handled_0_root;
    }

    private void mergeTwoRoots(
        ListNode[] l_out_created_root_current
        , ListNode l_handled_0_root
        , ListNode l_handled_1_root
        , String tt){
        
        
        String sFunMN =  tt + "-> mergeTwoRoots::";
        String lv = "[LVL-2]";
        
        if(DBG_MODE) dbgHeaderLV1(sFunMN + lv +  "[nodes:" + "start" + "]" + "s-start :");
        
        ListNode l_handled_0_current = l_handled_0_root;
        ListNode l_handled_1_current =   l_handled_1_root;      
        
        if(DBG_MODE) dbgList(l_handled_0_current, sFunMN + lv +  "[nodes:" + "start" + "]" + "l_handled_0_current-before");        
        if(DBG_MODE) dbgList(l_handled_1_current, sFunMN + lv +  "[nodes:" + "start" + "]" + "l_handled_1_current-before");

        if(DBG_MODE) dbgList(l_out_created_root_current[0], sFunMN + lv +  "[nodes:" + "start" + "]" + "l_out_created_root_current[0]-before");        
        if(DBG_MODE) dbgList(l_out_created_root_current[1], sFunMN + lv +  "[nodes:" + "start" + "]" + "l_out_created_root_current[1]-before");
        
        ListNode[] l_out_handled_0_root_current = new ListNode[2];
        l_out_handled_0_root_current[0] = l_handled_0_root;
        
        
        ListNode[] l_out_handled_1_root_current = new ListNode[2];
        l_out_handled_1_root_current[0] = l_handled_1_root;
        
        int ii = 0;
        while( true )                
        {
        	if(DBG_MODE) dbgInfo(sFunMN + lv +  "[nodes:" + ii + "]" + "=>");
        	if(DBG_MODE) dbgInfo(sFunMN + lv +  "[nodes:" + ii + "]" + "-start-merge-nodes-");
                    
            if(DBG_MODE) dbgList(l_handled_0_current, sFunMN + lv +  "[nodes:" + ii + "]"  + "l_handled_0_current-before-merge-nodes" );
            if(DBG_MODE) dbgList(l_handled_1_current, sFunMN + lv +  "[nodes:" + ii + "]"  + "l_handled_1_current-before-merge-nodes" );
            
        	if(DBG_MODE) dbgList(l_out_created_root_current[0], sFunMN + lv +  "[nodes:" + ii + "]"  + "l_out_created_root_current[0]-before-merge-nodes" );        	
        	if(DBG_MODE) dbgNode(l_out_created_root_current[1], sFunMN + lv + "[nodes:" + ii + "]"  + "l_out_created_root_current[1]-before-merge-node" );

        	if(DBG_MODE) dbgList(l_out_handled_0_root_current[0], sFunMN + lv +  "[nodes:" + ii + "]"  + "l_out_handled_0_root_current[0]-before-merge-nodes" );        	
        	if(DBG_MODE) dbgNode(l_out_handled_0_root_current[1], sFunMN + lv +  "[nodes:" + ii + "]" + "l_out_handled_0_root_current[1]-before-merge-node");
        	
        	if(DBG_MODE) dbgList(l_out_handled_1_root_current[0], sFunMN + lv +  "[nodes:" + ii + "]" + "l_out_handled_1_root_current[0]-before-merge-nodes" );        	
        	if(DBG_MODE) dbgNode(l_out_handled_1_root_current[1], sFunMN + lv +  "[nodes:" + ii + "]" + "l_out_handled_1_root_current[1]-before-merge-node" );
        	
        	mergeTwoNodes( 
        		l_handled_0_current
                , l_handled_1_current
                , l_out_created_root_current
                , l_out_handled_0_root_current
                , l_out_handled_1_root_current
                , sFunMN +  "[nodes:" + ii + "]");
        	
        	l_handled_0_current = l_out_handled_0_root_current[1];
        	l_handled_1_current = l_out_handled_1_root_current[1];            
            
        	if(DBG_MODE) dbgList(l_handled_0_root, sFunMN + lv +  "[nodes:" + ii + "]" + "l_handled_0_root-after-merge-nodes" );
        	if(DBG_MODE) dbgNode(l_handled_0_current, sFunMN + lv +  "[nodes:" + ii + "]" + "l_handled_0_current-after-merge-nodes" );
        	
        	if(DBG_MODE) dbgList(l_handled_1_root, sFunMN + lv +  "[nodes:" + ii + "]" + "l_handled_1_root-after-merge-nodes" );            
        	if(DBG_MODE) dbgNode(l_handled_1_current, sFunMN + lv +  "[nodes:" + ii + "]" + "l_handled_1_current-after-merge-nodes" );
        	
        	if(DBG_MODE) dbgList(l_out_created_root_current[0], sFunMN + lv +  "[nodes:" + ii + "]" + "l_out_created_root_current[0]-after-merge-nodes" );        	
        	if(DBG_MODE) dbgNode(l_out_created_root_current[1], sFunMN + lv +  "[nodes:" + ii + "]" + "l_out_created_root_current[1]-after-merge-nodes" );
        	
        	
            
            if( l_handled_0_current == null  && l_handled_1_current == null )
            {
            	if(DBG_MODE) dbgInfo(sFunMN + lv +  "[nodes:" + ii + "]" + "-ater=merge-break-on-empty-");
            	if(DBG_MODE) dbgInfo(sFunMN + lv +  "[nodes:" + ii + "]" + "<==|");
                break;
            }
            
            if(DBG_MODE) dbgInfo(sFunMN + lv +  "[nodes:" + ii + "]" + "-move-to-merge-next-node-");
            
            
            ii ++;
            if(DBG_MODE) dbgInfo(sFunMN + lv +  "[nodes:" + ii + "]" + "<=<");
            
        }        
        
        if(DBG_MODE) dbgList(l_out_created_root_current[0], sFunMN + lv +  "[nodes:" + ii + "]" + "l_out_created_root_current-list-after-merge-list");
                
        if(DBG_MODE) dbgHeaderLV1(sFunMN + lv +  "end :");
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
        if(DBG_MODE) dbgHeaderLV2(sFun2N  + lv + "-2N-start :");
        
        if(DBG_MODE) dbgNode(l_out_handled_0_root_current[1], sFun2N  + lv + "l_out_handled_0_root_current[1]-before-init");
        if(DBG_MODE) dbgNode(l_out_handled_1_root_current[1], sFun2N  + lv + "l_out_handled_1_root_current[1]-before-init");
        
        if(DBG_MODE) dbgInfo(sFun2N  + lv + "-initialize-out-current-pointers-start");        
        l_out_handled_0_root_current[1] = l_in_handled_0_current;
        l_out_handled_1_root_current[1] = l_in_handled_1_current;
        if(DBG_MODE) dbgInfo(sFun2N  + lv + "-initialize-out-current-pointers-end");
        
        
        if(DBG_MODE) dbgNode(l_in_handled_0_current, sFun2N  + lv + "l_in_handled_0_current-before-resolve");
        if(DBG_MODE) dbgNode(l_in_handled_1_current, sFun2N  + lv + "l_in_handled_1_current-before-resolve");        
        
        if(DBG_MODE) dbgList(l_out_created_root_current[0], sFun2N  + lv + "l_out_created_root_current[0]-before-resolve");
        if(DBG_MODE) dbgNode(l_out_created_root_current[1], sFun2N  + lv + "l_out_created_root_current[1]-before-resolve");

        if(DBG_MODE) dbgList(l_out_handled_0_root_current[0], sFun2N  + lv + "l_out_handled_0_root_current[0]-before-resolve");
        if(DBG_MODE) dbgNode(l_out_handled_0_root_current[1], sFun2N  + lv + "l_out_handled_0_root_current[1]-before-resolve");

        if(DBG_MODE) dbgList(l_out_handled_1_root_current[0], sFun2N  + lv + "l_out_handled_1_root_current[0]-before-resolve");
        if(DBG_MODE) dbgNode(l_out_handled_1_root_current[1], sFun2N  + lv + "l_out_handled_1_root_current[1]-before-resolve");
        
        ListNode l_created_left = null;                        
        
        int cases_check = 0;
        if(cases_check == 0) {
        	
        	if(DBG_MODE) dbgInfo(sFun2N + lv + " case-1-check-start") ;
        	
	        if(l_in_handled_0_current == null && l_in_handled_1_current == null){
	            if(DBG_MODE) dbgInfo(sFun2N + lv + "case-1-exec-start") ;
	            if(DBG_MODE) dbgInfo(sFun2N + lv + "no-nodes-to-handle") ;
	            l_created_left = null;
	            cases_check = 1;
	            if(DBG_MODE) dbgInfo(sFun2N + lv + "case 1-exec-end") ;
	        }
	        
	        if(DBG_MODE) dbgInfo(sFun2N + lv + " case-1-check-end") ;
	        
        }
        
        if(cases_check == 0) {
        	
        	if(DBG_MODE) dbgInfo(sFun2N + lv + " case-2-check-start") ;
        	
	        if(l_in_handled_0_current == null && l_in_handled_1_current != null){
	            if(DBG_MODE) dbgInfo(sFun2N + lv + " case-2-exec-start") ;
	            if(DBG_MODE) dbgInfo(sFun2N + lv + " item-from-list-1-was-taken") ;
	            l_out_handled_1_root_current[1] = l_in_handled_1_current.next;
	            l_created_left = new ListNode(l_in_handled_1_current.val);
	            l_created_left.next = null;
	            if(DBG_MODE) dbgInfo(sFun2N + lv + " case-2-exec-end") ;
	            cases_check = 2;
	        }
	        
	        if(DBG_MODE) dbgInfo(sFun2N + lv + " case-2-check-end") ;
	        
        }
        
        if(cases_check == 0) {
        	
        	if(DBG_MODE) dbgInfo(sFun2N + lv + " case-3-check-start") ;
        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current == null){
	            if(DBG_MODE) dbgInfo(sFun2N + lv + " case-3-exec-start") ;
	            if(DBG_MODE) dbgInfo(sFun2N + lv + " item-from-list-0-was-taken") ;
	            l_out_handled_0_root_current[1] = l_in_handled_0_current.next;
	            l_created_left = new ListNode(l_in_handled_0_current.val);   
	            l_created_left.next = null;
	            cases_check = 3;
	            if(DBG_MODE) dbgInfo(sFun2N + lv + " case-3-exec-end") ;
	        }
	        
	        if(DBG_MODE) dbgInfo(sFun2N + lv + " case-3-check-end") ;
	        
        }
        
        if(cases_check == 0) {
        	
        	if(DBG_MODE) dbgInfo(sFun2N + lv + " case-4-check-start") ;
        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current != null){
	        	if(DBG_MODE) dbgInfo(sFun2N + lv + " case-4-check-vals") ;
	            if( l_in_handled_0_current.val < l_in_handled_1_current.val ){
	            	if(DBG_MODE) dbgInfo(sFun2N + lv + " case-4-exec-start") ;
	            	if(DBG_MODE) dbgInfo(sFun2N + lv + " item-from-list-0-was-taken") ;
	            	l_out_handled_0_root_current[1] = l_in_handled_0_current.next;            	                
	                l_created_left = new ListNode(l_in_handled_0_current.val);
	                cases_check = 4;
	                if(DBG_MODE) dbgInfo(sFun2N + lv + " case-4-exec-end") ;	                
	            }
	        }
	        
	        if(DBG_MODE) dbgInfo(sFun2N + lv + " case-4-check-end") ;
	        
        }
        
        if(cases_check == 0) {
        	
        	if(DBG_MODE) dbgInfo(sFun2N + lv + " case-5-check-start") ;
        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current != null){
	        	if(DBG_MODE) dbgInfo(sFun2N + lv + " case-5-check-vals") ;
	            if(l_in_handled_0_current.val == l_in_handled_1_current.val){
	            	if(DBG_MODE) dbgInfo(sFun2N + lv + " case-5-exec-start") ;
	            	if(DBG_MODE) dbgInfo(sFun2N + lv + " item-from-list-0-was-taken") ;	            	
	            	l_out_handled_0_root_current[1] = l_in_handled_0_current.next;	                
	                l_created_left = new ListNode(l_in_handled_0_current.val);
	                cases_check = 5;
	                if(DBG_MODE) dbgInfo(sFun2N + lv + " case-5-exec-end") ;
	                
	            }
	        }
	        
	        if(DBG_MODE) dbgInfo(sFun2N + lv + " case-5-check-end") ;
	        
        }
        
        if(cases_check == 0) {
        	
        	if(DBG_MODE) dbgInfo(sFun2N + lv + " case-6-check-start") ;
        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current != null){
	        	if(DBG_MODE) dbgInfo(sFun2N + lv + " case-6-check-vals") ;
	            if(l_in_handled_0_current.val > l_in_handled_1_current.val){            	
	                if(DBG_MODE) dbgInfo(tt + " case-6-start") ;
	                l_out_handled_1_root_current[1] = l_in_handled_1_current.next;
	                l_created_left = new ListNode(l_in_handled_1_current.val);
	                cases_check = 6;
	                if(DBG_MODE) dbgInfo(tt + " case-6-end") ;
	            }
	        }
	        
	        if(DBG_MODE) dbgInfo(sFun2N + lv + " case-6-check-end") ;
	        
        }
        
        if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-cases-end-" + cases_check);
        
        if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-cases-end-" + cases_check);
        
        if(DBG_MODE) dbgInfo("") ;
        
        int resolved_items = 0;
        if( resolved_items == 0 ) {        	
        	
        	if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-4-start :");
        	
	        if( l_created_left == null ){
	        	if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-4-exec-start :");
	        	if(DBG_MODE) dbgInfo(sFun2N + lv + "no-items-to-handle-work-finished-current-out-pinter-to-null:");	        		            
	            l_out_created_root_current[1] = null;
	            resolved_items = 4;
	            if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-4-exec-end :");
	        }else {
	        	if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-4-no-check :");
	        }
	        
	        if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-4-end :");
	        
        }
        
        if( resolved_items == 0 ) {
        	
        	if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-1-start :");
        	
	        if( l_out_created_root_current[0] == null ){
	        	if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-1-exec-start :");
	        	if(DBG_MODE) dbgInfo(sFun2N + lv + "fill-root-first-time-set-current-as-root :");
	        	l_created_left.next = null;
	            l_out_created_root_current[0] = l_created_left;
	            l_out_created_root_current[1] = l_created_left;
	            resolved_items = 1;
	            if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-1-exec-end :");
	        }else {
	        	if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-1-no-check :");
	        }
	        
	        if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-1-end :");
	        
        }
        
        if( resolved_items == 0 ) {
        	
        	if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-2-start :");
        	
	        if( l_out_created_root_current[0] != null && l_out_created_root_current[1] == null){
	        	if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-2-exec-start :");
	        	if(DBG_MODE) dbgInfo(sFun2N + lv + " should-not-exists:ERROR-OCCURED");
	            l_out_created_root_current[1].next = l_created_left;
	            l_out_created_root_current[1] = l_created_left;
	            resolved_items = 2;
	            if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-2-exec-end :");
	        }else {
	        	if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-2-no-check :");
	        }
	        
	        if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-2-end :");
        }
        
        if( resolved_items == 0 ) {
        	
        	if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-3-start :");
        	
	        if( l_out_created_root_current[0] != null && l_out_created_root_current[1] != null){
	        	if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-3-exec-start :");
	        	if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-2-move-current-to-right :");
	            l_out_created_root_current[1].next = l_created_left;
	            l_out_created_root_current[1] = l_created_left;
	            resolved_items = 3;
	            if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-3-exec-end :");
	        }else {
	        	if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-3-no-check :");
	        }
	        
	        if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-resolve-3-end :");	        
        }
                
        if(DBG_MODE) dbgNode(l_in_handled_0_current, sFun2N  + lv + "l_in_handled_0_current-after-resolve");
        if(DBG_MODE) dbgNode(l_in_handled_1_current, sFun2N  + lv + "l_in_handled_1_current-after-resolve");
        
        if(DBG_MODE) dbgList(l_out_created_root_current[0], sFun2N  + lv + "l_out_created_root_current[0]-after-resolve");
        if(DBG_MODE) dbgNode(l_out_created_root_current[1], sFun2N  + lv + "l_out_created_root_current[1]-after-resolve");

        if(DBG_MODE) dbgList(l_out_handled_0_root_current[0], sFun2N  + lv + "l_out_handled_0_root_current[0]-after-resolve");
        if(DBG_MODE) dbgNode(l_out_handled_0_root_current[1], sFun2N  + lv + "l_out_handled_0_root_current[1]-after-resolve");

        if(DBG_MODE) dbgList(l_out_handled_1_root_current[0], sFun2N  + lv + "l_out_handled_1_root_current[0]-after-resolve");
        if(DBG_MODE) dbgNode(l_out_handled_1_root_current[1], sFun2N  + lv + "l_out_handled_1_root_current[1]-after-resolve");

                
        if(DBG_MODE) dbgInfo(sFun2N + lv + " nodes-cases-resolves-end:" + "[cases_check:" + cases_check + "]" + "[resolved_items:" + resolved_items + "]");
        
        if(DBG_MODE) dbgHeaderLV2(sFun2N + lv + "-2N-end :");
        
        return ;
        
    }
    
    private void dbgNode ( 
            ListNode p_nl
            , String tt){
    	
    	String sFun =  tt + " -> dbgNode::";
    	
		if(DBG_MODE) dbgInfo(" ");
		if(DBG_MODE) dbgInfo(">>");
        if(DBG_MODE) dbgInfo(sFun + " -> dbgNode-start :");
        if(p_nl != null) {
        	if(DBG_MODE) dbgInfo(sFun + " value :" + p_nl.val) ;
        }else {
        	if(DBG_MODE) dbgInfo(sFun + " value :" + "NULL") ;
        }
        if(p_nl != null && p_nl.next != null) {
        	if(DBG_MODE) dbgInfo(sFun + " -> :" + p_nl.next.val) ;
        }
        
        if(DBG_MODE) dbgInfo(sFun + " dbgNode-end :");
        if(DBG_MODE) dbgInfo("<<");
        if(DBG_MODE) dbgInfo(" ");
    }

    
    private int dbgList ( 
            ListNode p_nl
            , String tt){
    	if(!DBG_MODE) {
    		return 0;
    	}
    	int ii = dbgListTxt(p_nl,tt);
    	dbgListShort(p_nl,tt);
    	checkList(p_nl,tt);
    	return ii;
    }    
    
    private int dbgListTxt ( 
        ListNode p_nl
        , String tt){
    	if(!DBG_MODE) {
    		return 0;
    	}
        
    	String sFun =  tt + " -> dbgList::";
        if(DBG_MODE) dbgInfo(" ");
        if(DBG_MODE) dbgInfo(" ");
        if(DBG_MODE) dbgInfo("<<<<<");
        if(DBG_MODE) dbgInfo(sFun + "-start :");
        
        ListNode nl = p_nl;
        int ii =0;
        while(true){
        	
            if(nl == null){
                if(DBG_MODE) dbgInfo(sFun + " node is null:") ;
                break;                   
            }
            if(DBG_MODE) dbgInfo(sFun + " value: " + nl.val) ;
            nl = nl.next;
            ii++;
        }
        
        if(DBG_MODE) dbgInfo(sFun + "end :");
        if(DBG_MODE) dbgInfo(">>>>");
        if(DBG_MODE) dbgInfo(" ");
        if(DBG_MODE) dbgInfo(" ");
        return ii;
    }
	
    private int dbgListShort ( 
            ListNode p_nl
            , String tt){
	    	if(!DBG_MODE) {
	    		return 0;
	    	}
            
        	String sFun =  tt + " -> dbgListShort::";
            if(DBG_MODE) dbgInfo(" ");
            if(DBG_MODE) dbgInfo(" ");
            if(DBG_MODE) dbgInfo("<<<<<");
            if(DBG_MODE) dbgInfo(sFun + "-start :");
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
            if(DBG_MODE) dbgInfo(sFun + " " + sList);
            if(DBG_MODE) dbgInfo(sFun + "end :");
            if(DBG_MODE) dbgInfo(">>>>");
            if(DBG_MODE) dbgInfo(" ");
            if(DBG_MODE) dbgInfo(" ");
            return ii;
    }

    
    private void dbgHeaderLV0 (String tt) {
    	if(!DBG_MODE) {
    		return ;
    	}
    	
    	dbgN5();
    	if(DBG_MODE) dbgInfo("");
    	if(DBG_MODE) dbgInfo("");
        if(DBG_MODE) dbgInfo("==================================================");
        if(DBG_MODE) dbgInfo("=");
        if(DBG_MODE) dbgInfo("=");
        if(DBG_MODE) dbgInfo("=" + tt);
        if(DBG_MODE) dbgInfo("=");
        if(DBG_MODE) dbgInfo("=");
        if(DBG_MODE) dbgInfo("==================================================");
        if(DBG_MODE) dbgInfo("");
        if(DBG_MODE) dbgInfo("");
        dbgN5();
    	
    }
    
    private void dbgHeaderLV1 (String tt) {
    	if(!DBG_MODE) {
    		return ;
    	}
    	
    	dbgN5();
    	if(DBG_MODE) dbgInfo("");
        if(DBG_MODE) dbgInfo("****************************************************");        
        if(DBG_MODE) dbgInfo("*");
        if(DBG_MODE) dbgInfo("**" + tt);
        if(DBG_MODE) dbgInfo("*");        
        if(DBG_MODE) dbgInfo("****************************************************");
        if(DBG_MODE) dbgInfo("");
        dbgN5();
    	
    }
    
    private void dbgHeaderLV2 (String tt) {
    	if(!DBG_MODE) {
    		return ;
    	}
    	
    	dbgN5();
    	if(DBG_MODE) dbgInfo("");
        if(DBG_MODE) dbgInfo("---------------------------------------------------");                
        if(DBG_MODE) dbgInfo("-" + tt);               
        if(DBG_MODE) dbgInfo("---------------------------------------------------");
        if(DBG_MODE) dbgInfo("");
        dbgN5();
    	
    }
    
    private void dbgN5 () {
    	if(!DBG_MODE) {
    		return ;
    	}
    	
    	if(DBG_MODE) dbgInfo("");
    	if(DBG_MODE) dbgInfo("");
    	if(DBG_MODE) dbgInfo("");
    	if(DBG_MODE) dbgInfo("");
    	if(DBG_MODE) dbgInfo("");
    }
    
    private  String checkList ( 
            ListNode p_nl
            , String tt
            ){
    	if(!DBG_MODE) {
    		return "";
    	}
            
        	String sFun =  tt + " -> checkList::";
            if(DBG_MODE) dbgInfo("<<<");        	
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

            if(DBG_MODE) dbgInfo(sFun + "end :");
            if(DBG_MODE) dbgInfo(">>>>");
            if(DBG_MODE) dbgInfo(" ");
            if(DBG_MODE) dbgInfo(" ");
            return  sOut;
    }
    
    private void dbgInfo ( String tt){
    	if(!DBG_MODE) {
    		return ;
    	}
    	
        dbgInfoSubmitted(tt);
    }
    
    private void dbgInfoSubmitted ( String tt){
    	if(!DBG_MODE) {
    		return ;
    	}
    	
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
        
}
