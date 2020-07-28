import sys
import os
import logging
import shutil

# C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py
# C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\createswipper\lkdcore\LKD_FinAnalysis.py

class LKD_FinAmounts:
        
        def __init__(self):
                self.m_title = ""
                self.m_data = ""
                self.m_amount = ""
                self.m_amount_out = 0
                self.m_amount_out_jt = 0
                self.m_amount_out_njt = 0
                self.m_amount_in = 0
                self.m_amount_out = 0
                self.m_amount_out_jt_alim_g = 0
                self.m_amount_out_jt_alim_j = 0
                self.m_amount_out_jt_czynsz = 0
                self.m_amount_out_jt_hipo = 0
                self.m_amount_out_jt_multi = 0
                self.m_amount_out_jt_sum = 0
                self.m_amount_out_jt_mandate = 0
                self.m_amount_out_jt_sport = 0
                self.m_amount_sum_0 = 0
                self.m_amount_sum_1 = 0
                self.m_amount_sum_2 = 0
                self.m_amount_sum_3 = 0


        def xx_dbg(self, tt):
                "" ""
                print tt

        def create_sum(self, tt):
                "" ""

                self.m_amount_out_jt_sum = 0
                self.m_amount_out_jt_sum = self.m_amount_out_jt_sum + self.m_amount_out_jt_alim_g
                self.m_amount_out_jt_sum = self.m_amount_out_jt_sum + self.m_amount_out_jt_alim_j
                self.m_amount_out_jt_sum = self.m_amount_out_jt_sum + self.m_amount_out_jt_czynsz 
                self.m_amount_out_jt_sum = self.m_amount_out_jt_sum + self.m_amount_out_jt_hipo 
                self.m_amount_out_jt_sum = self.m_amount_out_jt_sum + self.m_amount_out_jt_multi
                self.m_amount_out_jt_sum = self.m_amount_out_jt_sum + self.m_amount_out_jt_mandate
                self.m_amount_out_jt_sum = self.m_amount_out_jt_sum + self.m_amount_out_jt_sport

                

class LKD_FinAmountsService:
        def __init__(self):
                self.m_title = ""

        def get_copy(self, p_fin_amounts_src):
                dd_out = LKD_FinAmounts()
                dd_out.m_title = p_fin_amounts_src.m_title
                dd_out.m_data = p_fin_amounts_src.m_data
                dd_out.m_amount_out_jt = p_fin_amounts_src.m_amount_out_jt
                dd_out.m_amount_out_njt = p_fin_amounts_src.m_amount_out_njt
                dd_out.m_amount_in = p_fin_amounts_src.m_amount_in
                dd_out.m_amount_out = p_fin_amounts_src.m_amount_out
                dd_out.m_amount_out_jt_alim_g = p_fin_amounts_src.m_amount_out_jt_alim_g
                dd_out.m_amount_out_jt_alim_j = p_fin_amounts_src.m_amount_out_jt_alim_j
                dd_out.m_amount_out_jt_czynsz = p_fin_amounts_src.m_amount_out_jt_czynsz
                dd_out.m_amount_out_jt_hipo = p_fin_amounts_src.m_amount_out_jt_hipo
                dd_out.m_amount_out_jt_sum = p_fin_amounts_src.m_amount_out_jt_sum
                dd_out.m_amount_out_jt_multi = p_fin_amounts_src.m_amount_out_jt_multi                
                dd_out.m_amount_out_jt_mandate = p_fin_amounts_src.m_amount_out_jt_mandate
                dd_out.m_amount_out_jt_sport = p_fin_amounts_src.m_amount_out_jt_sport
                dd_out.m_amount_sum_0 = p_fin_amounts_src.m_amount_sum_0
                dd_out.m_amount_sum_1 = p_fin_amounts_src.m_amount_sum_1
                dd_out.m_amount_sum_2 = p_fin_amounts_src.m_amount_sum_2
                
                return dd_out

