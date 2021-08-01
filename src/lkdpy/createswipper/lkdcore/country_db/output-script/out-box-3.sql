LKD_MainExec::__init__::in::
LKD_MainExec::__init__::out:
 
 
-- ID[id_s1:0][pk_s1:15][name_s1:Vymazanie chybovej hlášky vozidla][pk_prod_new:15][dbg_add:GENERATE-UPDATE-PROD-ITEM]
-- ID[id_s1:0][pk_s1:15][name_s1:Vymazanie chybovej hlášky vozidla][pk_prod_new:15][dbg_add:GENERATE-UPDATE-NEW-ITEM]

update service_translation set
   description_short = '<p>Chybov&eacute; k&oacute;dy obsahuj&uacute; inform&aacute;cie o nefunkčnej alebo chybnej s&uacute;časti vozidla, od brzdov&eacute;ho syst&eacute;mu po klimatiz&aacute;ciu až po motor. Chybov&eacute; k&oacute;dy uložen&eacute; v pam&auml;ti poč&iacute;tača vozidla uľahčuj&uacute; diagnostiku a poskytuj&uacute; inform&aacute;cie o poruch&aacute;ch. Chyby sa ru&scaron;ia pripojen&iacute;m poč&iacute;tača \/ testera k diagnostickej z&aacute;strčke vozidla, preč&iacute;tan&iacute;m k&oacute;dov a ich odstr&aacute;nen&iacute;m z pam&auml;te palubn&eacute;ho poč&iacute;tača.<\/p>'
,   info_box_procedures = '<ul><li>Pripojenie diagnostick&eacute;ho zariadenia k autu<\/li><li>Zapnutie zapaľovania alebo na&scaron;tartovanie motora<\/li><li>Č&iacute;tanie chybov&yacute;ch k&oacute;dov uložen&yacute;ch v pam&auml;ti poč&iacute;tača<\/li><li>Odstr&aacute;nenie chybov&yacute;ch k&oacute;dov pomocou diagnostick&eacute;ho programu alebo testera<\/li><\/ul>'
,   info_box_tips = '<ul><li>D&aacute;vajte pozor na v&yacute;stražn&eacute; svetl&aacute; na palubnej doske, ktor&eacute; po zapnut&iacute; motora nezhasn&uacute;<\/li><li>Neignorujte žiadne zn&aacute;mky poruchy<\/li><li>Ak budete pokračovať v jazde, bez toho aby ste dlh&scaron;iu dobu ru&scaron;ili chybov&eacute; k&oacute;dy, riskujete v&aacute;žne po&scaron;kodenie vozidla<\/li><\/ul>'
 where pk = 15
 and locale = 'sk';
 
 
-- ID[id_s1:0][pk_s1:2][name_s1:Systémy podpory brzdenia - ABS, BAS, EBD][pk_prod_new:2][dbg_add:GENERATE-UPDATE-PROD-ITEM]
-- ID[id_s1:0][pk_s1:2][name_s1:Podporné brzdové systémy - ABS, BAS, EBD][pk_prod_new:2][dbg_add:GENERATE-UPDATE-NEW-ITEM]

update service_translation set
  name = 'Podporné brzdové systémy - ABS, BAS, EBD'
,   info_box_procedures = '<ul><li>Pripojenie diagnostick&eacute;ho zariadenia k autu<\/li><li>Položenie vozidla na valčekov&yacute; tester<\/li><li>Niekoľkokr&aacute;t zabrzdiť<\/li><li>Overenie brzdn&eacute;ho protokolu<\/li><\/ul>'
,   info_box_tips = '<ul><li>Na v&scaron;etky koles&aacute; použ&iacute;vajte rovnak&eacute; pneumatiky (veľkosť, model, rok)<\/li><li>Nezanedb&aacute;vajte v&yacute;stražn&eacute; svetl&aacute; signalizuj&uacute;ci poruchu podporn&eacute;ho syst&eacute;mu<\/li><li>Každ&aacute; pravideln&aacute; kontrola by mala zahŕňať kontrolu nosn&eacute;ho syst&eacute;mu bŕzd<\/li><\/ul>'
 where pk = 2
 and locale = 'sk';
 
 
-- ID[id_s1:0][pk_s1:204][name_s1:Oprava elektronického systému][pk_prod_new:204][dbg_add:GENERATE-UPDATE-PROD-ITEM]
-- ID[id_s1:0][pk_s1:204][name_s1:Oprava elektronických systémov][pk_prod_new:204][dbg_add:GENERATE-UPDATE-NEW-ITEM]

update service_translation set
  name = 'Oprava elektronických systémov'
