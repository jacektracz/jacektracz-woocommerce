select * from service st  where market = 'SK';
select * from service st;
select * from service_translation st  where st.locale = 'sk';

select locale,name,description,description_short,info_box_price,name_synonyms,badge_label ,info_box_procedures ,info_box_price ,info_box_tips from service_translation st  where st.locale = 'sk';


select 'YY_START','YY_SEP',locale,'YY_SEP',name,'YY_SEP',description,'YY_SEP',description_short,'YY_SEP',info_box_price,'YY_SEP',name_synonyms,'YY_SEP',badge_label ,'YY_SEP',info_box_procedures ,'YY_SEP',info_box_price ,'YY_SEP',info_box_tips,'YY_END' from service_translation st  where st.locale = 'sk';



select 'YY_START','YY_SEP',locale,'YY_SEP',name,'YY_SEP',description,'YY_SEP',description_short,'YY_SEP',info_box_price,'YY_SEP',name_synonyms,'YY_SEP',badge_label ,'YY_SEP',info_box_procedures ,'YY_SEP',info_box_tips,'YY_SEP',info_box_price ,'YY_SEP',pk,'YY_SEP','YY_END' from service_translation st  where st.locale = 'sk';



select 'YY_START',"YY_SEP_S",locale,"YY_SEP",name,"YY_SEP",description,"YY_SEP",description_short,"YY_SEP",info_box_price,"YY_SEP",name_synonyms,"YY_SEP",badge_label ,"YY_SEP",info_box_procedures ,"YY_SEP",info_box_tips,"YY_SEP",info_box_price ,"YY_SEP",pk,"YY_SEP","YY_END" from service_translation st  where st.locale = 'sk';