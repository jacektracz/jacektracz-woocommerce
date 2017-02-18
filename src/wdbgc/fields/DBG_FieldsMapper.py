import sys
import os

from .. appcore.logging.DBG_Log import *
from .. fields.DBG_FieldStrings import *
from .. fields.DBG_FieldInts import *
from .. fields.DBG_FieldHexs import *
from .. fields.DBG_FieldBools import *
from .. appcore.htmlwriters.DBG_Html import *
from .. fields.DBG_FieldsBase import *
class DBG_FieldsMapper(DBG_FieldsBase):
        def __init__(self,pparent,sdbg): 
                DBG_FieldsBase.__init__(self,pparent,sdbg)
                self.xx_dbg("DBG_FieldsMapper::init_object_internal::")
                self.xx_set_class_name ( "FieldsMapper" )
                self.xx_set_full_class_name ( "iastora!FieldsMapper" )
                self.m_parent_loc = pparent
                self.m_strs = DBG_FieldStrings("DBG_FieldsMapper",pparent)
                self.m_ints = DBG_FieldInts("DBG_FieldsMapper",pparent)
                self.m_hexs = DBG_FieldHexs("DBG_FieldsMapper",pparent)
                self.m_bools = DBG_FieldBools("DBG_FieldsMapper",pparent)
                self.m_tag = "fields"
                self.xx_dbg("DBG_FieldsMapper::init_object_internal::out::")
                
                #self.init_object(pparent, sdbg)
                
                
        def set_parent(self, pparent):
                self.xx_dbg("DBG_FieldsMapper::set_parent::in::")
                self.m_parent_loc = pparent
                self.m_strs.set_parent(pparent)
                self.m_ints.set_parent(pparent)
                self.m_hexs.set_parent(pparent)
                self.m_bools.set_parent(pparent)
                self.xx_dbg("DBG_FieldsMapper::set_parent::out::")

        def add_fields_asstr_u32s(self, pvv):
                for pvar in pvv :
                        self.m_strs.add_asstr_u32( pvar)                
                
        def add_fields_asstr_u32(self, pvv):
                self.m_strs.add_asstr_u32( pvv)

        def add_fields_asstr_ints(self, pvv):
                for pvar in pvv :
                    self.m_strs.add_asstr_int( pvar )
                
        def add_fields_asstr_int(self, pvar):
                self.m_strs.add_asstr_int( pvar)
                
        def add_fields_asstr_hex(self, pvar):
                self.m_strs.add_asstr_hex( pvar)
                
        def add_fields_asstr_bool(self, pvar):
                self.m_strs.add_asstr_bool( pvar)

        def add_fields_asstr_addr_method(self, pvar):
                self.m_strs.add_asstr_addr_method( pvar)
                
        def add_fields_asstr_addr_class(self, pvar):
                self.m_strs.add_asstr_addr_class( pvar )

        def add_fields_asstr_addr_memory(self, pvar):
                self.m_strs.add_asstr_addr_memory( pvar )
                                
        def add_fields_asstr_addr(self, pvar):
                self.m_strs.add_asstr_addr( pvar)

        def add_fields_asstr_addrs(self, pvar_arr):
                for pvar in pvar_arr:
                        self.m_strs.add_asstr_addr( pvar)
                
        def add_fields_asstr_str_uni(self, pvar, plen):
                self.m_strs.add_struni( pvar, plen)
                
        def add_fields_asstr_raw_output(self, pvar):
                self.m_strs.add_asstr_raw_output( pvar)
                
        def add_str(self, pvar, plen):
                self.m_strs.add_str( pvar, plen)
                
        def add_int(self, pvar,ptitle = "" ):
                self.m_ints.add_int( pvar,ptitle )
                
        def add_bool(self, pvar,ptitle = "" ):
                self.m_bools.add_item( pvar,ptitle )
                
        def add_hex(self, pvar,ptitle = "" ):
                self.m_hexs.add_item( pvar,ptitle )
                
        def add_raw_str(self, pvar,length=0):
                self.m_strs.add_raw_str( pvar)
                
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_FieldsMapper::print_object")
                                        
        def prepare_object_internal(self,pparent):
                self.xx_dbg("DBG_FieldsMapper::prepare_object_internal::")
                self.m_strs.prepare_object()
                self.m_ints.prepare_object()
                self.m_hexs.prepare_object()
                self.m_bools.prepare_object()                
                self.xx_dbg("DBG_FieldsMapper::prepare_object_internal::out::")
                
        def print_object(self):
                try:
                        DBG_Html.xx_print_props_start(self.m_tag)
                        self.print_object_internal()
                        DBG_Html.xx_print_props_end(self.m_tag)
                except:
                        self.xx_exception("DBG_FieldsMapper::print_object")
                
        def print_object_internal(self):
                self.xx_dbg("DBG_FieldsMapper::print_object::")
                self.prepare_object()
                self.m_strs.print_object()
                self.m_ints.print_object()
                self.m_hexs.print_object()
                self.m_bools.print_object()
                self.xx_dbg("DBG_FieldsMapper::print_object::out::")                                                

        def xx_print_fields(self,sdbg):
                try:
                    self.xx_dbg( "DBG_FieldsMapper::xx_print_ptr::method_in::")
                    
                    self.print_object()
                    self.xx_dbg( "DBG_FieldsMapper::xx_print_ptr::method_out::")
                except:
                    self.xx_exception("DBG_FieldsMapper::xx_print_fields::exception::")
                    
        def set_fields_parent(self, pparent):
                self.xx_dbg("DBG_FieldsMapper::set_fields_parent")
                self.set_parent( pparent )
        
        def add_fields_int(self,ss):
                self.xx_dbg("DBG_FieldsMapper::self.add_fields_int::in::")
                self.add_int(ss)
                self.xx_dbg("DBG_FieldsMapper::self.add_fields_int::out::")
                
        def add_fields_int_array(self,ss):
                self.xx_dbg("DBG_FieldsMapper::self.add_fields_int_array::in::")
                for ii_f in ss :
                    self.add_fields_int(ii_f)
                self.xx_dbg("DBG_FieldsMapper::self.add_fields_int_array::out::")                
                
                
        def add_fields_str(self,pss,plen):
                self.xx_dbg("DBG_FieldsMapper::add_fields_str::in::")
                self.add_str(pss,plen)
                self.xx_dbg("DBG_FieldsMapper::add_fields_str::out")

        def add_fields_uchar(self, pss):
                self.xx_dbg("DBG_FieldsMapper::add_fields_str::in::")
                self.m_strs.add_uchar( pss )
                self.xx_dbg("DBG_FieldsMapper::add_fields_str::out")
                
                
        def add_fields_hex_array(self,ss):
                self.xx_dbg("DBG_FieldsMapper::add_fields_hex_array")
                for ii_f in ss :
                    self.add_hex(ii_f)
                self.xx_dbg("DBG_FieldsMapper::add_fields_hex_array::out::")
                
        def add_fields_hex(self,ss):
                self.xx_dbg("DBG_FieldsMapper::add_fields_hex::in::")
                self.add_hex(ss)
                self.xx_dbg("DBG_FieldsMapper::add_fields_hex::out::")
              
              
                
        def add_fields_bool_array(self,ss):
                self.xx_dbg("DBG_FieldsMapper::add_fields_bool_array")
                for ii_f in ss :
                    self.add_bool(ii_f)
                self.xx_dbg("DBG_FieldsMapper::add_fields_bool_array::out::")
                
        def get_fields_int(self,smb):
                try:
                        return self.m_ints.fields_get_int(smb)
                except:
                        self.xx_exception("DBG_FieldsMapper::get_fields_int::exception::")
                        return 0
        
        def get_fields_hex(self, smb):
                return self.m_hexs.fields_get_hex( smb )

        def get_fields_string(self, smb):
                return self.m_strs.fields_get_string( smb )
        
        def get_fields_asstr_int(self, smb):
                try:
                        vv_out = 0
                        vv = self.m_strs.fields_get_string( smb )
                        if(vv != ""):
                                vv_out = int(vv)
                                
                        return vv_out                                
                except:
                        self.xx_exception("DBG_FieldsMapper::get_fields_asstr_int::exception::")
                return 0

        def get_fields_asstr_u32(self, smb):
                try:
                        vv_out = 0
                        vv = self.m_strs.fields_get_string( smb )
                        if(vv != ""):
                                vv_out = int(vv)
                                
                        return vv_out                                
                except:
                        self.xx_exception("DBG_FieldsMapper::get_fields_asstr_int::exception::")
                return 0

        def initialize_by_parent(self,pparent):
                self.xx_dbg("DBG_FieldsMapper::initialize_by_parent::in::")
                self.set_parent(pparent)
                self.prepare_object()
                self.xx_dbg("DBG_FieldsMapper::initialize_by_parent::out::")