,   description_short = '<pre id="tw-target-text" class="tw-data-text tw-text-large XcVN5d tw-ta" dir="ltr" data-placeholder="Tłumaczenie"><span lang="sk">Elektronick&eacute; syst&eacute;my v automobiloch zohr&aacute;vaj&uacute; niekoľko &uacute;loh. S&uacute; zodpovedn&eacute; za najz&aacute;kladnej&scaron;ie funkcie, ako je rozsvietenie osvetlenie interi&eacute;ru, <\/span><\/pre><pre class="tw-data-text tw-text-large XcVN5d tw-ta" dir="ltr" data-placeholder="Tłumaczenie"><span lang="sk">osvetlenie kľučiek dver&iacute; a palubnej dosky, ovl&aacute;danie teploty interi&eacute;ru (hor&uacute;ci a chladn&yacute; vzduch), ovl&aacute;danie motora, podpora brzdov&yacute;ch a riadiacich <\/span><\/pre><pre class="tw-data-text tw-text-large XcVN5d tw-ta" dir="ltr" data-placeholder="Tłumaczenie"><span lang="sk">syst&eacute;mov. Spolupracuj&uacute; s mnoh&yacute;mi senzormi a použ&iacute;vaj&uacute; riadiace moduly, ktor&eacute; navz&aacute;jom spolupracuj&uacute;. Porucha alebo nespr&aacute;vna funkcia jedn&eacute;ho <\/span><\/pre><pre class="tw-data-text tw-text-large XcVN5d tw-ta" dir="ltr" data-placeholder="Tłumaczenie"><span lang="sk">prvku ovplyvn&iacute; činnosť cel&eacute;ho elektronick&eacute;ho syst&eacute;mu. U v&auml;č&scaron;iny modern&yacute;ch automobilov je porucha elektronick&eacute;ho syst&eacute;mu signalizovan&aacute; <\/span><\/pre><pre class="tw-data-text tw-text-large XcVN5d tw-ta" dir="ltr" data-placeholder="Tłumaczenie"><span lang="sk">kontrolkou na palubnej doske.<\/span><\/pre>'
,   info_box_procedures = '<ul><li id="tw-target-text" class="tw-data-text tw-text-large XcVN5d tw-ta" dir="ltr" data-placeholder="Tłumaczenie"><span lang="sk">Identifik&aacute;cia chybn&eacute;ho prvku pomocou diagnostick&eacute;ho zariadenia <\/span><\/li><li class="tw-data-text tw-text-large XcVN5d tw-ta" dir="ltr" data-placeholder="Tłumaczenie"><span lang="sk">V&yacute;mena chybn&eacute;ho prvku za nov&yacute; <\/span><\/li><li class="tw-data-text tw-text-large XcVN5d tw-ta" dir="ltr" data-placeholder="Tłumaczenie"><span lang="sk">Kontrola syst&eacute;mu, aby sa zabezpečilo jeho spr&aacute;vne fungovanie<\/span><\/li><\/ul>'
,   info_box_tips = '<ul><li id="tw-target-text" class="tw-data-text tw-text-large XcVN5d tw-ta" dir="ltr" data-placeholder="Tłumaczenie"><span lang="sk">Nechajte svoje elektronick&eacute; syst&eacute;my opraviť, akon&aacute;hle si v&scaron;imnete ich zlyhanie <\/span><\/li><li class="tw-data-text tw-text-large XcVN5d tw-ta" dir="ltr" data-placeholder="Tłumaczenie"><span lang="sk">Takmer v&scaron;etky prvky riadiacich syst&eacute;mov nie s&uacute; opraviteľn&eacute; a musia byť nahraden&eacute; nov&yacute;mi <\/span><\/li><li class="tw-data-text tw-text-large XcVN5d tw-ta" dir="ltr" data-placeholder="Tłumaczenie"><span lang="sk">Nechajte opraviť elektronick&eacute; syst&eacute;my v&aacute;&scaron;ho vozidla profesion&aacute;lmi - maj&uacute; k dispoz&iacute;cii pr&iacute;slu&scaron;n&eacute; diagnostick&eacute; n&aacute;stroje, ktor&eacute; t&uacute;to &uacute;lohu zvl&aacute;dnu<\/span><\/li><\/ul>'
 where pk = 204
 and locale = 'sk';
 
 
-- ID[id_s1:0][pk_s1:230][name_s1:Počítačová diagnostika][pk_prod_new:230][dbg_add:GENERATE-UPDATE-PROD-ITEM]
-- ID[id_s1:0][pk_s1:230][name_s1:Diagnostika počítača][pk_prod_new:230][dbg_add:GENERATE-UPDATE-NEW-ITEM]

update service_translation set
  name = 'Diagnostika počítača'
,   description_short = '<p>Diagnostika poč&iacute;tača v aute spoč&iacute;va v pripojen&iacute; &scaron;peci&aacute;lneho diagnostick&eacute;ho poč&iacute;tača (označovan&eacute;ho aj ako diagnostick&yacute; tester) k palubn&eacute;mu poč&iacute;taču v aute. T&aacute;to služba umožňuje skontrolovať celkov&yacute; technick&yacute; stav automobilu, vr&aacute;tane kontroly jeho parametrov proti požadovan&yacute;m, a identifik&aacute;ciu pr&iacute;čin a lokaliz&aacute;cia pr&iacute;padn&yacute;ch por&uacute;ch, aby ich bolo možn&eacute; r&yacute;chlo odstr&aacute;niť.<\/p>'
,   info_box_procedures = '<ul><li>Pripojenie diagnostick&eacute;ho testera<\/li><li>Č&iacute;tanie chybov&yacute;ch k&oacute;dov<\/li><li>De&scaron;ifrovanie chybov&yacute;ch k&oacute;dov<\/li><li>Aktu&aacute;lne v&yacute;tlačok z diagnostick&eacute;ho testera<\/li><li>Koment&aacute;re k v&yacute;sledkom diagnostick&yacute;ch testov<\/li><\/ul>'
,   info_box_tips = '<ul><li>Včasn&eacute; odhalenie poruchy znižuje n&aacute;klady na opravu<\/li><li>Kontrolka "Skontrolovať motor" nemus&iacute; nutne znamenať, že va&scaron;e vozidlo vyžaduje z&aacute;sadn&eacute; opravu. V tomto pr&iacute;pade je kľ&uacute;čov&aacute; r&yacute;chla a spr&aacute;vna diagn&oacute;za.<\/li><li>Pri každej gener&aacute;lnej oprave nechajte svoj poč&iacute;tač diagnostikovať a vždy si vyžiadajte pr&iacute;slu&scaron;n&yacute; v&yacute;tlačok testera<\/li><li>Každ&yacute; kupuj&uacute;ci je povinn&yacute; nechať si diagnostikovať auto pred zak&uacute;pen&iacute;m.<\/li><li>Vždy nechajte svoje auto diagnostikovať odborn&iacute;kmi, pretože s&uacute; jedin&iacute;, ktor&iacute; s&uacute; schopn&iacute; spr&aacute;vne identifikovať pr&iacute;činu poruchy na z&aacute;klade &uacute;dajov z&iacute;skan&yacute;ch z poč&iacute;tača<\/li><\/ul>'
 where pk = 230
 and locale = 'sk';
 
 
-- ID[id_s1:0][pk_s1:21][name_s1:Výmena brzdových doštičiek (predné)][pk_prod_new:21][dbg_add:GENERATE-UPDATE-PROD-ITEM]
-- ID[id_s1:0][pk_s1:21][name_s1:Výmena brzdových doštičiek (predné)][pk_prod_new:21][dbg_add:GENERATE-UPDATE-NEW-ITEM]

