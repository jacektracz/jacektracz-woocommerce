import sys
import os
import logging
import shutil

class LKD_FinItem:
        def __init__(self):
                self.m_title = ""
                self.m_data = ""
                self.m_amount = ""


        def xx_dbg(self, tt):
                "" ""
                print tt

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
                dd = self.get_data_1()
                for iData in dd:

                        s_amnt = self.get_number(iData.m_amount)              
                        s_tt = self.get_is_dop(iData.m_title)
                        self.xx_dbg(";" + self.get_stmt(iData.m_data) + ";" + self.get_stmt(s_tt) + ";" + self.get_stmt(s_amnt))

                        # self.xx_dbg("" + iData.m_amount)

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

        def get_data_1(self):
                self.xx_dbg("LKD_FinAnalysis::copy_files::in::")

                dd = []

                # dd.append(self.get_item("2020-07-18","16-06-2020","'73 1090 2590 0000 0001 3616 3985","JACEK J TRACZ UL. NISKA 1F/41 81-646 GDYNIA","PLN","6950 27","9762 63","82",""))

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

        def get_item(self
                ,p_data_1
                ,p_data_2
                ,p_title
                ,p_1
                ,p_2
                ,p_amount
                ,p_account
                ,p_3
                ,p_4
                ):

                        self.xx_dbg("LKD_FinAnalysis::get_item::in::")
                        dd = LKD_FinItem()
                        dd.m_data = p_data_1
                        dd.m_title = p_title
                        dd.m_amount = p_amount
                        self.xx_dbg("LKD_FinAnalysis::get_item::out::")
                        return dd