class LKD_FinAnalysis:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_FinAnalysis::__init__::in::")
                self.m_src = "blogtech_x2"             
               
        def xx_dbg(self, tt):
                "" ""
                print tt
        
        def prepare_object(self):
                self.xx_dbg("LKD_FinAnalysis::prepare_object::in::")
                        
                self.xx_dbg("LKD_FinAnalysis::prepare_object::out::")

        def read_file(self):
                self.xx_dbg("LKD_FinAnalysis::copy_files::in::")
                        
                self.xx_dbg("LKD_FinAnalysis::copy_files::out::")

        def print_data(self):

                self.print_data_1()
                self.print_data_2()
                self.print_data_sum()

        def print_data_1(self):

                dd = self.get_data_1()

                for p_fin_item in dd:
                        s_line = self.get_line(p_fin_item)
                        self.xx_dbg(s_line)
                        
                for p_fin_item in dd:

                        s_line = self.get_line_def(p_fin_item)
                        self.xx_dbg(s_line)

        def print_data_2(self):

                dd = self.get_data_2()

                for p_fin_item in dd:
                        s_line = self.get_line(p_fin_item)
                        self.xx_dbg(s_line)
                        

                for p_fin_item in dd:
                        s_line = self.get_line_def(p_fin_item)
                        self.xx_dbg(s_line)


                h_srv = LKD_FinAmountsService()                              
                dd_amounts_out = LKD_FinAmounts()
                for p_fin_item in dd:

                        out_loc_amounts = self.process_amounts(
                                         h_srv.get_copy(dd_amounts_out)
                                        , p_fin_item)
                                        
                        dd_amounts_out = h_srv.get_copy(
                                        out_loc_amounts)

                        dd_amounts_out.create_sum("")
                        
                        self.print_amounts(dd_amounts_out)        

                self.print_amounts(dd_amounts_out)


        def print_data_sum( self ):
                dd = self.get_items_sum()
                for p_fin_item in dd:
                        self.print_amounts( p_fin_item ) 

                
        def process_amounts(self, p_fin_amounts, p_fin_item):

                self.xx_dbg("LKD_FinAnalysis::get_line::in::")
                self.xx_dbg("m_amount:[" + p_fin_item.m_amount+ "]")
                self.xx_dbg("m_title:[" + p_fin_item.m_title+ "]")
                self.xx_dbg("m_type:[" + p_fin_item.m_type + "]")

                
                ff = self.get_float( p_fin_item.m_amount )

                l_fin_amounts = LKD_FinAmounts()
                h_srv = LKD_FinAmountsService()
                l_fin_amounts = h_srv.get_copy(p_fin_amounts)

                self.xx_dbg("amount:[" + str(ff) + "]")

                if(ff < 0 ):
                        self.xx_dbg("processed[m_amount_out]")
                        l_fin_amounts.m_amount_out = p_fin_amounts.m_amount_out + ff

                if(ff > 0 ):
                        self.xx_dbg("processed[m_amount_in]")
                        l_fin_amounts.m_amount_in = p_fin_amounts.m_amount_in + ff

                if(p_fin_item.m_type == "JT"):
                        self.xx_dbg("processed[m_amount_out_jt]")
                        l_fin_amounts.m_amount_out_jt = p_fin_amounts.m_amount_out_jt + ff

                if(p_fin_item.m_type == ""):
                        self.xx_dbg("processed[m_amount_out_njt]")
                        l_fin_amounts.m_amount_out_njt = p_fin_amounts.m_amount_out_njt + ff

                if(p_fin_item.m_title == "HIPO"):
                        self.xx_dbg("processed[m_amount_out_jt_hipo]")
                        l_fin_amounts.m_amount_out_jt_hipo = p_fin_amounts.m_amount_out_jt_hipo + ff

                if(p_fin_item.m_title == "CZYNSZ"):
                        self.xx_dbg("processed[m_amount_out_jt_czynsz]")
                        l_fin_amounts.m_amount_out_jt_czynsz = p_fin_amounts.m_amount_out_jt_czynsz + ff

                if(p_fin_item.m_title == "MULTI"):
                        self.xx_dbg("processed[m_amount_out_jt_multi]")
                        l_fin_amounts.m_amount_out_jt_multi = p_fin_amounts.m_amount_out_jt_multi + ff

                if(p_fin_item.m_title == "MANDATY"):
                        self.xx_dbg("processed[m_amount_out_jt_multi]")
                        l_fin_amounts.m_amount_out_jt_mandate = p_fin_amounts.m_amount_out_jt_mandate + ff

                if(p_fin_item.m_title == "ALIM_G"):
                        self.xx_dbg("processed[m_amount_out_jt_alim_g]")
                        l_fin_amounts.m_amount_out_jt_alim_g = p_fin_amounts.m_amount_out_jt_alim_g + ff

                if(p_fin_item.m_title == "SPORT"):
                        self.xx_dbg("processed[m_amount_out_jt_sport]")
                        l_fin_amounts.m_amount_out_jt_sport = p_fin_amounts.m_amount_out_jt_sport + ff

                if(p_fin_item.m_title == "ALIM_J"):
                        self.xx_dbg("processed[m_amount_out_jt_alim_j]")
                        l_fin_amounts.m_amount_out_jt_alim_j = p_fin_amounts.m_amount_out_jt_alim_j + ff

                # self.xx_dbg("LKD_FinAnalysis::get_line::out::")

                return l_fin_amounts

        def print_amounts(self, p_fin_amounts):
                self.xx_dbg("")
                self.xx_dbg("")
                self.xx_dbg(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                self.xx_dbg("m_amount_out::" + str(p_fin_amounts.m_amount_out))
                self.xx_dbg("m_amount_in::" + str(p_fin_amounts.m_amount_in))
                self.xx_dbg("")
                self.xx_dbg("m_amount_out_jt::" + str(p_fin_amounts.m_amount_out_jt))
                self.xx_dbg("")
                self.xx_dbg("m_amount_out_jt_hipo::" + str(p_fin_amounts.m_amount_out_jt_hipo))
                self.xx_dbg("m_amount_out_jt_czynsz::" + str(p_fin_amounts.m_amount_out_jt_czynsz))
                self.xx_dbg("m_amount_out_jt_alim_g::" + str(p_fin_amounts.m_amount_out_jt_alim_g))
                self.xx_dbg("m_amount_out_jt_alim_j::" + str(p_fin_amounts.m_amount_out_jt_alim_j))
                self.xx_dbg("m_amount_out_jt_multi::" + str(p_fin_amounts.m_amount_out_jt_multi))                                
                self.xx_dbg("m_amount_out_jt_mandate::" + str(p_fin_amounts.m_amount_out_jt_mandate))                
                self.xx_dbg("m_amount_out_jt_sport::" + str(p_fin_amounts.m_amount_out_jt_sport))
                self.xx_dbg("")
                self.xx_dbg("m_amount_out_jt::" + str(p_fin_amounts.m_amount_out_jt)) 
                self.xx_dbg("m_amount_out_jt_sum::" + str(p_fin_amounts.m_amount_out_jt_sum))
                self.xx_dbg("m_amount_out_njt::" + str(p_fin_amounts.m_amount_out_njt))

                
                self.xx_dbg("m_amount_sum_0::" + str(p_fin_amounts.m_amount_sum_0))
                self.xx_dbg("m_amount_sum_1::" + str(p_fin_amounts.m_amount_sum_1))
                self.xx_dbg("m_amount_sum_2::" + str(p_fin_amounts.m_amount_sum_2))
                self.xx_dbg("m_amount_sum_3::" + str(p_fin_amounts.m_amount_sum_3))
                self.xx_dbg("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                self.xx_dbg("")
                self.xx_dbg("")

                
        def get_line(self, p_fin_item):

                # self.xx_dbg("LKD_FinAnalysis::get_line::in::")
                s_amnt = self.get_number(p_fin_item.m_amount)              
                s_tt = self.get_is_dop(p_fin_item.m_title)

                dd_out = ""
                dd_out = dd_out + ";" + self.get_stmt(p_fin_item.m_data) 
                dd_out = dd_out + ";" + self.get_stmt(s_tt) 
                dd_out = dd_out + ";" + self.get_stmt(s_amnt)
                # self.xx_dbg("LKD_FinAnalysis::get_line::out::")

                return dd_out

        def get_line_def(self, p_fin_item):

                # self.xx_dbg("LKD_FinAnalysis::get_line::in::")
                s_amnt = self.get_number(p_fin_item.m_amount)              
                s_tt = self.get_is_dop(p_fin_item.m_title)

                dd_out = ""
                dd_out = dd_out + "dd.append(self.get_item("
                dd_out = dd_out + "" + self.get_stmt(p_fin_item.m_data) 
                dd_out = dd_out + "," + self.get_stmt(p_fin_item.m_data) 
                dd_out = dd_out + "," + self.get_stmt(s_tt) 
                dd_out = dd_out + "," + self.get_stmt("") 
                dd_out = dd_out + "," + self.get_stmt("") 
                dd_out = dd_out + "," + self.get_stmt(s_amnt)
                dd_out = dd_out + "," + self.get_stmt("") 
                dd_out = dd_out + "," + self.get_stmt("") 
                dd_out = dd_out + "," + self.get_stmt("") 
                # dd_out = dd_out + "," + self.get_stmt("") 
                dd_out = dd_out + "))"
                # self.xx_dbg("LKD_FinAnalysis::get_line::out::")

                return dd_out

        def get_stmt(self,dd):
                dd_out = '"' + dd + '"'
                return dd_out

        def get_is_dop(self,dd):
                dd_out = dd
                if dd.find("DOP.") >=0 :
                        dd_out = "VISA"
                if dd.find("dot.karty 421352")>=0:
                        dd_out = "BANKOMAT-PROWIZJA"
                return dd_out

        def get_number(self,s_amount):
                s_amnt = s_amount.replace(" ",",")
                return s_amnt

        def get_float(self,s_amount):
                s_amount = s_amount.replace(" ",".")
                s_amount = s_amount.replace(",",".")
                f_amnt = float(s_amount)
                return f_amnt

        def get_data_2(self):
                self.xx_dbg("LKD_FinAnalysis::get_data_2::in::")

                dd = []
                
                dd.append(self.get_item("21-07-2020","21-07-2020","HIPO","","","-1000,00","","","JT"))
                dd.append(self.get_item("20-07-2020","20-07-2020","VISA","","","-2,00","","",""))
                dd.append(self.get_item("20-07-2020","20-07-2020","VISA","","","-5,88","","",""))
                dd.append(self.get_item("20-07-2020","20-07-2020","VISA","","","-11,35","","",""))
                dd.append(self.get_item("20-07-2020","20-07-2020","VISA","","","-115,14","","",""))
                dd.append(self.get_item("20-07-2020","20-07-2020","VISA","","","-30,00","","",""))
                dd.append(self.get_item("20-07-2020","20-07-2020","VISA","","","-5,00","","",""))
                dd.append(self.get_item("20-07-2020","20-07-2020","VISA","","","-2,99","","",""))
                dd.append(self.get_item("20-07-2020","20-07-2020","VISA","","","-3,30","","",""))

                dd.append(self.get_item("18-07-2020","18-07-2020","VISA","","","-2,00","","",""))
                dd.append(self.get_item("18-07-2020","18-07-2020","VISA","","","-19,48","","",""))
                dd.append(self.get_item("17-07-2020","17-07-2020","VISA","","","-5,49","","",""))
                dd.append(self.get_item("17-07-2020","17-07-2020","VISA","","","-109,28","","",""))
                dd.append(self.get_item("16-07-2020","16-07-2020","VISA","","","-21,79","","",""))
                dd.append(self.get_item("16-07-2020","16-07-2020","VISA","","","-0,60","","",""))
                dd.append(self.get_item("15-07-2020","15-07-2020","VISA","","","-0,46","","",""))
                dd.append(self.get_item("15-07-2020","15-07-2020","VISA","","","-16,30","","",""))
                dd.append(self.get_item("15-07-2020","15-07-2020","VISA","","","-45,34","","",""))
                dd.append(self.get_item("15-07-2020","15-07-2020","VISA","","","-13,99","","",""))
                dd.append(self.get_item("15-07-2020","15-07-2020","VISA","","","-19,90","","",""))
                dd.append(self.get_item("14-07-2020","14-07-2020","SPORT","","","-300,00","","","JT"))
                dd.append(self.get_item("14-07-2020","14-07-2020","VISA","","","-18,00","","",""))
                dd.append(self.get_item("14-07-2020","14-07-2020","VISA","","","-15,19","","",""))
                dd.append(self.get_item("14-07-2020","14-07-2020","VISA","","","-26,00","","",""))
                dd.append(self.get_item("14-07-2020","14-07-2020","VISA","","","-12,00","","",""))
                dd.append(self.get_item("13-07-2020","13-07-2020","MANDATY","","","-430,20","","","JT"))
                dd.append(self.get_item("13-07-2020","13-07-2020","VISA","","","-18,95","","",""))
                dd.append(self.get_item("13-07-2020","13-07-2020","VISA","","","-22,00","","",""))
                dd.append(self.get_item("13-07-2020","13-07-2020","VISA","","","-34,99","","",""))
                dd.append(self.get_item("13-07-2020","13-07-2020","VISA","","","-49,80","","",""))
                dd.append(self.get_item("13-07-2020","13-07-2020","MULTI","","","-150,00","","","JT"))
                dd.append(self.get_item("13-07-2020","13-07-2020","CZYNSZ","","","-950,00","","","JT"))
                dd.append(self.get_item("13-07-2020","13-07-2020","ALIM_J","","","-1100,00","","","JT"))
                dd.append(self.get_item("13-07-2020","13-07-2020","VISA","","","-64,89","","",""))
                dd.append(self.get_item("13-07-2020","13-07-2020","VISA","","","-29,91","","",""))
                dd.append(self.get_item("10-07-2020","10-07-2020","VISA","","","-6,50","","",""))
                dd.append(self.get_item("10-07-2020","10-07-2020","VISA","","","-3,00","","",""))
                dd.append(self.get_item("09-07-2020","09-07-2020","VISA","","","-32,00","","",""))
                dd.append(self.get_item("09-07-2020","09-07-2020","VISA","","","-29,50","","",""))
                dd.append(self.get_item("09-07-2020","09-07-2020","VISA","","","-6,50","","",""))
                dd.append(self.get_item("09-07-2020","09-07-2020","VISA","","","-25,75","","",""))
                dd.append(self.get_item("08-07-2020","08-07-2020","VISA","","","-3,50","","",""))
                dd.append(self.get_item("08-07-2020","08-07-2020","VISA","","","-5,00","","",""))
                dd.append(self.get_item("08-07-2020","08-07-2020","VISA","","","-7,60","","",""))
                dd.append(self.get_item("07-07-2020","07-07-2020","VISA","","","-21,49","","",""))
                dd.append(self.get_item("06-07-2020","06-07-2020","VISA","","","-28,00","","",""))
                dd.append(self.get_item("06-07-2020","06-07-2020","VISA","","","-6,00","","",""))
                dd.append(self.get_item("06-07-2020","06-07-2020","VISAA","","","-5,00","","",""))
                dd.append(self.get_item("06-07-2020","06-07-2020","VISA","","","-150,00","","",""))
                dd.append(self.get_item("06-07-2020","06-07-2020","VISA","","","-37,00","","",""))
                dd.append(self.get_item("06-07-2020","06-07-2020","VISA","","","-10,00","","",""))
                dd.append(self.get_item("06-07-2020","06-07-2020","VISA","","","-40,00","","",""))
                dd.append(self.get_item("06-07-2020","06-07-2020","VISA","","","-28,89","","",""))
                dd.append(self.get_item("04-07-2020","04-07-2020","VISA","","","-22,46","","",""))
                dd.append(self.get_item("03-07-2020","03-07-2020","VISA","","","-91,20","","",""))
                dd.append(self.get_item("02-07-2020","02-07-2020","VISA","","","-5,20","","",""))
                dd.append(self.get_item("02-07-2020","02-07-2020","VISA","","","-37,70","","",""))
                dd.append(self.get_item("01-07-2020","01-07-2020","VISA","","","-31,42","","",""))
                dd.append(self.get_item("01-07-2020","01-07-2020","VISA","","","-16,00","","",""))
                dd.append(self.get_item("01-07-2020","01-07-2020","VISA","","","-2,43","","",""))
                dd.append(self.get_item("30-06-2020","30-06-2020","VISA","","","-5,49","","",""))
                dd.append(self.get_item("29-06-2020","29-06-2020","VISA","","","-12,80","","",""))
                dd.append(self.get_item("29-06-2020","29-06-2020","VISA","","","-2,98","","",""))
                dd.append(self.get_item("29-06-2020","29-06-2020","VISA","","","-22,34","","",""))
                dd.append(self.get_item("29-06-2020","29-06-2020","VISA","","","-33,78","","",""))
                dd.append(self.get_item("29-06-2020","29-06-2020","VISA","","","-18,28","","",""))
                dd.append(self.get_item("27-06-2020","27-06-2020","VISA","","","-25,07","","",""))
                dd.append(self.get_item("25-06-2020","25-06-2020","ALIM_G","","","-1000,00","","","JT"))
                dd.append(self.get_item("25-06-2020","25-06-2020","VISA","","","-1,98","","",""))
                dd.append(self.get_item("25-06-2020","25-06-2020","VISA","","","-20,00","","",""))
                dd.append(self.get_item("25-06-2020","25-06-2020","VISA_PROV","","","-5,00","","",""))
                dd.append(self.get_item("25-06-2020","25-06-2020","VISA","","","-50,00","","",""))
                dd.append(self.get_item("24-06-2020","24-06-2020","PENSJA","","","10623,58","","","JTIN"))
                dd.append(self.get_item("23-06-2020","23-06-2020","VISA","","","-36,00","","",""))
                dd.append(self.get_item("23-06-2020","23-06-2020","VISA_PROV","","","-5,00","","",""))
                dd.append(self.get_item("23-06-2020","23-06-2020","VISA","","","-150,00","","",""))
                dd.append(self.get_item("22-06-2020","22-06-2020","HIPO","","","-1000,00","","","JT"))
                dd.append(self.get_item("22-06-2020","22-06-2020","VISA","","","-10,00","","",""))
                dd.append(self.get_item("22-06-2020","22-06-2020","MULTI","","","-150,00","","","JT"))
                dd.append(self.get_item("22-06-2020","22-06-2020","VISA","","","-28,38","","",""))
                dd.append(self.get_item("22-06-2020","22-06-2020","CZYNSZ","","","-850,00","","","JT"))
                dd.append(self.get_item("22-06-2020","22-06-2020","VISA","","","-73,55","","",""))
                dd.append(self.get_item("22-06-2020","22-06-2020","VISA","","","-2,39","","",""))
                dd.append(self.get_item("22-06-2020","22-06-2020","VISA","","","-9,98","","",""))
                dd.append(self.get_item("22-06-2020","22-06-2020","VISA","","","-19,47","","",""))
                dd.append(self.get_item("22-06-2020","22-06-2020","VISA","","","-4,50","","",""))
                dd.append(self.get_item("22-06-2020","22-06-2020","VISA","","","-33,72","","",""))
                dd.append(self.get_item("22-06-2020","22-06-2020","VISA","","","-7,70","","",""))
                dd.append(self.get_item("22-06-2020","22-06-2020","VISA","","","-45,31","","",""))
                dd.append(self.get_item("18-06-2020","18-06-2020","VISA","","","-38,80","","",""))
                dd.append(self.get_item("18-06-2020","18-06-2020","VISA","","","-20,00","","",""))
                self.xx_dbg("LKD_FinAnalysis::get_data_2::out::")
                return dd

        def get_data_1(self):
                self.xx_dbg("LKD_FinAnalysis::copy_files::in::")

                dd = []

                # dd.append(self.get_item("2020-07-18","16-06-2020","'73 1090 2590 0000 0001 3616 3985","JACEK J TRACZ UL. NISKA 1F/41 81-646 GDYNIA","PLN","6950 27","9762 63","82",""))

                dd.append(self.get_item("2020-07-21","01-07-2020","'73 1090 2590 0000 0001 3616 3985","JACEK J TRACZ UL. NISKA 1F/41 81-646 GDYNIA","PLN","","","55",""))
                dd.append(self.get_item("21-07-2020","21-07-2020","Przelew na spłate kredytu hipotecznego za Pionierow 1/14 częśc p. Jacka Tracza","JOANNA TRACZ","68 1500 1881 1018 8035 6958 0000","-1000 00","","1",""))
                dd.append(self.get_item("20-07-2020","18-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 2.00 PLN ENERGY PROFIT GDYNIA","","","-2 00","","2",""))
                dd.append(self.get_item("20-07-2020","18-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 5.88 PLN ROSSMANN 19 GDYNIA","","","-5 88","","3",""))
                dd.append(self.get_item("20-07-2020","18-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 11.35 PLN GZIK IWONA GAWLIKOWSKA GDYNIA","","","-11 35","","4",""))
                dd.append(self.get_item("20-07-2020","18-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 115.14 PLN SUPERMARKET SAM 34 Gdynia","","","-115 14","","5",""))
                dd.append(self.get_item("20-07-2020","17-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 30.00 PLN ZABKA Z6542 K.1 GDYNIA","","","-30 00","","6",""))
                dd.append(self.get_item("20-07-2020","17-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 5.00 PLN ZABKA Z6542 K.1 GDYNIA","","","-5 00","","7",""))
                dd.append(self.get_item("20-07-2020","17-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 2.99 PLN SUPER-PHARM GDYNIA WZGO GDYNIA","","","-2 99","","8",""))
                dd.append(self.get_item("20-07-2020","17-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 3.30 PLN SPP GDYNIA GDYNIA","","","-3 30","","9",""))
                dd.append(self.get_item("18-07-2020","16-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 2.00 PLN ENERGY PROFIT GDYNIA","","","-2 00","9762 63","1",""))
                dd.append(self.get_item("18-07-2020","16-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 19.48 PLN ZABKA Z6542 K.1 GDYNIA","","","-19 48","9764 63","2",""))
                dd.append(self.get_item("17-07-2020","15-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 5.49 PLN ZABKA Z6465 K.1 GDYNIA","","","-5 49","9784 11","3",""))
                dd.append(self.get_item("17-07-2020","15-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 109.28 PLN SUPERMARKET SAM 34 Gdynia","","","-109 28","9789 60","4",""))
                dd.append(self.get_item("16-07-2020","14-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 21.79 PLN ZABKA Z6542 K.1 GDYNIA","","","-21 79","9898 88","5",""))
                dd.append(self.get_item("16-07-2020","14-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 0.60 PLN TRUSKAWKA GDYNIA","","","-0 60","9920 67","6",""))
                dd.append(self.get_item("15-07-2020","15-07-2020","PROWIZJA ZA PRZEWALUTOW. 2 8% dot.karty 421352******9656 GITHUB HTTPSGITHUB.C","","","-0 46","9921 27","7",""))
                dd.append(self.get_item("15-07-2020","13-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 4.00 USD 1 USD=4.0748 PLN GITHUB HTTPSGITHUB.C","","","-16 30","9921 73","8",""))
                dd.append(self.get_item("15-07-2020","13-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 45.34 PLN SUPERMARKET SAM 34 Gdynia","","","-45 34","9938 03","9",""))
                dd.append(self.get_item("15-07-2020","13-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 13.99 PLN GZIK IWONA GAWLIKOWSKA GDYNIA","","","-13 99","9983 37","10",""))
                dd.append(self.get_item("15-07-2020","13-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 19.90 PLN ZOODELIKATESY GDYNIA","","","-19 90","9997 36","11",""))
                dd.append(self.get_item("14-07-2020","14-07-2020","Zgłoszenie załogi na Mistrzostwa Polski klasy Puck 2020 w składzie Jacek Tracz - sternik  Michał Tracz  Aneta Senejko","PSKP","66 8348 0003 0000 0009 2614 0001","-300 00","10017 26","12",""))
                dd.append(self.get_item("14-07-2020","12-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 18.00 PLN SOPOT MOLO-VISA FASTLA SOPOT","","","-18 00","10317 26","13",""))
                dd.append(self.get_item("14-07-2020","12-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 15.19 PLN GZIK IWONA GAWLIKOWSKA GDYNIA","","","-15 19","10335 26","14",""))
                dd.append(self.get_item("14-07-2020","12-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 26.00 PLN MERIDIAN MOLO SOPOT","","","-26 00","10350 45","15",""))
                dd.append(self.get_item("14-07-2020","11-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 12.00 PLN CONTRAST CAFE Gdynia","","","-12 00","10376 45","16",""))
                dd.append(self.get_item("13-07-2020","13-07-2020","CAŁ 2208-SEE.711.21233397.2020.1.T NIP7411703712PESEL72090709219","PIERWSZY URZĄD SKARBOWY GDYNIA UL. WŁADYSŁAWA IV 2/4 81-353 GDYNIA","72 1010 1140 0143 7113 9120 0000","-430 20","10388 45","17",""))
                dd.append(self.get_item("13-07-2020","11-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 18.95 PLN Berlin Doner Kebap Gdynia","","","-18 95","10818 65","18",""))
                dd.append(self.get_item("13-07-2020","11-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 22.00 PLN TRUSKAWKA GDYNIA","","","-22 00","10837 60","19",""))
                dd.append(self.get_item("13-07-2020","11-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 34.99 PLN EURO-NET SP. Z O.O. GDYNIA","","","-34 99","10859 60","20",""))
                dd.append(self.get_item("13-07-2020","11-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 49.80 PLN HALLOO GDYNIA","","","-49 80","10894 59","21",""))
                dd.append(self.get_item("13-07-2020","11-07-2020","Platnosc Jacek Tracz 81-645 Gdynia Pionierow 1/14","Multimedia Polska","67 1750 1312 7040 0000 6339 9087","-150 00","10944 39","22",""))
                dd.append(self.get_item("13-07-2020","11-07-2020","Oplata za czynsz Jacek Tracz 81-645 Gdynia Pionierow 1/14","SM BAłtyk","91 1160 2244 8871 0001 1005 6188","-950 00","11094 39","23",""))
                dd.append(self.get_item("13-07-2020","11-07-2020","Przelew Alimenty na mojego syna Jana Tracza","Joanna Tracz","63 1240 3510 1111 0010 1222 1061","-1100 00","12044 39","24",""))
                dd.append(self.get_item("13-07-2020","09-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 64.89 PLN LOTOS SF344 K.1 GDANSK","","","-64 89","13144 39","25",""))
                dd.append(self.get_item("13-07-2020","09-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 29.91 PLN LOTOS SF344 K.2 GDANSK","","","-29 91","13209 28","26",""))
                dd.append(self.get_item("10-07-2020","08-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 6.50 PLN GZIK IWONA GAWLIKOWSKA GDYNIA","","","-6 50","13239 19","27",""))
                dd.append(self.get_item("10-07-2020","09-07-2020","Opłata miesięczna za kartę od 01.06.2020 do 30.06.2020 dot.karty 421352******9656","","","-3 00","13245 69","28",""))
                dd.append(self.get_item("09-07-2020","07-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 32.00 PLN Bar Letni Gruba R63821 Gdynia","","","-32 00","13248 69","29",""))
                dd.append(self.get_item("09-07-2020","07-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 29.50 PLN BAR STERNIK 80687 Gdynia","","","-29 50","13280 69","30",""))
                dd.append(self.get_item("09-07-2020","07-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 6.50 PLN Bar Sternik 34218 Gdynia","","","-6 50","13310 19","31",""))
                dd.append(self.get_item("09-07-2020","07-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 25.75 PLN GZIK IWONA GAWLIKOWSKA GDYNIA","","","-25 75","13316 69","32",""))
                dd.append(self.get_item("08-07-2020","06-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 3.50 PLN Drobiarz s.c. 27075 Gdansk","","","-3 50","13342 44","33",""))
                dd.append(self.get_item("08-07-2020","06-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 5.00 PLN GZIK IWONA GAWLIKOWSKA GDYNIA","","","-5 00","13345 94","34",""))
                dd.append(self.get_item("08-07-2020","06-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 7.60 PLN Relay 53324 Gdynia","","","-7 60","13350 94","35",""))
                dd.append(self.get_item("07-07-2020","05-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 21.49 PLN GZIK IWONA GAWLIKOWSKA GDYNIA","","","-21 49","13358 54","36",""))
                dd.append(self.get_item("06-07-2020","04-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 28.00 PLN NIE/MIESNY FOOD TRUCK Gdansk","","","-28 00","13380 03","37",""))
                dd.append(self.get_item("06-07-2020","04-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 6.00 PLN PKP SKM 56128 GDYNIA","","","-6 00","13408 03","38",""))
                dd.append(self.get_item("06-07-2020","06-07-2020","Za wypłatę gotówki z bankomatu dot.karty 421352******9656 ul. Sloneczna 2 Gdynia","","","-5 00","13414 03","39",""))
                dd.append(self.get_item("06-07-2020","04-07-2020","DOP. VISA 421352******9656 WYPŁATA Z BANKOMATU KARTĄ 150.00 PLN ul. Sloneczna 2 Gdynia","","","-150 00","13419 03","40",""))
                dd.append(self.get_item("06-07-2020","04-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 37.00 PLN KLUB B90 GDANSK","","","-37 00","13569 03","41",""))
                dd.append(self.get_item("06-07-2020","04-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 10.00 PLN KLUB B90 GDANSK","","","-10 00","13606 03","42",""))
                dd.append(self.get_item("06-07-2020","04-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 40.00 PLN KLUB B90 GDANSK","","","-40 00","13616 03","43",""))
                dd.append(self.get_item("06-07-2020","03-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 28.89 PLN CUKIERNIA GRZES GDYNIA","","","-28 89","13656 03","44",""))
                dd.append(self.get_item("04-07-2020","02-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 22.46 PLN ZABKA Z4242 K.1 GDYNIA","","","-22 46","13684 92","45",""))
                dd.append(self.get_item("03-07-2020","01-07-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 91.20 PLN SUPERMARKET SAM 34 Gdynia","","","-91 20","13707 38","46",""))
                dd.append(self.get_item("02-07-2020","30-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 5.20 PLN GZIK IWONA GAWLIKOWSKA GDYNIA","","","-5 20","13798 58","47",""))
                dd.append(self.get_item("02-07-2020","30-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 37.70 PLN ZOODELIKATESY GDYNIA","","","-37 70","13803 78","48",""))
                dd.append(self.get_item("01-07-2020","29-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 31.42 PLN GZIK IWONA GAWLIKOWSKA GDYNIA","","","-31 42","13841 48","49",""))
                dd.append(self.get_item("01-07-2020","29-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 16.00 PLN GZIK IWONA GAWLIKOWSKA GDYNIA","","","-16 00","13872 90","50",""))
                dd.append(self.get_item("01-07-2020","29-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 2.43 PLN MAJCHRZAK - WARZYWA OWOCE GDYNIA","","","-2 43","13888 90","51",""))
                dd.append(self.get_item("30-06-2020","28-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 5.49 PLN ZABKA Z4242 K.1 GDYNIA","","","-5 49","13891 33","52",""))
                dd.append(self.get_item("29-06-2020","27-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 12.80 PLN SKLEP SPOZYWCZY ALFA 5 GDYNIA","","","-12 80","13896 82","53",""))
                dd.append(self.get_item("29-06-2020","27-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 2.98 PLN SKLEP SPOZYWCZY ALFA 5 GDYNIA","","","-2 98","13909 62","54",""))
                dd.append(self.get_item("29-06-2020","27-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 22.34 PLN GZIK IWONA GAWLIKOWSKA GDYNIA","","","-22 34","13912 60","55",""))
                dd.append(self.get_item("29-06-2020","27-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 33.78 PLN GZIK IWONA GAWLIKOWSKA GDYNIA","","","-33 78","13934 94","56",""))
                dd.append(self.get_item("29-06-2020","26-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 18.28 PLN GZIK IWONA GAWLIKOWSKA GDYNIA","","","-18 28","13968 72","57",""))
                dd.append(self.get_item("27-06-2020","25-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 25.07 PLN SKLEP WARZYWA-OWOCE GDYNIA","","","-25 07","13987 00","58",""))
                dd.append(self.get_item("25-06-2020","25-06-2020","Alimenty dla mojej córki Małgorzaty Tracz za msc czerwiec 2020.","Małgorzata Tracz","31 1020 1853 0000 9502 0203 3926","-1000 00","14012 07","59",""))
                dd.append(self.get_item("25-06-2020","23-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 1.98 PLN JMP S.A. BIEDRONKA 1156 GDYNIA","","","-1 98","15012 07","60",""))
                dd.append(self.get_item("25-06-2020","23-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 20.00 PLN SLONY KARMEL 28232 Gdynia","","","-20 00","15014 05","61",""))
                dd.append(self.get_item("25-06-2020","25-06-2020","Za wypłatę gotówki z bankomatu dot.karty 421352******9656 ul. Sloneczna 2 Gdynia","","","-5 00","15034 05","62",""))
                dd.append(self.get_item("25-06-2020","23-06-2020","DOP. VISA 421352******9656 WYPŁATA Z BANKOMATU KARTĄ 50.00 PLN ul. Sloneczna 2 Gdynia","","","-50 00","15039 05","63",""))
                dd.append(self.get_item("24-06-2020","24-06-2020","Wynagrodzenie 06/2020","FINEOS POLSKA SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ UL.CYPRIANA KAMILA NORWIDA 2 80-280 GDAŃSK POMORSKIE","85 1090 1043 0000 0001 1106 8977","10623 58","15089 05","64",""))
                dd.append(self.get_item("23-06-2020","21-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 36.00 PLN PUB DONEGAL 01 Gdynia","","","-36 00","4465 47","65",""))
                dd.append(self.get_item("23-06-2020","23-06-2020","Za wypłatę gotówki z bankomatu dot.karty 421352******9656 ul. Wladyslawa IV 68 Gdynia","","","-5 00","4501 47","66",""))
                dd.append(self.get_item("23-06-2020","21-06-2020","DOP. VISA 421352******9656 WYPŁATA Z BANKOMATU KARTĄ 150.00 PLN ul. Wladyslawa IV 68 Gdynia","","","-150 00","4506 47","67",""))
                dd.append(self.get_item("22-06-2020","22-06-2020","Przelew na splate kredytu mieszkaniowego.","JOANNA TRACZ","68 1500 1881 1018 8035 6958 0000","-1000 00","4656 47","68",""))
                dd.append(self.get_item("22-06-2020","20-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 10.00 PLN F. MINGA GDYNIA","","","-10 00","5656 47","69",""))
                dd.append(self.get_item("22-06-2020","22-06-2020","Platnosc Jacek Tracz 81-645 Gdynia Pionierow 1/14","Multimedia Polska","67 1750 1312 7040 0000 6339 9087","-150 00","5666 47","70",""))
                dd.append(self.get_item("22-06-2020","20-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 28.38 PLN FRESHMARKET Z8036 K.1 GDYNIA","","","-28 38","5816 47","71",""))
                dd.append(self.get_item("22-06-2020","22-06-2020","Oplata za czynsz Jacek Tracz 81-645 Gdynia Pionierow 1/14","SM BALTYK","91 1160 2244 8871 0001 1005 6188","-850 00","5844 85","72",""))
                dd.append(self.get_item("22-06-2020","20-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 73.55 PLN SUPERMARKET SAM 34 Gdynia","","","-73 55","6694 85","73",""))
                dd.append(self.get_item("22-06-2020","20-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 2.39 PLN ROSSMANN 07 Gdynia","","","-2 39","6768 40","74",""))
                dd.append(self.get_item("22-06-2020","20-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 9.98 PLN PEPCO 956 GDYNIA","","","-9 98","6770 79","75",""))
                dd.append(self.get_item("22-06-2020","19-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 19.47 PLN ZABKA Z6542 K.1 GDYNIA","","","-19 47","6780 77","76",""))
                dd.append(self.get_item("22-06-2020","18-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 4.50 PLN SKLEP WARZYWA-OWOCE GDYNIA","","","-4 50","6800 24","77",""))
                dd.append(self.get_item("22-06-2020","18-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 33.72 PLN ZABKA Z4674 K.1 GDYNIA","","","-33 72","6804 74","78",""))
                dd.append(self.get_item("22-06-2020","18-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 7.70 PLN GZIK IWONA GAWLIKOWSKA GDYNIA","","","-7 70","6838 46","79",""))
                dd.append(self.get_item("22-06-2020","18-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 45.31 PLN STOKROTKA 627 GDYNIA","","","-45 31","6846 16","80",""))
                dd.append(self.get_item("18-06-2020","16-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 38.80 PLN GZIK IWONA GAWLIKOWSKA GDYNIA","","","-38 80","6891 47","81",""))
                dd.append(self.get_item("18-06-2020","16-06-2020","DOP. VISA 421352******9656 PŁATNOŚĆ KARTĄ 20.00 PLN GZIK IWONA GAWLIKOWSKA GDYNIA","","","-20 00","6930 27","82",""))
                return dd

# 58 858,85 PLN	286 451,59 PLN	-227 592,74 PLN	

        def get_items_sum(self):
                self.xx_dbg("LKD_FinAnalysis::get_items_sum::in::")
                dd = []
                dd.append(self.get_item_sum("24-07-2020", "5885 85", "286451 59", "0 0", "-227592 74"	))
                self.xx_dbg("LKD_FinAnalysis::get_items_sum::out::")
                return dd


        def get_item_sum(self
                        ,       p_data_1
                        ,       p_amount_0
                        ,       p_amount_1
                        ,       p_amount_2
                        ,       p_amount_3
                ):

                dd = LKD_FinAmounts()
                dd.m_data = p_data_1
                dd.m_amount_sum_0 = self.get_float( p_amount_0 )
                dd.m_amount_sum_1 = self.get_float( p_amount_1 )
                dd.m_amount_sum_2 = self.get_float( p_amount_2 )
                dd.m_amount_sum_3 = self.get_float( p_amount_3 )
                # self.xx_dbg("LKD_FinAnalysis::get_item::out::")
                return dd

        def get_item(self
                        ,       p_data_1
                        ,       p_data_2
                        ,       p_title
                        ,       p_1
                        ,       p_2
                        ,       p_amount
                        ,       p_account
                        ,       p_3
                        ,       p_type
                ):

                # self.xx_dbg("LKD_FinAnalysis::get_item::in::")
                dd = LKD_FinAmounts()
                dd.m_data = p_data_1
                dd.m_title = p_title
                dd.m_amount = p_amount
                dd.m_type = p_type
                # self.xx_dbg("LKD_FinAnalysis::get_item::out::")
                return dd


#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py
# 600 446 066 Rafal tel

if __name__ == "__main__":
        dd_fin = LKD_FinAnalysis("")
        dd_fin.print_data()