update service_translation set
   description = '<p>Udržiavanie dobr&eacute;ho stavu bŕzd zvy&scaron;uje bezpečnosť v&aacute;&scaron;ho vozidla. Kvalitnej&scaron;ie diely pravidelne vymieňan&eacute; v profesion&aacute;lnych gar&aacute;žach zaisťuj&uacute; krat&scaron;iu brzdn&uacute; dr&aacute;hu.<\/p><p>Brzdov&eacute; do&scaron;tičky, z&aacute;kladn&aacute; s&uacute;časť brzdov&eacute;ho syst&eacute;mu, si vyžaduj&uacute; osobitn&uacute; pozornosť vodiča. Ich v&scaron;eobecn&eacute; podmienky, nielen ich opotrebenie, ale aj trvanlivosť materi&aacute;lu, z ktor&eacute;ho s&uacute; vyroben&eacute;, maj&uacute; priamy vplyv na va&scaron;e pohodlie pri riaden&iacute; a pokoj. Riadenie automobilu vybaven&eacute;ho star&yacute;mi alebo chybn&yacute;mi brzdov&yacute;mi do&scaron;tičkami je dr&aacute;ždiv&eacute;, hlučn&eacute;, ale čo je najd&ocirc;ležitej&scaron;ie, nebezpečn&eacute;.<\/p>'
,   description_short = '<p>Brzdov&eacute; do&scaron;tičky tvor&iacute; jeden zo z&aacute;kladn&yacute;ch prvkov brzdov&eacute;ho syst&eacute;mu. Patr&iacute; k t&yacute;m niekoľk&yacute;m prvkom, ktor&yacute;ch opotrebenie m&ocirc;žete zistiť jednoducho odstr&aacute;nen&iacute;m kolies. Ak sa brzdov&eacute; do&scaron;tičky hrub&eacute; menej ako 3 mm, určite ich vymeňte za nov&eacute;. Pod&scaron;&iacute;vka pokr&yacute;vaj&uacute;ci podložky obsahuje charakteristick&uacute; dr&aacute;žku viditeľnou po demont&aacute;ži k&ocirc;l. Ak je dr&aacute;žka sotva viditeľn&aacute; alebo v&ocirc;bec neviditeľn&aacute;, znamen&aacute; to, že je nutn&eacute; vymeniť podložky. Vyžaduj&uacute; v&yacute;menu tiež v pr&iacute;pade, že obloženie vykazuje nerovnomern&eacute; opotrebovanie, ktor&eacute; m&ocirc;že ovplyvniť brzdenia. Opotrebovan&eacute; brzdov&eacute; do&scaron;tičky sp&ocirc;sobuj&uacute; r&yacute;chlej&scaron;ie opotrebovanie brzdov&yacute;ch kot&uacute;čov.<\/p>'
,   info_box_procedures = '<ul><li>Demont&aacute;ž kolies<\/li><li>Demont&aacute;ž brzdov&yacute;ch do&scaron;tičiek<\/li><li>Mont&aacute;ž nov&yacute;ch brzdov&yacute;ch do&scaron;tičiek<\/li><li>Odvzdu&scaron;nenie brzdov&eacute;ho syst&eacute;mu<\/li><li>Sp&auml;tn&aacute; mont&aacute;ž kolies<\/li><li>Kontrola stavu brzdovej kvapaliny<\/li><\/ul>'
,   info_box_tips = '<ul><li>Nikdy ne&scaron;etrite peniazmi na brzdov&yacute;ch do&scaron;tičk&aacute;ch - tie lep&scaron;ie m&ocirc;žu byť drah&scaron;ie, ale s&uacute; tiež bezpečnej&scaron;ie.<\/li><li>Po v&yacute;mene brzdov&yacute;ch do&scaron;tičiek sa prv&yacute;ch niekoľko sto kilometrov vyvarujte n&aacute;hleho brzdenia. Nechajte ich usadiť sa do strmeňa.<\/li><li>N&aacute;kupom značkov&yacute;ch brzdov&yacute;ch do&scaron;tičiek m&ocirc;žete zdvojn&aacute;sobiť životnosť diskov.<\/li><li>Pri n&aacute;kupe brzdov&yacute;ch do&scaron;tičiek sa uistite, že s&uacute; vybaven&eacute; sn&iacute;mačom opotrebovania, ktor&yacute; je v nov&yacute;ch, drah&scaron;&iacute;ch automobiloch &scaron;tandardom.<\/li><li>Skontrolujte si občas brzdov&eacute; do&scaron;tičky - m&ocirc;žete to urobiť napr. Pri v&yacute;mene pneumat&iacute;k<\/li><\/ul>'
 where pk = 21
 and locale = 'sk';
 
 
-- ID[id_s1:0][pk_s1:22][name_s1:Výmena brzdových doštičiek (zadné)][pk_prod_new:22][dbg_add:GENERATE-UPDATE-PROD-ITEM]
-- ID[id_s1:0][pk_s1:22][name_s1:Výmena brzdových doštičiek (zadné)][pk_prod_new:22][dbg_add:GENERATE-UPDATE-NEW-ITEM]

update service_translation set
   description_short = '<p>Brzdov&eacute; do&scaron;tičky tvor&iacute; jeden zo z&aacute;kladn&yacute;ch prvkov brzdov&eacute;ho syst&eacute;mu. Patr&iacute; k t&yacute;m niekoľk&yacute;m prvkom, ktor&yacute;ch opotrebenie m&ocirc;žete zistiť jednoducho odstr&aacute;nen&iacute;m kolies. Ak sa brzdov&eacute; do&scaron;tičky hrub&eacute; menej ako 3 mm, určite ich vymeňte za nov&eacute;. Pod&scaron;&iacute;vka pokr&yacute;vaj&uacute;ci podložky obsahuje charakteristick&uacute; dr&aacute;žku viditeľnou po demont&aacute;ži k&ocirc;l. Ak je dr&aacute;žka sotva viditeľn&aacute; alebo v&ocirc;bec neviditeľn&aacute;, znamen&aacute; to, že je nutn&eacute; vymeniť podložky. Vyžaduj&uacute; v&yacute;menu tiež v pr&iacute;pade, že obloženie vykazuje nerovnomern&eacute; opotrebovanie, ktor&eacute; m&ocirc;že ovplyvniť brzdenia. Opotrebovan&eacute; brzdov&eacute; do&scaron;tičky sp&ocirc;sobuj&uacute; r&yacute;chlej&scaron;ie opotrebovanie brzdov&yacute;ch kot&uacute;čov.<\/p>'
