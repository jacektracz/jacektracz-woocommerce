select locale,name,description,description_short
,info_box_price,name_synonyms,badge_label 
,info_box_procedures ,info_box_tips,info_box_price 
,pk from service_translation st  where st.locale = 'sk';


select 'YY_START','YY_SE','YY_SS',locale,'YY_SE','YY_SS',name,'YY_SE','YY_SS',description,'YY_SE','YY_SS',description_short,'YY_SE','YY_SS',info_box_price,'YY_SE','YY_SS',name_synonyms,'YY_SE','YY_SS',badge_label ,'YY_SE','YY_SS',info_box_procedures ,'YY_SE','YY_SS',info_box_tips,'YY_SE','YY_SS',info_box_price ,'YY_SE','YY_SS',pk,'YY_SE','YY_SS','YY_END' from service_translation st  where st.locale = 'sk';
