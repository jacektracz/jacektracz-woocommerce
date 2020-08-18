package com.jacektracz.letcode.mergeklists;

public class JacekTraczKlistsValidations {
	
	private boolean TEST_DEBUG_MODE = true;
	
	public void setDebugMode(boolean dbg) {
		TEST_DEBUG_MODE = dbg;
	}
	
	public int dbgLists ( 
            ListNode []p_nl
            , String tt){
    	
    	boolean proceed = false;
    	if(TEST_DEBUG_MODE) {
    		proceed = true;
    	}    	
    	
    		
    	if(!proceed) {
    		return 0;
    	}
	    for (int ii = 0;ii<p_nl.length;ii++) {	    	
	    	if(p_nl[ii] != null) {	    		
	    		dbgList(p_nl[ii],tt);	    		
	    		dbgInfoSubmitted(tt + "list-idx:" + ii);
	    	}else {	    		
	    		dbgInfoSubmitted(tt + "list-idx:" + ii +" -> null");	    		
	    	}
	    }
	    return 0;
    }	
    public void dbgInfo ( String tt){
    	if(!TEST_DEBUG_MODE) {
    		return;
    	}
    	
        dbgInfoSubmitted(tt);
    }
    
    public void dbgInfoSubmitted ( String tt){

        System.out.println( tt );
    }
	
    public void dbgNode ( 
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

    public int dbgList ( 
            ListNode p_nl
            , String tt){
    	
    	if(!TEST_DEBUG_MODE) {
    		return 0;
    	}
    	
    	
    	int ii = dbgListTxt(p_nl,tt);
    	dbgListShort(p_nl,tt);
    	return ii;
    }    
    
    public int dbgListTxt ( 
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
	
    public int dbgListShort ( 
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
    
    public  String checkList ( 
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

}