,   info_box_procedures = '<ul><li>Demont&aacute;ž kolies<\/li><li>Demont&aacute;ž brzdov&yacute;ch do&scaron;tičiek<\/li><li>Mont&aacute;ž nov&yacute;ch brzdov&yacute;ch do&scaron;tičiek<\/li><li>Odvzdu&scaron;nenie brzdov&eacute;ho syst&eacute;mu<\/li><li>Sp&auml;tn&aacute; mont&aacute;ž kolies<\/li><li>Kontrola stavu brzdovej kvapaliny<\/li><\/ul>'
,   info_box_tips = '<ul><li>Nikdy ne&scaron;etrite peniazmi na brzdov&yacute;ch do&scaron;tičk&aacute;ch - tie lep&scaron;ie m&ocirc;žu byť drah&scaron;ie, ale s&uacute; tiež bezpečnej&scaron;ie.<\/li><li>Po v&yacute;mene brzdov&yacute;ch do&scaron;tičiek sa prv&yacute;ch niekoľko sto kilometrov vyvarujte n&aacute;hleho brzdenia. Nechajte ich usadiť sa vo strmeňa.<\/li><li>N&aacute;kupom značkov&yacute;ch brzdov&yacute;ch do&scaron;tičiek m&ocirc;žete zdvojn&aacute;sobiť životnosť diskov.<\/li><li>Pri n&aacute;kupe brzdov&yacute;ch do&scaron;tičiek sa uistite, že s&uacute; vybaven&eacute; sn&iacute;mačom opotrebovania, ktor&yacute; je v nov&yacute;ch, drah&scaron;&iacute;ch automobiloch &scaron;tandardom.<\/li><li>Skontrolujte si občas brzdov&eacute; do&scaron;tičky - m&ocirc;žete to urobiť napr. Pri v&yacute;mene pneumat&iacute;k<\/li><\/ul>'
 where pk = 22
 and locale = 'sk';
 
 
-- ID[id_s1:0][pk_s1:23][name_s1:Výmena brzdovej doštičky][pk_prod_new:23][dbg_add:GENERATE-UPDATE-PROD-ITEM]
-- ID[id_s1:0][pk_s1:23][name_s1:Výmena brzdovej doštičky][pk_prod_new:23][dbg_add:GENERATE-UPDATE-NEW-ITEM]

update service_translation set
   description_short = '<p>Brzdov&eacute; do&scaron;tičky tvor&iacute; jeden zo z&aacute;kladn&yacute;ch prvkov brzdov&eacute;ho syst&eacute;mu. Patr&iacute; k t&yacute;m niekoľk&yacute;m prvkom, ktor&yacute;ch opotrebenie m&ocirc;žete zistiť jednoducho odstr&aacute;nen&iacute;m kolies. Ak sa brzdov&eacute; do&scaron;tičky hrub&eacute; menej ako 3 mm, určite ich vymeňte za nov&eacute;. Pod&scaron;&iacute;vka pokr&yacute;vaj&uacute;ci podložky obsahuje charakteristick&uacute; dr&aacute;žku viditeľnou po demont&aacute;ži k&ocirc;l. Ak je dr&aacute;žka sotva viditeľn&aacute; alebo v&ocirc;bec neviditeľn&aacute;, znamen&aacute; to, že je nutn&eacute; vymeniť podložky. Vyžaduj&uacute; v&yacute;menu tiež v pr&iacute;pade, že obloženie vykazuje nerovnomern&eacute; opotrebovanie, ktor&eacute; m&ocirc;že ovplyvniť brzdenia. Opotrebovan&eacute; brzdov&eacute; do&scaron;tičky sp&ocirc;sobuj&uacute; r&yacute;chlej&scaron;ie opotrebovanie brzdov&yacute;ch kot&uacute;čov.<\/p>'
,   info_box_procedures = '<ul><li>Demont&aacute;ž kolies<\/li><li>Demont&aacute;ž brzdov&yacute;ch do&scaron;tičiek<\/li><li>Mont&aacute;ž nov&yacute;ch brzdov&yacute;ch do&scaron;tičiek<\/li><li>Odvzdu&scaron;nenie brzdov&eacute;ho syst&eacute;mu<\/li><li>Sp&auml;tn&aacute; mont&aacute;ž kolies<\/li><li>Kontrola stavu brzdovej kvapaliny<\/li><\/ul>'
,   info_box_tips = '<ul><li>Nikdy ne&scaron;etrite peniazmi na brzdov&yacute;ch do&scaron;tičk&aacute;ch - tie lep&scaron;ie m&ocirc;žu byť drah&scaron;ie, ale s&uacute; tiež bezpečnej&scaron;ie.<\/li><li>Po v&yacute;mene brzdov&yacute;ch do&scaron;tičiek sa prv&yacute;ch niekoľko sto kilometrov vyvarujte n&aacute;hleho brzdenia. Nechajte ich usadiť sa vo strmeňa.<\/li><li>N&aacute;kupom značkov&yacute;ch brzdov&yacute;ch do&scaron;tičiek m&ocirc;žete zdvojn&aacute;sobiť životnosť diskov.<\/li><li>Pri n&aacute;kupe brzdov&yacute;ch do&scaron;tičiek sa uistite, že s&uacute; vybaven&eacute; sn&iacute;mačom opotrebovania, ktor&yacute; je v nov&yacute;ch, drah&scaron;&iacute;ch automobiloch &scaron;tandardom.<\/li><li>Skontrolujte si občas brzdov&eacute; do&scaron;tičky - m&ocirc;žete to urobiť napr. pri v&yacute;mene pneumat&iacute;k<\/li><\/ul>'
 where pk = 23
 and locale = 'sk';
 
 
