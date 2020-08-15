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
    
    public ListNode mergeKLists( ListNode[] lists ) {
    	
    	String tt = "";
    	String sFun = "> mergeKLists::"; 
    	dbgInfo(sFun  + "start :");
    	ListNode out_list = mergeKListsInternal(tt,lists);
        dbgList(out_list, sFun + "out_list::end");
        dbgInfo(sFun  + "end :");
        
        return out_list;
    }
    
    public ListNode mergeKListsInternal(String tt, ListNode[] lists) {
    	
        String sFunR = tt + " -> mergeKListsInternal::";
        String lv = "[LVL-0]";
        dbgInfo(sFunR  + "start :");
        dbgHeaderLV0(sFunR  + "start :");
        int ii = 0;        
        ListNode [] l_created_root_current = new ListNode[2];
        ListNode handled_0_root = null;
        
        for (ListNode handled_1_root : lists){
        	
        	dbgInfo(sFunR   + "-" + ii + "merge-list-start");	
        	
        	dbgList(handled_0_root, sFunR + lv + "[roots:" + ii + "]" + "handled_0_root-before-merge-roots");
            dbgList(handled_1_root, sFunR + lv + "[roots:" + ii + "]" + "handled_1_root-before-merge-roots");
        	dbgList(l_created_root_current[0], sFunR + lv + "[roots:" + ii + "]" + "l_created_root_current[0]-before-merge-roots");
            dbgList(l_created_root_current[1], sFunR + lv + "[roots:" + ii + "]" + "l_created_root_current[1]-before-merge-roots");
            
            mergeTwoRoots(
            		l_created_root_current
            		, handled_0_root
            		, handled_1_root
            		, sFunR + "[roots:" + ii + "]");

        	dbgList(l_created_root_current[0], sFunR + lv + "[roots:" + ii + "]" + "l_created_root_current[0]-after-merge-roots");
        	dbgList(l_created_root_current[1], sFunR + lv + "[roots:" + ii + "]" + "l_created_root_current[1]-after-merge-roots");
            
            handled_0_root = l_created_root_current[0];
            
            l_created_root_current[0] = null;
            l_created_root_current[1] = null;
            
            dbgList(handled_1_root, sFunR + lv + "[roots:" + ii + "]" + "handled_1_root::after-merge-after-merge-roots");
            dbgList(handled_0_root, sFunR + lv + "[roots:" + ii + "]" + "handled_0_root::after-merge-after-merge-roots");
            
            dbgInfo(sFunR   + "[" + ii + "]" +  "merge-list-end :");
            
            ii++;
            
        }
        
        dbgList(handled_0_root, sFunR+ "handled_out_root::end");
        dbgHeaderLV0(sFunR  + "end");
        dbgInfo(sFunR  + "end :");
        
        return handled_0_root;
    }

    private void mergeTwoRoots(
        ListNode[] l_out_created_root_current
        , ListNode l_handled_0_root
        , ListNode l_handled_1_root
        , String tt){
        
        
        String sFunMN =  tt + "-> mergeTwoRoots::";
        String lv = "[LVL-2]";
        
        dbgHeaderLV1(sFunMN + lv +  "[nodes:" + "start" + "]" + "s-start :");
        
        ListNode l_handled_0_current = l_handled_0_root;
        ListNode l_handled_1_current =   l_handled_1_root;      
        
        dbgList(l_handled_0_current, sFunMN + lv +  "[nodes:" + "start" + "]" + "l_handled_0_current-before");        
        dbgList(l_handled_1_current, sFunMN + lv +  "[nodes:" + "start" + "]" + "l_handled_1_current-before");

        dbgList(l_out_created_root_current[0], sFunMN + lv +  "[nodes:" + "start" + "]" + "l_out_created_root_current[0]-before");        
        dbgList(l_out_created_root_current[1], sFunMN + lv +  "[nodes:" + "start" + "]" + "l_out_created_root_current[1]-before");
        
        ListNode[] l_out_handled_0_root_current = new ListNode[2];
        l_out_handled_0_root_current[0] = l_handled_0_root;
        
        
        ListNode[] l_out_handled_1_root_current = new ListNode[2];
        l_out_handled_1_root_current[0] = l_handled_1_root;
        
        int ii = 0;
        while( true )                
        {
        	dbgInfo(sFunMN + lv +  "[nodes:" + ii + "]" + "=>");
        	dbgInfo(sFunMN + lv +  "[nodes:" + ii + "]" + "-start-merge-nodes-");
                    
            dbgList(l_handled_0_current, sFunMN + lv +  "[nodes:" + ii + "]"  + "l_handled_0_current-before-merge-nodes" );
            dbgList(l_handled_1_current, sFunMN + lv +  "[nodes:" + ii + "]"  + "l_handled_1_current-before-merge-nodes" );
            
        	dbgList(l_out_created_root_current[0], sFunMN + lv +  "[nodes:" + ii + "]"  + "l_out_created_root_current[0]-before-merge-nodes" );        	
        	dbgNode(l_out_created_root_current[1], sFunMN + lv + "[nodes:" + ii + "]"  + "l_out_created_root_current[1]-before-merge-node" );

        	dbgList(l_out_handled_0_root_current[0], sFunMN + lv +  "[nodes:" + ii + "]"  + "l_out_handled_0_root_current[0]-before-merge-nodes" );        	
        	dbgNode(l_out_handled_0_root_current[1], sFunMN + lv +  "[nodes:" + ii + "]" + "l_out_handled_0_root_current[1]-before-merge-node");
        	
        	dbgList(l_out_handled_1_root_current[0], sFunMN + lv +  "[nodes:" + ii + "]" + "l_out_handled_1_root_current[0]-before-merge-nodes" );        	
        	dbgNode(l_out_handled_1_root_current[1], sFunMN + lv +  "[nodes:" + ii + "]" + "l_out_handled_1_root_current[1]-before-merge-node" );
        	
        	mergeTwoNodes( 
        		l_handled_0_current
                , l_handled_1_current
                , l_out_created_root_current
                , l_out_handled_0_root_current
                , l_out_handled_1_root_current
                , sFunMN +  "[nodes:" + ii + "]");
        	
        	l_handled_0_current = l_out_handled_0_root_current[1];
        	l_handled_1_current = l_out_handled_1_root_current[1];            
            
        	dbgList(l_handled_0_root, sFunMN + lv +  "[nodes:" + ii + "]" + "l_handled_0_root-after-merge-nodes" );
        	dbgNode(l_handled_0_current, sFunMN + lv +  "[nodes:" + ii + "]" + "l_handled_0_current-after-merge-nodes" );
        	
        	dbgList(l_handled_1_root, sFunMN + lv +  "[nodes:" + ii + "]" + "l_handled_1_root-after-merge-nodes" );            
        	dbgNode(l_handled_1_current, sFunMN + lv +  "[nodes:" + ii + "]" + "l_handled_1_current-after-merge-nodes" );
        	
        	dbgList(l_out_created_root_current[0], sFunMN + lv +  "[nodes:" + ii + "]" + "l_out_created_root_current[0]-after-merge-nodes" );        	
        	dbgNode(l_out_created_root_current[1], sFunMN + lv +  "[nodes:" + ii + "]" + "l_out_created_root_current[1]-after-merge-nodes" );
        	
        	
            
            if( l_handled_0_current == null  && l_handled_1_current == null )
            {
            	dbgInfo(sFunMN + lv +  "[nodes:" + ii + "]" + "-ater=merge-break-on-empty-");
            	dbgInfo(sFunMN + lv +  "[nodes:" + ii + "]" + "<==|");
                break;
            }
            
            dbgInfo(sFunMN + lv +  "[nodes:" + ii + "]" + "-move-to-merge-next-node-");
            
            
            ii ++;
            dbgInfo(sFunMN + lv +  "[nodes:" + ii + "]" + "<=<");
            
        }        
        
        dbgList(l_out_created_root_current[0], sFunMN + lv +  "[nodes:" + ii + "]" + "l_out_created_root_current-list-after-merge-list");
                
        dbgHeaderLV1(sFunMN + lv +  "end :");
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
        dbgHeaderLV2(sFun2N  + lv + "-2N-start :");
        
        dbgNode(l_out_handled_0_root_current[1], sFun2N  + lv + "l_out_handled_0_root_current[1]-before-init");
        dbgNode(l_out_handled_1_root_current[1], sFun2N  + lv + "l_out_handled_1_root_current[1]-before-init");
        
        dbgInfo(sFun2N  + lv + "-initialize-out-current-pointers-start");        
        l_out_handled_0_root_current[1] = l_in_handled_0_current;
        l_out_handled_1_root_current[1] = l_in_handled_1_current;
        dbgInfo(sFun2N  + lv + "-initialize-out-current-pointers-end");
        
        
        dbgNode(l_in_handled_0_current, sFun2N  + lv + "l_in_handled_0_current-before-resolve");
        dbgNode(l_in_handled_1_current, sFun2N  + lv + "l_in_handled_1_current-before-resolve");        
        
        dbgList(l_out_created_root_current[0], sFun2N  + lv + "l_out_created_root_current[0]-before-resolve");
        dbgNode(l_out_created_root_current[1], sFun2N  + lv + "l_out_created_root_current[1]-before-resolve");

        dbgList(l_out_handled_0_root_current[0], sFun2N  + lv + "l_out_handled_0_root_current[0]-before-resolve");
        dbgNode(l_out_handled_0_root_current[1], sFun2N  + lv + "l_out_handled_0_root_current[1]-before-resolve");

        dbgList(l_out_handled_1_root_current[0], sFun2N  + lv + "l_out_handled_1_root_current[0]-before-resolve");
        dbgNode(l_out_handled_1_root_current[1], sFun2N  + lv + "l_out_handled_1_root_current[1]-before-resolve");
        
        ListNode l_created_left = null;                        
        
        int cases_check = 0;
        if(cases_check == 0) {
        	
        	dbgInfo(sFun2N + lv + " case-1-check-start") ;
        	
	        if(l_in_handled_0_current == null && l_in_handled_1_current == null){
	            dbgInfo(sFun2N + lv + "case-1-exec-start") ;
	            dbgInfo(sFun2N + lv + "no-nodes-to-handle") ;
	            l_created_left = null;
	            cases_check = 1;
	            dbgInfo(sFun2N + lv + "case 1-exec-end") ;
	        }
	        
	        dbgInfo(sFun2N + lv + " case-1-check-end") ;
	        
        }
        
        if(cases_check == 0) {
        	
        	dbgInfo(sFun2N + lv + " case-2-check-start") ;
        	
	        if(l_in_handled_0_current == null && l_in_handled_1_current != null){
	            dbgInfo(sFun2N + lv + " case-2-exec-start") ;
	            dbgInfo(sFun2N + lv + " item-from-list-1-was-taken") ;
	            l_out_handled_1_root_current[1] = l_in_handled_1_current.next;
	            l_created_left = new ListNode(l_in_handled_1_current.val);
	            l_created_left.next = null;
	            dbgInfo(sFun2N + lv + " case-2-exec-end") ;
	            cases_check = 2;
	        }
	        
	        dbgInfo(sFun2N + lv + " case-2-check-end") ;
	        
        }
        
        if(cases_check == 0) {
        	
        	dbgInfo(sFun2N + lv + " case-3-check-start") ;
        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current == null){
	            dbgInfo(sFun2N + lv + " case-3-exec-start") ;
	            dbgInfo(sFun2N + lv + " item-from-list-0-was-taken") ;
	            l_out_handled_0_root_current[1] = l_in_handled_0_current.next;
	            l_created_left = new ListNode(l_in_handled_0_current.val);   
	            l_created_left.next = null;
	            cases_check = 3;
	            dbgInfo(sFun2N + lv + " case-3-exec-end") ;
	        }
	        
	        dbgInfo(sFun2N + lv + " case-3-check-end") ;
	        
        }
        
        if(cases_check == 0) {
        	
        	dbgInfo(sFun2N + lv + " case-4-check-start") ;
        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current != null){
	        	dbgInfo(sFun2N + lv + " case-4-check-vals") ;
	            if( l_in_handled_0_current.val < l_in_handled_1_current.val ){
	            	dbgInfo(sFun2N + lv + " case-4-exec-start") ;
	            	dbgInfo(sFun2N + lv + " item-from-list-0-was-taken") ;
	            	l_out_handled_0_root_current[1] = l_in_handled_0_current.next;            	                
	                l_created_left = new ListNode(l_in_handled_0_current.val);
	                cases_check = 4;
	                dbgInfo(sFun2N + lv + " case-4-exec-end") ;	                
	            }
	        }
	        
	        dbgInfo(sFun2N + lv + " case-4-check-end") ;
	        
        }
        
        if(cases_check == 0) {
        	
        	dbgInfo(sFun2N + lv + " case-5-check-start") ;
        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current != null){
	        	dbgInfo(sFun2N + lv + " case-5-check-vals") ;
	            if(l_in_handled_0_current.val == l_in_handled_1_current.val){
	            	dbgInfo(sFun2N + lv + " case-5-exec-start") ;
	            	dbgInfo(sFun2N + lv + " item-from-list-0-was-taken") ;	            	
	            	l_out_handled_0_root_current[1] = l_in_handled_0_current.next;	                
	                l_created_left = new ListNode(l_in_handled_0_current.val);
	                cases_check = 5;
	                dbgInfo(sFun2N + lv + " case-5-exec-end") ;
	                
	            }
	        }
	        
	        dbgInfo(sFun2N + lv + " case-5-check-end") ;
	        
        }
        
        if(cases_check == 0) {
        	
        	dbgInfo(sFun2N + lv + " case-6-check-start") ;
        	
	        if(l_in_handled_0_current != null && l_in_handled_1_current != null){
	        	dbgInfo(sFun2N + lv + " case-6-check-vals") ;
	            if(l_in_handled_0_current.val > l_in_handled_1_current.val){            	
	                dbgInfo(tt + " case-6-start") ;
	                l_out_handled_1_root_current[1] = l_in_handled_1_current.next;
	                l_created_left = new ListNode(l_in_handled_1_current.val);
	                cases_check = 6;
	                dbgInfo(tt + " case-6-end") ;
	            }
	        }
	        
	        dbgInfo(sFun2N + lv + " case-6-check-end") ;
	        
        }
        
        dbgInfo(sFun2N + lv + " nodes-cases-end-" + cases_check);
        
        dbgInfo(sFun2N + lv + " nodes-cases-end-" + cases_check);
        
        dbgInfo("") ;
        
        int resolved_items = 0;
        if( resolved_items == 0 ) {        	
        	
        	dbgInfo(sFun2N + lv + " nodes-resolve-4-start :");
        	
	        if( l_created_left == null ){
	        	dbgInfo(sFun2N + lv + " nodes-resolve-4-exec-start :");
	        	dbgInfo(sFun2N + lv + "no-items-to-handle-work-finished-current-out-pinter-to-null:");	        		            
	            l_out_created_root_current[1] = null;
	            resolved_items = 4;
	            dbgInfo(sFun2N + lv + " nodes-resolve-4-exec-end :");
	        }else {
	        	dbgInfo(sFun2N + lv + " nodes-resolve-4-no-check :");
	        }
	        
	        dbgInfo(sFun2N + lv + " nodes-resolve-4-end :");
	        
        }
        
        if( resolved_items == 0 ) {
        	
        	dbgInfo(sFun2N + lv + " nodes-resolve-1-start :");
        	
	        if( l_out_created_root_current[0] == null ){
	        	dbgInfo(sFun2N + lv + " nodes-resolve-1-exec-start :");
	        	dbgInfo(sFun2N + lv + "fill-root-first-time-set-current-as-root :");
	        	l_created_left.next = null;
	            l_out_created_root_current[0] = l_created_left;
	            l_out_created_root_current[1] = l_created_left;
	            resolved_items = 1;
	            dbgInfo(sFun2N + lv + " nodes-resolve-1-exec-end :");
	        }else {
	        	dbgInfo(sFun2N + lv + " nodes-resolve-1-no-check :");
	        }
	        
	        dbgInfo(sFun2N + lv + " nodes-resolve-1-end :");
	        
        }
        
        if( resolved_items == 0 ) {
        	
        	dbgInfo(sFun2N + lv + " nodes-resolve-2-start :");
        	
	        if( l_out_created_root_current[0] != null && l_out_created_root_current[1] == null){
	        	dbgInfo(sFun2N + lv + " nodes-resolve-2-exec-start :");
	        	dbgInfo(sFun2N + lv + " should-not-exists:ERROR-OCCURED");
	            l_out_created_root_current[1].next = l_created_left;
	            l_out_created_root_current[1] = l_created_left;
	            resolved_items = 2;
	            dbgInfo(sFun2N + lv + " nodes-resolve-2-exec-end :");
	        }else {
	        	dbgInfo(sFun2N + lv + " nodes-resolve-2-no-check :");
	        }
	        
	        dbgInfo(sFun2N + lv + " nodes-resolve-2-end :");
        }
        
        if( resolved_items == 0 ) {
        	
        	dbgInfo(sFun2N + lv + " nodes-resolve-3-start :");
        	
	        if( l_out_created_root_current[0] != null && l_out_created_root_current[1] != null){
	        	dbgInfo(sFun2N + lv + " nodes-resolve-3-exec-start :");
	        	dbgInfo(sFun2N + lv + " nodes-resolve-2-move-current-to-right :");
	            l_out_created_root_current[1].next = l_created_left;
	            l_out_created_root_current[1] = l_created_left;
	            resolved_items = 3;
	            dbgInfo(sFun2N + lv + " nodes-resolve-3-exec-end :");
	        }else {
	        	dbgInfo(sFun2N + lv + " nodes-resolve-3-no-check :");
	        }
	        
	        dbgInfo(sFun2N + lv + " nodes-resolve-3-end :");	        
        }
                
        dbgNode(l_in_handled_0_current, sFun2N  + lv + "l_in_handled_0_current-after-resolve");
        dbgNode(l_in_handled_1_current, sFun2N  + lv + "l_in_handled_1_current-after-resolve");
        
        dbgList(l_out_created_root_current[0], sFun2N  + lv + "l_out_created_root_current[0]-after-resolve");
        dbgNode(l_out_created_root_current[1], sFun2N  + lv + "l_out_created_root_current[1]-after-resolve");

        dbgList(l_out_handled_0_root_current[0], sFun2N  + lv + "l_out_handled_0_root_current[0]-after-resolve");
        dbgNode(l_out_handled_0_root_current[1], sFun2N  + lv + "l_out_handled_0_root_current[1]-after-resolve");

        dbgList(l_out_handled_1_root_current[0], sFun2N  + lv + "l_out_handled_1_root_current[0]-after-resolve");
        dbgNode(l_out_handled_1_root_current[1], sFun2N  + lv + "l_out_handled_1_root_current[1]-after-resolve");

        
        
        dbgInfo(sFun2N + lv + " nodes-cases-resolves-end:" + "[cases_check:" + cases_check + "]" + "[resolved_items:" + resolved_items + "]");
        
        dbgHeaderLV2(sFun2N + lv + "-2N-end :");
        
        return ;
        
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

    
    private void dbgList ( 
        ListNode p_nl
        , String tt){
        
    	String sFun =  tt + " -> dbgList::";
        dbgInfo(" ");
        dbgInfo(" ");
        dbgInfo("<<<<<");
        dbgInfo(sFun + "-start :");
        
        ListNode nl = p_nl;
        
        while(true){
        	
            if(nl == null){
                dbgInfo(sFun + " node is null:") ;
                break;                   
            }
            dbgInfo(sFun + " value: " + nl.val) ;
            nl = nl.next;
        }
        
        dbgInfo(sFun + "end :");
        dbgInfo(">>>>");
        dbgInfo(" ");
        dbgInfo(" ");        
    }

    
    private void dbgHeaderLV0(String tt) {
    	dbgN5();
    	dbgInfo("");
    	dbgInfo("");
        dbgInfo("==================================================");
        dbgInfo("=");
        dbgInfo("=");
        dbgInfo("=" + tt);
        dbgInfo("=");
        dbgInfo("=");
        dbgInfo("==================================================");
        dbgInfo("");
        dbgInfo("");
        dbgN5();
    	
    }
    
    private void dbgHeaderLV1(String tt) {
    	dbgN5();
    	dbgInfo("");
        dbgInfo("****************************************************");        
        dbgInfo("*");
        dbgInfo("**" + tt);
        dbgInfo("*");        
        dbgInfo("****************************************************");
        dbgInfo("");
        dbgN5();
    	
    }
    
    private void dbgHeaderLV2(String tt) {
    	dbgN5();
    	dbgInfo("");
        dbgInfo("---------------------------------------------------");                
        dbgInfo("-" + tt);               
        dbgInfo("---------------------------------------------------");
        dbgInfo("");
        dbgN5();
    	
    }
    
    private void dbgN5() {
    	dbgInfo("");
    	dbgInfo("");
    	dbgInfo("");
    	dbgInfo("");
    	dbgInfo("");
    }
    
    private void dbgInfo ( String tt){
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