-- ID[id_s1:0][pk_s1:24][name_s1:Výmena brzdového kotúča (predný)][pk_prod_new:24][dbg_add:GENERATE-UPDATE-PROD-ITEM]
-- ID[id_s1:0][pk_s1:24][name_s1:Výmena brzdového kotúča (predné)][pk_prod_new:24][dbg_add:GENERATE-UPDATE-NEW-ITEM]

update service_translation set
  name = 'Výmena brzdového kotúča (predné)'
,   description_short = '<p>Brzdov&eacute; kot&uacute;če sa opotrebov&aacute;vaj&uacute; dvakr&aacute;t až trikr&aacute;t menej často ako brzdov&eacute; do&scaron;tičky. Preto nesmiete ignorovať žiadne zn&aacute;mky ich opotrebenie. Disky sa l&iacute;&scaron;ia typom a cenou v z&aacute;vislosti na tom, či si chcete k&uacute;piť bežn&eacute; alebo sofistikovanej&scaron;ie, tj. Ventilovan&eacute;, vŕtan&eacute;, &scaron;trbinov&eacute; alebo keramick&eacute;. Ich &uacute;roveň opotrebenia z&aacute;vis&iacute; na va&scaron;om &scaron;t&yacute;le jazdy, ich kvalite a kvalite brzdov&yacute;ch do&scaron;tičiek. N&aacute;kupom značkov&yacute;ch produktov predlžujete životnosť oboch prvkov. Kedykoľvek si nech&aacute;te vymeniť brzdov&eacute; kot&uacute;če, nechajte ich vymeniť spoločne s do&scaron;tičkami. Pri nov&yacute;ch diskov sa nikdy nesmie použ&iacute;vať star&eacute; podložky.<\/p>'
,   info_box_procedures = '<ul><li>Demont&aacute;ž kolies<\/li><li>Demont&aacute;ž brzdov&yacute;ch strmeňov<\/li><li>Demont&aacute;ž brzdov&yacute;ch do&scaron;tičiek a brzdov&yacute;ch kot&uacute;čov<\/li><li>Mont&aacute;ž nov&yacute;ch diskov a podložiek<\/li><li>Sp&auml;tn&aacute; mont&aacute;ž kolies<\/li><li>Odvzdu&scaron;nenie brzdov&eacute;ho syst&eacute;mu<\/li><\/ul>'
,   info_box_tips = '<ul><li>Vždy použ&iacute;vajte brzdov&eacute; do&scaron;tičky od renomovan&yacute;ch v&yacute;robcov - va&scaron;e brzdy s&uacute; va&scaron;e bezpečnosť<\/li><li>Zabr&aacute;ňte brzdenia vo veľk&yacute;ch kalužiach - voda m&ocirc;že sp&ocirc;sobiť deform&aacute;ciu hor&uacute;cich kot&uacute;čov<\/li><li>N&aacute;kupom vysoko kvalitn&yacute;ch brzdov&yacute;ch do&scaron;tičiek m&ocirc;žete zdvojn&aacute;sobiť životnosť diskov.<\/li><li>Nikdy nemeňte disky, ak nem&aacute;te v &uacute;mysle vymeniť brzdov&eacute; do&scaron;tičky. Pri nov&yacute;ch diskov sa nikdy nesmie použ&iacute;vať star&eacute;, čiastočne opotrebovan&eacute; do&scaron;tičky<\/li><li>Ihneď po v&yacute;mene buďte opatrn&iacute; k brzd&aacute;m. Disky a podložky s&uacute; trecie prvky a treba ich spr&aacute;vne usadiť, preto sa vyhnite n&aacute;hlemu brzden&iacute; niekoľko sto kilometrov po tom, čo ich nech&aacute;te vymeniť.<\/li><\/ul>'
 where pk = 24
 and locale = 'sk';
 
 
-- ID[id_s1:0][pk_s1:25][name_s1:Výmena brzdového kotúča (zadný)][pk_prod_new:25][dbg_add:GENERATE-UPDATE-PROD-ITEM]
-- ID[id_s1:0][pk_s1:25][name_s1:Výmena brzdového kotúča (zadné)][pk_prod_new:25][dbg_add:GENERATE-UPDATE-NEW-ITEM]

update service_translation set
  name = 'Výmena brzdového kotúča (zadné)'
,   description_short = '<p>Brzdov&eacute; kot&uacute;če sa opotrebov&aacute;vaj&uacute; dvakr&aacute;t až trikr&aacute;t menej často ako brzdov&eacute; do&scaron;tičky. Preto nesmiete ignorovať žiadne zn&aacute;mky ich opotrebenie. Disky sa l&iacute;&scaron;ia typom a cenou v z&aacute;vislosti na tom, či si chcete k&uacute;piť bežn&eacute; alebo sofistikovanej&scaron;ie, tj. ventilovan&eacute;, vŕtan&eacute;, &scaron;trbinov&eacute; alebo keramick&eacute;. Ich &uacute;roveň opotrebenia z&aacute;vis&iacute; na va&scaron;om &scaron;t&yacute;le jazdy, ich kvalite a kvalite brzdov&yacute;ch do&scaron;tičiek. N&aacute;kupom značkov&yacute;ch produktov predlžujete životnosť oboch prvkov. Kedykoľvek si nech&aacute;te vymeniť brzdov&eacute; kot&uacute;če, nechajte ich vymeniť spoločne s do&scaron;tičkami. Pri nov&yacute;ch diskov sa nikdy nesmie použ&iacute;vať star&eacute; podložky.<\/p>'
,   info_box_procedures = '<ul><li>Demont&aacute;ž kolies<\/li><li>Demont&aacute;ž brzdov&yacute;ch strmeňov<\/li><li>Demont&aacute;ž brzdov&yacute;ch do&scaron;tičiek a brzdov&yacute;ch kot&uacute;čov<\/li><li>Mont&aacute;ž nov&yacute;ch diskov a podložiek<\/li><li>Sp&auml;tn&aacute; mont&aacute;ž kolies<\/li><li>Odvzdu&scaron;nenie brzdov&eacute;ho syst&eacute;mu<\/li><\/ul>'
,   info_box_tips = '<ul><li>Vždy použ&iacute;vajte brzdov&eacute; do&scaron;tičky od renomovan&yacute;ch v&yacute;robcov - va&scaron;e brzdy s&uacute; va&scaron;e bezpečnosť<\/li><li>Zabr&aacute;ňte brzdenia vo veľk&yacute;ch kalužiach - voda m&ocirc;že sp&ocirc;sobiť deform&aacute;ciu hor&uacute;cich kot&uacute;čov<\/li><li>N&aacute;kupom vysoko kvalitn&yacute;ch brzdov&yacute;ch do&scaron;tičiek m&ocirc;žete zdvojn&aacute;sobiť životnosť diskov.<\/li><li>Nikdy nemeňte disky, ak nem&aacute;te v &uacute;mysle vymeniť brzdov&eacute; do&scaron;tičky. Pri nov&yacute;ch diskov sa nikdy nesmie použ&iacute;vať star&eacute;, čiastočne opotrebovan&eacute; do&scaron;tičky<\/li><li>Ihneď po v&yacute;mene buďte opatrn&iacute; k brzd&aacute;m. Disky a podložky s&uacute; trecie prvky a treba ich spr&aacute;vne usadiť, preto sa vyhnite n&aacute;hlemu brzden&iacute; niekoľko sto kilometrov po tom, čo ich nech&aacute;te vymeniť.<\/li><\/ul>'
 where pk = 25
 and locale = 'sk';
 
 
-- ID[id_s1:0][pk_s1:26][name_s1:Výmena brzdového kotúča][pk_prod_new:26][dbg_add:GENERATE-UPDATE-PROD-ITEM]
-- ID[id_s1:0][pk_s1:26][name_s1:Výmena brzdového kotúča][pk_prod_new:26][dbg_add:GENERATE-UPDATE-NEW-ITEM]

update service_translation set
   description_short = '<p>Brzdov&eacute; kot&uacute;če sa opotrebov&aacute;vaj&uacute; dvakr&aacute;t až trikr&aacute;t menej často ako brzdov&eacute; do&scaron;tičky. Preto nesmiete ignorovať žiadne zn&aacute;mky ich opotrebenie. Disky sa l&iacute;&scaron;ia typom a cenou v z&aacute;vislosti na tom, či si chcete k&uacute;piť bežn&eacute; alebo sofistikovanej&scaron;ie, tj. ventilovan&eacute;, vŕtan&eacute;, &scaron;trbinov&eacute; alebo keramick&eacute;. Ich &uacute;roveň opotrebenia z&aacute;vis&iacute; na va&scaron;om &scaron;t&yacute;le jazdy, ich kvalite a kvalite brzdov&yacute;ch do&scaron;tičiek. N&aacute;kupom značkov&yacute;ch produktov predlžujete životnosť oboch prvkov. Kedykoľvek si nech&aacute;te vymeniť brzdov&eacute; kot&uacute;če, nechajte ich vymeniť spoločne s do&scaron;tičkami. Pri nov&yacute;ch diskov sa nikdy nesmie použ&iacute;vať star&eacute; podložky.<\/p>'
,   info_box_procedures = '<ul><li>Demont&aacute;ž kolies<\/li><li>Demont&aacute;ž brzdov&yacute;ch strmeňov<\/li><li>Demont&aacute;ž brzdov&yacute;ch do&scaron;tičiek a brzdov&yacute;ch kot&uacute;čov<\/li><li>Mont&aacute;ž nov&yacute;ch diskov a podložiek<\/li><li>Sp&auml;tn&aacute; mont&aacute;ž kolies<\/li><li>Odvzdu&scaron;nenie brzdov&eacute;ho syst&eacute;mu<\/li><\/ul>'
,   info_box_tips = '<ul><li>Vždy použ&iacute;vajte brzdov&eacute; do&scaron;tičky od renomovan&yacute;ch v&yacute;robcov - va&scaron;e brzdy s&uacute; va&scaron;e bezpečnosť<\/li><li>Zabr&aacute;ňte brzdenia vo veľk&yacute;ch kalužiach - voda m&ocirc;že sp&ocirc;sobiť deform&aacute;ciu hor&uacute;cich kot&uacute;čov<\/li><li>N&aacute;kupom vysoko kvalitn&yacute;ch brzdov&yacute;ch do&scaron;tičiek m&ocirc;žete zdvojn&aacute;sobiť životnosť diskov.<\/li><li>Nikdy nemeňte disky, ak nem&aacute;te v &uacute;mysle vymeniť brzdov&eacute; do&scaron;tičky. Pri nov&yacute;ch diskov sa nikdy nesmie použ&iacute;vať star&eacute;, čiastočne opotrebovan&eacute; do&scaron;tičky<\/li><li>Ihneď po v&yacute;mene buďte opatrn&iacute; k brzd&aacute;m. Disky a podložky s&uacute; trecie prvky a treba ich spr&aacute;vne usadiť, preto sa vyhnite n&aacute;hlemu brzden&iacute; niekoľko sto kilometrov po tom, čo ich nech&aacute;te vymeniť.<\/li><\/ul>'
 where pk = 26
 and locale = 'sk';
 
 
-- ID[id_s1:0][pk_s1:27][name_s1:Výmena brzdovej čelusti][pk_prod_new:27][dbg_add:GENERATE-UPDATE-PROD-ITEM]
-- ID[id_s1:0][pk_s1:27][name_s1:Výmena brzdovej čeľuste][pk_prod_new:27][dbg_add:GENERATE-UPDATE-NEW-ITEM]

update service_translation set
  name = 'Výmena brzdovej čeľuste'
,   description_short = '<p>Brzdov&eacute; bubny sa bežne použ&iacute;vaj&uacute; na zadn&uacute; n&aacute;pravu vozidla. Jedn&yacute;m z kľ&uacute;čov&yacute;ch prvkov tohto typu brzdov&eacute;ho syst&eacute;mu s&uacute; brzdov&eacute; čeľuste. S&uacute; zabrzden&eacute; ako v hlavnej, tak v parkovacej brzde, preto je veľmi d&ocirc;ležit&eacute; nechať ich pravidelne vymieňať, aby bol cel&yacute; brzdov&yacute; syst&eacute;m funkčn&yacute;. Porucha parkovacej brzdy alebo nerovnomern&eacute; rozloženie brzdnej sily na zadnej n&aacute;prave znamen&aacute;, že je potrebn&eacute; sa postarať o obloženie. Brzdov&eacute; čeľuste a bubny nie s&uacute; vystaven&eacute; tak veľk&eacute;mu zaťaženiu ako disky a do&scaron;tičky a je potrebn&eacute; ich vymeniť po 100 tis. Kilometroch.<\/p>'
,   info_box_procedures = '<ul><li>Demont&aacute;ž kolies<\/li><li>Odskrutkujte nastavovacie skrutky bubna. Možno budete musieť demontovať tiež maticu n&aacute;boja kolesa<\/li><li>Demont&aacute;ž bubna<\/li><li>Demont&aacute;ž pruž&iacute;n a ich upevnenie<\/li><li>Zaistenie valce (napr. Pomocou svorky)<\/li><li>Odpojenie lanka ručnej brzdy<\/li><li>Demont&aacute;ž brzdov&yacute;ch strmeňov<\/li><li>Mont&aacute;ž strmeňov, uloženie pruž&iacute;n, pruž&iacute;n a lank&aacute; ručnej brzdy<\/li><li>nasadenie bubna<\/li><li>Namontovanie nastavovac&iacute;ch skrutiek bubna a matice n&aacute;boja kolesa<\/li><li>Sp&auml;tn&aacute; mont&aacute;ž kolies<\/li><\/ul>'
,   info_box_tips = '<ul><li>Použite pod&scaron;&iacute;vku iba renomovan&yacute;mi v&yacute;robcami. Pam&auml;tajte, že brzdov&yacute; syst&eacute;m je zodpovedn&yacute; za va&scaron;u bezpečnosť<\/li><li>Nezabudnite vždy vymeniť obe brzdov&eacute; čeľuste<\/li><li>Funkčn&eacute; bubnov&eacute; brzdy zaisťuj&uacute; spr&aacute;vnu funkciu ručnej brzdy<\/li><\/ul>'
 where pk = 27
 and locale = 'sk';
 
 
-- ID[id_s1:0][pk_s1:232][name_s1:Výmena brzdového valca][pk_prod_new:232][dbg_add:GENERATE-UPDATE-PROD-ITEM]
-- ID[id_s1:0][pk_s1:232][name_s1:Výmena brzdových valcov][pk_prod_new:232][dbg_add:GENERATE-UPDATE-NEW-ITEM]

update service_translation set
  name = 'Výmena brzdových valcov'
,   description_short = '<p>Brzdov&yacute; valec je t&aacute; s&uacute;časť bubnov&eacute;ho brzdov&eacute;ho syst&eacute;mu, ktor&aacute; tlač&iacute; brzdov&eacute; čeľuste na vonkaj&scaron;&iacute; povrch bubna. Jeho po&scaron;kodenie sp&ocirc;sob&iacute; pokles tlaku brzdovej kvapaliny a &uacute;nik kvapaliny na trecie obloženia. Jeho v&yacute;mena vyžaduje demont&aacute;ž kolesa, obuvi, had&iacute;c a nakoniec samotn&eacute;ho valca. Nov&eacute; komponenty s&uacute; osaden&eacute; v opačnom porad&iacute;. Po oprave by mal byť syst&eacute;m odvetran&yacute;. Dobr&yacute;m n&aacute;padom je tiež vyčistiť cel&yacute; brzdov&yacute; syst&eacute;m, skontrolovať hr&uacute;bku obloženia a stav bubna. Mali by ste vždy nechať vymeniť oba valce, pretože maj&uacute; podobn&uacute; životnosť.<\/p>'
,   info_box_procedures = '<ul><li>V&yacute;mena brzdov&yacute;ch valcov<\/li><li>Čistenie vn&uacute;tra bubna<\/li><li>Kontrola hr&uacute;bky ostenia<\/li><li>Mazanie pohybliv&yacute;ch prvkov vysokoteplotn&yacute;m mazivom<\/li><\/ul>'
,   info_box_tips = '<ul><li>Mali by ste vždy nechať vymeniť oba valce<\/li><li>Brzdov&eacute; valce ovplyvňuj&uacute; tlak brzdovej kvapaliny<\/li><li>Valce treba vymeniť zakažd&yacute;m, keď nech&aacute;te vymeniť brzdov&eacute; čeľuste alebo bubny<\/li><li>Chybn&yacute; valec bude vytekať z brzdovej kvapaliny a n&aacute;sledne ovplyvn&iacute; činnosť brzdov&eacute;ho syst&eacute;mu<\/li><\/ul>'
 where pk = 232
 and locale = 'sk';
 
 
-- ID[id_s1:0][pk_s1:28][name_s1:Výmena brzdového bubna][pk_prod_new:28][dbg_add:GENERATE-UPDATE-PROD-ITEM]
-- ID[id_s1:0][pk_s1:28][name_s1:Výmena brzdového bubna][pk_prod_new:28][dbg_add:GENERATE-UPDATE-NEW-ITEM]

update service_translation set
   description_short = '<p>Brzdov&eacute; bubny sa v s&uacute;časnosti použ&iacute;vaj&uacute; len na zadn&uacute; n&aacute;pravu a ich v&yacute;mena nie je ľahk&aacute;. Ak zist&iacute;te, že zadn&eacute; brzdy s&uacute; slab&scaron;ie alebo je parkovacia brzda menej &uacute;činn&aacute; než predt&yacute;m, mali by ste skontrolovať syst&eacute;m bubnov&yacute;ch bŕzd. V&yacute;mena bubnov vyžaduje &scaron;peci&aacute;lne n&aacute;radie. Preto by to malo byť vykonan&eacute; v &scaron;pecializovanej gar&aacute;ži. V&yacute;mena bubnov vyžaduje tiež v&yacute;menu brzdov&yacute;ch čeľust&iacute; a - u mnoh&yacute;ch modelov automobilov - tiež lož&iacute;sk kolies.<\/p>'
,   info_box_procedures = '<ul><li>Demont&aacute;ž kolies<\/li><li>Demont&aacute;ž bubnov - u niektor&yacute;ch automobilov - tiež ložisk&aacute; kolies<\/li><li>V&yacute;mena brzdov&yacute;ch čeľust&iacute;<\/li><li>Odvzdu&scaron;nenie brzdov&eacute;ho syst&eacute;mu<\/li><li>Mont&aacute;ž nov&yacute;ch bubnov \/ lož&iacute;sk kolies<\/li><li>Sp&auml;tn&aacute; mont&aacute;ž kolies<\/li><li>Skontrolovať spr&aacute;vnu funkciu brzdov&eacute;ho syst&eacute;mu<\/li><\/ul>'
,   info_box_tips = '<ul><li>Prvky brzdov&eacute;ho bubna by mali byť vždy vymieňan&eacute; vo dvojiciach<\/li><li>Životnosť bubnov z&aacute;vis&iacute; na va&scaron;om &scaron;t&yacute;le jazdy a pohybuje sa medzi 100 a 150 tis&iacute;ckami kilometre<\/li><li>Po v&yacute;mene by mal byť brzdov&yacute; syst&eacute;m odvzdu&scaron;nen&yacute; a skontrolovan&yacute;<\/li><\/ul>'
 where pk = 28
 and locale = 'sk';
 
 
-- ID[id_s1:0][pk_s1:176][name_s1:Výmena nastavovača bŕzd][pk_prod_new:176][dbg_add:GENERATE-UPDATE-PROD-ITEM]
-- ID[id_s1:0][pk_s1:176][name_s1:Výmena brzdových valčekov][pk_prod_new:176][dbg_add:GENERATE-UPDATE-NEW-ITEM]

update service_translation set
  name = 'Výmena brzdových valčekov'
,   description_short = '<p>Nastavovačom je mal&yacute; valec obsahuj&uacute;ci brzdov&uacute; kvapalinu, ktor&eacute;ho krajn&eacute; povrchy sa pohybuj&uacute; pod tlakom, ktor&yacute; je v&yacute;sledkom zo&scaron;liapnutie brzdov&eacute;ho ped&aacute;lu. Nastavovač tlač&iacute; proti bubna. &Uacute;nik brzdovej kvapaliny z nastavovacieho zariadenia sp&ocirc;sob&iacute; pokles tlaku v syst&eacute;me, čo m&aacute; za n&aacute;sledok &uacute;nik kvapaliny cez trecie obloženia. Valec zlyh&aacute; s časom alebo sa m&ocirc;že po&scaron;kodiť v d&ocirc;sledku nespr&aacute;vneho nasadenia brzdov&yacute;ch čeľust&iacute;.<\/p>'
,   info_box_procedures = '<ul><li>Demont&aacute;ž kolies<\/li><li>Demont&aacute;ž bubnov<\/li><li>Odskrutkujte brzdy hadice na zadnej časti bubnov<\/li><li>Odstr&aacute;ňte skrutku, ktor&aacute; drž&iacute; valce<\/li><li>V&yacute;mena nastavovača<\/li><li>Op&auml;tovn&eacute; pripojenie brzdov&yacute;ch had&iacute;c<\/li><li>Mont&aacute;ž prvkov bubna<\/li><li>Kontrola hladiny brzdovej kvapaliny<\/li><\/ul>'
,   info_box_tips = '<ul><li>Nastavovač by mal byť vždy nahraden&yacute; nov&yacute;m<\/li><li>Pri každej v&yacute;mene prvkov bubnov&eacute; brzdy je potrebn&eacute; skontrolovať tesnosť valca<\/li><\/ul>'
 where pk = 176
 and locale = 'sk';
 
 
-- ID[id_s1:0][pk_s1:231][name_s1:Vymazanie hlášky servisného intervalu][pk_prod_new:231][dbg_add:GENERATE-UPDATE-PROD-ITEM]
-- ID[id_s1:0][pk_s1:231][name_s1:Vymazanie hlášky servisného intervalu][pk_prod_new:231][dbg_add:GENERATE-UPDATE-NEW-ITEM]

update service_translation set
   description_short = '<p>Spr&aacute;va o servisnej prehliadke v&aacute;s informuje, že va&scaron;e auto mus&iacute; podst&uacute;piť kontrolu. Spr&aacute;va sa zobraz&iacute; na palubnej doske vo forme v&yacute;stražn&eacute;ho svetla so &scaron;peci&aacute;lnou grafikou alebo textom. Spr&aacute;va je zvyčajne zru&scaron;en&aacute; nastaven&iacute;m ďal&scaron;ieho &uacute;daja kontroly, použit&iacute;m &scaron;peci&aacute;lneho zariadenia alebo stlačen&iacute;m prep&iacute;načov na palubnej doske v spr&aacute;vnom porad&iacute;.<\/p>'
,   info_box_procedures = '<ul><li>Pripojenie diagnostick&eacute;ho zariadenia k autu<\/li><li>Stlačen&iacute;m tlačidiel na palubnej doske v spr&aacute;vnom porad&iacute;<\/li><li>Zapnutie zapaľovania pri &scaron;tartovan&iacute; motora<\/li><li>Nastavenie ďal&scaron;ieho &uacute;daja kontroly<\/li><\/ul>'
,   info_box_tips = '<ul><li>Nezru&scaron;&iacute; spr&aacute;vu o servisnej prehliadke, k&yacute;m si nenech&aacute;te vykonať prehliadku svojho vozidla<\/li><li>Nechajte svoje auto skontrolovať čo najsk&ocirc;r po rozsvieten&iacute; kontroln&eacute;ho svetla alebo spr&aacute;vy<\/li><li>Nastavenie nespr&aacute;vnej doby kontroly m&ocirc;že mať za n&aacute;sledok nadmern&eacute; opotrebovanie s&uacute;časťou automobilu<\/li><\/ul>'
 where pk = 231
 and locale = 'sk';
