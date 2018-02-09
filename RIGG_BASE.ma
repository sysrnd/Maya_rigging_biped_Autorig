//Maya ASCII 2015 scene
//Name: RIGG_BASE_I.ma
//Last modified: Mon, Oct 09, 2017 07:43:10 PM
//Codeset: 1252
requires maya "2015";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2015";
fileInfo "version" "2015";
fileInfo "cutIdentifier" "201503261530-955654";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	setAttr ".t" -type "double3" 18.187261928283789 19.71772198367098 48.421420209080523 ;
	setAttr ".r" -type "double3" -10.538352729390924 23.799999999998342 4.3452115885854425e-016 ;
createNode camera -s -n "perspShape" -p "persp";
	setAttr -k off ".v";
	setAttr ".fl" 34.999999999999986;
	setAttr ".coi" 57.03292989416412;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 18.038557429396882 -5.8570092103643034 3.1713017358758022 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	setAttr ".t" -type "double3" -0.66328373914519867 105.96032803264163 -0.6501146312209829 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	setAttr -k off ".v";
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 20.942452060976763;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	setAttr ".t" -type "double3" -0.0077514538099932029 0.36063518637080066 103.6794123239622 ;
createNode camera -s -n "frontShape" -p "front";
	setAttr -k off ".v";
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 24.069288981816662;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	setAttr ".t" -type "double3" 102.30388622047279 0.056207893040220086 1.8580702727558651 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	setAttr -k off ".v";
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 8.7326866983678197;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "DEFORM_CURV_NARIZ";
	setAttr ".rp" -type "double3" 19.026560169728874 -6.9482169347214935 3.6348763446438599 ;
	setAttr ".sp" -type "double3" 19.026560169728874 -6.9482169347214935 3.6348763446438599 ;
createNode nurbsCurve -n "DEFORM_CURV_NARIZShape" -p "DEFORM_CURV_NARIZ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		18.433354926366643 -7.0236960537692852 3.2803908549662446
		19.026560169728874 -6.8727378156736982 3.9893618343214752
		19.619765413091105 -7.0236960537692852 3.2803908549662446
		;
createNode transform -n "DEFORM_CURV_BOCA_SUP";
	setAttr ".rp" -type "double3" 19.007144562447763 -7.3467672206508112 2.9882825783993896 ;
	setAttr ".sp" -type "double3" 19.007144562447763 -7.3467672206508112 2.9882825783993896 ;
createNode nurbsCurve -n "DEFORM_CURV_BOCA_SUPShape" -p "DEFORM_CURV_BOCA_SUP";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		18.014707479136888 -7.2905305478588645 2.8018676366440274
		18.510926020792326 -7.3568579699220535 3.0003701952651833
		19.007144562447763 -7.403003893442758 3.1746975201547518
		19.503363104103201 -7.3568579699220535 3.0003701952651833
		19.999581645758639 -7.2905305478588645 2.8018676366440274
		;
createNode transform -n "DEFORM_CURV_BOCA_INF";
	setAttr ".rp" -type "double3" 19.007144562447763 -7.4605792408699507 2.9527232754181725 ;
	setAttr ".sp" -type "double3" 19.007144562447763 -7.4605792408699507 2.9527232754181725 ;
createNode nurbsCurve -n "DEFORM_CURV_BOCA_INFShape" -p "DEFORM_CURV_BOCA_INF";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		18.060512850742782 -7.3920932683815153 2.7935937995350741
		18.510926020792326 -7.4829192898376817 2.9573810881520854
		19.007144562447763 -7.5290652133583862 3.1118527513012713
		19.503363104103201 -7.4829192898376817 2.9573810881520854
		19.953776274152741 -7.3920932683815153 2.7935937995350741
		;
createNode transform -n "DEFORM_CURV_DER";
	setAttr ".rp" -type "double3" 18.038557429396882 -5.8570092103643034 3.1713017358758022 ;
	setAttr ".sp" -type "double3" 18.038557429396882 -5.8570092103643034 3.1713017358758022 ;
createNode nurbsCurve -n "DEFORM_CURV_DERShape" -p "DEFORM_CURV_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 12 2 no 3
		17 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
		15
		17.188586522144966 -5.3662782782590632 3.1713017358758022
		17.547826497291638 -5.0070383031123882 3.1713017358758022
		18.038557429396882 -4.8755473461538159 3.1713017358758022
		18.529288361502125 -5.0070383031123882 3.1713017358758022
		18.888528336648797 -5.3662782782590597 3.1713017358758022
		19.020019293607369 -5.8570092103643034 3.1713017358758022
		18.888528336648797 -6.3477401424695472 3.1713017358758022
		18.529288361502125 -6.7069801176162187 3.1713017358758022
		18.038557429396882 -6.838471074574791 3.1713017358758022
		17.547826497291638 -6.7069801176162187 3.1713017358758022
		17.188586522144966 -6.3477401424695472 3.1713017358758022
		17.057095565186394 -5.8570092103643034 3.1713017358758022
		17.188586522144966 -5.3662782782590632 3.1713017358758022
		17.547826497291638 -5.0070383031123882 3.1713017358758022
		18.038557429396882 -4.8755473461538159 3.1713017358758022
		;
createNode transform -n "MASTER";
	setAttr ".rp" -type "double3" 0 0 0.93937092674000233 ;
	setAttr ".sp" -type "double3" 0 0 0.93937092674000233 ;
createNode nurbsCurve -n "MASTERShape" -p "MASTER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
		25
		-2.2215208837003106 -6.6329118552736169e-033 -2.0222764359694336
		-1.5760070814525711 -6.6329118552736169e-033 -4.5287767966268353
		-3.1520141629051479 -6.6329118552736169e-033 -4.5287767966268353
		-6.1495240180876772e-015 -6.6329118552736169e-033 -7.5959103132802417
		3.152014162905127 -6.6329118552736169e-033 -4.5287767966268353
		1.576007081452562 -6.6329118552736169e-033 -4.5287767966268353
		2.2215208837003071 -6.6329118552736169e-033 -2.0222764359694336
		4.7280212443577003 -6.6329118552736169e-033 -1.3767626337217003
		4.7280212443577003 -6.6329118552736169e-033 -2.9527697151742656
		7.795154761011112 -6.6329118552736169e-033 0.19924444773086847
		4.7280212443577003 -6.6329118552736169e-033 3.3512586106360018
		4.7280212443577003 -6.6329118552736169e-033 1.7752515291834368
		2.2215208837003071 -6.6329118552736169e-033 2.4207653314311686
		1.576007081452562 -6.6329118552736169e-033 4.9272656920885716
		3.152014162905127 -6.6329118552736169e-033 4.9272656920885716
		-6.1495240180876772e-015 -6.6329118552736169e-033 7.9943992087419939
		-3.1520141629051479 -6.6329118552736169e-033 4.9272656920885716
		-1.5760070814525711 -6.6329118552736169e-033 4.9272656920885716
		-2.2215208837003106 -6.6329118552736169e-033 2.4207653314311686
		-4.7280212443577154 -6.6329118552736169e-033 1.7752515291834368
		-4.7280212443577154 -6.6329118552736169e-033 3.3512586106360018
		-7.795154761011112 -6.6329118552736169e-033 0.19924444773086847
		-4.7280212443577154 -6.6329118552736169e-033 -2.9527697151742656
		-4.7280212443577154 -6.6329118552736169e-033 -1.3767626337217003
		-2.2215208837003106 -6.6329118552736169e-033 -2.0222764359694336
		;
createNode transform -n "DRIVER_RODILLA_DER";
	setAttr ".rp" -type "double3" -1.1685200000000011 4.28726 4.0907987591282975 ;
	setAttr ".sp" -type "double3" -1.1685200000000009 4.28726 4.0907987591282975 ;
createNode nurbsCurve -n "DRIVER_RODILLA_DERShape" -p "DRIVER_RODILLA_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
		25
		-1.3253378472631026 4.2872600000002201 4.0907987591283348
		-1.5129070077430591 4.4594535038716918 4.0907987591283348
		-1.5990037596787949 4.3733567519359458 4.0907987591283348
		-1.5943667577068605 4.7131067577070089 4.0907987591283348
		-1.2546167519358185 4.7177437596789549 4.0907987591283348
		-1.3407135038715552 4.6316470077431902 4.0907987591283348
		-1.1685200000000673 4.4440778472632418 4.0907987591283348
		-0.99632649612858515 4.631647007743191 4.0907987591283348
		-1.0824232480643119 4.7177437596789549 4.0907987591283348
		-0.74267324229328102 4.7131067577070098 4.0907987591283348
		-0.73803624032134885 4.3733567519359458 4.0907987591283348
		-0.82413299225709946 4.4594535038716918 4.0907987591283348
		-1.0117021527369958 4.2872600000002219 4.0907987591283348
		-0.82413299225709968 4.1150664961286774 4.0907987591283348
		-0.73803624032134907 4.2011632480644581 4.0907987591283348
		-0.74267324229328124 3.8614132422934824 4.0907987591283348
		-1.0824232480643123 3.8567762403215404 4.0907987591283348
		-0.99632649612858515 3.9428729922572874 4.0907987591283348
		-1.1685200000000691 4.1304421527371211 4.0907987591283348
		-1.3407135038715556 3.9428729922572869 4.0907987591283348
		-1.2546167519358185 3.8567762403215404 4.0907987591283348
		-1.5943667577068605 3.8614132422934828 4.0907987591283348
		-1.5990037596787949 4.2011632480644572 4.0907987591283348
		-1.5129070077430595 4.1150664961286774 4.0907987591283348
		-1.3253378472631026 4.2872600000002201 4.0907987591283348
		;
createNode joint -n "R_ROOT";
	setAttr ".t" -type "double3" 0 8.7132271986612011 0.18069868322541349 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90 21.383635164761763 90 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_COLUMNA_BAJA" -p "R_ROOT";
	setAttr ".t" -type "double3" 1.3592013762614867 2.5761607423616181e-016 -1.509016663027703e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 7.5686098235000747 ;
	setAttr ".radi" 0.52259370277152639;
createNode joint -n "R_COLUMNA_MEDIA" -p "R_COLUMNA_BAJA";
	setAttr ".t" -type "double3" 1.4368115869161771 1.3322676295501878e-015 -1.4762305327668325e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 4.6445526411110376e-016 5.0623350927090133e-015 10.484107960811651 ;
	setAttr ".radi" 0.52293610614286301;
createNode joint -n "R_COLUMNA_ALTA" -p "R_COLUMNA_MEDIA";
	setAttr ".t" -type "double3" 1.443431385428684 -2.7755575615628914e-017 -1.2753353595101686e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 4.1112367750016471e-015 10.066928594569356 ;
	setAttr ".radi" 0.50460879205797804;
createNode joint -n "R_CUELLO" -p "R_COLUMNA_ALTA";
	setAttr ".t" -type "double3" 0.97501663004366268 -1.8041124150158794e-016 6.9961945883961836e-017 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -6.2586055777971534 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_CUELLO_SEC" -p "R_CUELLO";
	setAttr ".t" -type "double3" 0.81376688813207243 -4.163336342344337e-016 3.8193815413782679e-017 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.7109739420078524e-017 -3.013218097554932e-015 1.411198187229372 ;
	setAttr ".radi" 0.51308788540535555;
createNode joint -n "R_CABEZA" -p "R_CUELLO_SEC";
	setAttr ".t" -type "double3" 1.2530324511702062 4.4408920985006262e-016 6.5897699460178739e-017 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.5601944247390472e-016 -4.0209083498230684e-015 
		4.4441566619681394 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_CABEZA_ALTA" -p "R_CABEZA";
	setAttr ".t" -type "double3" 3.8035175790681413 1.4432899320127035e-015 2.6692359755541876e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 82.860738057281097 89.999999999999943 0 ;
	setAttr ".radi" 0.64500952995180039;
createNode joint -n "R_OJO_DER" -p "R_CABEZA_ALTA";
	setAttr ".t" -type "double3" -0.78837371753915542 -2.5781719232551943 1.2322024176368775 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -4.9298597562684521e-014 1.3292816646217324e-014 -4.3310199980768558e-014 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_OJO_IZQ" -p "R_CABEZA_ALTA";
	setAttr ".t" -type "double3" 0.78837371753915553 -2.5781719232552014 1.2322024176368764 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -4.9298597562684521e-014 1.3292816646217324e-014 -4.3310199980768558e-014 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_DIENTES_ARRIBA" -p "R_CABEZA";
	setAttr ".t" -type "double3" -0.10051539876732107 -2.1351054109164433 -4.8585021093867975e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.55883466074071964;
createNode joint -n "R_MANDIBULA" -p "R_CABEZA";
	setAttr ".t" -type "double3" -0.66860466948992503 -0.26497786275343049 -1.0634254066090235e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.3698699940756828e-014 1.0693660171329217e-014 -144.78825112142795 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_BOCA_1" -p "R_MANDIBULA";
	setAttr ".t" -type "double3" 0.62571848571684341 5.6906906805896314e-016 -1.1678383479618832e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 46.526138700420574 ;
	setAttr ".radi" 0.53549279413611195;
createNode joint -n "R_BOCA_2" -p "R_BOCA_1";
	setAttr ".t" -type "double3" 1.6861940199648304 1.8873791418627661e-015 -3.9120831053427193e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -7.3336042339983414e-015 -5.5865703068859238e-015 
		105.40137436372635 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_DIENTES_BAJA" -p "R_BOCA_2";
	setAttr ".t" -type "double3" 0.98765368823933408 3.3306690738754696e-016 9.6300230402562218e-017 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -7.1392619427189628 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_LENGUA_1" -p "R_MANDIBULA";
	setAttr ".t" -type "double3" 0.12322080879818209 0.23103901649658987 -4.1331192578072786e-017 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 8.1051248416849092e-015 1.0937036409119461e-014 73.082172803075139 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_LENGUA_2" -p "R_LENGUA_1";
	setAttr ".t" -type "double3" 0.76577535626406346 -0.15099795757319567 -1.5058584311591282e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -2.1036297916225148e-015 1.2867723890901738e-014 -18.56929002990292 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_LENGUA_3" -p "R_LENGUA_2";
	setAttr ".t" -type "double3" 0.71715331881975897 0.093328171627229395 -1.6624680184612668e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -54.512882773172215 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_CLAVICULA_IZQ" -p "R_COLUMNA_ALTA";
	setAttr ".t" -type "double3" 0.16086960653645832 0.019000347228715686 -1.076989314315111 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.000000000000242 80.625352979108854 6.7360112141195172 ;
	setAttr ".radi" 0.50471268734568542;
createNode joint -n "R_HOMBRO_IZQ" -p "R_CLAVICULA_IZQ";
	setAttr ".t" -type "double3" 1.0911119553499182 9.1593399531575415e-016 5.2222796637331994e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.1023216300637443e-012 5.6358403616014243 -9.3746470208910537 ;
	setAttr ".radi" 0.59704833651003142;
createNode joint -n "R_CODO_IZQ" -p "R_HOMBRO_IZQ";
	setAttr ".t" -type "double3" 2.8762678391939387 -2.9088006330002314e-015 -8.8817841970012523e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 7.4625022989917234e-015 -14.430440342312302 -5.894585613885645e-014 ;
	setAttr ".radi" 0.57392190162732382;
createNode joint -n "R_CODO_SEC_IZQ" -p "R_CODO_IZQ";
	setAttr ".t" -type "double3" 0.98423999512474047 -0.0012045657891253114 -0.0077856508572380356 ;
	setAttr ".radi" 0.57392190162732382;
createNode joint -n "R_MANO_IZQ" -p "R_CODO_SEC_IZQ";
	setAttr ".t" -type "double3" 1.4827921084934546 -0.0017235890215477312 -0.011730006326813643 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.0081127280851612 5.2078667684428526 -3.9964603400648171 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_MIDDLE_IZQ_1" -p "R_MANO_IZQ";
	setAttr ".t" -type "double3" 1.4625601003658102 -8.7281727465425664e-017 4.1945113213044843e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 4.928742780702958 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_MIDDLE_IZQ_2" -p "R_MIDDLE_IZQ_1";
	setAttr ".t" -type "double3" 0.4163767503376547 -6.7307270867900115e-016 -2.1857515797307769e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 3.7472124008557326e-015 0.54127410510358209 7.9330548690213613e-013 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_MIDDLE_IZQ_3" -p "R_MIDDLE_IZQ_2";
	setAttr ".t" -type "double3" 0.30521726326902099 -1.0616507672978059e-015 5.0480453150925086e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.1323115366376642e-015 -0.6620262699199313 1.959920725104381e-013 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_MIDDLE_IZQ_4" -p "R_MIDDLE_IZQ_3";
	setAttr ".t" -type "double3" 0.31038076300484313 3.1225022567582528e-017 7.6588041464376033e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -91.276695262256411 -7.0419799138103452 94.169749292940992 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_PINKY_SEC_IZQ" -p "R_MANO_IZQ";
	setAttr ".t" -type "double3" 0.43318924604574505 6.7045079295591115e-017 -0.41454392021277159 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 10.71748008617759 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_PINKY_IZQ_1" -p "R_PINKY_SEC_IZQ";
	setAttr ".t" -type "double3" 0.93900472479798758 -0.018216171239016535 -0.0012843397171242361 ;
	setAttr ".r" -type "double3" 0 0 -6.8690539463847893 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -0.58382984406895078 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_PINKY_IZQ_2" -p "R_PINKY_IZQ_1";
	setAttr ".t" -type "double3" 0.22387820993577198 0.0012233019788163437 0.0011801797114500488 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -2.1250020198942806e-031 -4.4208651669519972 5.5054036713306073e-030 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_PINKY_IZQ_3" -p "R_PINKY_IZQ_2";
	setAttr ".t" -type "double3" 0.2165517339293157 -1.7763568394002503e-015 3.2959746043559335e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.791915219911692e-014 4.6278950862124129 -4.4345583705820839e-013 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_PINKY_IZQ_4" -p "R_PINKY_IZQ_3";
	setAttr ".t" -type "double3" 0.23753345597066877 0.00087684232747319805 0.0018144402089301376 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -10.34068016136905 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_CANCEL_IZQ_1" -p "R_MANO_IZQ";
	setAttr ".t" -type "double3" 1.4077138040605872 0.087336261133938345 -0.30991499559067087 ;
	setAttr ".r" -type "double3" 0 0 -7.9533971014506841 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 7.4037120803680816 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_CANCEL_IZQ_2" -p "R_CANCEL_IZQ_1";
	setAttr ".t" -type "double3" 0.37688492281917252 1.9884351325972013e-032 -1.8735013540549517e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 5.5210241232701605e-015 -1.6791363363616143 -3.7675170632947004e-013 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_CANCEL_IZQ_3" -p "R_CANCEL_IZQ_2";
	setAttr ".t" -type "double3" 0.27618270903279984 0.00082597349125568698 0.00022852323681000285 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 3.427427038457143e-033 0.10374482489103187 3.7857705277440378e-030 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_CANCEL_IZQ_4" -p "R_CANCEL_IZQ_3";
	setAttr ".t" -type "double3" 0.27928780060505914 -0.00011799621303352497 -3.4177766619309322e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -5.8283205688975013 0 ;
	setAttr ".radi" 0.56364323295275121;
createNode joint -n "R_INDEX_IZQ_1" -p "R_MANO_IZQ";
	setAttr ".t" -type "double3" 1.4663952104361568 -5.3290705182007514e-015 0.31665033626886241 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 3.1395128455277872 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_INDEX_IZQ_2" -p "R_INDEX_IZQ_1";
	setAttr ".t" -type "double3" 0.37432623887793071 -1.7763568394002505e-015 -2.2551405187698492e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 1.4908561152356761 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_INDEX_IZQ_3" -p "R_INDEX_IZQ_2";
	setAttr ".t" -type "double3" 0.32186155442042391 -1.7763568394002505e-015 6.9388939039072284e-018 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.0745325081721283e-014 1.6870984604159376 7.2979414921776405e-013 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_INDEX_IZQ_4" -p "R_INDEX_IZQ_3";
	setAttr ".t" -type "double3" 0.27904276347459606 1.7763568394002505e-015 -1.0200174038743626e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -6.3174674211794031 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_THUMB_IZQ_1" -p "R_MANO_IZQ";
	setAttr ".t" -type "double3" 0.60001714049506649 -5.3290705182007514e-015 0.54890756108893857 ;
	setAttr ".r" -type "double3" 41.295087426667322 0.68208271769190998 -19.761220231791302 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 5.7183313164998569e-014 -26.788481971200454 -2.4013748937730446e-013 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_THUMB_IZQ_2" -p "R_THUMB_IZQ_1";
	setAttr ".t" -type "double3" 0.47478698634454919 -1.7763568394002503e-015 2.7755575615628914e-017 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.3715304995009489e-030 3.3965354189382886 -4.625884027261953e-029 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_THUMB_IZQ_3" -p "R_THUMB_IZQ_2";
	setAttr ".t" -type "double3" 0.26394676403861228 0.0099383328785099204 0.0018919675224100948 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.2554036256381601e-014 -4.4339209495244623 -3.2428827576260377e-013 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_THUMB_IZQ_4" -p "R_THUMB_IZQ_3";
	setAttr ".t" -type "double3" 0.32140149315883604 -0.00088139515058639328 -0.0047417376385099535 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 27.825867501786615 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_CLAVICULA_DER" -p "R_COLUMNA_ALTA";
	setAttr ".t" -type "double3" 0.16088063883362125 0.019001929365822789 1.0769900000000001 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.000000000000185 80.625352979108882 -173.26398878588066 ;
	setAttr ".radi" 0.50471268734568542;
createNode joint -n "R_HOMBRO_DER" -p "R_CLAVICULA_DER";
	setAttr ".t" -type "double3" -1.0911075385519444 3.0250887645522084e-005 -7.7715611723760958e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 4.7440679014250113e-013 5.6358403616014101 -9.3746470208910626 ;
	setAttr ".radi" 0.59704833651003142;
createNode joint -n "R_CODO_DER" -p "R_HOMBRO_DER";
	setAttr ".t" -type "double3" -2.8762652734835217 2.7799624996660555e-005 1.9865951015329841e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.9473126074158124e-015 -14.430440342312302 1.5381704985152627e-014 ;
	setAttr ".radi" 0.57392190162732382;
createNode joint -n "R_CODO_SEC_DER" -p "R_CODO_DER";
	setAttr ".t" -type "double3" -0.98424310237100432 0.0011572998828555114 0.0077842415866822279 ;
	setAttr ".radi" 0.57392190162732382;
createNode joint -n "R_MANO_DER" -p "R_CODO_SEC_DER";
	setAttr ".t" -type "double3" -1.4827966049742223 0.0016747104830088233 0.011730841304797401 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.008112728085599 5.2078667684428144 -3.9964603400647767 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_MIDDLE_DER_1" -p "R_MANO_DER";
	setAttr ".t" -type "double3" -1.4625591089989456 5.3290705182007514e-015 4.6134563147504082e-007 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.0623260177876064e-016 4.9287427807029598 2.4683478624019161e-015 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_MIDDLE_DER_2" -p "R_MIDDLE_DER_1";
	setAttr ".t" -type "double3" -0.41638024405096097 0 -2.4992780062182973e-007 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.8033968948383908e-017 0.54127410510290874 5.9349455027812166e-015 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_MIDDLE_DER_3" -p "R_MIDDLE_DER_2";
	setAttr ".t" -type "double3" -0.30521105597433085 -1.7763568394002505e-015 1.8409142599207229e-007 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -9.7287762181122899e-018 -0.66202626991883018 1.683956183687121e-015 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_MIDDLE_DER_4" -p "R_MIDDLE_DER_3";
	setAttr ".t" -type "double3" -0.31038460677842394 1.7763568394002505e-015 -4.384910923249663e-008 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -91.276695262256823 -7.0419799138107129 94.169749292941049 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_PINKY_SEC_DER" -p "R_MANO_DER";
	setAttr ".t" -type "double3" -0.43319151466700223 -1.7763568394002505e-015 0.41454110471883165 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 3.776090194142536e-015 10.717480086177586 4.0256256981235178e-014 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_PINKY_DER_1" -p "R_PINKY_SEC_DER";
	setAttr ".t" -type "double3" -0.93900487172164837 0.018299999999999983 0.0012880539597451696 ;
	setAttr ".r" -type "double3" 0 0 -6.8690539463847893 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.8253402455298918e-016 -0.58382984406832639 3.5826667094990362e-014 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_PINKY_DER_2" -p "R_PINKY_DER_1";
	setAttr ".t" -type "double3" -0.22386387786304152 -0.0012834718333039064 -0.0011813924729709158 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.5776148504194374e-016 -4.4208651669524919 4.0872462746534165e-015 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_PINKY_DER_3" -p "R_PINKY_DER_2";
	setAttr ".t" -type "double3" -0.216550915908444 -2.2742689562704754e-005 1.4084813549919417e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.5427488014607259e-015 4.6278950862123347 3.8179315266714501e-014 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_PINKY_DER_4" -p "R_PINKY_DER_3";
	setAttr ".t" -type "double3" -0.2375374398285528 -0.00081608389801779424 -0.001818484745074872 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 3.6830919891334522e-015 -10.340680161369011 -4.0703804182636821e-014 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_CANCEL_DER_1" -p "R_MANO_DER";
	setAttr ".t" -type "double3" -1.407714782672409 -0.087299999999997269 0.30991514889494365 ;
	setAttr ".r" -type "double3" 0 0 -7.9533971014506841 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.1968426297920325e-015 7.4037120803680816 1.8498446644539546e-014 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_CANCEL_DER_2" -p "R_CANCEL_DER_1";
	setAttr ".t" -type "double3" -0.37688572697765466 5.1725279325509632e-005 1.0101815620111587e-006 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.5682561420050562e-016 -1.67913633636118 1.0701695270120769e-014 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_CANCEL_DER_3" -p "R_CANCEL_DER_2";
	setAttr ".t" -type "double3" -0.27617428431757407 -0.00090493813639191956 -0.00022924363714060814 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.216196267485551e-017 0.10374482489103187 1.3433517136142169e-014 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_CANCEL_DER_4" -p "R_CANCEL_DER_3";
	setAttr ".t" -type "double3" -0.27929486814444271 0.00017075965380008995 3.4326640161452815e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.1780255018156101e-015 -5.8283205688978761 -2.3141375498091097e-014 ;
	setAttr ".radi" 0.56364323295275121;
createNode joint -n "R_INDEX_DER_1" -p "R_MANO_DER";
	setAttr ".t" -type "double3" -1.4663927500948279 8.8817841970012523e-015 -0.31665023847350371 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -2.4780754365965218e-016 3.1395128455277872 -9.0426600526576685e-015 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_INDEX_DER_2" -p "R_INDEX_DER_1";
	setAttr ".t" -type "double3" -0.37432968710616166 1.7763568394002505e-015 -5.035840844325179e-008 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 7.0709908367739506e-018 1.4908561152356763 5.4346636005714814e-016 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_INDEX_DER_3" -p "R_INDEX_DER_2";
	setAttr ".t" -type "double3" -0.32185703577986757 -3.5527136788005009e-015 4.1833592978601786e-009 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.6755386444493222e-016 1.6870984604159376 1.1379816712920705e-014 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_INDEX_DER_4" -p "R_INDEX_DER_3";
	setAttr ".t" -type "double3" -0.27904505841338256 0 2.6539098330058408e-007 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.6190191653275831e-015 -6.3174674211793009 -2.9337378471731352e-014 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_THUMB_DER_1" -p "R_MANO_DER";
	setAttr ".t" -type "double3" -0.60001686096056428 8.8817841970012523e-015 -0.54890738355821345 ;
	setAttr ".r" -type "double3" 41.295087426667322 0.68208271769190998 -19.761220231791302 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 5.1037687223593854e-014 -26.788481971200412 -2.1432934531327236e-013 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_THUMB_DER_2" -p "R_THUMB_DER_1";
	setAttr ".t" -type "double3" -0.47481790058111817 6.0231982406122597e-005 -5.2122310888691459e-005 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -5.6679810969500626e-015 3.3965354189381811 -1.9116908616137313e-013 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_THUMB_DER_3" -p "R_THUMB_DER_2";
	setAttr ".t" -type "double3" -0.26393540841874019 -0.0099621548596910969 -0.001870597333789803 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 8.3978020655970822e-015 -4.4339209495242971 -2.1692694655584343e-013 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_THUMB_DER_4" -p "R_THUMB_DER_3";
	setAttr ".t" -type "double3" -0.32141022692758625 0.00090660668941389133 0.0047160286968193077 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.603587775517759e-014 27.825867501786512 -6.4735306815253083e-014 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_CINTURA" -p "R_ROOT";
	setAttr ".t" -type "double3" -0.63833454827948621 -0.30318330547630618 5.4039316970270638e-017 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999999901 -55.116441788216029 -158.61636483523813 ;
	setAttr ".radi" 0.51593275491347201;
createNode joint -n "R_PIERNA_IZQ" -p "R_CINTURA";
	setAttr ".t" -type "double3" 1.4667798932451173 0.079214889486074608 -0.25807621444770795 ;
	setAttr ".r" -type "double3" 0 1.751016603660563 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.000000000000028 -19.407238163462182 -55.116441788216029 ;
	setAttr ".radi" 0.60997308065702804;
createNode joint -n "R_RODILLA_IZQ" -p "R_PIERNA_IZQ";
	setAttr ".t" -type "double3" 3.1232273924086247 5.773159728050814e-015 0.095478694683758469 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 1.0164089298295571e-014 -38.343303475263497 ;
	setAttr ".radi" 0.62926894798024147;
createNode joint -n "R_TALON_IZQ" -p "R_RODILLA_IZQ";
	setAttr ".t" -type "double3" 3.4971899122292527 0.0015896716984901138 -0.083820915652749017 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 178.63513760827794 1.097012964773052 -89.559602045571935 ;
	setAttr ".radi" 0.52608389778031572;
createNode joint -n "R_DEDOS_PIE_IZQ" -p "R_TALON_IZQ";
	setAttr ".t" -type "double3" 1.5042886904194366 3.3306690738754696e-016 2.3245294578089215e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -4.0740242154587478e-015 7.8000518948984514e-014 -5.9797672800990531 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_PUNTA_PIE_IZQ" -p "R_DEDOS_PIE_IZQ";
	setAttr ".t" -type "double3" 1.2158807939645544 0.046160354934911739 -1.5454654262127367e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -91.2983150864506 63.377534309703734 -65.783022821189448 ;
	setAttr ".radi" 0.59781307637981407;
createNode joint -n "R_PIERNA_DER" -p "R_CINTURA";
	setAttr ".t" -type "double3" -0.58159811089191571 -1.3488749607895789 -0.25807621481561621 ;
	setAttr ".r" -type "double3" 0 1.751016603660563 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90.000000000000099 19.407238163462207 124.88355821178392 ;
	setAttr ".radi" 0.60997308065702804;
createNode joint -n "R_RODILLA_DER" -p "R_PIERNA_DER";
	setAttr ".t" -type "double3" -3.1232332050953016 1.7460193943996671e-006 -0.095478872380630797 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 2.211479426955099e-015 -38.343303475263497 ;
	setAttr ".radi" 0.62926894798024147;
createNode joint -n "R_TALON_DER" -p "R_RODILLA_DER";
	setAttr ".t" -type "double3" -3.4971882105618395 -0.001590076924667061 0.083820867167230473 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 178.63513760828323 1.0970129647730664 -89.55960204557195 ;
	setAttr ".radi" 0.52608389778031572;
createNode joint -n "R_DEDOS_PIE_DER" -p "R_TALON_DER";
	setAttr ".t" -type "double3" -1.5042929908338489 -1.4673953000476914e-006 -2.2204460492503131e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.8800285304795015e-014 -5.5140496984009469e-013 -5.9797672800989927 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_PUNTA_PIE_DER" -p "R_DEDOS_PIE_DER";
	setAttr ".t" -type "double3" -0.98627085442002771 -3.8518170153434284e-007 -7.3274719625260332e-015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -91.298315086454409 63.377534309698675 -65.783022821192901 ;
	setAttr ".radi" 0.59781307637981407;
createNode joint -n "R_REV_IZQ_1";
	setAttr ".t" -type "double3" 1.2485268812659505 0 -1.3618286702918883 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 138.66574751091818 -88.34962290828436 -138.65395815421797 ;
	setAttr ".radi" 0.59614253979186849;
createNode joint -n "R_REV_IZQ_2" -p "R_REV_IZQ_1";
	setAttr ".t" -type "double3" 3.6730441767014632 0.06989517967514372 -0.07946415482729563 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -179.46902035323063 -1.119630195805954 155.7156767122427 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_REV_IZQ_3" -p "R_REV_IZQ_2";
	setAttr ".t" -type "double3" 1.2158807939645548 -0.046160354934911663 -1.4210854715202004e-014 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.0021732898087537e-016 -1.9187425638090287e-015 -5.9797672800990522 ;
	setAttr ".radi" 0.52608389778031561;
createNode joint -n "R_REV_IZQ_4" -p "R_REV_IZQ_3";
	setAttr ".t" -type "double3" 1.5042886904194366 -4.4408920985006262e-016 4.4408920985006262e-016 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -19.389530444065549 -89.999999999999972 0 ;
	setAttr ".radi" 0.52608389778031561;
createNode transform -n "DRIVER_LENGUA";
	setAttr ".rp" -type "double3" 0 15.364664664220429 0.95216732969087803 ;
	setAttr ".sp" -type "double3" 0 15.364664664220429 0.95216732969087803 ;
createNode nurbsCurve -n "DRIVER_LENGUAShape" -p "DRIVER_LENGUA";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 12 0 no 3
		13 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		-0.095054576344098862 14.937998494232401 2.784070644407747
		-0.095054576344098862 14.990400646525034 2.5991711276292619
		-0.1901091526881924 14.993775497405984 2.5928368060478149
		-1.7763568394002055e-015 15.001548072463356 2.3879192224264401
		0.19010915268819595 14.993775497405984 2.5928368060478149
		0.095054576344100639 14.990400646525034 2.5991711276292619
		0.095054576344100639 14.937998494232401 2.784070644407747
		0.095054576344099126 14.826937930802325 2.9423513477539252
		0.19010915268819595 14.830216389526351 2.9360020535020905
		-1.7763568394002102e-015 14.673096480845775 3.0737642491748312
		-0.1901091526881924 14.830216389526351 2.9360020535020905
		-0.095054576344100375 14.826937930802325 2.9423513477539252
		-0.095054576344098862 14.937998494232401 2.784070644407747
		;
createNode transform -n "DRIVER_COLUMNA_BOTTOM";
	setAttr ".rp" -type "double3" 0 9.9788611441405717 -0.31488087373940044 ;
	setAttr ".sp" -type "double3" 0 9.9788611441405717 -0.31488087373940044 ;
createNode nurbsCurve -n "DRIVER_COLUMNA_BOTTOMShape" -p "DRIVER_COLUMNA_BOTTOM";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		1.2042228757472391 9.9788611441405699 -2.5950621236227223
		7.459957194592308e-016 9.9788611441405699 -2.834596946690346
		-1.2042228757472411 9.9788611441405699 -2.5950621236227223
		-2.2251137349695171 9.9788611441405699 -1.9129246598433198
		-2.9072511987489196 9.9788611441405699 -0.89203380062104376
		-2.8993984655814793 9.9788611441405699 0.90626109680648725
		-1.3981997809080668 9.9788611441405699 2.2210802155941094
		-2.6071718574233702 9.9788611441405699 0.82620177273788076
		-2.1296914129663076 9.9788611441405699 -1.476212934827617
		2.6145321697228361e-016 9.9788611441405699 -2.4468941174522874
		2.1296914129663094 9.9788611441405699 -1.4762129348276156
		2.6071718574233702 9.9788611441405699 0.82620177273785145
		1.3981997809080688 9.9788611441405699 2.221080215594109
		2.899398465581478 9.9788611441405699 0.90626109680648725
		2.9072511987489196 9.9788611441405699 -0.89203380062104509
		2.2251137349695158 9.9788611441405699 -1.9129246598433203
		1.2042228757472391 9.9788611441405699 -2.5950621236227223
		7.459957194592308e-016 9.9788611441405699 -2.834596946690346
		-1.2042228757472411 9.9788611441405699 -2.5950621236227223
		;
createNode transform -n "MOVE_ALL";
	setAttr ".rp" -type "double3" 0 0 0.93937092674000233 ;
	setAttr ".sp" -type "double3" 0 0 0.93937092674000233 ;
createNode nurbsCurve -n "MOVE_ALLShape" -p "MOVE_ALL";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.7535085509530117 1.0737143171010578e-016 -1.5542641032221385
		-6.6842011011462129e-016 3.5874861514669284e-016 -5.6595650538571443
		-1.7535085509530084 1.0737143171010587e-016 -1.5542641032221398
		-5.8588095015880182 9.7323461632529058e-032 0.19924444773086686
		-1.7535085509530093 -1.0737143171010581e-016 1.9527529986838759
		-1.7653736440480694e-015 -3.5874861514669294e-016 6.0580539493188796
		1.7535085509530066 -1.0737143171010587e-016 1.9527529986838776
		5.8588095015880182 -1.9931749287385047e-031 0.19924444773087177
		1.7535085509530117 1.0737143171010578e-016 -1.5542641032221385
		-6.6842011011462129e-016 3.5874861514669284e-016 -5.6595650538571443
		-1.7535085509530084 1.0737143171010587e-016 -1.5542641032221398
		;
createNode transform -n "DRIVER_CINTURA";
	setAttr ".rp" -type "double3" 0 8.0082916844570846 0.13113021481561482 ;
	setAttr ".sp" -type "double3" 0 8.0082916844570846 0.13113021481561482 ;
createNode nurbsCurve -n "DRIVER_CINTURAShape" -p "DRIVER_CINTURA";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-2.5400809095018282 8.0082916844570846 -2.4089506946862116
		2.5400809095018246 8.0082916844570846 -2.4089506946862116
		2.5400809095018246 8.0082916844570846 2.6712111243174395
		-2.5400809095018282 8.0082916844570846 2.6712111243174395
		-2.5400809095018282 8.0082916844570846 -2.4089506946862116
		;
createNode transform -n "DRIVER_MANO_IZQ";
	setAttr ".rp" -type "double3" 7.4441288599560931 13.52245092162403 -0.66514120092053219 ;
	setAttr ".sp" -type "double3" 7.4441288599560922 13.52245092162403 -0.66514120092053219 ;
createNode nurbsCurve -n "DRIVER_MANO_IZQShape" -p "DRIVER_MANO_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 12 2 no 3
		17 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
		15
		10.6794934403021 13.52245092162403 -1.8098344995076223
		10.135199074793753 13.52245092162403 -2.1074207329150791
		8.0556720240699207 13.52245092162403 -1.7973385924712333
		7.5871250725464554 13.52245092162403 -1.4421673688232137
		7.4138643484085316 13.52245092162403 -0.50040499699323759
		7.6059529748850778 13.52245092162403 0.04443564295746661
		8.9760591668849212 13.52245092162403 1.1060311547253936
		10.000763988061118 13.52245092162403 1.3102492836036288
		10.059603296219644 13.52245092162403 0.46380428433561471
		11.047424284438414 13.522450921624026 0.65177695120686385
		11.595058325487225 13.52245092162403 -0.31542933484235991
		11.174474132863924 13.52245092162403 -1.3316887945756632
		10.6794934403021 13.52245092162403 -1.8098344995076223
		10.135199074793753 13.52245092162403 -2.1074207329150791
		8.0556720240699207 13.52245092162403 -1.7973385924712333
		;
createNode transform -n "DRIVER_ROOT";
	setAttr ".rp" -type "double3" 0 8.7132271986612011 0.18069868322541349 ;
	setAttr ".sp" -type "double3" 0 8.7132271986612011 0.18069868322541349 ;
createNode nurbsCurve -n "DRIVER_ROOTShape" -p "DRIVER_ROOT";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.8826837901139726 8.7132271986612011 -2.7019851068885545
		-4.6510620579287864e-016 8.7132271986612011 -3.896031828786839
		-2.8826837901139695 8.7132271986612011 -2.7019851068885559
		-4.0767305120122526 8.7132271986612011 0.1806986832254123
		-2.8826837901139704 8.7132271986612011 3.0633824733393822
		-1.2283984652244298e-015 8.7132271986612011 4.2574291952376671
		2.8826837901139681 8.7132271986612011 3.0633824733393835
		4.0767305120122526 8.7132271986612011 0.18069868322541568
		2.8826837901139726 8.7132271986612011 -2.7019851068885545
		-4.6510620579287864e-016 8.7132271986612011 -3.896031828786839
		-2.8826837901139695 8.7132271986612011 -2.7019851068885559
		;
createNode transform -n "DRIVER_BOCA";
	setAttr ".rp" -type "double3" -3.1554436208840472e-030 14.555369654099279 0.28139203617900543 ;
	setAttr ".sp" -type "double3" -3.1554436208840472e-030 14.555369654099279 0.28139203617900543 ;
createNode nurbsCurve -n "DRIVER_BOCAShape" -p "DRIVER_BOCA";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.68825483906168894 14.177044418130793 2.6681766796278201
		-1.2633964012575297e-016 13.864573220614348 2.4877124009893126
		-0.68825483906168805 14.177044418130953 2.6681766796278139
		-0.97333932776995225 14.385043256585785 2.7883041046121022
		-0.78304100892113226 13.706965249063499 2.396687662966638
		-3.3367737969220759e-016 13.426096142000928 2.2344748215888122
		0.78304100892115591 13.706965249063499 2.396687662966638
		0.97333932776995225 14.385043256585567 2.7883041046120893
		0.68825483906168894 14.177044418130793 2.6681766796278201
		-1.2633964012575297e-016 13.864573220614348 2.4877124009893126
		-0.68825483906168805 14.177044418130953 2.6681766796278139
		;
createNode transform -n "DRIVER_DIENTES_BOTTOM";
	setAttr ".rp" -type "double3" -2.8842726847143244e-030 15.095205210404005 1.9070332000512029 ;
	setAttr ".sp" -type "double3" -2.8842726847143244e-030 15.095205210404005 1.9070332000512029 ;
createNode nurbsCurve -n "DRIVER_DIENTES_BOTTOMShape" -p "DRIVER_DIENTES_BOTTOM";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.19032212897928349 13.728979772643694 2.4078279271894028
		-4.3611460165543611e-017 13.691004677199004 2.3868161989856147
		-0.19032212897928935 13.728979772643694 2.4078279271894028
		-0.30570524273181365 13.880932322112987 2.4935128195351157
		-0.27029965998435718 13.64573729600977 2.3603016868020235
		-1.151828336545368e-016 13.548316326395332 2.3051238289648914
		0.27029965998435684 13.64573729600977 2.3603016868020235
		0.30570524273182575 13.880932322112988 2.4935128195351157
		0.19032212897928349 13.728979772643694 2.4078279271894028
		-4.3611460165543611e-017 13.691004677199004 2.3868161989856147
		-0.19032212897928935 13.728979772643694 2.4078279271894028
		;
createNode transform -n "DRIVER_RODILLA_IZQ";
	setAttr ".rp" -type "double3" 1.1685239477799845 4.2872621762102092 4.0907984739644725 ;
	setAttr ".sp" -type "double3" 1.1685239477799847 4.2872621762102092 4.0907984739644725 ;
createNode nurbsCurve -n "DRIVER_RODILLA_IZQShape" -p "DRIVER_RODILLA_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
		25
		1.0117061005169596 4.2872621762102092 4.0907984739644725
		0.82413694003702953 4.4594556800816862 4.0907984739644725
		0.73804018810129035 4.3733589281459473 4.0907984739644725
		0.74267719007322586 4.7131089339169669 4.0907984739644725
		1.0824271958442455 4.7177459358889031 4.0907984739644725
		0.99633044390850678 4.6316491839531633 4.0907984739644725
		1.1685239477799867 4.4440800234732363 4.0907984739644725
		1.3407174516514619 4.6316491839531642 4.0907984739644725
		1.2546206997157232 4.7177459358889031 4.0907984739644725
		1.5943707054867433 4.7131089339169678 4.0907984739644725
		1.5990077074586782 4.3733589281459473 4.0907984739644725
		1.5129109555229394 4.4594556800816862 4.0907984739644725
		1.325341795043012 4.287262176210211 4.0907984739644725
		1.5129109555229392 4.1150686723387313 4.0907984739644725
		1.5990077074586779 4.2011654242744703 4.0907984739644725
		1.5943707054867431 3.8614154185034502 4.0907984739644725
		1.2546206997157228 3.8567784165315149 4.0907984739644725
		1.3407174516514619 3.9428751684672538 4.0907984739644725
		1.1685239477799849 4.1304443289471839 4.0907984739644725
		0.99633044390850656 3.9428751684672534 4.0907984739644725
		1.0824271958442453 3.8567784165315149 4.0907984739644725
		0.74267719007322608 3.8614154185034506 4.0907984739644725
		0.73804018810129035 4.2011654242744694 4.0907984739644725
		0.82413694003702909 4.1150686723387313 4.0907984739644725
		1.0117061005169596 4.2872621762102092 4.0907984739644725
		;
createNode transform -n "DRIVER_COLUMNA_MIDDLE";
	setAttr ".rp" -type "double3" 2.4651903288156619e-032 11.374108204518429 -0.6579744131765789 ;
	setAttr ".sp" -type "double3" 2.4651903288156619e-032 11.374108204518429 -0.6579744131765789 ;
createNode nurbsCurve -n "DRIVER_COLUMNA_MIDDLEShape" -p "DRIVER_COLUMNA_MIDDLE";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		1.3652596481092905 11.374108204518427 -3.2430768170064481
		8.4575527832251561e-016 11.374108204518427 -3.5146438456997871
		-1.3652596481092925 11.374108204518427 -3.2430768170064481
		-2.5226708909034743 11.374108204518427 -2.4697193492837495
		-3.2960283586261729 11.374108204518427 -1.3123081064895676
		-3.2871255052285218 11.374108204518427 0.72646686474255662
		-1.5851764480761323 11.374108204518427 2.2171124284464416
		-2.9558203919831456 11.374108204518427 0.63570147005766497
		-2.4144880549985888 11.374108204518427 -1.9746075987698144
		2.9641649746865001e-016 11.374108204518427 -3.0750947897261738
		2.4144880549985905 11.374108204518427 -1.9746075987698131
		2.9558203919831456 11.374108204518427 0.63570147005763178
		1.5851764480761346 11.374108204518427 2.2171124284464407
		3.2871255052285204 11.374108204518427 0.72646686474255662
		3.2960283586261729 11.374108204518427 -1.312308106489569
		2.522670890903473 11.374108204518427 -2.4697193492837504
		1.3652596481092905 11.374108204518427 -3.2430768170064481
		8.4575527832251561e-016 11.374108204518427 -3.5146438456997871
		-1.3652596481092925 11.374108204518427 -3.2430768170064481
		;
createNode transform -n "DRIVER_COLUMNA_TOP";
	setAttr ".rp" -type "double3" -3.2047474274603605e-031 12.815101070154579 -0.74184172281677785 ;
	setAttr ".sp" -type "double3" -3.2047474274603605e-031 12.815101070154579 -0.74184172281677785 ;
createNode nurbsCurve -n "DRIVER_COLUMNA_TOPShape" -p "DRIVER_COLUMNA_TOP";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.9015499470564923 12.662494491463292 -2.6433916698732629
		-5.6051947860544743e-016 12.815101070154579 -5.6548848784387893
		-1.9015499470564874 12.662494491463292 -2.6433916698732647
		-4.9130431556220113 11.746855019315579 -0.74184172281677929
		-1.9015499470564881 12.662494491463292 1.1597082242397088
		-1.4803957863205777e-015 12.815101070154579 4.1712014328052351
		1.9015499470564858 12.662494491463292 1.1597082242397101
		4.9130431556220113 11.746855019315579 -0.74184172281677518
		1.9015499470564923 12.662494491463292 -2.6433916698732629
		-5.6051947860544743e-016 12.815101070154579 -5.6548848784387893
		-1.9015499470564874 12.662494491463292 -2.6433916698732647
		;
createNode transform -n "DRIVER_CODO_IZQ";
	setAttr ".rp" -type "double3" 5.0088095415392431 13.357047335818008 -4.1085417205481116 ;
	setAttr ".sp" -type "double3" 5.0088095415392431 13.357047335818008 -4.1085417205481116 ;
createNode nurbsCurve -n "DRIVER_CODO_IZQShape" -p "DRIVER_CODO_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
		25
		4.8519916942763919 13.357047335818487 -4.1085417205481143
		4.6644225337964542 13.529240839689971 -4.1085417205481143
		4.5783257818607126 13.443144087754227 -4.1085417205481143
		4.5829627838326479 13.782894093525259 -4.1085417205481143
		4.92271278960368 13.787531095497195 -4.1085417205481143
		4.8366160376679384 13.701434343561452 -4.1085417205481143
		5.0088095415394243 13.513865183081519 -4.1085417205481143
		5.1810030454109048 13.701434343561452 -4.1085417205481143
		5.0949062934751632 13.787531095497195 -4.1085417205481143
		5.4346562992461962 13.782894093525261 -4.1085417205481143
		5.4392933012181306 13.443144087754227 -4.1085417205481143
		5.3531965492823881 13.529240839689971 -4.1085417205481143
		5.1656273888024549 13.357047335818489 -4.1085417205481143
		5.3531965492823881 13.184853831947004 -4.1085417205481143
		5.4392933012181306 13.270950583882744 -4.1085417205481143
		5.4346562992461953 12.93120057811171 -4.1085417205481143
		5.0949062934751623 12.926563576139776 -4.1085417205481143
		5.1810030454109048 13.012660328075521 -4.1085417205481143
		5.0088095415394225 13.200229488555458 -4.1085417205481143
		4.8366160376679384 13.012660328075521 -4.1085417205481143
		4.92271278960368 12.926563576139776 -4.1085417205481143
		4.5829627838326488 12.93120057811171 -4.1085417205481143
		4.5783257818607126 13.270950583882744 -4.1085417205481143
		4.6644225337964542 13.184853831947004 -4.1085417205481143
		4.8519916942763919 13.357047335818487 -4.1085417205481143
		;
createNode transform -n "DRIVER_CODO_DER";
	setAttr ".rp" -type "double3" -5.00881 13.357000000000001 -4.1085439153295784 ;
	setAttr ".sp" -type "double3" -5.00881 13.357000000000001 -4.1085439153295784 ;
createNode nurbsCurve -n "DRIVER_CODO_DERShape" -p "DRIVER_CODO_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
		25
		-5.1656278472630257 13.357000000000001 -4.1085439153295784
		-5.3531970077429554 13.529193503871479 -4.1085439153295784
		-5.4392937596786943 13.443096751935739 -4.1085439153295784
		-5.434656757706759 13.782846757706759 -4.1085439153295784
		-5.0949067519357394 13.787483759678695 -4.1085439153295784
		-5.1810035038714783 13.701387007742955 -4.1085439153295784
		-5.0088099999999987 13.513817847263029 -4.1085439153295784
		-4.8366164961285234 13.701387007742955 -4.1085439153295784
		-4.9227132480642624 13.787483759678695 -4.1085439153295784
		-4.5829632422932418 13.782846757706761 -4.1085439153295784
		-4.5783262403213065 13.443096751935739 -4.1085439153295784
		-4.6644229922570455 13.529193503871479 -4.1085439153295784
		-4.8519921527369734 13.357000000000003 -4.1085439153295784
		-4.6644229922570464 13.184806496128523 -4.1085439153295784
		-4.5783262403213074 13.270903248064261 -4.1085439153295784
		-4.5829632422932418 12.931153242293242 -4.1085439153295784
		-4.9227132480642624 12.926516240321307 -4.1085439153295784
		-4.8366164961285234 13.012612992257045 -4.1085439153295784
		-5.0088100000000004 13.200182152736977 -4.1085439153295784
		-5.1810035038714783 13.012612992257045 -4.1085439153295784
		-5.0949067519357403 12.926516240321307 -4.1085439153295784
		-5.434656757706759 12.931153242293242 -4.1085439153295784
		-5.4392937596786943 13.270903248064261 -4.1085439153295784
		-5.3531970077429563 13.184806496128523 -4.1085439153295784
		-5.1656278472630257 13.357000000000001 -4.1085439153295784
		;
createNode transform -n "DRIVER_CLAVICULA_IZQ";
	setAttr ".rp" -type "double3" 1.0769893143151119 12.977088858280743 -0.74184172281677774 ;
	setAttr ".sp" -type "double3" 1.0769893143151119 12.977088858280743 -0.74184172281677774 ;
createNode nurbsCurve -n "DRIVER_CLAVICULA_IZQShape" -p "DRIVER_CLAVICULA_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		1.3179838919065419 14.616112858317367 -0.46173336245593855
		1.2845604854455375 14.516709429347966 -0.93580664033890337
		1.2008379562754699 14.26771307132552 -1.4098799182218669
		0.85647140142856271 14.388932020086729 -1.4098799182218669
		1.3317864269147521 13.71756514434677 -2.3580264739877919
		1.9918314225676199 14.007178595083706 -1.4098799182218669
		1.7685179668449913 14.076836358824007 -1.4098799182218669
		1.852240496015066 14.325832716846453 -0.93580664033890337
		1.8856639024760811 14.425236145815852 -0.46173336245593855
		1.852240496015066 14.325832716846453 0.012339915427026282
		1.7685179668449913 14.076836358824007 0.48641319330999044
		1.9918314225676199 14.007178595083706 0.48641319330999044
		1.3317864269147521 13.71756514434677 1.4345597490759179
		0.85647140142856271 14.388932020086729 0.48641319330999044
		1.2008379562754699 14.26771307132552 0.48641319330999044
		1.2845604854455375 14.516709429347966 0.012339915427026282
		1.3179838919065419 14.616112858317367 -0.46173336245593855
		;
createNode transform -n "DRIVER_CLAVICULA_DER";
	setAttr ".rp" -type "double3" -1.0769900000000003 12.977099999999998 -0.74184200000000056 ;
	setAttr ".sp" -type "double3" -1.0769900000000003 12.977099999999998 -0.74184200000000056 ;
createNode nurbsCurve -n "DRIVER_CLAVICULA_DERShape" -p "DRIVER_CLAVICULA_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-1.3179845775914303 14.616124000036622 -0.46173363963916136
		-1.2845611711304259 14.516720571067221 -0.93580691752212619
		-1.2008386419603583 14.267724213044776 -1.4098801954050897
		-0.85647208711345113 14.388943161805985 -1.4098801954050897
		-1.3317871125996406 13.717576286066025 -2.3580267511710149
		-1.9918321082525083 14.007189736802962 -1.4098801954050897
		-1.7685186525298797 14.076847500543263 -1.4098801954050897
		-1.8522411816999544 14.325843858565708 -0.93580691752212619
		-1.8856645881609695 14.425247287535107 -0.46173363963916136
		-1.8522411816999544 14.325843858565708 0.012339638243803464
		-1.7685186525298797 14.076847500543263 0.48641291612676762
		-1.9918321082525083 14.007189736802962 0.48641291612676762
		-1.3317871125996406 13.717576286066025 1.4345594718926953
		-0.85647208711345113 14.388943161805985 0.48641291612676762
		-1.2008386419603583 14.267724213044776 0.48641291612676762
		-1.2845611711304259 14.516720571067221 0.012339638243803464
		-1.3179845775914303 14.616124000036622 -0.46173363963916136
		;
createNode transform -n "DRIVER_MANO_DER";
	setAttr ".rp" -type "double3" -7.4441299999999995 13.522500000000003 -0.6651410000000002 ;
	setAttr ".sp" -type "double3" -7.44413 13.522500000000003 -0.6651410000000002 ;
createNode nurbsCurve -n "DRIVER_MANO_DERShape" -p "DRIVER_MANO_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 12 2 no 3
		17 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
		15
		-10.679494580346011 13.522500000000003 -1.8098342708138326
		-10.135200214837663 13.522500000000003 -2.1074205042212908
		-8.0556731641138324 13.522500000000003 -1.797338363777444
		-7.58712621259036 13.522500000000004 -1.4421671401294232
		-7.4138654884524371 13.522500000000004 -0.50040476829944835
		-7.6059541149289833 13.522500000000004 0.044435871651255926
		-8.9760603069288276 13.522500000000003 1.1060313834191833
		-10.000765128105026 13.522500000000003 1.3102495122974194
		-10.059604436263555 13.522500000000003 0.46380451302940423
		-11.047425424482325 13.522500000000001 0.65177717990065354
		-11.595059465531133 13.522500000000003 -0.31542910614857045
		-11.174475272907834 13.522500000000003 -1.3316885658818736
		-10.679494580346011 13.522500000000003 -1.8098342708138326
		-10.135200214837663 13.522500000000003 -2.1074205042212908
		-8.0556731641138324 13.522500000000003 -1.797338363777444
		;
createNode transform -n "DRIVER_DIENTES_TOP";
	setAttr ".rp" -type "double3" -3.1061398143077343e-030 15.438736928052469 1.9131676950092116 ;
	setAttr ".sp" -type "double3" -3.1061398143077343e-030 15.438736928052469 1.9131676950092116 ;
createNode nurbsCurve -n "DRIVER_DIENTES_TOPShape" -p "DRIVER_DIENTES_TOP";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.19032212897928694 13.927299650033437 2.5257338222828327
		-4.3611460165471726e-017 13.965274745477945 2.5467455504866505
		-0.19032212897928646 13.927299650033437 2.5257338222828327
		-0.30570524273181959 13.775347100564055 2.4400489299371628
		-0.27029965998435707 14.010542126667247 2.5732600626702489
		-1.1518283365450278e-016 14.107963096281672 2.6284379205073662
		0.27029965998435679 14.010542126667247 2.5732600626702489
		0.30570524273181959 13.775347100564055 2.4400489299371628
		0.19032212897928694 13.927299650033437 2.5257338222828327
		-4.3611460165471726e-017 13.965274745477945 2.5467455504866505
		-0.19032212897928646 13.927299650033437 2.5257338222828327
		;
createNode transform -n "DRIVER_CABEZA";
	setAttr ".rp" -type "double3" -1.035379938102578e-030 13.783387281455061 -0.62747720967105192 ;
	setAttr ".sp" -type "double3" -1.035379938102578e-030 13.783387281455061 -0.62747720967105192 ;
createNode nurbsCurve -n "DRIVER_CABEZAShape" -p "DRIVER_CABEZA";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 12 2 no 3
		17 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
		15
		1.7283324432398732 20.355083512494872 -0.62747720967105247
		-1.1983127091512918e-015 20.532210891280272 -0.62747720967105258
		-1.7283324432398679 20.355083512494872 -0.62747720967105247
		-2.734865953608177 20.09077901438998 -0.62747720967105225
		-2.9552280506854878 19.291874757958148 -0.62747720967105203
		-2.2895532905713569 14.808448843168968 -0.62747720967105181
		-1.8645969174860757 14.122637115614072 -0.62747720967105158
		-2.4387257712677327e-015 13.827954557196019 -0.62747720967105147
		1.8645969174860733 14.122637115614072 -0.62747720967105158
		2.2895532905713543 14.808448843168964 -0.62747720967105181
		2.9552280506854869 19.291874757958141 -0.62747720967105203
		2.734865953608177 20.09077901438998 -0.62747720967105225
		1.7283324432398732 20.355083512494872 -0.62747720967105247
		-1.1983127091512918e-015 20.532210891280272 -0.62747720967105258
		-1.7283324432398679 20.355083512494872 -0.62747720967105247
		;
createNode nurbsCurve -n "DRIVER_CABEZA1Shape" -p "DRIVER_CABEZA";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 12 2 no 3
		17 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
		15
		-2.2204460492503131e-016 20.355083512494872 -2.3558096529109251
		-6.6613381477509392e-016 20.532210891280272 -0.6274772096710507
		-8.8817841970012523e-016 20.355083512494872 1.100855233568816
		-8.8817841970012523e-016 20.09077901438998 2.1073887439371251
		-7.7715611723760958e-016 19.291874757958148 2.3277508410144359
		-4.4408920985006262e-016 14.808448843168968 1.662076080900305
		-1.1102230246251565e-016 14.122637115614072 1.2371197078150238
		4.4408920985006262e-016 13.827954557196019 -0.62747720967104947
		7.7715611723760958e-016 14.122637115614072 -2.4920741271571254
		6.6613381477509392e-016 14.808448843168964 -2.9170305002424062
		5.5511151231257827e-016 19.291874757958141 -3.5827052603565388
		2.2204460492503131e-016 20.09077901438998 -3.3623431632792289
		-2.2204460492503131e-016 20.355083512494872 -2.3558096529109251
		-6.6613381477509392e-016 20.532210891280272 -0.6274772096710507
		-8.8817841970012523e-016 20.355083512494872 1.100855233568816
		;
createNode transform -n "DRIVER_OJOS";
	setAttr ".rp" -type "double3" 0 17.046100073815637 5.8284431416822873 ;
	setAttr ".sp" -type "double3" 0 17.046100073815637 5.8284431416822873 ;
createNode nurbsCurve -n "DRIVER_OJOSShape" -p "DRIVER_OJOS";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.4696094967039177 18.247960631776081 5.8284431416822944
		-3.9536194549336448e-016 17.363462526569442 5.8284431416822944
		-1.4696094967039146 18.247960631776081 5.8284431416822944
		-2.0783416816309757 17.04610007381563 5.8284431416822944
		-1.4696094967039155 15.844239515855183 5.8284431416822926
		-4.6801958467589111e-016 16.728737621061821 5.8284431416822926
		1.4696094967039133 15.844239515855179 5.8284431416822926
		2.0783416816309757 17.04610007381563 5.8284431416822944
		1.4696094967039177 18.247960631776081 5.8284431416822944
		-3.9536194549336448e-016 17.363462526569442 5.8284431416822944
		-1.4696094967039146 18.247960631776081 5.8284431416822944
		;
createNode transform -n "DRIVER_OJO_IZQ";
	setAttr ".rp" -type "double3" 0.78837371753915575 16.999684024249976 5.8284431416822873 ;
	setAttr ".sp" -type "double3" 0.78837371753915575 16.999684024249976 5.8284431416822873 ;
createNode nurbsCurve -n "DRIVER_OJO_IZQShape" -p "DRIVER_OJO_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.3277741200712609 17.539084426782757 5.8284431416825271
		0.78837371753920393 17.762511389061082 5.8284431416825271
		0.24897331500714312 17.539084426782757 5.8284431416825271
		0.025546352728856022 16.999684024250698 5.8284431416825253
		0.2489733150071429 16.460283621718563 5.8284431416825253
		0.78837371753920349 16.236856659440143 5.8284431416825253
		1.3277741200712596 16.460283621718563 5.8284431416825253
		1.5512010823495588 16.999684024250698 5.8284431416825253
		1.3277741200712609 17.539084426782757 5.8284431416825271
		0.78837371753920393 17.762511389061082 5.8284431416825271
		0.24897331500714312 17.539084426782757 5.8284431416825271
		;
createNode transform -n "DRIVER_PIE_IZQ";
	setAttr ".rp" -type "double3" 1.2523840219923328 0.97864343443490087 -0.22463545383475858 ;
	setAttr ".sp" -type "double3" 1.2523840219923328 0.97864343443490087 -0.22463545383475858 ;
createNode nurbsCurve -n "DRIVER_PIE_IZQShape" -p "DRIVER_PIE_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 12 2 no 3
		17 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
		15
		1.7008809096009774 0.11105763332017138 -1.1368534757527833
		1.2974439911406468 0.11105763332017138 -1.2102564284707635
		0.84779159043750729 0.11105763332017127 -1.1368534757527833
		0.48679029738533997 0.11105763332017127 -0.59882253279522968
		0.57390457015753427 0.11105763332017127 0.83316592602067929
		0.45711038284078975 0.11105763332017127 1.8006066081764065
		0.7399384194643025 0.11105763332017127 2.5578105099426267
		1.2406766552341819 0.11105763332017127 2.6802096601688072
		1.6331439074129264 0.11105763332017127 2.4185958391146443
		1.9148490807455258 0.11105763332017127 1.8691812352684924
		1.9316081576022133 0.11105763332017127 1.253880819484817
		2.1351604843098455 0.11105763332017127 -0.3357639545392842
		1.7008809096009774 0.11105763332017138 -1.1368534757527833
		1.2974439911406468 0.11105763332017138 -1.2102564284707635
		0.84779159043750729 0.11105763332017127 -1.1368534757527833
		;
createNode transform -n "DRIVER_PIE_DER";
	setAttr ".rp" -type "double3" -1.2523799999999965 0.97864299999999638 -0.22463500000000003 ;
	setAttr ".sp" -type "double3" -1.2523799999999965 0.97864299999999638 -0.22463500000000003 ;
createNode nurbsCurve -n "DRIVER_PIE_DERShape" -p "DRIVER_PIE_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 12 2 no 3
		17 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
		15
		-1.7008764084603292 0.1110580000000001 -1.1368537398612002
		-1.2974394899999981 0.1110580000000001 -1.2102566925791804
		-0.84778708929685886 0.1110580000000001 -1.1368537398612002
		-0.48678579624469154 0.1110580000000001 -0.59882279690364681
		-0.57390006901688584 0.11105799999999999 0.83316566191226227
		-0.45710588170014138 0.11105799999999999 1.8006063440679894
		-0.73993391832365396 0.11105799999999999 2.5578102458342098
		-1.2406721540935333 0.11105799999999999 2.6802093960603903
		-1.6331394062722779 0.11105799999999999 2.4185955750062273
		-1.9148445796048772 0.11105799999999999 1.8691809711600755
		-1.9316036564615648 0.1110580000000001 1.2538805553764001
		-2.1351559831691977 0.11105799999999999 -0.33576421864770123
		-1.7008764084603292 0.1110580000000001 -1.1368537398612002
		-1.2974394899999981 0.1110580000000001 -1.2102566925791804
		-0.84778708929685886 0.1110580000000001 -1.1368537398612002
		;
createNode transform -n "DRIVER_OJO_DER";
	setAttr ".rp" -type "double3" -0.78837371753915497 16.999684024249984 5.8284431416822873 ;
	setAttr ".sp" -type "double3" -0.78837371753915497 16.999684024249984 5.8284431416822873 ;
createNode nurbsCurve -n "DRIVER_OJO_DERShape" -p "DRIVER_OJO_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-0.24897331500711994 17.539084426782008 5.8284431416822873
		-0.78837371753915109 17.762511389060279 5.8284431416822873
		-1.3277741200711821 17.539084426782008 5.8284431416822873
		-1.551201082349456 16.999684024249976 5.8284431416822873
		-1.3277741200711826 16.460283621717945 5.8284431416822873
		-0.78837371753915131 16.23685665943967 5.8284431416822873
		-0.24897331500712039 16.460283621717945 5.8284431416822873
		-0.0255463527288462 16.999684024249976 5.8284431416822873
		-0.24897331500711994 17.539084426782008 5.8284431416822873
		-0.78837371753915109 17.762511389060279 5.8284431416822873
		-1.3277741200711821 17.539084426782008 5.8284431416822873
		;
createNode transform -n "DRIVER_PINKY_SEC_IZQ";
	setAttr ".rp" -type "double3" 7.9021667701099556 13.522450921624028 -1.0520531515461713 ;
	setAttr ".sp" -type "double3" 7.9021667701099556 13.522450921624028 -1.0520531515461713 ;
createNode nurbsCurve -n "DRIVER_PINKY_SEC_IZQShape" -p "DRIVER_PINKY_SEC_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 2.2057469059999999 2.7203605089999998 2.9815836839999998 3 4
		 5 6 7 7.0350735120000003 7.277906518 7.8366471000000004 8 9 10 11 12
		19
		8.1502246879202609 13.79181554351932 -1.3059303974912253
		7.9021667701099902 13.791815543519377 -1.1955056471514633
		7.6315615475962257 13.79181554351932 -1.1731635428597604
		7.6207713767460188 13.742604441423676 -1.2153161110838455
		7.5929982439395305 13.627276815775748 -1.3238138255022545
		7.5793328428344822 13.505819555361732 -1.3771986847775235
		7.5890378780898287 13.40469060349406 -1.3392852757685527
		7.6135906913904234 13.298117980892235 -1.2433679680518206
		7.6245140084322394 13.253086299728817 -1.2006952547805883
		7.9021667701099947 13.253086299728761 -1.1955056471514638
		8.1431771487562763 13.253086299728817 -1.3334621094120465
		8.1321603829745612 13.29848960964563 -1.3764998868180922
		8.1077010184140192 13.404690603494062 -1.4720521304000718
		8.0979959831586683 13.505819555361732 -1.5099655394090421
		8.1116613842637939 13.627276815775753 -1.4565806801337755
		8.1396613996644653 13.743550268776685 -1.3471966327587048
		8.1502246879202609 13.79181554351932 -1.3059303974912253
		7.9021667701099902 13.791815543519377 -1.1955056471514633
		7.6315615475962257 13.79181554351932 -1.1731635428597604
		;
createNode transform -n "DRIVER_PINKY_SEC_DER";
	setAttr ".rp" -type "double3" -7.90217 13.522499999999997 -1.0520499999999997 ;
	setAttr ".sp" -type "double3" -7.90217 13.522499999999997 -1.0520499999999997 ;
createNode nurbsCurve -n "DRIVER_PINKY_SEC_DERShape" -p "DRIVER_PINKY_SEC_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 2.2057469059999999 2.7203605089999998 2.9815836839999998 3 4
		 5 6 7 7.0350735120000003 7.277906518 7.8366471000000004 8 9 10 11 12
		19
		-8.1502279178101702 13.791864621895247 -1.3059272459450577
		-7.9021700000000488 13.791864621895304 -1.1955024956052931
		-7.631564777486278 13.791864621895277 -1.1731603913135948
		-7.6207746066360391 13.742653519799603 -1.2153129595376799
		-7.5930014738295588 13.627325894151705 -1.32381067395609
		-7.5793360727245158 13.505868633737622 -1.3771955332313612
		-7.5890411079798588 13.404739681870018 -1.3392821242223847
		-7.6135939212804553 13.298167059268213 -1.2433648165056519
		-7.6245172383222908 13.253135378104796 -1.2006921032344207
		-7.9021700000000532 13.253135378104709 -1.1955024956052931
		-8.1431803786461732 13.253135378104766 -1.3334589578658897
		-8.1321636128645949 13.298538688021544 -1.3764967352719331
		-8.1077042483039854 13.404739681869989 -1.4720489788538982
		-8.0979992130486576 13.505868633737689 -1.5099623878628876
		-8.1116646141536872 13.62732589415171 -1.4565775285876139
		-8.1396646295543746 13.743599347152642 -1.3471934812125395
		-8.1502279178101702 13.791864621895247 -1.3059272459450577
		-7.9021700000000488 13.791864621895304 -1.1955024956052931
		-7.631564777486278 13.791864621895277 -1.1731603913135948
		;
createNode transform -n "DRIVER_TOE_IZQ";
	setAttr ".rp" -type "double3" 1.2523840219923323 0.056667576726437241 2.0854951605329939 ;
	setAttr ".sp" -type "double3" 1.2523840219923323 0.056667576726437241 2.0854951605329939 ;
createNode nurbsCurve -n "DRIVER_TOE_IZQShape" -p "DRIVER_TOE_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 10 2 no 3
		15 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		1.5817258166959365 0.38989571262963429 2.0854951605329939
		1.2523840219923321 0.53720253739936519 2.0854951605329939
		0.92304222728872731 0.38989571262963474 2.0854951605329939
		0.7194978042460094 0.13381545094841038 2.0854951605329939
		0.71949780424600895 0.032228881233570039 2.0854951605329939
		0.92304222728872731 0.0020708781135956311 2.0854951605329939
		1.2523840219923321 0.0020708781134775034 2.0854951605329939
		1.5817258166959365 0.0020708781135958532 2.0854951605329939
		1.7852702397386555 0.032228881233569984 2.0854951605329939
		1.7852702397386555 0.13381545094841027 2.0854951605329939
		1.5817258166959365 0.38989571262963429 2.0854951605329939
		1.2523840219923321 0.53720253739936519 2.0854951605329939
		0.92304222728872731 0.38989571262963474 2.0854951605329939
		;
createNode transform -n "DRIVER_BALL_IZQ";
	setAttr ".rp" -type "double3" 1.2523840219923326 0.47923647795466817 1.1943350024972175 ;
	setAttr ".sp" -type "double3" 1.2523840219923326 0.47923647795466817 1.1943350024972175 ;
createNode nurbsCurve -n "DRIVER_BALL_IZQShape" -p "DRIVER_BALL_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 10 2 no 3
		15 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		1.7527355794904216 0.98247409247610495 1.1943350024972175
		1.2977442132479411 1.1060948465823448 1.1943350024972172
		0.8427528470054606 0.98247409247610529 1.1943350024972172
		0.65239631196180636 0.60870134391019448 1.1943350024972175
		0.72545985256432011 0.42990461985423684 1.1943350024972175
		0.89889727568469779 0.56010959717246123 1.1943350024972175
		1.2977442132479411 0.67425873133537473 1.1943350024972175
		1.6965911508111853 0.56010959717246134 1.1943350024972177
		1.8700285739315625 0.429904619854237 1.1943350024972177
		1.9430921145340776 0.60870138257533035 1.1943350024972177
		1.7527355794904216 0.98247409247610495 1.1943350024972175
		1.2977442132479411 1.1060948465823448 1.1943350024972172
		0.8427528470054606 0.98247409247610529 1.1943350024972172
		;
createNode transform -n "DRIVER_TOE_DER";
	setAttr ".rp" -type "double3" -1.2523799999999963 0.056667576726437241 2.0854951605329939 ;
	setAttr ".sp" -type "double3" -1.2523799999999963 0.056667576726437241 2.0854951605329939 ;
createNode nurbsCurve -n "DRIVER_TOE_DERShape" -p "DRIVER_TOE_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 10 2 no 3
		15 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		-0.92303820529639213 0.38989571262963429 2.0854951605329939
		-1.2523799999999965 0.5372025373993653 2.0854951605329939
		-1.5817217947036013 0.38989571262963474 2.0854951605329939
		-1.785266217746319 0.13381545094841044 2.0854951605329939
		-1.7852662177463199 0.032228881233570039 2.0854951605329939
		-1.5817217947036013 0.0020708781135956311 2.0854951605329939
		-1.2523799999999965 0.0020708781134775034 2.0854951605329939
		-0.92303820529639191 0.0020708781135958532 2.0854951605329939
		-0.71949378225367333 0.032228881233569984 2.0854951605329939
		-0.71949378225367311 0.13381545094841032 2.0854951605329939
		-0.92303820529639213 0.38989571262963429 2.0854951605329939
		-1.2523799999999965 0.5372025373993653 2.0854951605329939
		-1.5817217947036013 0.38989571262963474 2.0854951605329939
		;
createNode transform -n "DRIVER_BALL_DER";
	setAttr ".rp" -type "double3" -1.2523799999999965 0.47923647795466817 1.1943350024972175 ;
	setAttr ".sp" -type "double3" -1.2523799999999965 0.47923647795466817 1.1943350024972175 ;
createNode nurbsCurve -n "DRIVER_BALL_DERShape" -p "DRIVER_BALL_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 10 2 no 3
		15 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		-0.75202844250190837 0.98247409247610507 1.1943350024972175
		-1.207019808744388 1.1060948465823448 1.1943350024972172
		-1.6620111749868685 0.98247409247610529 1.1943350024972172
		-1.8523677100305227 0.60870134391019448 1.1943350024972175
		-1.779304169428009 0.42990461985423684 1.1943350024972175
		-1.6058667463076313 0.56010959717246123 1.1943350024972175
		-1.207019808744388 0.67425873133537473 1.1943350024972175
		-0.80817287118114467 0.56010959717246123 1.1943350024972177
		-0.63473544806076698 0.42990461985423706 1.1943350024972177
		-0.56167190745825191 0.60870138257533024 1.1943350024972177
		-0.75202844250190837 0.98247409247610507 1.1943350024972175
		-1.207019808744388 1.1060948465823448 1.1943350024972172
		-1.6620111749868685 0.98247409247610529 1.1943350024972172
		;
createNode transform -n "DRIVER_HEEL_DER";
	setAttr ".rp" -type "double3" -1.3141899999999997 0.11105800000000011 -0.772075 ;
	setAttr ".sp" -type "double3" -1.3141899999999997 0.111058 -0.772075 ;
createNode nurbsCurve -n "DRIVER_HEEL_DERShape" -p "DRIVER_HEEL_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 10 2 no 3
		15 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		-0.38278924520764535 0.22683918115875101 -1.6425037464442473
		-1.3131414076152306 0.22683918110577542 -2.0228797518086195
		-2.2434935700223742 0.22683918115875101 -1.6425037464442473
		-2.2434935700228147 0.22683918121438343 -1.4636293691513382
		-2.2434935700228147 0.22683918121438343 -1.1089044112180868
		-2.2434935700223742 0.22683918115875104 -0.93003003392495054
		-1.3131414076152308 0.22683918110577542 -1.3918527408774444
		-0.38278924520764535 0.22683918115875104 -0.93003003392495054
		-0.38278924520808499 0.22683918121438343 -1.1089044112180857
		-0.38278924520808499 0.22683918121438343 -1.4636293691513365
		-0.38278924520764535 0.22683918115875101 -1.6425037464442473
		-1.3131414076152306 0.22683918110577542 -2.0228797518086195
		-2.2434935700223742 0.22683918115875101 -1.6425037464442473
		;
createNode transform -n "DRIVER_HOMBRO_IZQ_FK";
	setAttr ".rp" -type "double3" 2.1535287445750244 13.154819424597235 -0.74184172281677829 ;
	setAttr ".sp" -type "double3" 2.1535287445750244 13.154819424597235 -0.74184172281677829 ;
createNode nurbsCurve -n "DRIVER_HOMBRO_IZQ_FKShape" -p "DRIVER_HOMBRO_IZQ_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		4.7469994629433288 13.995146265101674 -0.11339773608651182
		4.7469994629433288 12.833038078299726 -0.11339773608651182
		2.1535287445750244 12.440230036136089 0.26397271061809524
		2.1535287445750244 14.094855989772501 0.26397271061809524
		4.7469994629433288 13.995146265101674 -0.11339773608651182
		4.7469994629433288 13.995146265101674 -1.4170491802081191
		2.1535287445750244 14.094855989772501 -1.5594740950243522
		2.1535287445750244 14.094855989772501 0.26397271061809524
		;
createNode nurbsCurve -n "DRIVER_HOMBRO_IZQ_FKShape1" -p "DRIVER_HOMBRO_IZQ_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		2.1535287445750244 12.440230036136089 0.26397271061809524
		2.1535287445750244 12.440230036136089 -1.5594740950243522
		2.1535287445750244 14.094855989772501 -1.5594740950243522
		;
createNode nurbsCurve -n "DRIVER_HOMBRO_IZQ_FKShape2" -p "DRIVER_HOMBRO_IZQ_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		4.7469994629433288 12.833038078299726 -1.4170491802081191
		4.7469994629433288 13.995146265101674 -1.4170491802081191
		;
createNode nurbsCurve -n "DRIVER_HOMBRO_IZQ_FKShape3" -p "DRIVER_HOMBRO_IZQ_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		2.1535287445750244 12.440230036136089 -1.5594740950243522
		4.7469994629433288 12.833038078299726 -1.4170491802081191
		4.7469994629433288 12.833038078299726 -0.11339773608651182
		;
createNode transform -n "DRIVER_HOMBRO_DER_FK";
	setAttr ".rp" -type "double3" -2.15353 13.154799999999998 -0.74184200000000033 ;
	setAttr ".sp" -type "double3" -2.15353 13.154799999999998 -0.74184200000000033 ;
createNode nurbsCurve -n "DRIVER_HOMBRO_DER_FKShape" -p "DRIVER_HOMBRO_DER_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		-4.7470007183683043 13.995126840504437 -0.11339773608651182
		-4.7470007183683043 12.833018653702489 -0.11339773608651182
		-2.1535299999999999 12.440210611538852 0.2639724334348732
		-2.1535299999999999 14.094836565175264 0.2639724334348732
		-4.7470007183683043 13.995126840504437 -0.11339773608651182
		-4.7470007183683043 13.995126840504437 -1.4170491802081191
		-2.1535299999999999 14.094836565175264 -1.5594743722075743
		-2.1535299999999999 14.094836565175264 0.2639724334348732
		;
createNode nurbsCurve -n "DRIVER_HOMBRO_DER_FKShape1" -p "DRIVER_HOMBRO_DER_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		-2.1535299999999999 12.440210611538852 0.2639724334348732
		-2.1535299999999999 12.440210611538852 -1.5594743722075743
		-2.1535299999999999 14.094836565175264 -1.5594743722075743
		;
createNode nurbsCurve -n "DRIVER_HOMBRO_DER_FKShape2" -p "DRIVER_HOMBRO_DER_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		-4.7470007183683043 12.833018653702489 -1.4170491802081191
		-4.7470007183683043 13.995126840504437 -1.4170491802081191
		;
createNode nurbsCurve -n "DRIVER_HOMBRO_DER_FKShape3" -p "DRIVER_HOMBRO_DER_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		-2.1535299999999999 12.440210611538852 -1.5594743722075743
		-4.7470007183683043 12.833018653702489 -1.4170491802081191
		-4.7470007183683043 12.833018653702489 -0.11339773608651182
		;
createNode transform -n "DRIVER_CODO_IZQ_FK";
	setAttr ".rp" -type "double3" 5.0088095415392431 13.357047335818008 -1.0236078052185347 ;
	setAttr ".sp" -type "double3" 5.0088095415392431 13.357047335818008 -1.0236078052185347 ;
createNode nurbsCurve -n "DRIVER_CODO_IZQ_FKShape" -p "DRIVER_CODO_IZQ_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		7.2496689265281908 13.942445170560195 -0.035351213217357347
		7.2496689265281908 12.961677815659662 -0.035351213217357236
		5.0088095415392431 12.82624350125014 -0.11339773608649324
		5.0088095415392431 13.994554223345164 -0.11339773608649324
		7.2496689265281908 13.942445170560195 -0.035351213217357347
		7.2496689265281908 13.942445170560195 -1.2626795509840181
		5.0088095415392431 13.994554223345164 -1.4170491802081353
		5.0088095415392431 13.994554223345164 -0.11339773608649324
		;
createNode nurbsCurve -n "DRIVER_CODO_IZQ_FKShape1" -p "DRIVER_CODO_IZQ_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		5.0088095415392431 12.82624350125014 -0.11339773608649324
		5.0088095415392431 12.82624350125014 -1.4170491802081353
		5.0088095415392431 13.994554223345164 -1.4170491802081353
		;
createNode nurbsCurve -n "DRIVER_CODO_IZQ_FKShape2" -p "DRIVER_CODO_IZQ_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		7.2496689265281908 12.961677815659662 -1.2626795509840176
		7.2496689265281908 13.942445170560195 -1.2626795509840181
		;
createNode nurbsCurve -n "DRIVER_CODO_IZQ_FKShape3" -p "DRIVER_CODO_IZQ_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		5.0088095415392431 12.82624350125014 -1.4170491802081353
		7.2496689265281908 12.961677815659662 -1.2626795509840176
		7.2496689265281908 12.961677815659662 -0.035351213217357236
		;
createNode transform -n "DRIVER_CODO_DER_FK";
	setAttr ".rp" -type "double3" -5.00881 13.357000000000001 -1.0236100000000001 ;
	setAttr ".sp" -type "double3" -5.00881 13.357000000000001 -1.0236100000000001 ;
createNode nurbsCurve -n "DRIVER_CODO_DER_FKShape" -p "DRIVER_CODO_DER_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		-7.2496693849889482 13.942397834742188 -0.035353407998822806
		-7.2496693849889482 12.961630479841656 -0.035353407998822695
		-5.0088100000000004 12.826196165432133 -0.11339773608649324
		-5.0088100000000004 13.994506887527157 -0.11339773608649324
		-7.2496693849889482 13.942397834742188 -0.035353407998822806
		-7.2496693849889482 13.942397834742188 -1.2626817457654835
		-5.0088100000000004 13.994506887527157 -1.4170491802081353
		-5.0088100000000004 13.994506887527157 -0.11339773608649324
		;
createNode nurbsCurve -n "DRIVER_CODO_DER_FKShape1" -p "DRIVER_CODO_DER_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		-5.0088100000000004 12.826196165432133 -0.11339773608649324
		-5.0088100000000004 12.826196165432133 -1.4170491802081353
		-5.0088100000000004 13.994506887527157 -1.4170491802081353
		;
createNode nurbsCurve -n "DRIVER_CODO_DER_FKShape2" -p "DRIVER_CODO_DER_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		-7.2496693849889482 12.961630479841656 -1.2626817457654831
		-7.2496693849889482 13.942397834742188 -1.2626817457654835
		;
createNode nurbsCurve -n "DRIVER_CODO_DER_FKShape3" -p "DRIVER_CODO_DER_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		-5.0088100000000004 12.826196165432133 -1.4170491802081353
		-7.2496693849889482 12.961630479841656 -1.2626817457654831
		-7.2496693849889482 12.961630479841656 -0.035353407998822695
		;
createNode transform -n "DRIVER_MANO_IZQ_FK";
	setAttr ".rp" -type "double3" 7.4441288599560931 13.52245092162403 -0.66514120092053353 ;
	setAttr ".sp" -type "double3" 7.4441288599560931 13.52245092162403 -0.66514120092053353 ;
createNode nurbsCurve -n "DRIVER_MANO_IZQ_FKShape" -p "DRIVER_MANO_IZQ_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		8.6542457779491286 13.747986970142097 0.028249568728278052
		8.6542457779491286 13.346348850490813 0.028249568728278163
		7.4441288599560931 12.977853294326851 -0.021861909489837794
		7.4441288599560931 13.937835909344201 -0.021861909489838016
		8.6542457779491286 13.747986970142097 0.028249568728278052
		8.6542457779491286 13.747986970142097 -1.4430348952600434
		7.4441288599560931 13.937835909344201 -1.2515706682808858
		7.4441288599560931 13.937835909344201 -0.021861909489838016
		;
createNode nurbsCurve -n "DRIVER_MANO_IZQ_FKShape1" -p "DRIVER_MANO_IZQ_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		7.4441288599560931 12.977853294326851 -0.021861909489837794
		7.4441288599560931 12.977853294326851 -1.2515706682808858
		7.4441288599560931 13.937835909344201 -1.2515706682808858
		;
createNode nurbsCurve -n "DRIVER_MANO_IZQ_FKShape2" -p "DRIVER_MANO_IZQ_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		8.6542457779491286 13.346348850490813 -1.4430348952600425
		8.6542457779491286 13.747986970142097 -1.4430348952600434
		;
createNode nurbsCurve -n "DRIVER_MANO_IZQ_FKShape3" -p "DRIVER_MANO_IZQ_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		7.4441288599560931 12.977853294326851 -1.2515706682808858
		8.6542457779491286 13.346348850490813 -1.4430348952600425
		8.6542457779491286 13.346348850490813 0.028249568728278163
		;
createNode transform -n "DRIVER_MANO_DER_FK";
	setAttr ".rp" -type "double3" -7.4441299999999995 13.522499999999999 -0.665141 ;
	setAttr ".sp" -type "double3" -7.4441299999999995 13.522499999999999 -0.665141 ;
createNode nurbsCurve -n "DRIVER_MANO_DER_FKShape" -p "DRIVER_MANO_DER_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		-8.654246917993035 13.748036048518067 0.028249769648811596
		-8.654246917993035 13.346397928866782 0.028249769648811707
		-7.4441299999999995 12.97790237270282 -0.02186170856930425
		-7.4441299999999995 13.937884987720171 -0.021861708569304472
		-8.654246917993035 13.748036048518067 0.028249769648811596
		-8.654246917993035 13.748036048518067 -1.4430346943395098
		-7.4441299999999995 13.937884987720171 -1.2515704673603523
		-7.4441299999999995 13.937884987720171 -0.021861708569304472
		;
createNode nurbsCurve -n "DRIVER_MANO_DER_FKShape1" -p "DRIVER_MANO_DER_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		-7.4441299999999995 12.97790237270282 -0.02186170856930425
		-7.4441299999999995 12.97790237270282 -1.2515704673603523
		-7.4441299999999995 13.937884987720171 -1.2515704673603523
		;
createNode nurbsCurve -n "DRIVER_MANO_DER_FKShape2" -p "DRIVER_MANO_DER_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		-8.654246917993035 13.346397928866782 -1.4430346943395089
		-8.654246917993035 13.748036048518067 -1.4430346943395098
		;
createNode nurbsCurve -n "DRIVER_MANO_DER_FKShape3" -p "DRIVER_MANO_DER_FK";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		-7.4441299999999995 12.97790237270282 -1.2515704673603523
		-8.654246917993035 13.346397928866782 -1.4430346943395089
		-8.654246917993035 13.346397928866782 0.028249769648811707
		;
createNode transform -n "GRP_DRIVER_THUMB_IZQ_1";
	setAttr ".rp" -type "double3" 8.0048955178762249 13.517386184829427 -0.086606438551114384 ;
	setAttr ".sp" -type "double3" 8.0048955178762249 13.517386184829427 -0.086606438551114384 ;
createNode transform -n "DRIVER_THUMB_IZQ_1" -p "GRP_DRIVER_THUMB_IZQ_1";
	setAttr ".rp" -type "double3" 8.0048955178762249 13.521781912486343 -0.086606438551114384 ;
	setAttr ".sp" -type "double3" 8.0048955178762249 13.521781912486343 -0.086606438551114384 ;
createNode nurbsCurve -n "DRIVER_THUMB_IZQ_1Shape" -p "DRIVER_THUMB_IZQ_1";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		8.0048452199953086 13.937809458694158 -0.086656306548636874
		8.0051046697161539 13.937759375293705 -0.0261978505161099
		8.0052052654779953 14.058677359260518 -0.026098114521064919
		8.0046863660363012 14.058777526061421 -0.1470150265861313
		8.0045857702744492 13.937859542094609 -0.14711476258115852
		8.0048452199953086 13.937809458694158 -0.086656306548636874
		8.0044931348288344 13.514596514810322 -0.087005382531239239
		;
createNode transform -n "DRIVER_CARA";
	addAttr -ci true -sn "BS_TRISTE" -ln "BS_TRISTE" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_ENOJADO" -ln "BS_ENOJADO" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_SORPRENDIDO" -ln "BS_SORPRENDIDO" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_STRETCH" -ln "BS_STRETCH" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_SQUASH" -ln "BS_SQUASH" -min 0 -max 1 -at "double";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".t" -type "double3" -1.2349398499056159 2.0885402152238797 -4.5201266721249116 ;
	setAttr ".rp" -type "double3" -6.0000000000000071 17.248347707999187 3.1960322910190886 ;
	setAttr ".sp" -type "double3" -6.0000000000000071 17.248347707999187 3.1960322910190886 ;
	setAttr -k on ".BS_TRISTE";
	setAttr -k on ".BS_ENOJADO";
	setAttr -k on ".BS_SORPRENDIDO";
	setAttr -k on ".BS_STRETCH";
	setAttr -k on ".BS_SQUASH";
createNode nurbsCurve -n "DRIVER_CARAShape" -p "DRIVER_CARA";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-3.9592324328695927 19.713846326851598 3.1960397755793712
		-6 20.194862403766734 3.1960397755793712
		-8.0407675671304091 19.713846326851598 3.1960397755793712
		-8.8860811710869783 17.673078759721186 3.1960397755793712
		-8.0407675671304091 15.147146616188204 3.1960397755793712
		-6.0000000000000009 14.301833012231643 3.1960397755793712
		-3.9592324328695954 15.147146616188204 3.1960397755793712
		-3.1139188289130351 17.673078759721186 3.1960397755793712
		-3.9592324328695927 19.713846326851598 3.1960397755793712
		-6 20.194862403766734 3.1960397755793712
		-8.0407675671304091 19.713846326851598 3.1960397755793712
		;
createNode transform -n "CEJA_DER_01" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" -7.9540447302431261 18.474365433820719 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -7.9540447302431261 18.474365433820719 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "CEJA_DER_01Shape" -p "CEJA_DER_01";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-7.8960652049081741 18.532344959155672 3.1960397755793712
		-7.9540447302431261 18.556360864889363 3.1960397755793712
		-8.0120242555780798 18.532344959155672 3.1960397755793712
		-8.0360401613117709 18.474365433820719 3.1960397755793712
		-8.0120242555780798 18.416385908485768 3.1960397755793712
		-7.9540447302431261 18.392370002752074 3.1960397755793712
		-7.8960652049081741 18.416385908485768 3.1960397755793712
		-7.8720492991744813 18.474365433820719 3.1960397755793712
		-7.8960652049081741 18.532344959155672 3.1960397755793712
		-7.9540447302431261 18.556360864889363 3.1960397755793712
		-8.0120242555780798 18.532344959155672 3.1960397755793712
		;
createNode transform -n "CEJA_DER_02" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" -7.6067851451733626 18.821625018890483 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -7.6067851451733626 18.821625018890483 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "CEJA_DER_02Shape" -p "CEJA_DER_02";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-7.5488056198384097 18.879604544225437 3.1960397755793712
		-7.6067851451733626 18.903620449959128 3.1960397755793712
		-7.6647646705083163 18.879604544225437 3.1960397755793712
		-7.6887805762420074 18.821625018890479 3.1960397755793712
		-7.6647646705083163 18.763645493555529 3.1960397755793712
		-7.6067851451733626 18.739629587821835 3.1960397755793712
		-7.5488056198384097 18.763645493555529 3.1960397755793712
		-7.5247897141047178 18.821625018890479 3.1960397755793712
		-7.5488056198384097 18.879604544225437 3.1960397755793712
		-7.6067851451733626 18.903620449959128 3.1960397755793712
		-7.6647646705083163 18.879604544225437 3.1960397755793712
		;
createNode transform -n "CEJA_DER_03" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" -7.132419711352644 18.948730867641437 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -7.132419711352644 18.948730867641437 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "CEJA_DER_03Shape" -p "CEJA_DER_03";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-7.0744401860176911 19.006710392976391 3.1960397755793712
		-7.132419711352644 19.030726298710082 3.1960397755793712
		-7.1903992366875968 19.006710392976391 3.1960397755793712
		-7.2144151424212888 18.948730867641441 3.1960397755793712
		-7.1903992366875968 18.890751342306487 3.1960397755793712
		-7.1324197113526449 18.866735436572792 3.1960397755793712
		-7.0744401860176911 18.890751342306487 3.1960397755793712
		-7.0504242802839991 18.948730867641441 3.1960397755793712
		-7.0744401860176911 19.006710392976391 3.1960397755793712
		-7.132419711352644 19.030726298710082 3.1960397755793712
		-7.1903992366875968 19.006710392976391 3.1960397755793712
		;
createNode transform -n "PARPADO_SUPERIOR_DER" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -7.1324198313442899 18.375402060040976 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -7.1324198313442899 18.375402060040976 3.1960397755793712 ;
	setAttr ".mxtl" -type "double3" 1 0 1 ;
	setAttr ".mtye" yes;
	setAttr ".xtye" yes;
	setAttr ".mrye" yes;
	setAttr ".xrye" yes;
createNode nurbsCurve -n "PARPADO_SUPERIOR_DERShape" -p "PARPADO_SUPERIOR_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-6.6106041033297123 18.528238348246653 3.1960397755793712
		-7.1324198313442899 18.744381499849879 3.1960397755793712
		-7.6542355593588658 18.528238348246653 3.1960397755793712
		-7.8703787109620951 18.006422620232076 3.1960397755793712
		-7.6542355593588658 18.250467223806336 3.1960397755793712
		-7.1324198313442908 18.276437727873773 3.1960397755793712
		-6.6106041033297132 18.250467223806336 3.1960397755793712
		-6.3944609517264848 18.006422620232076 3.1960397755793712
		-6.6106041033297123 18.528238348246653 3.1960397755793712
		-7.1324198313442899 18.744381499849879 3.1960397755793712
		-7.6542355593588658 18.528238348246653 3.1960397755793712
		;
createNode transform -n "PARPADO_INFERIOR_DER" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -7.1324198313442899 17.637443180423176 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -7.1324198313442899 17.637443180423176 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -1 0 -1 ;
	setAttr ".mtye" yes;
	setAttr ".xtye" yes;
createNode nurbsCurve -n "PARPADO_INFERIOR_DERShape" -p "PARPADO_INFERIOR_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-6.6106041033297123 17.484606892217499 3.1960397755793712
		-7.1324198313442899 17.268463740614273 3.1960397755793712
		-7.6542355593588658 17.484606892217499 3.1960397755793712
		-7.8703787109620951 18.006422620232076 3.1960397755793712
		-7.6542355593588658 17.762378016657816 3.1960397755793712
		-7.1324198313442908 17.736407512590382 3.1960397755793712
		-6.6106041033297132 17.762378016657816 3.1960397755793712
		-6.3944609517264848 18.006422620232076 3.1960397755793712
		-6.6106041033297123 17.484606892217499 3.1960397755793712
		-7.1324198313442899 17.268463740614273 3.1960397755793712
		-7.6542355593588658 17.484606892217499 3.1960397755793712
		;
createNode transform -n "NARIZ" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -6.0000000000000018 16.487755169694438 3.1960397755793695 ;
	setAttr ".sp" -type "double3" -6.0000000000000018 16.487755169694438 3.1960397755793695 ;
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "NARIZShape" -p "NARIZ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-5.7682094071308541 16.665607689595518 3.1960397755793695
		-6.0000000000000009 16.602186291029287 3.1960397755793695
		-6.2317905928691513 16.665607689595518 3.1960397755793695
		-6.3278014000660532 16.487755169694445 3.1960397755793695
		-6.2317905928691513 16.309902649793361 3.1960397755793695
		-6.0000000000000009 16.373324048359596 3.1960397755793695
		-5.7682094071308549 16.309902649793361 3.1960397755793695
		-5.6721985999339513 16.487755169694445 3.1960397755793695
		-5.7682094071308541 16.665607689595518 3.1960397755793695
		-6.0000000000000009 16.602186291029287 3.1960397755793695
		-6.2317905928691513 16.665607689595518 3.1960397755793695
		;
createNode transform -n "BOCA_TEMPLE" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr ".tmp" yes;
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "BOCA_TEMPLEShape" -p "BOCA_TEMPLE";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-5.2465369588923183 15.707935786631026 3.1960397755793699
		-5.9962835751525283 15.714124067332577 3.1960397755793699
		-6.7460301914127374 15.707935786631026 3.1960397755793699
		-7.0565854082110526 15.467035732827075 3.1960397755793699
		-6.7460301914127374 15.226135679023145 3.1960397755793699
		-5.9962835751525283 15.219947398321601 3.1960397755793699
		-5.2465369588923192 15.226135679023145 3.1960397755793699
		-4.9359817420940022 15.467035732827075 3.1960397755793699
		-5.2465369588923183 15.707935786631026 3.1960397755793699
		-5.9962835751525283 15.714124067332577 3.1960397755793699
		-6.7460301914127374 15.707935786631026 3.1960397755793699
		;
createNode transform -n "LABIO_SUPERIOR_CNT" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -5.9962835751525283 15.649856401591324 3.1960397755793699 ;
	setAttr ".sp" -type "double3" -5.9962835751525283 15.649856401591324 3.1960397755793699 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 0 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "LABIO_SUPERIOR_CNTShape" -p "LABIO_SUPERIOR_CNT";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-5.9561710496614797 15.689968927082372 3.1960397755793699
		-5.9962835751525274 15.7065840791618 3.1960397755793699
		-6.036396100643576 15.689968927082372 3.1960397755793699
		-6.0530112527230049 15.649856401591324 3.1960397755793699
		-6.036396100643576 15.609743876100277 3.1960397755793699
		-5.9962835751525274 15.593128724020847 3.1960397755793699
		-5.9561710496614797 15.609743876100273 3.1960397755793699
		-5.9395558975820508 15.649856401591324 3.1960397755793699
		-5.9561710496614797 15.689968927082372 3.1960397755793699
		-5.9962835751525274 15.7065840791618 3.1960397755793699
		-6.036396100643576 15.689968927082372 3.1960397755793699
		;
createNode transform -n "LABIO_INFERIOR_CNT" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -5.9962835751525283 15.273942152516403 3.1960397755793699 ;
	setAttr ".sp" -type "double3" -5.9962835751525283 15.273942152516403 3.1960397755793699 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 0 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "LABIO_INFERIOR_CNTShape" -p "LABIO_INFERIOR_CNT";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-5.9561710496614797 15.314054678007452 3.1960397755793699
		-5.9962835751525274 15.33066983008688 3.1960397755793699
		-6.036396100643576 15.314054678007452 3.1960397755793699
		-6.0530112527230049 15.273942152516405 3.1960397755793699
		-6.036396100643576 15.233829627025354 3.1960397755793699
		-5.9962835751525274 15.217214474945926 3.1960397755793699
		-5.9561710496614797 15.233829627025354 3.1960397755793699
		-5.9395558975820508 15.273942152516405 3.1960397755793699
		-5.9561710496614797 15.314054678007452 3.1960397755793699
		-5.9962835751525274 15.33066983008688 3.1960397755793699
		-6.036396100643576 15.314054678007452 3.1960397755793699
		;
createNode transform -n "LABIO_SUPERIOR_DER" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -6.3977477766004949 15.633447526981282 3.1960397755793699 ;
	setAttr ".sp" -type "double3" -6.3977477766004949 15.633447526981282 3.1960397755793699 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 0 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "LABIO_SUPERIOR_DERShape" -p "LABIO_SUPERIOR_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-6.3576352511094472 15.673560052472329 3.1960397755793699
		-6.3977477766004949 15.690175204551759 3.1960397755793699
		-6.4378603020915435 15.673560052472329 3.1960397755793699
		-6.4544754541709723 15.63344752698128 3.1960397755793699
		-6.4378603020915435 15.593335001490233 3.1960397755793699
		-6.3977477766004949 15.576719849410804 3.1960397755793699
		-6.3576352511094472 15.593335001490232 3.1960397755793699
		-6.3410200990300183 15.63344752698128 3.1960397755793699
		-6.3576352511094472 15.673560052472329 3.1960397755793699
		-6.3977477766004949 15.690175204551759 3.1960397755793699
		-6.4378603020915435 15.673560052472329 3.1960397755793699
		;
createNode transform -n "LABIO_INFERIOR_DER" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -6.3977477766004949 15.294522038763255 3.1960397755793699 ;
	setAttr ".sp" -type "double3" -6.3977477766004949 15.294522038763255 3.1960397755793699 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 0 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "LABIO_INFERIOR_DERShape" -p "LABIO_INFERIOR_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-6.3576352511094472 15.334634564254305 3.1960397755793699
		-6.3977477766004949 15.351249716333733 3.1960397755793699
		-6.4378603020915435 15.334634564254305 3.1960397755793699
		-6.4544754541709723 15.294522038763255 3.1960397755793699
		-6.4378603020915435 15.254409513272208 3.1960397755793699
		-6.3977477766004949 15.237794361192776 3.1960397755793699
		-6.3576352511094472 15.254409513272208 3.1960397755793699
		-6.3410200990300183 15.294522038763255 3.1960397755793699
		-6.3576352511094472 15.334634564254305 3.1960397755793699
		-6.3977477766004949 15.351249716333733 3.1960397755793699
		-6.4378603020915435 15.334634564254305 3.1960397755793699
		;
createNode transform -n "LABIO_SUPERIOR_ESQ_DER" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -6.8089892326776909 15.550577638119494 3.1960397755793699 ;
	setAttr ".sp" -type "double3" -6.8089892326776909 15.550577638119494 3.1960397755793699 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "LABIO_SUPERIOR_ESQ_DERShape" -p "LABIO_SUPERIOR_ESQ_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-6.7688767071866422 15.590690163610542 3.1960397755793699
		-6.80898923267769 15.60730531568997 3.1960397755793699
		-6.8491017581687386 15.590690163610542 3.1960397755793699
		-6.8657169102481674 15.550577638119496 3.1960397755793699
		-6.8491017581687386 15.510465112628445 3.1960397755793699
		-6.80898923267769 15.493849960549017 3.1960397755793699
		-6.7688767071866422 15.510465112628445 3.1960397755793699
		-6.7522615551072134 15.550577638119496 3.1960397755793699
		-6.7688767071866422 15.590690163610542 3.1960397755793699
		-6.80898923267769 15.60730531568997 3.1960397755793699
		-6.8491017581687386 15.590690163610542 3.1960397755793699
		;
createNode transform -n "LABIO_INFERIOR_ESQ_DER" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -6.8089892326776909 15.388614944804871 3.1960397755793699 ;
	setAttr ".sp" -type "double3" -6.8089892326776909 15.388614944804871 3.1960397755793699 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 0 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "LABIO_INFERIOR_ESQ_DERShape" -p "LABIO_INFERIOR_ESQ_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-6.7688767071866422 15.428727470295918 3.1960397755793699
		-6.80898923267769 15.445342622375346 3.1960397755793699
		-6.8491017581687386 15.428727470295922 3.1960397755793699
		-6.8657169102481674 15.388614944804871 3.1960397755793699
		-6.8491017581687386 15.348502419313824 3.1960397755793699
		-6.80898923267769 15.331887267234396 3.1960397755793699
		-6.7688767071866422 15.348502419313821 3.1960397755793699
		-6.7522615551072134 15.388614944804871 3.1960397755793699
		-6.7688767071866422 15.428727470295918 3.1960397755793699
		-6.80898923267769 15.445342622375346 3.1960397755793699
		-6.8491017581687386 15.428727470295922 3.1960397755793699
		;
createNode transform -n "LABIO_SUPERIOR_IZQ" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -5.5944213968605681 15.633447526981282 3.1960397755793699 ;
	setAttr ".sp" -type "double3" -5.5944213968605681 15.633447526981282 3.1960397755793699 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 0 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "LABIO_SUPERIOR_IZQShape" -p "LABIO_SUPERIOR_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-5.5543088713695195 15.673560052472329 3.1960397755793699
		-5.5944213968605681 15.690175204551759 3.1960397755793699
		-5.6345339223516158 15.673560052472329 3.1960397755793699
		-5.6511490744310446 15.63344752698128 3.1960397755793699
		-5.6345339223516158 15.593335001490233 3.1960397755793699
		-5.5944213968605681 15.576719849410804 3.1960397755793699
		-5.5543088713695195 15.593335001490232 3.1960397755793699
		-5.5376937192900906 15.63344752698128 3.1960397755793699
		-5.5543088713695195 15.673560052472329 3.1960397755793699
		-5.5944213968605681 15.690175204551759 3.1960397755793699
		-5.6345339223516158 15.673560052472329 3.1960397755793699
		;
createNode transform -n "LABIO_INFERIOR_IZQ" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -5.5944213968605681 15.294522038763255 3.1960397755793699 ;
	setAttr ".sp" -type "double3" -5.5944213968605681 15.294522038763255 3.1960397755793699 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 0 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "LABIO_INFERIOR_IZQShape" -p "LABIO_INFERIOR_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-5.5543088713695195 15.334634564254305 3.1960397755793699
		-5.5944213968605681 15.351249716333733 3.1960397755793699
		-5.6345339223516158 15.334634564254305 3.1960397755793699
		-5.6511490744310446 15.294522038763255 3.1960397755793699
		-5.6345339223516158 15.254409513272208 3.1960397755793699
		-5.5944213968605681 15.237794361192776 3.1960397755793699
		-5.5543088713695195 15.254409513272208 3.1960397755793699
		-5.5376937192900906 15.294522038763255 3.1960397755793699
		-5.5543088713695195 15.334634564254305 3.1960397755793699
		-5.5944213968605681 15.351249716333733 3.1960397755793699
		-5.6345339223516158 15.334634564254305 3.1960397755793699
		;
createNode transform -n "LABIO_SUPERIOR_ESQ_IZQ" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -5.1835779176273657 15.550577638119494 3.1960397755793699 ;
	setAttr ".sp" -type "double3" -5.1835779176273657 15.550577638119494 3.1960397755793699 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 0 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "LABIO_SUPERIOR_ESQ_IZQShape" -p "LABIO_SUPERIOR_ESQ_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-5.143465392136318 15.590690163610542 3.1960397755793699
		-5.1835779176273657 15.60730531568997 3.1960397755793699
		-5.2236904431184144 15.590690163610542 3.1960397755793699
		-5.2403055951978432 15.550577638119496 3.1960397755793699
		-5.2236904431184144 15.510465112628445 3.1960397755793699
		-5.1835779176273657 15.493849960549017 3.1960397755793699
		-5.143465392136318 15.510465112628445 3.1960397755793699
		-5.1268502400568883 15.550577638119496 3.1960397755793699
		-5.143465392136318 15.590690163610542 3.1960397755793699
		-5.1835779176273657 15.60730531568997 3.1960397755793699
		-5.2236904431184144 15.590690163610542 3.1960397755793699
		;
createNode transform -n "LABIO_INFERIOR_ESQ_IZQ" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -5.1835779176273657 15.388614944804871 3.1960397755793699 ;
	setAttr ".sp" -type "double3" -5.1835779176273657 15.388614944804871 3.1960397755793699 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 0 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "LABIO_INFERIOR_ESQ_IZQShape" -p "LABIO_INFERIOR_ESQ_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-5.143465392136318 15.428727470295918 3.1960397755793699
		-5.1835779176273657 15.445342622375346 3.1960397755793699
		-5.2236904431184144 15.428727470295922 3.1960397755793699
		-5.2403055951978432 15.388614944804871 3.1960397755793699
		-5.2236904431184144 15.348502419313824 3.1960397755793699
		-5.1835779176273657 15.331887267234396 3.1960397755793699
		-5.143465392136318 15.348502419313821 3.1960397755793699
		-5.1268502400568883 15.388614944804871 3.1960397755793699
		-5.143465392136318 15.428727470295918 3.1960397755793699
		-5.1835779176273657 15.445342622375346 3.1960397755793699
		-5.2236904431184144 15.428727470295922 3.1960397755793699
		;
createNode transform -n "CEJA_DER_04" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" -6.6580542775319254 18.821625018890483 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -6.6580542775319254 18.821625018890483 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "CEJA_DER_04Shape" -p "CEJA_DER_04";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-6.6000747521969725 18.879604544225437 3.1960397755793712
		-6.6580542775319254 18.903620449959128 3.1960397755793712
		-6.7160338028668782 18.879604544225437 3.1960397755793712
		-6.7400497086005702 18.821625018890487 3.1960397755793712
		-6.7160338028668782 18.763645493555533 3.1960397755793712
		-6.6580542775319254 18.739629587821838 3.1960397755793712
		-6.6000747521969725 18.763645493555533 3.1960397755793712
		-6.5760588464632805 18.821625018890487 3.1960397755793712
		-6.6000747521969725 18.879604544225437 3.1960397755793712
		-6.6580542775319254 18.903620449959128 3.1960397755793712
		-6.7160338028668782 18.879604544225437 3.1960397755793712
		;
createNode transform -n "CEJA_DER_05" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" -6.3107946924621618 18.474365433820719 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -6.3107946924621618 18.474365433820719 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "CEJA_DER_05Shape" -p "CEJA_DER_05";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-6.252815167127209 18.532344959155672 3.1960397755793712
		-6.3107946924621618 18.556360864889363 3.1960397755793712
		-6.3687742177971147 18.532344959155672 3.1960397755793712
		-6.3927901235308067 18.474365433820719 3.1960397755793712
		-6.3687742177971147 18.416385908485765 3.1960397755793712
		-6.3107946924621627 18.392370002752074 3.1960397755793712
		-6.252815167127209 18.416385908485765 3.1960397755793712
		-6.228799261393517 18.474365433820719 3.1960397755793712
		-6.252815167127209 18.532344959155672 3.1960397755793712
		-6.3107946924621618 18.556360864889363 3.1960397755793712
		-6.3687742177971147 18.532344959155672 3.1960397755793712
		;
createNode transform -n "CEJA_DER_06" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" -6.1836888437112076 18 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -6.1836888437112076 18 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "CEJA_DER_06Shape" -p "CEJA_DER_06";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-6.1257093183762548 18.05797952533495 3.1960397755793712
		-6.1836888437112076 18.081995431068645 3.1960397755793712
		-6.2416683690461605 18.05797952533495 3.1960397755793712
		-6.2656842747798525 18 3.1960397755793712
		-6.2416683690461605 17.94202047466505 3.1960397755793712
		-6.1836888437112076 17.918004568931352 3.1960397755793712
		-6.1257093183762548 17.94202047466505 3.1960397755793712
		-6.1016934126425628 18 3.1960397755793712
		-6.1257093183762548 18.05797952533495 3.1960397755793712
		-6.1836888437112076 18.081995431068645 3.1960397755793712
		-6.2416683690461605 18.05797952533495 3.1960397755793712
		;
createNode transform -n "POMULO_DER_03" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" -7.132419711352644 17.051269132358563 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -7.132419711352644 17.051269132358563 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "POMULO_DER_03Shape" -p "POMULO_DER_03";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-7.0744401860176902 17.109248657693517 3.1960397755793712
		-7.1324197113526431 17.133264563427208 3.1960397755793712
		-7.1903992366875968 17.109248657693517 3.1960397755793712
		-7.2144151424212888 17.051269132358563 3.1960397755793712
		-7.1903992366875968 16.993289607023609 3.1960397755793712
		-7.132419711352644 16.969273701289918 3.1960397755793712
		-7.0744401860176902 16.993289607023609 3.1960397755793712
		-7.0504242802839983 17.051269132358563 3.1960397755793712
		-7.0744401860176902 17.109248657693517 3.1960397755793712
		-7.1324197113526431 17.133264563427208 3.1960397755793712
		-7.1903992366875968 17.109248657693517 3.1960397755793712
		;
createNode transform -n "POMULO_DER_02" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" -7.6067851451733626 17.178374981109517 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -7.6067851451733626 17.178374981109517 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "POMULO_DER_02Shape" -p "POMULO_DER_02";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-7.5488056198384088 17.236354506444471 3.1960397755793712
		-7.6067851451733617 17.260370412178165 3.1960397755793712
		-7.6647646705083146 17.236354506444471 3.1960397755793712
		-7.6887805762420074 17.178374981109517 3.1960397755793712
		-7.6647646705083146 17.120395455774567 3.1960397755793712
		-7.6067851451733626 17.096379550040872 3.1960397755793712
		-7.5488056198384088 17.120395455774567 3.1960397755793712
		-7.5247897141047169 17.178374981109517 3.1960397755793712
		-7.5488056198384088 17.236354506444471 3.1960397755793712
		-7.6067851451733617 17.260370412178165 3.1960397755793712
		-7.6647646705083146 17.236354506444471 3.1960397755793712
		;
createNode transform -n "POMULO_DER_01" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" -7.9540447302431261 17.525634566179281 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -7.9540447302431261 17.525634566179281 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "POMULO_DER_01Shape" -p "POMULO_DER_01";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-7.8960652049081732 17.583614091514235 3.1960397755793712
		-7.9540447302431252 17.607629997247926 3.1960397755793712
		-8.0120242555780763 17.583614091514235 3.1960397755793712
		-8.0360401613117709 17.525634566179285 3.1960397755793712
		-8.0120242555780763 17.467655040844331 3.1960397755793712
		-7.9540447302431252 17.443639135110637 3.1960397755793712
		-7.8960652049081732 17.467655040844331 3.1960397755793712
		-7.8720492991744804 17.525634566179285 3.1960397755793712
		-7.8960652049081732 17.583614091514235 3.1960397755793712
		-7.9540447302431252 17.607629997247926 3.1960397755793712
		-8.0120242555780763 17.583614091514235 3.1960397755793712
		;
createNode transform -n "CEJA_IZQ_00" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" -3.9188492490529874 18 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -3.9188492490529874 18 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "CEJA_IZQ_00Shape" -p "CEJA_IZQ_00";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-3.9768287743879385 18.057979525334954 3.1960397755793712
		-3.9188492490529865 18.081995431068645 3.1960397755793712
		-3.8608697237180341 18.057979525334954 3.1960397755793712
		-3.8368538179843426 18 3.1960397755793712
		-3.8608697237180341 17.94202047466505 3.1960397755793712
		-3.9188492490529865 17.918004568931355 3.1960397755793712
		-3.9768287743879385 17.94202047466505 3.1960397755793712
		-4.0008446801216326 18 3.1960397755793712
		-3.9768287743879385 18.057979525334954 3.1960397755793712
		-3.9188492490529865 18.081995431068645 3.1960397755793712
		-3.8608697237180341 18.057979525334954 3.1960397755793712
		;
createNode transform -n "PARPADO_SUPERIOR_IZQ" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.867580168655711 18.375402060040976 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -4.867580168655711 18.375402060040976 3.1960397755793712 ;
	setAttr ".mxtl" -type "double3" 1 0 1 ;
	setAttr ".mtye" yes;
	setAttr ".xtye" yes;
	setAttr ".mrye" yes;
	setAttr ".xrye" yes;
createNode nurbsCurve -n "PARPADO_SUPERIOR_IZQShape" -p "PARPADO_SUPERIOR_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-5.3893958966702886 18.528238348246653 3.1960397755793712
		-4.867580168655711 18.744381499849879 3.1960397755793712
		-4.3457644406411342 18.528238348246653 3.1960397755793712
		-4.1296212890379058 18.006422620232076 3.1960397755793712
		-4.3457644406411342 18.250467223806336 3.1960397755793712
		-4.8675801686557101 18.276437727873773 3.1960397755793712
		-5.3893958966702877 18.250467223806336 3.1960397755793712
		-5.6055390482735161 18.006422620232076 3.1960397755793712
		-5.3893958966702886 18.528238348246653 3.1960397755793712
		-4.867580168655711 18.744381499849879 3.1960397755793712
		-4.3457644406411342 18.528238348246653 3.1960397755793712
		;
createNode transform -n "PARPADO_INFERIOR_IZQ" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".t" -type "double3" 0 1.2434497875801753e-014 0 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -4.867580168655711 17.637443180423176 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -4.867580168655711 17.637443180423176 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -1 0 -1 ;
	setAttr ".mtye" yes;
	setAttr ".xtye" yes;
createNode nurbsCurve -n "PARPADO_INFERIOR_IZQShape" -p "PARPADO_INFERIOR_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-5.3893958966702886 17.484606892217499 3.1960397755793712
		-4.867580168655711 17.268463740614273 3.1960397755793712
		-4.3457644406411342 17.484606892217499 3.1960397755793712
		-4.1296212890379058 18.006422620232076 3.1960397755793712
		-4.3457644406411342 17.762378016657816 3.1960397755793712
		-4.8675801686557101 17.736407512590382 3.1960397755793712
		-5.3893958966702877 17.762378016657816 3.1960397755793712
		-5.6055390482735161 18.006422620232076 3.1960397755793712
		-5.3893958966702886 17.484606892217499 3.1960397755793712
		-4.867580168655711 17.268463740614273 3.1960397755793712
		-4.3457644406411342 17.484606892217499 3.1960397755793712
		;
createNode transform -n "POMULO_IZQ_01" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" -4.045955097803942 17.525634566179281 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -4.045955097803942 17.525634566179281 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "POMULO_IZQ_01Shape" -p "POMULO_IZQ_01";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.1039346231388958 17.583614091514235 3.1960397755793712
		-4.045955097803942 17.607629997247926 3.1960397755793712
		-3.98797557246899 17.583614091514235 3.1960397755793712
		-3.9639596667352972 17.525634566179285 3.1960397755793712
		-3.98797557246899 17.467655040844331 3.1960397755793712
		-4.045955097803942 17.443639135110637 3.1960397755793712
		-4.1039346231388958 17.467655040844331 3.1960397755793712
		-4.1279505288725868 17.525634566179285 3.1960397755793712
		-4.1039346231388958 17.583614091514235 3.1960397755793712
		-4.045955097803942 17.607629997247926 3.1960397755793712
		-3.98797557246899 17.583614091514235 3.1960397755793712
		;
createNode transform -n "NARIZ_SEC_IZQ" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -5.6188760917314085 16.357301228034096 3.1960248064588059 ;
	setAttr ".sp" -type "double3" -5.6188760917314085 16.357301228034096 3.1960248064588059 ;
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "NARIZ_SEC_IZQShape" -p "NARIZ_SEC_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-5.690813279886787 16.538484422444302 3.1960248064588059
		-5.5114992156782767 16.504676322403334 3.1960248064588059
		-5.4954500170906488 16.282290770456932 3.1960248064588059
		-5.6282956589683479 16.176118033623894 3.1960248064588059
		-5.7241707675474851 16.219250674213939 3.1960248064588059
		-5.7423021663721672 16.298216203396112 3.1960248064588059
		-5.6087316100196505 16.320423221650614 3.1960248064588059
		-5.6085429825672124 16.479449879102507 3.1960248064588059
		-5.690813279886787 16.538484422444302 3.1960248064588059
		-5.5114992156782767 16.504676322403334 3.1960248064588059
		-5.4954500170906488 16.282290770456932 3.1960248064588059
		;
createNode transform -n "NARIZ_SEC_DER" -p "DRIVER_CARA";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -6.3873798593676128 16.357301228034096 3.1960248064588059 ;
	setAttr ".sp" -type "double3" -6.3873798593676128 16.357301228034096 3.1960248064588059 ;
	setAttr ".mntl" -type "double3" -1 -1 0 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "NARIZ_SEC_DERShape" -p "NARIZ_SEC_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-6.3154426712122333 16.538484422444302 3.1960248064588059
		-6.4947567354207436 16.504676322403334 3.1960248064588059
		-6.5108059340083715 16.282290770456932 3.1960248064588059
		-6.3779602921306724 16.176118033623894 3.1960248064588059
		-6.2820851835515352 16.219250674213939 3.1960248064588059
		-6.2639537847268532 16.298216203396112 3.1960248064588059
		-6.3975243410793698 16.320423221650614 3.1960248064588059
		-6.3977129685318079 16.479449879102507 3.1960248064588059
		-6.3154426712122333 16.538484422444302 3.1960248064588059
		-6.4947567354207436 16.504676322403334 3.1960248064588059
		-6.5108059340083715 16.282290770456932 3.1960248064588059
		;
createNode transform -n "CEJA_DER_00" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" -8.0811505789940803 18 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -8.0811505789940803 18 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "CEJA_DER_00Shape" -p "CEJA_DER_00";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-8.0231710536591283 18.057979525334954 3.1960397755793712
		-8.0811505789940803 18.081995431068645 3.1960397755793712
		-8.1391301043290341 18.057979525334954 3.1960397755793712
		-8.1631460100627251 18 3.1960397755793712
		-8.1391301043290341 17.94202047466505 3.1960397755793712
		-8.0811505789940803 17.918004568931355 3.1960397755793712
		-8.0231710536591283 17.94202047466505 3.1960397755793712
		-7.9991551479254355 18 3.1960397755793712
		-8.0231710536591283 18.057979525334954 3.1960397755793712
		-8.0811505789940803 18.081995431068645 3.1960397755793712
		-8.1391301043290341 18.057979525334954 3.1960397755793712
		;
createNode transform -n "POMULO_DER_04" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" -6.6580542775319254 17.178374981109517 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -6.6580542775319254 17.178374981109517 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "POMULO_DER_04Shape" -p "POMULO_DER_04";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-6.6000747521969716 17.236354506444471 3.1960397755793712
		-6.6580542775319245 17.260370412178162 3.1960397755793712
		-6.7160338028668782 17.236354506444471 3.1960397755793712
		-6.7400497086005702 17.178374981109517 3.1960397755793712
		-6.7160338028668782 17.120395455774563 3.1960397755793712
		-6.6580542775319254 17.096379550040872 3.1960397755793712
		-6.6000747521969716 17.120395455774563 3.1960397755793712
		-6.5760588464632797 17.178374981109517 3.1960397755793712
		-6.6000747521969716 17.236354506444471 3.1960397755793712
		-6.6580542775319245 17.260370412178162 3.1960397755793712
		-6.7160338028668782 17.236354506444471 3.1960397755793712
		;
createNode transform -n "POMULO_DER_05" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" -6.3107946924621618 17.525634566179281 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -6.3107946924621618 17.525634566179281 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "POMULO_DER_05Shape" -p "POMULO_DER_05";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-6.2528151671272081 17.583614091514235 3.1960397755793712
		-6.310794692462161 17.607629997247926 3.1960397755793712
		-6.3687742177971147 17.583614091514235 3.1960397755793712
		-6.3927901235308067 17.525634566179281 3.1960397755793712
		-6.3687742177971147 17.467655040844328 3.1960397755793712
		-6.3107946924621618 17.443639135110637 3.1960397755793712
		-6.2528151671272081 17.467655040844328 3.1960397755793712
		-6.2287992613935161 17.525634566179281 3.1960397755793712
		-6.2528151671272081 17.583614091514235 3.1960397755793712
		-6.310794692462161 17.607629997247926 3.1960397755793712
		-6.3687742177971147 17.583614091514235 3.1960397755793712
		;
createNode transform -n "CEJA_IZQ_01" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" -4.045955097803942 18.474365433820719 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -4.045955097803942 18.474365433820719 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "CEJA_IZQ_01Shape" -p "CEJA_IZQ_01";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.1039346231388931 18.532344959155672 3.1960397755793712
		-4.0459550978039411 18.556360864889363 3.1960397755793712
		-3.9879755724689887 18.532344959155672 3.1960397755793712
		-3.9639596667352972 18.474365433820719 3.1960397755793712
		-3.9879755724689887 18.416385908485768 3.1960397755793712
		-4.0459550978039411 18.392370002752074 3.1960397755793712
		-4.1039346231388931 18.416385908485768 3.1960397755793712
		-4.1279505288725868 18.474365433820719 3.1960397755793712
		-4.1039346231388931 18.532344959155672 3.1960397755793712
		-4.0459550978039411 18.556360864889363 3.1960397755793712
		-3.9879755724689887 18.532344959155672 3.1960397755793712
		;
createNode transform -n "CEJA_IZQ_02" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" -4.3932146828737055 18.821625018890483 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -4.3932146828737055 18.821625018890483 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "CEJA_IZQ_02Shape" -p "CEJA_IZQ_02";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.4511942082086566 18.879604544225437 3.1960397755793712
		-4.3932146828737046 18.903620449959128 3.1960397755793712
		-4.3352351575387527 18.879604544225437 3.1960397755793712
		-4.3112192518050607 18.821625018890483 3.1960397755793712
		-4.3352351575387527 18.763645493555533 3.1960397755793712
		-4.3932146828737046 18.739629587821838 3.1960397755793712
		-4.4511942082086566 18.763645493555533 3.1960397755793712
		-4.4752101139423512 18.821625018890483 3.1960397755793712
		-4.4511942082086566 18.879604544225437 3.1960397755793712
		-4.3932146828737046 18.903620449959128 3.1960397755793712
		-4.3352351575387527 18.879604544225437 3.1960397755793712
		;
createNode transform -n "CEJA_IZQ_03" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" -4.8675801166944241 18.948730867641437 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -4.8675801166944241 18.948730867641437 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "CEJA_IZQ_03Shape" -p "CEJA_IZQ_03";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.9255596420293752 19.006710392976391 3.1960397755793712
		-4.8675801166944233 19.030726298710082 3.1960397755793712
		-4.8096005913594713 19.006710392976391 3.1960397755793712
		-4.7855846856257793 18.948730867641437 3.1960397755793712
		-4.8096005913594713 18.890751342306487 3.1960397755793712
		-4.8675801166944233 18.866735436572792 3.1960397755793712
		-4.9255596420293752 18.890751342306487 3.1960397755793712
		-4.9495755477630698 18.948730867641437 3.1960397755793712
		-4.9255596420293752 19.006710392976391 3.1960397755793712
		-4.8675801166944233 19.030726298710082 3.1960397755793712
		-4.8096005913594713 19.006710392976391 3.1960397755793712
		;
createNode transform -n "CEJA_IZQ_04" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" -5.3419455505151427 18.821625018890483 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -5.3419455505151427 18.821625018890483 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "CEJA_IZQ_04Shape" -p "CEJA_IZQ_04";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-5.3999250758500938 18.879604544225437 3.1960397755793712
		-5.3419455505151419 18.903620449959128 3.1960397755793712
		-5.2839660251801899 18.879604544225437 3.1960397755793712
		-5.2599501194464979 18.821625018890483 3.1960397755793712
		-5.2839660251801899 18.763645493555533 3.1960397755793712
		-5.3419455505151419 18.739629587821838 3.1960397755793712
		-5.3999250758500938 18.763645493555533 3.1960397755793712
		-5.4239409815837885 18.821625018890483 3.1960397755793712
		-5.3999250758500938 18.879604544225437 3.1960397755793712
		-5.3419455505151419 18.903620449959128 3.1960397755793712
		-5.2839660251801899 18.879604544225437 3.1960397755793712
		;
createNode transform -n "CEJA_IZQ_05" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" -5.6892051355849063 18.474365433820719 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -5.6892051355849063 18.474365433820719 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "CEJA_IZQ_05Shape" -p "CEJA_IZQ_05";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-5.7471846609198574 18.532344959155672 3.1960397755793712
		-5.6892051355849054 18.556360864889363 3.1960397755793712
		-5.6312256102499534 18.532344959155672 3.1960397755793712
		-5.6072097045162614 18.474365433820719 3.1960397755793712
		-5.6312256102499534 18.416385908485768 3.1960397755793712
		-5.6892051355849054 18.392370002752074 3.1960397755793712
		-5.7471846609198574 18.416385908485768 3.1960397755793712
		-5.771200566653552 18.474365433820719 3.1960397755793712
		-5.7471846609198574 18.532344959155672 3.1960397755793712
		-5.6892051355849054 18.556360864889363 3.1960397755793712
		-5.6312256102499534 18.532344959155672 3.1960397755793712
		;
createNode transform -n "CEJA_IZQ_06" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" -5.8163109843358605 18 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -5.8163109843358605 18 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "CEJA_IZQ_06Shape" -p "CEJA_IZQ_06";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-5.8742905096708116 18.057979525334954 3.1960397755793712
		-5.8163109843358596 18.081995431068645 3.1960397755793712
		-5.7583314590009076 18.057979525334954 3.1960397755793712
		-5.7343155532672156 18 3.1960397755793712
		-5.7583314590009076 17.94202047466505 3.1960397755793712
		-5.8163109843358596 17.918004568931355 3.1960397755793712
		-5.8742905096708116 17.94202047466505 3.1960397755793712
		-5.8983064154045062 18 3.1960397755793712
		-5.8742905096708116 18.057979525334954 3.1960397755793712
		-5.8163109843358596 18.081995431068645 3.1960397755793712
		-5.7583314590009076 18.057979525334954 3.1960397755793712
		;
createNode transform -n "POMULO_IZQ_02" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" -4.3932146828737055 17.178374981109517 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -4.3932146828737055 17.178374981109517 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "POMULO_IZQ_02Shape" -p "POMULO_IZQ_02";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.4511942082086593 17.236354506444471 3.1960397755793712
		-4.3932146828737055 17.260370412178162 3.1960397755793712
		-4.3352351575387535 17.236354506444471 3.1960397755793712
		-4.3112192518050607 17.178374981109521 3.1960397755793712
		-4.3352351575387535 17.120395455774567 3.1960397755793712
		-4.3932146828737055 17.096379550040872 3.1960397755793712
		-4.4511942082086593 17.120395455774567 3.1960397755793712
		-4.4752101139423504 17.178374981109521 3.1960397755793712
		-4.4511942082086593 17.236354506444471 3.1960397755793712
		-4.3932146828737055 17.260370412178162 3.1960397755793712
		-4.3352351575387535 17.236354506444471 3.1960397755793712
		;
createNode transform -n "POMULO_IZQ_03" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" -4.8675801166944241 17.051269132358563 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -4.8675801166944241 17.051269132358563 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "POMULO_IZQ_03Shape" -p "POMULO_IZQ_03";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.9255596420293779 17.109248657693517 3.1960397755793712
		-4.8675801166944241 17.133264563427208 3.1960397755793712
		-4.8096005913594722 17.109248657693517 3.1960397755793712
		-4.7855846856257793 17.051269132358566 3.1960397755793712
		-4.8096005913594722 16.993289607023613 3.1960397755793712
		-4.8675801166944241 16.969273701289918 3.1960397755793712
		-4.9255596420293779 16.993289607023613 3.1960397755793712
		-4.949575547763069 17.051269132358566 3.1960397755793712
		-4.9255596420293779 17.109248657693517 3.1960397755793712
		-4.8675801166944241 17.133264563427208 3.1960397755793712
		-4.8096005913594722 17.109248657693517 3.1960397755793712
		;
createNode transform -n "POMULO_IZQ_04" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" -5.3419455505151427 17.178374981109517 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -5.3419455505151427 17.178374981109517 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "POMULO_IZQ_04Shape" -p "POMULO_IZQ_04";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-5.3999250758500965 17.236354506444471 3.1960397755793712
		-5.3419455505151427 17.260370412178162 3.1960397755793712
		-5.2839660251801908 17.236354506444471 3.1960397755793712
		-5.2599501194464979 17.178374981109521 3.1960397755793712
		-5.2839660251801908 17.120395455774567 3.1960397755793712
		-5.3419455505151427 17.096379550040872 3.1960397755793712
		-5.3999250758500965 17.120395455774567 3.1960397755793712
		-5.4239409815837876 17.178374981109521 3.1960397755793712
		-5.3999250758500965 17.236354506444471 3.1960397755793712
		-5.3419455505151427 17.260370412178162 3.1960397755793712
		-5.2839660251801908 17.236354506444471 3.1960397755793712
		;
createNode transform -n "POMULO_IZQ_05" -p "DRIVER_CARA";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" -5.6892051355849063 17.525634566179281 3.1960397755793712 ;
	setAttr ".sp" -type "double3" -5.6892051355849063 17.525634566179281 3.1960397755793712 ;
	setAttr ".mntl" -type "double3" -0.7 -0.7 -0.7 ;
	setAttr ".mxtl" -type "double3" 0.7 0.7 0.7 ;
	setAttr ".mtxe" yes;
	setAttr ".mtye" yes;
	setAttr ".mtze" yes;
	setAttr ".xtxe" yes;
	setAttr ".xtye" yes;
	setAttr ".xtze" yes;
createNode nurbsCurve -n "POMULO_IZQ_05Shape" -p "POMULO_IZQ_05";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-5.74718466091986 17.583614091514235 3.1960397755793712
		-5.6892051355849063 17.607629997247926 3.1960397755793712
		-5.6312256102499543 17.583614091514235 3.1960397755793712
		-5.6072097045162614 17.525634566179285 3.1960397755793712
		-5.6312256102499543 17.467655040844331 3.1960397755793712
		-5.6892051355849063 17.443639135110637 3.1960397755793712
		-5.74718466091986 17.467655040844331 3.1960397755793712
		-5.7712005666535511 17.525634566179285 3.1960397755793712
		-5.74718466091986 17.583614091514235 3.1960397755793712
		-5.6892051355849063 17.607629997247926 3.1960397755793712
		-5.6312256102499543 17.583614091514235 3.1960397755793712
		;
createNode transform -n "BOCA" -p "DRIVER_CARA";
	addAttr -ci true -sn "BS_BOCA_A" -ln "BS_BOCA_A" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_BOCA_E" -ln "BS_BOCA_E" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_BOCA_I" -ln "BS_BOCA_I" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_BOCA_O" -ln "BS_BOCA_O" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_BOCA_U" -ln "BS_BOCA_U" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_BOCA_F" -ln "BS_BOCA_F" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_BOCA_M" -ln "BS_BOCA_M" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_BOCA_BESO" -ln "BS_BOCA_BESO" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_BOCA_CHICA" -ln "BS_BOCA_CHICA" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_BOCA_SMIRK_IZQ" -ln "BS_BOCA_SMIRK_IZQ" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_BOCA_SMIRK_DER" -ln "BS_BOCA_SMIRK_DER" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_FELIZ" -ln "BS_FELIZ" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_BOCA_ABIERTA_SONRISA" -ln "BS_BOCA_ABIERTA_SONRISA" -min 
		0 -max 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -6.0087211086609313 14.161549828301268 3.197208862206006 ;
	setAttr ".sp" -type "double3" -6.0087211086609305 14.161549828301268 3.1972088622060055 ;
	setAttr -k on ".BS_BOCA_A";
	setAttr -k on ".BS_BOCA_E";
	setAttr -k on ".BS_BOCA_I";
	setAttr -k on ".BS_BOCA_O";
	setAttr -k on ".BS_BOCA_U";
	setAttr -k on ".BS_BOCA_F";
	setAttr -k on ".BS_BOCA_M";
	setAttr -k on ".BS_BOCA_BESO";
	setAttr -k on ".BS_BOCA_CHICA";
	setAttr -k on ".BS_BOCA_SMIRK_IZQ";
	setAttr -k on ".BS_BOCA_SMIRK_DER";
	setAttr -k on ".BS_FELIZ";
	setAttr -k on ".BS_BOCA_ABIERTA_SONRISA";
createNode nurbsCurve -n "O_Shape1" -p "BOCA";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 22 1 no 3
		25 0 0 0.49687495231555667 0.49687495231555667 1.4968749523155567 2.4968749523155567
		 3.4968749523155567 4.4968749523155562 4.4968749523155562 5.4968749523155562 6.4968749523155562
		 7.4968749523155562 8.4968749523155562 8.4968749523155562 9.0171862363622495 9.0171862363622495
		 10.017186236362249 11.017186236362249 12.017186236362249 12.017186236362249 13.017186236362249
		 14.017186236362249 15.017186236362249 16.017186236362249 16.017186236362249
		24
		-6.0862446163902222 14.174874384508833 3.1972088622060055
		-6.0862446163902222 14.110675235831621 3.1972088622060055
		-6.0862446163902222 14.04647608715441 3.1972088622060055
		-6.0862446163902222 13.975816744744169 3.1972088622060055
		-6.1003763271478837 13.910002301189344 3.1972088622060055
		-6.1464058236066261 13.852667120675701 3.1972088622060055
		-6.2186802637389977 13.825614628141004 3.1972088622060055
		-6.2655177033697722 13.825614628141004 3.1972088622060055
		-6.3180075907170314 13.825614628141004 3.1972088622060055
		-6.3906858052799356 13.849033545111876 3.1972088622060055
		-6.4306586852806937 13.895870590431684 3.1972088622060055
		-6.4480209857935815 13.962492188536604 3.1972088622060055
		-6.4480209857935815 14.029114180952494 3.1972088622060055
		-6.4480209857935815 14.09634144070321 3.1972088622060055
		-6.4480209857935815 14.163568700453929 3.1972088622060055
		-6.4480209857935815 14.236651083758332 3.1972088622060055
		-6.4169307489535647 14.318615715912511 3.1972088622060055
		-6.3353694969189505 14.368279182246045 3.1972088622060055
		-6.2723814743778536 14.368279182246045 3.1972088622060055
		-6.2190840381695303 14.368279182246045 3.1972088622060055
		-6.1427718537318361 14.336381790855931 3.1972088622060055
		-6.1015876504394804 14.285103226800267 3.1972088622060055
		-6.0862446163902222 14.230594467300349 3.1972088622060055
		-6.0862446163902222 14.174874384508833 3.1972088622060055
		;
createNode nurbsCurve -n "MShape" -p "BOCA";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 27 1 no 3
		30 0 0 2.6000000000000001 2.6000000000000001 3.2000000000000002 3.2000000000000002
		 4.9554005454191383 4.9554005454191383 6.716488669289788 6.716488669289788 7.216488669289788
		 7.216488669289788 8.9775766631923037 8.9775766631923037 10.732977252074519 10.732977252074519
		 11.332977252074519 11.332977252074519 13.932977252074519 13.932977252074519 14.807978396501161
		 14.807978396501161 15.807978396501161 15.807978396501161 16.477298910783489 16.477298910783489
		 17.703907828221102 17.703907828221102 18.578907446745554 18.578907446745554
		29
		-6.5255444935228724 14.497485028461529 3.1972088622060055
		-6.5255444935228724 14.161549828301268 3.1972088622060055
		-6.5255444935228724 13.825614628141004 3.1972088622060055
		-6.6030680012521632 13.825614628141004 3.1972088622060055
		-6.6805915089814549 13.825614628141004 3.1972088622060055
		-6.6870517027144878 14.052330619241644 3.1972088622060055
		-6.6935118964475198 14.279046610342284 3.1972088622060055
		-6.7128928719575844 14.052330619241644 3.1972088622060055
		-6.7322738474676491 13.825614628141004 3.1972088622060055
		-6.7968767705753912 13.825614628141004 3.1972088622060055
		-6.8614796936831342 13.825614628141004 3.1972088622060055
		-6.8808604720377158 14.052330619241644 3.1972088622060055
		-6.9002412503922965 14.279046610342284 3.1972088622060055
		-6.9067016412808124 14.052330619241644 3.1972088622060055
		-6.9131620321693283 13.825614628141004 3.1972088622060055
		-6.9906855398986192 13.825614628141004 3.1972088622060055
		-7.0682090476279109 13.825614628141004 3.1972088622060055
		-7.0682090476279109 14.161549828301268 3.1972088622060055
		-7.0682090476279109 14.497485028461529 3.1972088622060055
		-6.9551537843227482 14.497485028461529 3.1972088622060055
		-6.8420985210175864 14.497485028461529 3.1972088622060055
		-6.8336196522873758 14.437323821245126 3.1972088622060055
		-6.8215064193714081 14.354955020349447 3.1972088622060055
		-6.8091914963956581 14.269356221164994 3.1972088622060055
		-6.7968765734199081 14.183757421980541 3.1972088622060055
		-6.774265599621069 14.340621225221035 3.1972088622060055
		-6.7516546258222299 14.497485028461529 3.1972088622060055
		-6.6385995596725511 14.497485028461529 3.1972088622060055
		-6.5255444935228724 14.497485028461529 3.1972088622060055
		;
createNode nurbsCurve -n "O_Shape2" -p "BOCA";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 15 1 no 3
		18 0 0 1 2 2 3 4 4 4.8609384298466471 4.8609384298466471 5.8609384298466471
		 6.8609384298466471 6.8609384298466471 7.8609384298466471 8.860938429846648 8.860938429846648
		 9.7406256198977665 9.7406256198977665
		17
		-6.2412916318488048 14.207579719070978 3.1972088622060055
		-6.2412916318488048 14.245129952488544 3.1972088622060055
		-6.2509818238706112 14.264914505273655 3.1972088622060055
		-6.2667290266613698 14.264914505273655 3.1972088622060055
		-6.2824758351411596 14.264914505273655 3.1972088622060055
		-6.2929739703349981 14.245129952488544 3.1972088622060055
		-6.2929739703349981 14.207579719070978 3.1972088622060055
		-6.2929739703349981 14.09634144070321 3.1972088622060055
		-6.2929739703349981 13.985103162335442 3.1972088622060055
		-6.2929739703349981 13.949975575501071 3.1972088622060055
		-6.2824758351411596 13.928979305113394 3.1972088622060055
		-6.2671328010919014 13.928979305113394 3.1972088622060055
		-6.2513855983011437 13.928979305113394 3.1972088622060055
		-6.2412916318488048 13.948360477778941 3.1972088622060055
		-6.2412916318488048 13.980258263480025 3.1972088622060055
		-6.2412916318488048 14.093918991275501 3.1972088622060055
		-6.2412916318488048 14.207579719070978 3.1972088622060055
		;
createNode nurbsCurve -n "UShape" -p "BOCA";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 29 1 no 3
		32 0 0 2.1000000000000001 2.1000000000000001 2.7109361409933621 2.7109361409933621
		 2.9440058568908842 2.9440058568908842 3.9440058568908842 4.9440058568908842 4.9440058568908842
		 5.9440058568908842 6.9440058568908842 7.9440058568908842 8.9440058568908842 8.9440058568908842
		 10.334630713837555 10.334630713837555 10.934630713837555 10.934630713837555 12.309630332362007
		 12.309630332362007 13.309630332362007 14.309630332362007 14.309630332362007 15.309630332362007
		 16.309630332362005 16.309630332362005 17.670567236306461 17.670567236306461 18.270567236306462
		 18.270567236306462
		31
		-5.646944739257572 14.368279182246045 3.1972088622060055
		-5.646944739257572 14.096946905193526 3.1972088622060055
		-5.646944739257572 13.825614628141004 3.1972088622060055
		-5.7258812603382419 13.825614628141004 3.1972088622060055
		-5.8048177814189126 13.825614628141004 3.1972088622060055
		-5.8034047680675336 13.855695428904692 3.1972088622060055
		-5.8019917547161546 13.885776229668377 3.1972088622060055
		-5.8185461120570094 13.855897316119957 3.1972088622060055
		-5.8665944806684136 13.825614628141004 3.1972088622060055
		-5.898088491938962 13.825614628141004 3.1972088622060055
		-5.933619853203866 13.825614628141004 3.1972088622060055
		-5.9808610672651721 13.851455797384105 3.1972088622060055
		-6.0030682666334787 13.893851718279024 3.1972088622060055
		-6.0087211086609305 13.940284989168298 3.1972088622060055
		-6.0087211086609305 14.008925459425878 3.1972088622060055
		-6.0087211086609305 14.188602320835962 3.1972088622060055
		-6.0087211086609305 14.368279182246045 3.1972088622060055
		-5.9311976009316396 14.368279182246045 3.1972088622060055
		-5.8536740932023488 14.368279182246045 3.1972088622060055
		-5.8536740932023488 14.190621192988623 3.1972088622060055
		-5.8536740932023488 14.012963203731204 3.1972088622060055
		-5.8536740932023488 13.951994447653732 3.1972088622060055
		-5.8455986045917037 13.928979305113394 3.1972088622060055
		-5.8282363040788159 13.928979305113394 3.1972088622060055
		-5.8092593001547677 13.928979305113394 3.1972088622060055
		-5.8019917547161546 13.952398222084266 3.1972088622060055
		-5.8019917547161546 14.016597173605991 3.1972088622060055
		-5.8019917547161546 14.192438177926018 3.1972088622060055
		-5.8019917547161546 14.368279182246045 3.1972088622060055
		-5.7244682469868629 14.368279182246045 3.1972088622060055
		-5.646944739257572 14.368279182246045 3.1972088622060055
		;
createNode nurbsCurve -n "TShape" -p "BOCA";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 33 1 no 3
		36 0 0 0.30000000000000027 0.30000000000000027 0.50000000000000022 0.50000000000000022
		 0.80000000000000027 0.80000000000000027 1.0000000000000002 1.0000000000000002 2.2234363317311363
		 2.2234363317311363 3.2234363317311363 4.2234363317311363 4.2234363317311363 4.5234363317311361
		 4.5234363317311361 4.7687479972533762 4.7687479972533762 5.7687479972533762 6.7687479972533762
		 7.7687479972533762 8.7687479972533762 8.7687479972533762 9.8874967574578463 9.8874967574578463
		 9.9874967574578459 9.9874967574578459 10.287496757457847 10.287496757457847 10.387496757457846
		 10.387496757457846 10.687496757457847 10.687496757457847 11.287496757457847 11.287496757457847
		
		35
		-5.4143742160696977 14.445802689975338 3.1972088622060055
		-5.4143742160696977 14.40704093611069 3.1972088622060055
		-5.4143742160696977 14.368279182246045 3.1972088622060055
		-5.3885330468266011 14.368279182246045 3.1972088622060055
		-5.3626918775835035 14.368279182246045 3.1972088622060055
		-5.3626918775835035 14.329517428381401 3.1972088622060055
		-5.3626918775835035 14.290755674516753 3.1972088622060055
		-5.3885330468266011 14.290755674516753 3.1972088622060055
		-5.4143742160696977 14.290755674516753 3.1972088622060055
		-5.4143742160696977 14.132680547984663 3.1972088622060055
		-5.4143742160696977 13.974605421452573 3.1972088622060055
		-5.4143742160696977 13.916462692077861 3.1972088622060055
		-5.4034723064453267 13.903138135870297 3.1972088622060055
		-5.3626918775835035 13.903138135870297 3.1972088622060055
		-5.3626918775835035 13.864376382005652 3.1972088622060055
		-5.3626918775835035 13.825614628141004 3.1972088622060055
		-5.3943875789138351 13.825614628141004 3.1972088622060055
		-5.4260832802441659 13.825614628141004 3.1972088622060055
		-5.4797844908830218 13.825614628141004 3.1972088622060055
		-5.5258139873417642 13.835305214473781 3.1972088622060055
		-5.5609419684871035 13.871240744480183 3.1972088622060055
		-5.5694212315282803 13.916866466508395 3.1972088622060055
		-5.5694212315282803 14.001657913987266 3.1972088622060055
		-5.5694212315282803 14.146206794252009 3.1972088622060055
		-5.5694212315282803 14.290755674516753 3.1972088622060055
		-5.5823418161498291 14.290755674516753 3.1972088622060055
		-5.5952624007713778 14.290755674516753 3.1972088622060055
		-5.5952624007713778 14.329517428381401 3.1972088622060055
		-5.5952624007713778 14.368279182246045 3.1972088622060055
		-5.5823418161498291 14.368279182246045 3.1972088622060055
		-5.5694212315282803 14.368279182246045 3.1972088622060055
		-5.5694212315282803 14.40704093611069 3.1972088622060055
		-5.5694212315282803 14.445802689975338 3.1972088622060055
		-5.4918977237989894 14.445802689975338 3.1972088622060055
		-5.4143742160696977 14.445802689975338 3.1972088622060055
		;
createNode nurbsCurve -n "HShape" -p "BOCA";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		2 28 1 no 3
		31 0 0 0.68906233310444809 0.68906233310444809 1.6890623331044481 2.6890623331044479
		 2.6890623331044479 3.6890623331044479 4.6890623331044479 5.6890623331044479 5.6890623331044479
		 7.110937666895552 7.110937666895552 7.7109376668955516 7.7109376668955516 9.1343755245288776
		 9.1343755245288776 10.134375524528878 11.134375524528878 11.134375524528878 12.134375524528878
		 13.134375524528878 13.134375524528878 14.576563668268864 14.576563668268864 15.176563668268864
		 15.176563668268864 17.776563668268864 17.776563668268864 18.376563668268865 18.376563668268865
		
		30
		-5.1559625236387276 14.497485028461529 3.1972088622060055
		-5.1559625236387276 14.408454146617551 3.1972088622060055
		-5.1559625236387276 14.319423264773576 3.1972088622060055
		-5.1357738021121149 14.344053110725078 3.1972088622060055
		-5.0885329823617749 14.368279182246045 3.1972088622060055
		-5.0614804898270815 14.368279182246045 3.1972088622060055
		-5.0202962865347258 14.368279182246045 3.1972088622060055
		-4.9621535571600157 14.325076106801028 3.1972088622060055
		-4.9492331696939509 14.268144700717915 3.1972088622060055
		-4.9492331696939509 14.193043839571818 3.1972088622060055
		-4.9492331696939509 14.009329233856413 3.1972088622060055
		-4.9492331696939509 13.825614628141004 3.1972088622060055
		-5.0267566774232417 13.825614628141004 3.1972088622060055
		-5.1042801851525335 13.825614628141004 3.1972088622060055
		-5.1042801851525335 14.009531121071678 3.1972088622060055
		-5.1042801851525335 14.193447614002348 3.1972088622060055
		-5.1042801851525335 14.239073336030557 3.1972088622060055
		-5.1135666027438074 14.264914505273655 3.1972088622060055
		-5.1301213543956301 14.264914505273655 3.1972088622060055
		-5.1454643884448883 14.264914505273655 3.1972088622060055
		-5.1559625236387276 14.238266181480462 3.1972088622060055
		-5.1559625236387276 14.198292907168735 3.1972088622060055
		-5.1559625236387276 14.01195376765487 3.1972088622060055
		-5.1559625236387276 13.825614628141004 3.1972088622060055
		-5.2334860313680185 13.825614628141004 3.1972088622060055
		-5.3110095390973093 13.825614628141004 3.1972088622060055
		-5.3110095390973093 14.161549828301268 3.1972088622060055
		-5.3110095390973093 14.497485028461529 3.1972088622060055
		-5.2334860313680185 14.497485028461529 3.1972088622060055
		-5.1559625236387276 14.497485028461529 3.1972088622060055
		;
createNode transform -n "CEJAS" -p "DRIVER_CARA";
	addAttr -ci true -sn "BS_CEJAS_ENOJADAS" -ln "BS_CEJAS_ENOJADAS" -min 0 -max 1 
		-at "double";
	addAttr -ci true -sn "BS_CEJAS_TRISTES" -ln "BS_CEJAS_TRISTES" -min 0 -max 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -6.0032081562833319 19.387357874155427 3.1962888346144744 ;
	setAttr ".sp" -type "double3" -6.0032081562833319 19.387357874155427 3.1962888346144744 ;
	setAttr -k on ".BS_CEJAS_ENOJADAS";
	setAttr -k on ".BS_CEJAS_TRISTES";
createNode nurbsCurve -n "CejaIzq" -p "CEJAS";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 19 0 no 3
		24 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 19 19
		22
		-6.3468681014810828 19.519836019890128 3.1962888346144744
		-6.259524756159573 19.421085086021222 3.1962888346144744
		-6.259524756159573 19.322334152152319 3.1962888346144744
		-6.3468681014810828 19.223583218283412 3.1962888346144744
		-6.5163452003192663 19.230152516237531 3.1962888346144744
		-6.6320986640034398 19.288805329366902 3.1962888346144744
		-6.8034691536766969 19.326107924145379 3.1962888346144744
		-7.0236922887957167 19.335024812459721 3.1962888346144744
		-7.2837649440941448 19.345717071820062 3.1962888346144744
		-7.4192102938360875 19.359880395941079 3.1962888346144744
		-7.5554722357842294 19.366496979864742 3.1962888346144744
		-7.6917341777323704 19.373113563788401 3.1962888346144744
		-7.6998449698789031 19.457681810124292 3.1962888346144744
		-7.6740215644764902 19.536809089465798 3.1962888346144744
		-7.5377596225283501 19.530192505542136 3.1962888346144744
		-7.4014976805802073 19.52357592161847 3.1962888346144744
		-7.2640108503227605 19.52827944799084 3.1962888346144744
		-7.0882578697935665 19.519463030534734 3.1962888346144744
		-6.8523128668848639 19.543968317172755 3.1962888346144744
		-6.6416932303035141 19.544328940867153 3.1962888346144744
		-6.4942806658922976 19.551132530027438 3.1962888346144744
		-6.3468681014810828 19.519836019890128 3.1962888346144744
		;
createNode nurbsCurve -n "CejaDer" -p "CEJAS";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 19 0 no 3
		24 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 19 19
		22
		-5.659548211085581 19.519836019890128 3.1962888346144744
		-5.7468915564070908 19.421085086021222 3.1962888346144744
		-5.7468915564070908 19.322334152152319 3.1962888346144744
		-5.659548211085581 19.223583218283412 3.1962888346144744
		-5.4900711122473975 19.230152516237531 3.1962888346144744
		-5.374317648563224 19.288805329366902 3.1962888346144744
		-5.2029471588899669 19.326107924145379 3.1962888346144744
		-4.9827240237709471 19.335024812459721 3.1962888346144744
		-4.7226513684725191 19.345717071820062 3.1962888346144744
		-4.5872060187305763 19.359880395941079 3.1962888346144744
		-4.4509440767824344 19.366496979864742 3.1962888346144744
		-4.3146821348342934 19.373113563788401 3.1962888346144744
		-4.3065713426877608 19.457681810124292 3.1962888346144744
		-4.3323947480901737 19.536809089465798 3.1962888346144744
		-4.4686566900383138 19.530192505542136 3.1962888346144744
		-4.6049186319864566 19.52357592161847 3.1962888346144744
		-4.7424054622439034 19.52827944799084 3.1962888346144744
		-4.9181584427730973 19.519463030534734 3.1962888346144744
		-5.1541034456818 19.543968317172755 3.1962888346144744
		-5.3647230822631498 19.544328940867153 3.1962888346144744
		-5.5121356466743663 19.551132530027438 3.1962888346144744
		-5.659548211085581 19.519836019890128 3.1962888346144744
		;
createNode transform -n "EXTRAS" -p "DRIVER_CARA";
	addAttr -ci true -sn "BS_CENO_ENOJADO" -ln "BS_CENO_ENOJADO" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_CACHETE_INFLADO_IZQ" -ln "BS_CACHETE_INFLADO_IZQ" -min 
		0 -max 1 -at "double";
	addAttr -ci true -sn "BS_CACHETE_INFLADO_DER" -ln "BS_CACHETE_INFLADO_DER" -min 
		0 -max 1 -at "double";
	addAttr -ci true -sn "BS_CABEZA_STRETCH" -ln "BS_CABEZA_STRETCH" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_CABEZA_SQUASH" -ln "BS_CABEZA_SQUASH" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_VACIO1" -ln "BS_VACIO1" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_VACIO2" -ln "BS_VACIO2" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_VACIO3" -ln "BS_VACIO3" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "BS_VACIO4" -ln "BS_VACIO4" -min 0 -max 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -1.7763568394002505e-015 -2.5375514703607962 8.8817841970012523e-016 ;
	setAttr ".sp" -type "double3" -1.7763568394002505e-015 -2.5375514703607962 8.8817841970012523e-016 ;
	setAttr -k on ".BS_CENO_ENOJADO";
	setAttr -k on ".BS_CACHETE_INFLADO_IZQ";
	setAttr -k on ".BS_CACHETE_INFLADO_DER";
	setAttr -k on ".BS_CABEZA_STRETCH";
	setAttr -k on ".BS_CABEZA_SQUASH";
	setAttr -k on ".BS_VACIO1";
	setAttr -k on ".BS_VACIO2";
	setAttr -k on ".BS_VACIO3";
	setAttr -k on ".BS_VACIO4";
createNode nurbsCurve -n "AntenaIzq" -p "EXTRAS";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 25 0 no 3
		30 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 25 25
		28
		-7.5474158300947076 19.956567258244185 3.1894929581659612
		-7.58460776191788 20.035662626066834 3.1894929581659612
		-7.6217996937410533 20.114757993889484 3.1894929581659612
		-7.6589916255642265 20.193853361712129 3.1894929581659612
		-7.6961835573873998 20.272948729534782 3.1894929581659612
		-7.8543742930326976 20.198564865888436 3.1894929581659612
		-8.057353922937887 20.19640698095554 3.1894929581659612
		-8.2207388611739081 20.445357910279071 3.1894929581659612
		-8.2313631463413763 20.754461823727468 3.1894929581659612
		-8.0155497441435557 20.95213867136663 3.1894929581659612
		-7.8257896300357643 21.044890552886038 3.1894929581659612
		-7.6015971934211173 21.057536674823847 3.1894929581659612
		-7.3563923310762682 20.928770197297688 3.1894929581659612
		-7.2877553866767455 20.675892523723299 3.1894929581659612
		-7.2954255158703507 20.447676956826651 3.1894929581659612
		-7.5399513130523985 20.346411678628304 3.1894929581659612
		-7.5008008899189287 20.268237225358476 3.1894929581659612
		-7.4636089580957554 20.18914185753583 3.1894929581659612
		-7.4264170262725822 20.110046489713181 3.1894929581659612
		-7.3892250944494098 20.030951121890531 3.1894929581659612
		-7.3520331626262365 19.951855754067882 3.1894929581659612
		-7.3148412308030633 19.872760386245233 3.1894929581659612
		-7.27764929897989 19.793665018422583 3.1894929581659612
		-7.3567446668025394 19.75647308659941 3.1894929581659612
		-7.4358400346251887 19.719281154776237 3.1894929581659612
		-7.473031966448362 19.798376522598886 3.1894929581659612
		-7.5102238982715344 19.877471890421536 3.1894929581659612
		-7.5474158300947076 19.956567258244185 3.1894929581659612
		;
createNode nurbsCurve -n "AntenaDer" -p "EXTRAS";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 25 0 no 3
		30 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 25 25
		28
		-4.604481024406927 20.033384663289933 3.1894929581659612
		-4.5627773772522433 20.110196920239833 3.1894929581659612
		-4.5210737300975596 20.187009177189733 3.1894929581659612
		-4.4793700829428751 20.263821434139629 3.1894929581659612
		-4.4376664357881914 20.340633691089529 3.1894929581659612
		-4.5912909496879903 20.424040985398896 3.1894929581659612
		-4.7132461800353154 20.586313313337957 3.1894929581659612
		-4.6094207657257122 20.865403776444236 3.1894929581659612
		-4.3666533503627658 21.057033854413302 3.1894929581659612
		-4.0795582625172058 21.000218617058305 3.1894929581659612
		-3.8924365122174733 20.902252995555877 3.1894929581659612
		-3.7494669333828932 20.729100252109113 3.1894929581659612
		-3.707995421776944 20.455263906864058 3.1894929581659612
		-3.8711001563185592 20.250190765036542 3.1894929581659612
		-4.0595270107218075 20.12120822204912 3.1894929581659612
		-4.2859438807755179 20.258259026538497 3.1894929581659612
		-4.3257455690430771 20.180414139830262 3.1894929581659612
		-4.3674492161977607 20.103601882880366 3.1894929581659612
		-4.4091528633524444 20.026789625930466 3.1894929581659612
		-4.450856510507128 19.949977368980566 3.1894929581659612
		-4.4925601576618126 19.873165112030666 3.1894929581659612
		-4.5342638048164963 19.796352855080769 3.1894929581659612
		-4.5759674519711799 19.71954059813087 3.1894929581659612
		-4.6527797089210789 19.761244245285553 3.1894929581659612
		-4.7295919658709789 19.802947892440237 3.1894929581659612
		-4.6878883187162943 19.879760149390137 3.1894929581659612
		-4.6461846715616106 19.956572406340033 3.1894929581659612
		-4.604481024406927 20.033384663289933 3.1894929581659612
		;
createNode transform -n "DRIVER_TOE_FINGERS_DER";
	setAttr ".rp" -type "double3" -1.2523799999999963 0.056667599999996821 2.0855000000000019 ;
	setAttr ".sp" -type "double3" -1.2523799999999963 0.056667599999996821 2.0855000000000019 ;
createNode nurbsCurve -n "DRIVER_TOE_FINGERS_DERShape" -p "DRIVER_TOE_FINGERS_DER";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 14 2 no 3
		19 -1 -0.4554399870000001 0 0.43359919600000002 1 1.73555149 2 3 4 5 6 7 8
		 8.4451647990000005 9 9.5445600129999999 10 10.433599195999999 11
		17
		-1.1375328502696782 0.75339471698938065 2.0855000000000019
		-1.248814473776374 0.89358129257399388 2.0855000000000019
		-1.36224550448986 0.75384205679495286 2.0855000000000019
		-1.4943426016305505 0.63581942382294199 2.0855000000000019
		-1.345419907420222 0.64285637731165979 2.0855000000000019
		-1.3092933749570916 0.64384858469026152 2.0855000000000019
		-1.3525539699861 0.43658174600410415 2.0855000000000019
		-1.31545679701304 0.45026113814077739 2.0855000000000019
		-1.2509638809831609 0.47933864649206759 2.0855000000000019
		-1.1864709649532796 0.45026113814077739 2.0855000000000019
		-1.1493737919802212 0.43658174600410404 2.0855000000000019
		-1.1960868365390154 0.65157281439845693 2.0855000000000019
		-1.1413903215202978 0.6382212524647457 2.0855000000000019
		-1.0191786702268872 0.65361291920137421 2.0855000000000019
		-1.1375328502696782 0.75339471698938065 2.0855000000000019
		-1.248814473776374 0.89358129257399388 2.0855000000000019
		-1.36224550448986 0.75384205679495286 2.0855000000000019
		;
createNode transform -n "DRIVER_TOE_FINGERS_IZQ";
	setAttr ".rp" -type "double3" 1.2523840219923323 0.056667576726437241 2.0854951605329939 ;
	setAttr ".sp" -type "double3" 1.2523840219923323 0.056667576726437241 2.0854951605329939 ;
createNode nurbsCurve -n "DRIVER_TOE_FINGERS_IZQShape" -p "DRIVER_TOE_FINGERS_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 14 2 no 3
		19 -1 -0.4554399870000001 0 0.43359919600000002 1 1.73555149 2 3 4 5 6 7 8
		 8.4451647990000005 9 9.5445600129999999 10 10.433599195999999 11
		17
		1.3672311717226504 0.75339469371582102 2.0854951605329939
		1.2559495482159546 0.89358126930043436 2.0854951605329939
		1.1425185175024686 0.75384203352139334 2.0854951605329939
		1.0104214203617783 0.63581940054938235 2.0854951605329939
		1.1593441145721066 0.64285635403810026 2.0854951605329939
		1.1954706470352372 0.64384856141670188 2.0854951605329939
		1.1522100520062288 0.43658172273054463 2.0854951605329939
		1.1893072249792889 0.45026111486721776 2.0854951605329939
		1.2538001410091677 0.47933862321850806 2.0854951605329939
		1.318293057039049 0.45026111486721776 2.0854951605329939
		1.3553902300121072 0.43658172273054452 2.0854951605329939
		1.3086771854533132 0.6515727911248973 2.0854951605329939
		1.363373700472031 0.63822122919118607 2.0854951605329939
		1.4855853517654414 0.65361289592781469 2.0854951605329939
		1.3672311717226504 0.75339469371582102 2.0854951605329939
		1.2559495482159546 0.89358126930043436 2.0854951605329939
		1.1425185175024686 0.75384203352139334 2.0854951605329939
		;
createNode transform -n "DRIVER_HEEL_IZQ";
	setAttr ".rp" -type "double3" 1.3141946792602541 0.11105763332017127 -0.77207473589158293 ;
	setAttr ".sp" -type "double3" 1.3141946792602541 0.11105763332017116 -0.77207473589158293 ;
createNode nurbsCurve -n "DRIVER_HEEL_IZQShape" -p "DRIVER_HEEL_IZQ";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 10 2 no 3
		15 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		2.2455954340526088 0.22683881447892215 -1.6425034823358304
		1.3152432716450233 0.22683881442594658 -2.0228794877002025
		0.38489110923787972 0.22683881447892215 -1.6425034823358304
		0.38489110923743919 0.22683881453455459 -1.4636291050429211
		0.38489110923743919 0.22683881453455459 -1.1089041471096697
		0.38489110923787972 0.22683881447892218 -0.93002976981653351
		1.3152432716450231 0.22683881442594658 -1.3918524767690275
		2.2455954340526088 0.22683881447892218 -0.93002976981653351
		2.2455954340521691 0.22683881453455459 -1.1089041471096688
		2.2455954340521691 0.22683881453455459 -1.4636291050429193
		2.2455954340526088 0.22683881447892215 -1.6425034823358304
		1.3152432716450233 0.22683881442594658 -2.0228794877002025
		0.38489110923787972 0.22683881447892215 -1.6425034823358304
		;
createNode transform -n "GRP_DRIVER_THUMB_IZQ_2";
	setAttr ".rp" -type "double3" 8.3994182093148364 13.366911724051116 0.14419431585190967 ;
	setAttr ".sp" -type "double3" 8.3994182093148364 13.366911724051116 0.14419431585190967 ;
createNode transform -n "DRIVER_THUMB_IZQ_2" -p "GRP_DRIVER_THUMB_IZQ_2";
	setAttr ".rp" -type "double3" 8.3991854997622895 13.362498682402094 0.14396224002365443 ;
	setAttr ".sp" -type "double3" 8.3991854997622895 13.362498682402094 0.14396224002365443 ;
createNode nurbsCurve -n "DRIVER_THUMB_IZQ_Shape2" -p "DRIVER_THUMB_IZQ_2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		8.3993891206207554 13.731077041739121 0.14416530637340763
		8.39946090514532 13.731047992625806 0.19681931678757353
		8.399519082533466 13.836356095293461 0.19687733574466759
		8.3993755134843191 13.836414193520087 0.091569314916279537
		8.3993173360962174 13.731106090852411 0.091511295959152139
		8.3993891206207554 13.731077041739121 0.14416530637340763
		8.3991854997622308 13.362498682402205 0.14396224002357649
		;
createNode transform -n "GRP_DRIVER_THUMB_IZQ_3";
	setAttr ".rp" -type "double3" 8.6187671521482265 13.292572923438978 0.2568306087574137 ;
	setAttr ".sp" -type "double3" 8.6187671521482265 13.292572923438978 0.2568306087574137 ;
createNode transform -n "DRIVER_THUMB_IZQ_3" -p "GRP_DRIVER_THUMB_IZQ_3";
	setAttr ".rp" -type "double3" 8.618650407542269 13.28786996212003 0.25665505233223129 ;
	setAttr ".sp" -type "double3" 8.618650407542269 13.28786996212003 0.25665505233223129 ;
createNode nurbsCurve -n "DRIVER_THUMB_IZQ_Shape3" -p "DRIVER_THUMB_IZQ_3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		8.6188037569712357 13.585236748547761 0.25680866420421911
		8.6187674313108218 13.58521482273254 0.29928962382111246
		8.6188112454333972 13.670176761711874 0.2993335129274568
		8.6188838967541397 13.670220613342334 0.21437159369372472
		8.6188400826316158 13.585258674363011 0.21432770458737194
		8.6188037569712357 13.585236748547761 0.25680866420421911
		8.6186504075422867 13.287869962120158 0.25665505233207142
		;
createNode transform -n "GRP_DRIVER_THUMB_DER_1";
	setAttr ".rp" -type "double3" -8.009389564510851 13.527359485493854 -0.077957228337077411 ;
	setAttr ".sp" -type "double3" -8.009389564510851 13.527359485493854 -0.077957228337077411 ;
createNode transform -n "DRIVER_THUMB_DER_1" -p "GRP_DRIVER_THUMB_DER_1";
	setAttr ".rp" -type "double3" -8.0092927672640037 13.526529478278784 -0.078054807649484137 ;
	setAttr ".sp" -type "double3" -8.0092927672640037 13.526529478278784 -0.078054807649484137 ;
createNode nurbsCurve -n "DRIVER_THUMB_DER_1Shape" -p "DRIVER_THUMB_DER_1";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		-8.0093774648550138 13.949742695493306 -0.07796942575112098
		-8.009134211338786 13.949730546860035 -0.017510882860310772
		-8.0091584106505067 14.070648608921335 -0.01748648803221009
		-8.0096449176829161 14.070672906187898 -0.13840357381382162
		-8.0096207183712274 13.949754844126602 -0.1384279686419454
		-8.0093774648550138 13.949742695493306 -0.07796942575112098
		-8.0092927672639966 13.526529478278768 -0.078054807649468927
		;
createNode transform -n "GRP_DRIVER_INDEX_IZQ_1";
	setAttr ".rp" -type "double3" 8.888091309513495 13.522959243006767 -0.25825695089670808 ;
	setAttr ".sp" -type "double3" 8.888091309513495 13.522959243006767 -0.25825695089670808 ;
createNode transform -n "DRIVER_INDEX_IZQ_1" -p "GRP_DRIVER_INDEX_IZQ_1";
	setAttr ".rp" -type "double3" 8.8880913095134932 13.522450921624028 -0.25825695089667455 ;
	setAttr ".sp" -type "double3" 8.8880913095134932 13.522450921624028 -0.25825695089667455 ;
createNode nurbsCurve -n "DRIVER_INDEX_IZQ_1Shape" -p "DRIVER_INDEX_IZQ_1";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		8.888091309513495 13.945664155926728 -0.25825695089670653
		8.8880913095135003 13.945664155926728 -0.19779791742491093
		8.8880913095135003 14.066582222870316 -0.19779791742491093
		8.8880913095134915 14.066582222870316 -0.31871598436850518
		8.8880913095134915 13.945664155926728 -0.31871598436850518
		8.888091309513495 13.945664155926728 -0.25825695089670653
		8.888091309513495 13.522450921624172 -0.25825695089670653
		;
createNode transform -n "GRP_DRIVER_INDEX_IZQ_2";
	setAttr ".rp" -type "double3" 9.2624078617368824 13.52750575778275 -0.25556402606055895 ;
	setAttr ".sp" -type "double3" 9.2624078617368824 13.52750575778275 -0.25556402606055895 ;
createNode transform -n "DRIVER_INDEX_IZQ_2" -p "GRP_DRIVER_INDEX_IZQ_2";
	setAttr ".rp" -type "double3" 9.262407861736774 13.522450921624026 -0.25556402606053563 ;
	setAttr ".sp" -type "double3" 9.262407861736774 13.522450921624026 -0.25556402606053563 ;
createNode nurbsCurve -n "DRIVER_INDEX_IZQ_Shape2" -p "DRIVER_INDEX_IZQ_2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		9.2624078617368859 13.884253057566122 -0.25556402606056072
		9.2624078617368628 13.884253057566122 -0.20387800664028041
		9.2624078617368628 13.98762509640668 -0.20387800664028041
		9.2624078617368824 13.98762509640668 -0.30725004548083923
		9.2624078617368824 13.884253057566122 -0.30725004548083923
		9.2624078617368859 13.884253057566122 -0.25556402606056072
		9.2624078617368859 13.52245092162417 -0.25556402606056072
		;
createNode transform -n "GRP_DRIVER_INDEX_IZQ_3";
	setAttr ".rp" -type "double3" 9.5842123796553977 13.526299616287371 -0.26162310694187907 ;
	setAttr ".sp" -type "double3" 9.5842123796553977 13.526299616287371 -0.26162310694187907 ;
createNode transform -n "DRIVER_INDEX_IZQ_3" -p "GRP_DRIVER_INDEX_IZQ_3";
	setAttr ".rp" -type "double3" 9.584212379655348 13.522450921624024 -0.26162310694184843 ;
	setAttr ".sp" -type "double3" 9.584212379655348 13.522450921624024 -0.26162310694184843 ;
createNode nurbsCurve -n "DRIVER_INDEX_IZQ_Shape3" -p "DRIVER_INDEX_IZQ_3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		9.5842123796554048 13.830682547242343 -0.26162310694188107
		9.5842123796553871 13.830682547242343 -0.21759001756787244
		9.5842123796553871 13.918748725990355 -0.21759001756787244
		9.5842123796554066 13.918748725990355 -0.30565619631588536
		9.5842123796554066 13.830682547242343 -0.30565619631588536
		9.5842123796554048 13.830682547242343 -0.26162310694188107
		9.5842123796554048 13.522450921624168 -0.26162310694188107
		;
createNode transform -n "GRP_DRIVER_MIDDLE_IZQ_1";
	setAttr ".rp" -type "double3" 8.903879820838899 13.526375923726041 -0.57453667904657324 ;
	setAttr ".sp" -type "double3" 8.903879820838899 13.526375923726041 -0.57453667904657324 ;
createNode transform -n "DRIVER_MIDDLE_IZQ_1" -p "GRP_DRIVER_MIDDLE_IZQ_1";
	setAttr ".rp" -type "double3" 8.9038798208388172 13.522450921624031 -0.57453667904656047 ;
	setAttr ".sp" -type "double3" 8.9038798208388172 13.522450921624031 -0.57453667904656047 ;
createNode nurbsCurve -n "DRIVER_MIDDLE_IZQ_1Shape" -p "DRIVER_MIDDLE_IZQ_1";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		8.9038798208388545 13.927969207060704 -0.57453667904657935
		8.9038798208389434 13.927969207060704 -0.51660549541278056
		8.9038798208389434 14.043831574328285 -0.51660549541278056
		8.9038798208389398 14.043831574328285 -0.63246786268036592
		8.9038798208389398 13.927969207060704 -0.63246786268036592
		8.9038798208388545 13.927969207060704 -0.57453667904657935
		8.9038798208388545 13.522450921624175 -0.57453667904657935
		;
createNode transform -n "GRP_DRIVER_MIDDLE_IZQ_2";
	setAttr ".rp" -type "double3" 9.3201363221284055 13.525253011662498 -0.58454284494296804 ;
	setAttr ".sp" -type "double3" 9.3201363221284055 13.525253011662498 -0.58454284494296804 ;
createNode transform -n "DRIVER_MIDDLE_IZQ_2" -p "GRP_DRIVER_MIDDLE_IZQ_2";
	setAttr ".rp" -type "double3" 9.3201363221283469 13.522450921624031 -0.58454284494294306 ;
	setAttr ".sp" -type "double3" 9.3201363221283469 13.522450921624031 -0.58454284494294306 ;
createNode nurbsCurve -n "DRIVER_MIDDLE_IZQ_Shape2" -p "DRIVER_MIDDLE_IZQ_2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		9.3201363221284268 13.869125765278914 -0.58454284494297359
		9.3201363221283842 13.869125765278914 -0.5350178672780016
		9.3201363221283842 13.968175720608839 -0.5350178672780016
		9.3201363221284215 13.968175720608839 -0.63406782260793637
		9.3201363221284215 13.869125765278914 -0.63406782260793637
		9.3201363221284268 13.869125765278914 -0.58454284494297359
		9.3201363221284268 13.522450921624175 -0.58454284494297359
		;
createNode transform -n "GRP_DRIVER_MIDDLE_IZQ_3";
	setAttr ".rp" -type "double3" 9.6251825321067734 13.52758689744066 -0.59475986874137665 ;
	setAttr ".sp" -type "double3" 9.6251825321067734 13.52758689744066 -0.59475986874137665 ;
createNode transform -n "DRIVER_MIDDLE_IZQ_3" -p "GRP_DRIVER_MIDDLE_IZQ_3";
	setAttr ".rp" -type "double3" 9.6251825321066615 13.52245092162403 -0.59475986874135778 ;
	setAttr ".sp" -type "double3" 9.6251825321066615 13.52245092162403 -0.59475986874135778 ;
createNode nurbsCurve -n "DRIVER_MIDDLE_IZQ_Shape3" -p "DRIVER_MIDDLE_IZQ_3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		9.6251825321068036 13.817795089071881 -0.59475986874138276
		9.625182532106745 13.817795089071881 -0.55256784482026999
		9.625182532106745 13.90217913691408 -0.55256784482026999
		9.6251825321067468 13.90217913691408 -0.6369518926624832
		9.6251825321067468 13.817795089071881 -0.6369518926624832
		9.6251825321068036 13.817795089071881 -0.59475986874138276
		9.6251825321068036 13.522450921624174 -0.59475986874138276
		;
createNode transform -n "GRP_DRIVER_CANCEL_IZQ_1";
	setAttr ".rp" -type "double3" 8.8683378737268601 13.612864277357048 -0.88725410853500908 ;
	setAttr ".sp" -type "double3" 8.8683378737268601 13.612864277357048 -0.88725410853500908 ;
createNode transform -n "DRIVER_CANCEL_IZQ_1" -p "GRP_DRIVER_CANCEL_IZQ_1";
	setAttr ".rp" -type "double3" 8.868337873726805 13.609787182757968 -0.88725410853499298 ;
	setAttr ".sp" -type "double3" 8.868337873726805 13.609787182757968 -0.88725410853499298 ;
createNode nurbsCurve -n "DRIVER_CANCEL_IZQ_1Shape" -p "DRIVER_CANCEL_IZQ_1";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		8.8683378737268299 13.97402400187106 -0.88725410853501718
		8.8683378737268903 13.97402400187106 -0.83522027723315706
		8.8683378737268903 14.078091664474758 -0.83522027723315706
		8.8683378737268388 14.078091664474758 -0.9392879398368611
		8.8683378737268388 13.97402400187106 -0.9392879398368611
		8.8683378737268299 13.97402400187106 -0.88725410853501718
		8.8683378737268299 13.609787182758112 -0.88725410853501718
		;
createNode transform -n "GRP_DRIVER_CANCEL_IZQ_2";
	setAttr ".rp" -type "double3" 9.2407542879003568 13.562397932085222 -0.91232952794318489 ;
	setAttr ".sp" -type "double3" 9.2407542879003568 13.562397932085222 -0.91232952794318489 ;
createNode transform -n "DRIVER_CANCEL_IZQ_2" -p "GRP_DRIVER_CANCEL_IZQ_2";
	setAttr ".rp" -type "double3" 9.2407542879003142 13.557638521758257 -0.91232952794318445 ;
	setAttr ".sp" -type "double3" 9.2407542879003142 13.557638521758257 -0.91232952794318445 ;
createNode nurbsCurve -n "DRIVER_CANCEL_IZQ_Shape2" -p "DRIVER_CANCEL_IZQ_2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		9.2407542879004136 13.869022118637027 -0.91232952794319366
		9.2407542879003319 13.869022118637043 -0.86784615696052436
		9.2407542879003159 13.957988860602349 -0.86784615696052436
		9.2407542879003159 13.957988860602349 -0.95681289892584365
		9.2407542879003319 13.869022118637011 -0.95681289892584565
		9.2407542879004136 13.869022118637027 -0.91232952794319366
		9.2407542879004136 13.557638521758401 -0.91232952794319366
		;
createNode transform -n "GRP_DRIVER_CANCEL_IZQ_3";
	setAttr ".rp" -type "double3" 9.5142116967567514 13.519634672333881 -0.92240182777641988 ;
	setAttr ".sp" -type "double3" 9.5142116967567514 13.519634672333881 -0.92240182777641988 ;
createNode transform -n "DRIVER_CANCEL_IZQ_3" -p "GRP_DRIVER_CANCEL_IZQ_3";
	setAttr ".rp" -type "double3" 9.5142116967567247 13.520259148550817 -0.922401827776413 ;
	setAttr ".sp" -type "double3" 9.5142116967567247 13.520259148550817 -0.922401827776413 ;
createNode nurbsCurve -n "DRIVER_CANCEL_IZQ_Shape3" -p "DRIVER_CANCEL_IZQ_3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		9.5142116967567549 13.785537494702229 -0.92240182777641921
		9.5142116967567532 13.785537494702261 -0.88450492118336843
		9.5142116967567691 13.861331307888348 -0.88450492118336843
		9.5142116967567798 13.861331307888348 -0.96029873436947177
		9.5142116967567798 13.785537494702245 -0.96029873436947133
		9.5142116967567549 13.785537494702229 -0.92240182777641921
		9.5142116967567389 13.520259148550945 -0.92240182777641921
		;
createNode transform -n "GRP_DRIVER_PINKY_IZQ_1";
	setAttr ".rp" -type "double3" 8.8336770876506385 13.511497790099181 -1.170459447986719 ;
	setAttr ".sp" -type "double3" 8.8336770876506385 13.511497790099181 -1.170459447986719 ;
createNode transform -n "DRIVER_PINKY_IZQ_1" -p "GRP_DRIVER_PINKY_IZQ_1";
	setAttr ".rp" -type "double3" 8.8336770876506101 13.504234750385011 -1.1704594479867017 ;
	setAttr ".sp" -type "double3" 8.8336770876506101 13.504234750385011 -1.1704594479867017 ;
createNode nurbsCurve -n "DRIVER_PINKY_IZQ_1Shape" -p "DRIVER_PINKY_IZQ_1";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		8.8336770876506243 13.840362767440379 -1.1704594479867025
		8.8336770876506527 13.840362767440379 -1.1224411598359894
		8.8336770876506527 13.93639934374187 -1.1224411598359894
		8.8336770876506243 13.93639934374187 -1.2184777361374484
		8.8336770876506243 13.840362767440379 -1.2184777361374484
		8.8336770876506243 13.840362767440379 -1.1704594479867025
		8.8336770876506243 13.504234750385155 -1.1704594479867025
		;
createNode transform -n "GRP_DRIVER_PINKY_IZQ_2";
	setAttr ".rp" -type "double3" 9.0547639351312945 13.48285424574615 -1.194781458888567 ;
	setAttr ".sp" -type "double3" 9.0547639351312945 13.48285424574615 -1.194781458888567 ;
createNode transform -n "DRIVER_PINKY_IZQ_2" -p "GRP_DRIVER_PINKY_IZQ_2";
	setAttr ".rp" -type "double3" 9.0547639351312235 13.478673298299844 -1.1947814588885604 ;
	setAttr ".sp" -type "double3" 9.0547639351312235 13.478673298299844 -1.1947814588885604 ;
createNode nurbsCurve -n "DRIVER_PINKY_IZQ_Shape2" -p "DRIVER_PINKY_IZQ_2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		9.0547639351313176 13.766026870125136 -1.1947814588885861
		9.0547639351313371 13.766026870125136 -1.1537309486278366
		9.0547639351313371 13.848127890646607 -1.1537309486278366
		9.0547639351312057 13.848127890646607 -1.2358319691492938
		9.0547639351312217 13.76602687012512 -1.2358319691492961
		9.0547639351313176 13.766026870125136 -1.1947814588885861
		9.0547639351313176 13.478673298299972 -1.1947814588885839
		;
createNode transform -n "GRP_DRIVER_PINKY_IZQ_3";
	setAttr ".rp" -type "double3" 9.2696220985294655 13.459588793980547 -1.2027697698918915 ;
	setAttr ".sp" -type "double3" 9.2696220985294655 13.459588793980547 -1.2027697698918915 ;
createNode transform -n "DRIVER_PINKY_IZQ_3" -p "GRP_DRIVER_PINKY_IZQ_3";
	setAttr ".rp" -type "double3" 9.2696220985293802 13.452850634295556 -1.2027697698918804 ;
	setAttr ".sp" -type "double3" 9.2696220985293802 13.452850634295554 -1.2027697698918796 ;
createNode nurbsCurve -n "DRIVER_PINKY_IZQ_Shape3" -p "DRIVER_PINKY_IZQ_3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		9.2696220985294193 13.662133925534887 -1.2027697698918933
		9.2696220985295277 13.662133925534887 -1.1728721568577227
		9.2696220985295117 13.721929151603252 -1.1728721568577227
		9.2696220985295241 13.721929151603236 -1.2326673829260599
		9.2696220985295241 13.662133925534903 -1.2326673829260604
		9.2696220985294193 13.662133925534887 -1.2027697698918933
		9.2696220985294353 13.45285063429573 -1.2027697698918898
		;
createNode transform -n "GRP_DRIVER_THUMB_DER_2";
	setAttr ".rp" -type "double3" -8.3897142421565256 13.36408149475179 0.14586287624738326 ;
	setAttr ".sp" -type "double3" -8.3897142421565256 13.36408149475179 0.14586287624738326 ;
createNode transform -n "DRIVER_THUMB_DER_2" -p "GRP_DRIVER_THUMB_DER_2";
	setAttr ".rp" -type "double3" -8.3895850641330583 13.358429732640959 0.14565071812126318 ;
	setAttr ".sp" -type "double3" -8.3895850641330583 13.358429732640959 0.14565071812126318 ;
createNode nurbsCurve -n "DRIVER_THUMB_DER_Shape2" -p "DRIVER_THUMB_DER_2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		-8.3897708400995228 13.727008110594065 0.14583635648162535
		-8.3897903413324162 13.72698158099748 0.19849041354707009
		-8.3898434201800018 13.832289688984094 0.19854345307859325
		-8.3898044177141973 13.83234274817729 0.093235338947697477
		-8.3897513388666294 13.727034640190674 0.093182299416169234
		-8.3897708400995228 13.727008110594065 0.14583635648162535
		-8.38958506413306 13.35842973264096 0.14565071812126013
		;
createNode transform -n "GRP_DRIVER_THUMB_DER_3";
	setAttr ".rp" -type "double3" -8.6174208769220346 13.294808684669247 0.26706205679572825 ;
	setAttr ".sp" -type "double3" -8.6174208769220346 13.294808684669247 0.26706205679572825 ;
createNode transform -n "DRIVER_THUMB_DER_3" -p "GRP_DRIVER_THUMB_DER_3";
	setAttr ".rp" -type "double3" -8.6176862039003215 13.290841072898651 0.26752751172778444 ;
	setAttr ".sp" -type "double3" -8.6176862039003215 13.290841072898651 0.26752751172778444 ;
createNode nurbsCurve -n "DRIVER_THUMB_DER_Shape3" -p "DRIVER_THUMB_DER_3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		-8.6172787987555388 13.588207380560839 0.2671202386622254
		-8.6172856460973737 13.588265571862348 0.30960117906086487
		-8.6171692446274264 13.673227374051525 0.30948481532784555
		-8.6171555499437495 13.673110991448505 0.22452293453060759
		-8.6172719514136791 13.58814918925934 0.22463929826362666
		-8.6172787987555388 13.588207380560839 0.2671202386622254
		-8.617686203900325 13.290841072898658 0.26752751172778222
		;
createNode transform -n "GRP_DRIVER_INDEX_DER_1";
	setAttr ".rp" -type "double3" -8.8880900000000143 13.523417674845675 -0.2582569999999984 ;
	setAttr ".sp" -type "double3" -8.8880900000000143 13.523417674845675 -0.2582569999999984 ;
createNode transform -n "DRIVER_INDEX_DER_1" -p "GRP_DRIVER_INDEX_DER_1";
	setAttr ".rp" -type "double3" -8.8880900000000018 13.522499999999994 -0.25825699999999929 ;
	setAttr ".sp" -type "double3" -8.8880900000000018 13.522499999999994 -0.25825699999999929 ;
createNode nurbsCurve -n "DRIVER_INDEX_DER_1Shape" -p "DRIVER_INDEX_DER_1";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		-8.8880900000000018 13.945713234302536 -0.25825699999999846
		-8.8880900000000018 13.945713234302547 -0.19779796652820536
		-8.8880900000000267 14.066631301246135 -0.19779796652820392
		-8.8880900000000302 14.066631301246135 -0.31871603347179034
		-8.8880900000000054 13.945713234302547 -0.31871603347179323
		-8.8880900000000018 13.945713234302536 -0.25825699999999846
		-8.8880900000000018 13.52249999999998 -0.25825699999999918
		;
createNode transform -n "GRP_DRIVER_INDEX_DER_2";
	setAttr ".rp" -type "double3" -9.2624100000000134 13.528494357264378 -0.25556399999999913 ;
	setAttr ".sp" -type "double3" -9.2624100000000134 13.528494357264378 -0.25556399999999913 ;
createNode transform -n "DRIVER_INDEX_DER_2" -p "GRP_DRIVER_INDEX_DER_2";
	setAttr ".rp" -type "double3" -9.2624100000000009 13.522499999999992 -0.25556399999999935 ;
	setAttr ".sp" -type "double3" -9.2624100000000009 13.522499999999992 -0.25556399999999935 ;
createNode nurbsCurve -n "DRIVER_INDEX_DER_Shape2" -p "DRIVER_INDEX_DER_2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		-9.2624099999999903 13.884302135941933 -0.25556399999999868
		-9.2624100000000258 13.884302135941947 -0.20387798057972034
		-9.2624100000000009 13.987674174782505 -0.20387798057972079
		-9.2624100000000045 13.987674174782491 -0.30725001942027819
		-9.2624100000000062 13.884302135941933 -0.3072500194202773
		-9.2624099999999903 13.884302135941933 -0.25556399999999868
		-9.2624099999999885 13.522499999999981 -0.25556399999999874
		;
createNode transform -n "GRP_DRIVER_INDEX_DER_3";
	setAttr ".rp" -type "double3" -9.5842099999999935 13.52902690022804 -0.26162300000000094 ;
	setAttr ".sp" -type "double3" -9.5842099999999935 13.52902690022804 -0.26162300000000094 ;
createNode transform -n "DRIVER_INDEX_DER_3" -p "GRP_DRIVER_INDEX_DER_3";
	setAttr ".rp" -type "double3" -9.5842100000000059 13.522499999999996 -0.26162299999999938 ;
	setAttr ".sp" -type "double3" -9.5842100000000059 13.522499999999996 -0.26162299999999938 ;
createNode nurbsCurve -n "DRIVER_INDEX_DER_Shape3" -p "DRIVER_INDEX_DER_3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		-9.5842100000000059 13.830731625618014 -0.26162299999999938
		-9.5842100000000023 13.830731625618014 -0.21758991062599509
		-9.5842100000000094 13.918797804366024 -0.21758991062599764
		-9.5842100000000059 13.918797804366024 -0.30565608937400734
		-9.5842100000000059 13.830731625618014 -0.30565608937400401
		-9.5842100000000059 13.830731625618014 -0.26162299999999938
		-9.5842099999999935 13.522499999999981 -0.26162300000000183
		;
createNode transform -n "GRP_DRIVER_MIDDLE_DER_1";
	setAttr ".rp" -type "double3" -8.9038800000000027 13.529344397677148 -0.57453700000000474 ;
	setAttr ".sp" -type "double3" -8.9038800000000027 13.529344397677148 -0.57453700000000474 ;
createNode transform -n "DRIVER_MIDDLE_DER_1" -p "GRP_DRIVER_MIDDLE_DER_1";
	setAttr ".rp" -type "double3" -8.9038800000000027 13.522499999999994 -0.57453699999999952 ;
	setAttr ".sp" -type "double3" -8.9038800000000027 13.522499999999994 -0.57453699999999952 ;
createNode nurbsCurve -n "DRIVER_MIDDLE_DER_1Shape" -p "DRIVER_MIDDLE_DER_1";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		-8.9038800000000187 13.928018285436501 -0.5745370000000054
		-8.9038799999999974 13.92801828543649 -0.5166058163662135
		-8.9038800000000116 14.043880652704077 -0.51660581636621261
		-8.9038799999999991 14.04388065270407 -0.63246818363379409
		-8.9038799999999902 13.92801828543649 -0.63246818363379698
		-8.9038800000000187 13.928018285436501 -0.5745370000000054
		-8.9038799999999991 13.522499999999972 -0.5745370000000013
		;
createNode transform -n "GRP_DRIVER_MIDDLE_DER_2";
	setAttr ".rp" -type "double3" -9.3201400000000056 13.528247424474637 -0.5845430000000027 ;
	setAttr ".sp" -type "double3" -9.3201400000000056 13.528247424474637 -0.5845430000000027 ;
createNode transform -n "DRIVER_MIDDLE_DER_2" -p "GRP_DRIVER_MIDDLE_DER_2";
	setAttr ".rp" -type "double3" -9.3201400000000039 13.522499999999994 -0.58454299999999948 ;
	setAttr ".sp" -type "double3" -9.3201400000000039 13.522499999999994 -0.58454299999999948 ;
createNode nurbsCurve -n "DRIVER_MIDDLE_DER_Shape2" -p "DRIVER_MIDDLE_DER_2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		-9.3201400000000163 13.869174843654706 -0.58454300000000325
		-9.3201400000000429 13.869174843654715 -0.53501802233503848
		-9.320140000000011 13.96822479898464 -0.53501802233504003
		-9.320139999999995 13.968224798984625 -0.63406797766496603
		-9.3201400000000181 13.869174843654701 -0.63406797766496648
		-9.3201400000000163 13.869174843654706 -0.58454300000000325
		-9.3201400000000163 13.522499999999958 -0.58454300000000348
		;
createNode transform -n "GRP_DRIVER_MIDDLE_DER_3";
	setAttr ".rp" -type "double3" -9.6251800000000234 13.528211424183292 -0.59476000000000573 ;
	setAttr ".sp" -type "double3" -9.6251800000000234 13.528211424183292 -0.59476000000000573 ;
createNode transform -n "DRIVER_MIDDLE_DER_3" -p "GRP_DRIVER_MIDDLE_DER_3";
	setAttr ".rp" -type "double3" -9.6251800000000038 13.522499999999996 -0.59475999999999951 ;
	setAttr ".sp" -type "double3" -9.6251800000000038 13.522499999999996 -0.59475999999999951 ;
createNode nurbsCurve -n "DRIVER_MIDDLE_DER_Shape3" -p "DRIVER_MIDDLE_DER_3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		-9.6251800000000483 13.817844167447678 -0.59476000000000762
		-9.6251800000000749 13.817844167447678 -0.55256797607890329
		-9.6251800000000483 13.902228215289878 -0.55256797607890418
		-9.6251800000000163 13.902228215289867 -0.63695202392110961
		-9.6251800000000287 13.817844167447667 -0.63695202392110972
		-9.6251800000000483 13.817844167447678 -0.59476000000000762
		-9.6251800000000411 13.522499999999971 -0.59476000000000795
		;
createNode transform -n "GRP_DRIVER_CANCEL_DER_1";
	setAttr ".rp" -type "double3" -8.8683399999999839 13.614484692665702 -0.8872539999999991 ;
	setAttr ".sp" -type "double3" -8.8683399999999839 13.614484692665702 -0.8872539999999991 ;
createNode transform -n "DRIVER_CANCEL_DER_1" -p "GRP_DRIVER_CANCEL_DER_1";
	setAttr ".rp" -type "double3" -8.8683400000000034 13.609799999999993 -0.88725399999999965 ;
	setAttr ".sp" -type "double3" -8.8683400000000034 13.609799999999993 -0.88725399999999965 ;
createNode nurbsCurve -n "DRIVER_CANCEL_DER_1Shape" -p "DRIVER_CANCEL_DER_1";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		-8.8683399999999679 13.974036819112898 -0.88725400000000021
		-8.8683399999999839 13.974036819112898 -0.83522016869815063
		-8.8683400000000034 14.078104481716601 -0.83522016869814752
		-8.8683399999999786 14.078104481716586 -0.93928783130184679
		-8.8683399999999679 13.974036819112884 -0.93928783130184956
		-8.8683399999999679 13.974036819112898 -0.88725400000000021
		-8.8683399999999679 13.609799999999943 -0.88725399999999977
		;
createNode transform -n "GRP_DRIVER_CANCEL_DER_2";
	setAttr ".rp" -type "double3" -9.2407499999999985 13.567049264461856 -0.91232999999999786 ;
	setAttr ".sp" -type "double3" -9.2407499999999985 13.567049264461856 -0.91232999999999786 ;
createNode transform -n "DRIVER_CANCEL_DER_2" -p "GRP_DRIVER_CANCEL_DER_2";
	setAttr ".rp" -type "double3" -9.2407500000000038 13.557599999999995 -0.91232999999999975 ;
	setAttr ".sp" -type "double3" -9.2407500000000038 13.557599999999995 -0.91232999999999975 ;
createNode nurbsCurve -n "DRIVER_CANCEL_DER_Shape2" -p "DRIVER_CANCEL_DER_2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		-9.2407499999999914 13.868983596878586 -0.91233000000000408
		-9.2407500000000162 13.868983596878577 -0.867846629017341
		-9.2407500000000073 13.95795033884391 -0.86784662901734344
		-9.2407500000000091 13.95795033884391 -0.9568133709826605
		-9.2407500000000233 13.868983596878598 -0.95681337098266139
		-9.2407499999999914 13.868983596878586 -0.91233000000000408
		-9.2407499999999683 13.557599999999978 -0.91233000000000208
		;
createNode transform -n "GRP_DRIVER_CANCEL_DER_3";
	setAttr ".rp" -type "double3" -9.5142099999999949 13.529312544139945 -0.92240199999999706 ;
	setAttr ".sp" -type "double3" -9.5142099999999949 13.529312544139945 -0.92240199999999706 ;
createNode transform -n "DRIVER_CANCEL_DER_3" -p "GRP_DRIVER_CANCEL_DER_3";
	setAttr ".rp" -type "double3" -9.5142100000000038 13.520299999999995 -0.92240199999999961 ;
	setAttr ".sp" -type "double3" -9.5142100000000038 13.520299999999995 -0.92240199999999961 ;
createNode nurbsCurve -n "DRIVER_CANCEL_DER_Shape3" -p "DRIVER_CANCEL_DER_3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		-9.5142099999999576 13.785578346151286 -0.92240199999999617
		-9.5142099999999505 13.785578346151299 -0.8845050934069516
		-9.5142099999999736 13.861372159337373 -0.88450509340695005
		-9.5142099999999754 13.861372159337357 -0.96029890659303563
		-9.5142099999999843 13.78557834615127 -0.9602989065930374
		-9.5142099999999576 13.785578346151286 -0.92240199999999617
		-9.5142099999999576 13.520299999999988 -0.92240199999999462
		;
createNode transform -n "GRP_DRIVER_PINKY_DER_1";
	setAttr ".rp" -type "double3" -8.8336799999999833 13.506741445663581 -1.1704600000000136 ;
	setAttr ".sp" -type "double3" -8.8336799999999833 13.506741445663581 -1.1704600000000136 ;
createNode transform -n "DRIVER_PINKY_DER_1" -p "GRP_DRIVER_PINKY_DER_1";
	setAttr ".rp" -type "double3" -8.83368 13.504199999999994 -1.1704599999999996 ;
	setAttr ".sp" -type "double3" -8.83368 13.504199999999994 -1.1704599999999996 ;
createNode nurbsCurve -n "DRIVER_PINKY_DER_1Shape" -p "DRIVER_PINKY_DER_1";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		-8.8336800000000064 13.840328017055164 -1.1704600000000112
		-8.83368000000001 13.840328017055167 -1.122441711849266
		-8.8336799999999887 13.936364593356659 -1.1224417118492653
		-8.833679999999978 13.936364593356661 -1.2184782881507601
		-8.8336799999999958 13.840328017055167 -1.2184782881507599
		-8.8336800000000064 13.840328017055164 -1.1704600000000112
		-8.8336799999999798 13.504199999999946 -1.1704600000000134
		;
createNode transform -n "GRP_DRIVER_PINKY_DER_2";
	setAttr ".rp" -type "double3" -9.0547600000000017 13.48620628373842 -1.1947800000000139 ;
	setAttr ".sp" -type "double3" -9.0547600000000017 13.48620628373842 -1.1947800000000139 ;
createNode transform -n "DRIVER_PINKY_DER_2" -p "GRP_DRIVER_PINKY_DER_2";
	setAttr ".rp" -type "double3" -9.0547600000000017 13.478699999999993 -1.1947799999999995 ;
	setAttr ".sp" -type "double3" -9.0547600000000017 13.478699999999993 -1.1947799999999995 ;
createNode nurbsCurve -n "DRIVER_PINKY_DER_Shape2" -p "DRIVER_PINKY_DER_2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		-9.0547600000000017 13.766053571825035 -1.1947800000000139
		-9.054760000000007 13.766053571825079 -1.1537294897392814
		-9.0547600000000177 13.848154592346548 -1.1537294897392818
		-9.0547600000000017 13.848154592346555 -1.2358305102607516
		-9.0547599999999893 13.766053571825076 -1.2358305102607523
		-9.0547600000000017 13.766053571825035 -1.1947800000000139
		-9.0547600000000017 13.478699999999868 -1.1947800000000162
		;
createNode transform -n "GRP_DRIVER_PINKY_DER_3";
	setAttr ".rp" -type "double3" -9.2696199999999891 13.462851670028734 -1.2027700000000161 ;
	setAttr ".sp" -type "double3" -9.2696199999999891 13.462851670028734 -1.2027700000000161 ;
createNode transform -n "DRIVER_PINKY_DER_3" -p "GRP_DRIVER_PINKY_DER_3";
	setAttr ".rp" -type "double3" -9.2696200000000015 13.452899999999994 -1.2027699999999997 ;
	setAttr ".sp" -type "double3" -9.2696200000000015 13.452899999999993 -1.2027699999999988 ;
createNode nurbsCurve -n "DRIVER_PINKY_DER_Shape3" -p "DRIVER_PINKY_DER_3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		-9.2696199999999713 13.662183291239142 -1.2027700000000112
		-9.2696199999999482 13.662183291239142 -1.1728723869658446
		-9.26961999999995 13.721978517307464 -1.1728723869658424
		-9.2696199999999696 13.721978517307468 -1.2326676130341783
		-9.2696199999999624 13.662183291239142 -1.2326676130341823
		-9.2696199999999713 13.662183291239142 -1.2027700000000112
		-9.2696199999999802 13.452899999999971 -1.2027700000000054
		;
createNode joint -n "R_REV_DER_1";
	setAttr ".t" -type "double3" -1.31419 0.111058 -0.772075 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -41.334252489082139 88.349622908284374 138.65395815421752 ;
	setAttr ".radi" 0.59614253979186849;
createNode joint -n "R_REV_DER_2" -p "R_REV_DER_1";
	setAttr ".t" -type "double3" -2.858844105958716 -1.3375094301132373e-006 -0.0038483321687325933 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -179.46902035323063 -1.1196301958058767 155.71567671224267 ;
	setAttr ".radi" 0.5;
createNode joint -n "R_REV_DER_3" -p "R_REV_DER_2";
	setAttr ".t" -type "double3" -0.98627085442002738 3.8518170319967737e-007 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -6.112773187408598e-016 1.1703403210666104e-014 -5.9797672800989918 ;
	setAttr ".radi" 0.52608389778031561;
createNode joint -n "R_REV_DER_4" -p "R_REV_DER_3";
	setAttr ".t" -type "double3" -1.5042929908338496 1.4673953029342712e-006 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -19.389530444065588 -89.999999999999901 0 ;
	setAttr ".radi" 0.52608389778031561;
	addAttr -ci true -m -sn "stringOptions" -ln "stringOptions" -at "compound" -nc 
		3;
	addAttr -ci true -sn "name" -ln "name" -dt "string" -p "stringOptions";
	addAttr -ci true -sn "value" -ln "value" -dt "string" -p "stringOptions";
	addAttr -ci true -sn "type" -ln "type" -dt "string" -p "stringOptions";
createNode lightLinker -s -n "lightLinker1";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode displayLayerManager -n "layerManager";
	setAttr ".cdl" 2;
	setAttr -s 66 ".dli[1:65]"  1 2 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
		0 0 0 0 0 0;
	setAttr -s 2 ".dli";
createNode displayLayer -n "defaultLayer";
createNode renderLayerManager -n "renderLayerManager";
createNode renderLayer -n "defaultRenderLayer";
	setAttr ".g" yes;
createNode hyperGraphInfo -n "nodeEditorPanel1Info";
createNode hyperView -n "hyperView1";
	setAttr ".vl" -type "double2" -541.66666666666674 -292.26190476190482 ;
	setAttr ".vh" -type "double2" 577.38095238095264 291.07142857142861 ;
	setAttr ".dag" no;
createNode hyperLayout -n "hyperLayout1";
	setAttr ".ihi" 0;
	setAttr -s 175 ".hyp";
	setAttr ".hyp[0].x" 1.4285714626312256;
	setAttr ".hyp[0].y" -72.857139587402344;
	setAttr ".hyp[0].nvs" 1920;
	setAttr ".hyp[1].x" 772.85711669921875;
	setAttr ".hyp[1].y" -72.857139587402344;
	setAttr ".hyp[1].nvs" 1920;
	setAttr ".hyp[2].x" 481.42855834960937;
	setAttr ".hyp[2].y" -72.857139587402344;
	setAttr ".hyp[2].nvs" 1920;
	setAttr ".hyp[3].x" 241.42857360839844;
	setAttr ".hyp[3].y" -72.857139587402344;
	setAttr ".hyp[3].nvs" 1920;
	setAttr ".hyp[4].nvs" 1920;
	setAttr ".hyp[5].nvs" 1920;
	setAttr ".hyp[6].nvs" 1920;
	setAttr ".hyp[7].nvs" 1920;
	setAttr ".hyp[8].nvs" 1920;
	setAttr ".hyp[9].nvs" 1920;
	setAttr ".hyp[10].nvs" 1920;
	setAttr ".hyp[11].nvs" 1920;
	setAttr ".hyp[12].nvs" 1920;
	setAttr ".hyp[13].nvs" 1920;
	setAttr ".hyp[14].nvs" 1920;
	setAttr ".hyp[15].nvs" 1920;
	setAttr ".hyp[16].nvs" 1920;
	setAttr ".hyp[17].nvs" 1920;
	setAttr ".hyp[18].nvs" 1920;
	setAttr ".hyp[19].nvs" 1920;
	setAttr ".hyp[20].nvs" 1920;
	setAttr ".hyp[21].nvs" 1920;
	setAttr ".hyp[22].nvs" 1920;
	setAttr ".hyp[23].nvs" 1920;
	setAttr ".hyp[24].nvs" 1920;
	setAttr ".hyp[25].nvs" 1920;
	setAttr ".hyp[26].nvs" 1920;
	setAttr ".hyp[27].nvs" 1920;
	setAttr ".hyp[28].nvs" 1920;
	setAttr ".hyp[29].nvs" 1920;
	setAttr ".hyp[30].nvs" 1920;
	setAttr ".hyp[31].nvs" 1920;
	setAttr ".hyp[32].nvs" 1920;
	setAttr ".hyp[33].nvs" 1920;
	setAttr ".hyp[34].nvs" 1920;
	setAttr ".hyp[35].nvs" 1920;
	setAttr ".hyp[36].nvs" 1920;
	setAttr ".hyp[37].nvs" 1920;
	setAttr ".hyp[38].nvs" 1920;
	setAttr ".hyp[39].nvs" 1920;
	setAttr ".hyp[40].nvs" 1920;
	setAttr ".hyp[41].nvs" 1920;
	setAttr ".hyp[42].nvs" 1920;
	setAttr ".hyp[43].nvs" 1920;
	setAttr ".hyp[44].nvs" 1920;
	setAttr ".hyp[45].nvs" 1920;
	setAttr ".hyp[46].nvs" 1920;
	setAttr ".hyp[47].nvs" 1920;
	setAttr ".hyp[48].nvs" 1920;
	setAttr ".hyp[49].nvs" 1920;
	setAttr ".hyp[50].nvs" 1920;
	setAttr ".hyp[51].nvs" 1920;
	setAttr ".hyp[52].nvs" 1920;
	setAttr ".hyp[53].nvs" 1920;
	setAttr ".hyp[54].nvs" 1920;
	setAttr ".hyp[55].nvs" 1920;
	setAttr ".hyp[56].nvs" 1920;
	setAttr ".hyp[57].nvs" 1920;
	setAttr ".hyp[58].nvs" 1920;
	setAttr ".hyp[59].nvs" 1920;
	setAttr ".hyp[60].nvs" 1920;
	setAttr ".hyp[61].nvs" 1920;
	setAttr ".hyp[62].nvs" 1920;
	setAttr ".hyp[63].nvs" 1920;
	setAttr ".hyp[64].nvs" 1920;
	setAttr ".hyp[65].nvs" 1920;
	setAttr ".hyp[66].nvs" 1920;
	setAttr ".hyp[67].nvs" 1920;
	setAttr ".hyp[68].nvs" 1920;
	setAttr ".hyp[69].nvs" 1920;
	setAttr ".hyp[70].nvs" 1920;
	setAttr ".hyp[71].nvs" 1920;
	setAttr ".hyp[72].nvs" 1920;
	setAttr ".hyp[73].nvs" 1920;
	setAttr ".hyp[74].nvs" 1920;
	setAttr ".hyp[75].nvs" 1920;
	setAttr ".hyp[76].nvs" 1920;
	setAttr ".hyp[77].nvs" 1920;
	setAttr ".hyp[78].nvs" 1920;
	setAttr ".hyp[79].nvs" 1920;
	setAttr ".hyp[80].nvs" 1920;
	setAttr ".hyp[81].nvs" 1920;
	setAttr ".hyp[82].nvs" 1920;
	setAttr ".hyp[83].nvs" 1920;
	setAttr ".hyp[84].nvs" 1920;
	setAttr ".hyp[85].nvs" 1920;
	setAttr ".hyp[86].nvs" 1920;
	setAttr ".hyp[87].nvs" 1920;
	setAttr ".hyp[88].nvs" 1920;
	setAttr ".hyp[89].nvs" 1920;
	setAttr ".hyp[90].nvs" 1920;
	setAttr ".hyp[91].nvs" 1920;
	setAttr ".hyp[92].nvs" 1920;
	setAttr ".hyp[93].nvs" 1920;
	setAttr ".hyp[94].nvs" 1920;
	setAttr ".hyp[95].nvs" 1920;
	setAttr ".hyp[96].nvs" 1920;
	setAttr ".hyp[97].nvs" 1920;
	setAttr ".hyp[98].nvs" 1920;
	setAttr ".hyp[99].nvs" 1920;
	setAttr ".hyp[100].nvs" 1920;
	setAttr ".hyp[101].nvs" 1920;
	setAttr ".hyp[102].nvs" 1920;
	setAttr ".hyp[103].nvs" 1920;
	setAttr ".hyp[104].nvs" 1920;
	setAttr ".hyp[105].nvs" 1920;
	setAttr ".hyp[106].nvs" 1920;
	setAttr ".hyp[107].nvs" 1920;
	setAttr ".hyp[108].nvs" 1920;
	setAttr ".hyp[109].nvs" 1920;
	setAttr ".hyp[110].nvs" 1920;
	setAttr ".hyp[111].nvs" 1920;
	setAttr ".hyp[112].nvs" 1920;
	setAttr ".hyp[113].nvs" 1920;
	setAttr ".hyp[114].nvs" 1920;
	setAttr ".hyp[115].nvs" 1920;
	setAttr ".hyp[116].nvs" 1920;
	setAttr ".hyp[117].nvs" 1920;
	setAttr ".hyp[118].nvs" 1920;
	setAttr ".hyp[119].nvs" 1920;
	setAttr ".hyp[120].nvs" 1920;
	setAttr ".hyp[121].nvs" 1920;
	setAttr ".hyp[122].nvs" 1920;
	setAttr ".hyp[123].nvs" 1920;
	setAttr ".hyp[124].nvs" 1920;
	setAttr ".hyp[125].nvs" 1920;
	setAttr ".hyp[126].nvs" 1920;
	setAttr ".hyp[127].nvs" 1920;
	setAttr ".hyp[128].nvs" 1920;
	setAttr ".hyp[129].nvs" 1920;
	setAttr ".hyp[130].nvs" 1920;
	setAttr ".hyp[131].nvs" 1920;
	setAttr ".hyp[132].nvs" 1920;
	setAttr ".hyp[133].nvs" 1920;
	setAttr ".hyp[134].nvs" 1920;
	setAttr ".hyp[135].nvs" 1920;
	setAttr ".hyp[136].nvs" 1920;
	setAttr ".hyp[137].nvs" 1920;
	setAttr ".hyp[138].nvs" 1920;
	setAttr ".hyp[139].nvs" 1920;
	setAttr ".hyp[140].nvs" 1920;
	setAttr ".hyp[141].nvs" 1920;
	setAttr ".hyp[142].nvs" 1920;
	setAttr ".hyp[143].nvs" 1920;
	setAttr ".hyp[144].nvs" 1920;
	setAttr ".hyp[145].nvs" 1920;
	setAttr ".hyp[146].nvs" 1920;
	setAttr ".hyp[147].nvs" 1920;
	setAttr ".hyp[148].nvs" 1920;
	setAttr ".hyp[149].nvs" 1920;
	setAttr ".hyp[150].nvs" 1920;
	setAttr ".hyp[151].nvs" 1920;
	setAttr ".hyp[152].nvs" 1920;
	setAttr ".hyp[153].nvs" 1920;
	setAttr ".hyp[154].nvs" 1920;
	setAttr ".hyp[155].nvs" 1920;
	setAttr ".hyp[156].nvs" 1920;
	setAttr ".hyp[157].nvs" 1920;
	setAttr ".hyp[158].nvs" 1920;
	setAttr ".hyp[159].nvs" 1920;
	setAttr ".hyp[160].nvs" 1920;
	setAttr ".hyp[161].nvs" 1920;
	setAttr ".hyp[162].nvs" 1920;
	setAttr ".hyp[163].nvs" 1920;
	setAttr ".hyp[164].nvs" 1920;
	setAttr ".hyp[165].nvs" 1920;
	setAttr ".hyp[166].nvs" 1920;
	setAttr ".hyp[167].nvs" 1920;
	setAttr ".hyp[168].nvs" 1920;
	setAttr ".hyp[169].nvs" 1920;
	setAttr ".hyp[170].nvs" 1920;
	setAttr ".hyp[171].nvs" 1920;
	setAttr ".hyp[172].nvs" 1920;
	setAttr ".hyp[173].nvs" 1920;
	setAttr ".hyp[174].nvs" 1920;
	setAttr ".anf" yes;
createNode script -n "uiConfigurationScriptNode";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"top\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n"
		+ "                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n"
		+ "                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n"
		+ "                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n"
		+ "            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n"
		+ "            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n"
		+ "            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"side\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n"
		+ "                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n"
		+ "                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n"
		+ "                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n"
		+ "        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n"
		+ "            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n"
		+ "            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"front\" \n"
		+ "                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n"
		+ "                -maxConstantTransparency 1\n                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n"
		+ "                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n"
		+ "            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n"
		+ "            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n"
		+ "                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n"
		+ "                -maxConstantTransparency 1\n                -rendererName \"vp2Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n"
		+ "                -controlVertices 1\n                -hulls 0\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 0\n            -grid 1\n            -imagePlane 1\n"
		+ "            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n"
		+ "            outlinerEditor -e \n                -docTag \"isolOutln_fromSeln\" \n                -showShapes 0\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 0\n                -showConnected 0\n                -showAnimCurvesOnly 0\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 1\n                -showAssets 1\n                -showContainedOnly 1\n                -showPublishedAsConnected 0\n                -showContainerContents 1\n                -ignoreDagHierarchy 0\n                -expandConnections 0\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 0\n                -highlightActive 1\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n"
		+ "                -transmitFilters 0\n                -setFilter \"defaultSetFilter\" \n                -showSetMembers 1\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 0\n                -showPinIcons 0\n                -mapMotionTrails 0\n                -ignoreHiddenAttribute 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n"
		+ "            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 0\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\toutlinerPanel -e -to $panelName;\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n"
		+ "\t\t\t$panelName = `scriptedPanel -unParent  -type \"graphEditor\" -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n"
		+ "                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                $editorName;\n"
		+ "\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n"
		+ "                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n"
		+ "                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n"
		+ "\t\t\t$panelName = `scriptedPanel -unParent  -type \"dopeSheetPanel\" -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n"
		+ "                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                $editorName;\n"
		+ "\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n"
		+ "                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n"
		+ "                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n"
		+ "                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"clipEditorPanel\" -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"sequenceEditorPanel\" -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n"
		+ "                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n"
		+ "                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n"
		+ "                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperShadePanel\" -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"visorPanel\" -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n"
		+ "                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -ignoreAssets 1\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -keyReleaseCommand \"nodeEdKeyReleaseCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                $editorName;\n\t\t\tif (`objExists nodeEditorPanel1Info`) nodeEditor -e -restoreInfo nodeEditorPanel1Info $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -ignoreAssets 1\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -keyReleaseCommand \"nodeEdKeyReleaseCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n"
		+ "                $editorName;\n\t\t\tif (`objExists nodeEditorPanel1Info`) nodeEditor -e -restoreInfo nodeEditorPanel1Info $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"createNodePanel\" -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Texture Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"polyTexturePlacementPanel\" -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"renderWindowPanel\" -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"blendShapePanel\" (localizedPanelLabel(\"Blend Shape\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\tblendShapePanel -unParent -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels ;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tblendShapePanel -edit -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynRelEdPanel\" -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"relationshipPanel\" -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"referenceEditorPanel\" -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"componentEditorPanel\" -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynPaintScriptedPanelType\" -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"scriptEditorPanel\" -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Model Panel5\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Model Panel5\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n"
		+ "                -xray 0\n                -jointXray 1\n                -activeComponentsXray 0\n                -displayTextures 1\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n"
		+ "                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n"
		+ "                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Model Panel5\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 1\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 4 4 \n            -bumpResolution 4 4 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 0\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n"
		+ "            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n"
		+ "            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Model Panel6\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Model Panel6\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n"
		+ "                -xray 0\n                -jointXray 1\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n"
		+ "                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n"
		+ "                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Model Panel6\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 4 4 \n            -bumpResolution 4 4 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 0\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n"
		+ "            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n"
		+ "            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Model Panel7\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Model Panel7\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n"
		+ "                -xray 0\n                -jointXray 1\n                -activeComponentsXray 0\n                -displayTextures 1\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n"
		+ "                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n"
		+ "                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Model Panel7\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 1\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 4 4 \n            -bumpResolution 4 4 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 0\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n"
		+ "            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n"
		+ "            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Model Panel8\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Model Panel8\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n"
		+ "                -xray 0\n                -jointXray 1\n                -activeComponentsXray 0\n                -displayTextures 1\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n"
		+ "                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n"
		+ "                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Model Panel8\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 1\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 4 4 \n            -bumpResolution 4 4 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 0\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n"
		+ "            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n"
		+ "            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 0\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 0\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        setFocus `paneLayout -q -p1 $gMainPane`;\n        sceneUIReplacement -deleteRemaining;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 24 -ast 1 -aet 48 ";
	setAttr ".st" 6;
createNode hyperGraphInfo -n "nodeEditorPanel2Info";
createNode hyperView -n "hyperView2";
	setAttr ".vl" -type "double2" -113.09523809523812 -513.88098624940733 ;
	setAttr ".vh" -type "double2" 523.80952380952385 87.690510058931153 ;
	setAttr ".dag" no;
createNode hyperLayout -n "hyperLayout2";
	setAttr ".ihi" 0;
	setAttr -s 4 ".hyp";
	setAttr ".hyp[0].x" 1.4285714626312256;
	setAttr ".hyp[0].y" -281.42855834960937;
	setAttr ".hyp[0].nvs" 1920;
	setAttr ".hyp[1].nvs" 1920;
	setAttr ".hyp[2].x" 1.4285714626312256;
	setAttr ".hyp[2].y" -72.857139587402344;
	setAttr ".hyp[2].nvs" 1920;
	setAttr ".hyp[3].x" 212.85714721679687;
	setAttr ".hyp[3].y" -281.42855834960937;
	setAttr ".hyp[3].nvs" 1920;
	setAttr ".anf" yes;
createNode hyperGraphInfo -n "nodeEditorPanel2Info1";
createNode hyperView -n "hyperView3";
	setAttr ".vl" -type "double2" -340.59345012087891 -855.49571479968313 ;
	setAttr ".vh" -type "double2" 1439.2335745613261 250.95876208281774 ;
	setAttr ".dag" no;
createNode hyperLayout -n "hyperLayout3";
	setAttr ".ihi" 0;
	setAttr -s 8 ".hyp";
	setAttr ".hyp[0].nvs" 1920;
	setAttr ".hyp[1].nvs" 1920;
	setAttr ".hyp[2].nvs" 1920;
	setAttr ".hyp[3].nvs" 1920;
	setAttr ".hyp[4].nvs" 1920;
	setAttr ".hyp[5].nvs" 1920;
	setAttr ".hyp[6].nvs" 1920;
	setAttr ".hyp[7].nvs" 1920;
	setAttr ".anf" yes;
createNode polyBridgeEdge -n "md_Freddy_v06_polyBridgeEdge1";
	setAttr ".c[0]"  0 1 1;
	setAttr ".dv" 5;
createNode polyBridgeEdge -n "polyBridgeEdge28";
	setAttr ".c[0]"  0 1 1;
	setAttr ".dv" 0;
createNode polyBridgeEdge -n "polyBridgeEdge1";
	setAttr ".c[0]"  0 1 1;
	setAttr ".dv" 5;
createNode hyperGraphInfo -n "nodeEditorPanel2Info2";
createNode hyperView -n "hyperView4";
	setAttr ".vl" -type "double2" -114.28571428571428 -288.09523809523813 ;
	setAttr ".vh" -type "double2" 441.66666666666674 30.952380952380956 ;
	setAttr ".dag" no;
createNode hyperLayout -n "hyperLayout4";
	setAttr ".ihi" 0;
	setAttr ".anf" yes;
createNode polyBridgeEdge -n "MD_nino_v01_md_Freddy_v06_polyBridgeEdge1";
	setAttr ".c[0]"  0 1 1;
	setAttr ".dv" 5;
createNode polyBridgeEdge -n "MD_nino_v01_polyBridgeEdge28";
	setAttr ".c[0]"  0 1 1;
	setAttr ".dv" 0;
createNode transformGeometry -n "transformGeometry3";
createNode hyperGraphInfo -n "nodeEditorPanel1Info1";
createNode hyperView -n "hyperView5";
	setAttr ".dag" no;
createNode hyperLayout -n "hyperLayout5";
	setAttr ".ihi" 0;
	setAttr -s 12 ".hyp";
	setAttr ".hyp[0].x" 561.4285888671875;
	setAttr ".hyp[0].y" -281.42855834960937;
	setAttr ".hyp[0].nvs" 1920;
	setAttr ".hyp[1].x" 772.85711669921875;
	setAttr ".hyp[1].y" -281.42855834960937;
	setAttr ".hyp[1].nvs" 1920;
	setAttr ".hyp[2].x" 561.4285888671875;
	setAttr ".hyp[2].y" -177.14285278320312;
	setAttr ".hyp[2].nvs" 1920;
	setAttr ".hyp[3].x" 772.85711669921875;
	setAttr ".hyp[3].y" -177.14285278320312;
	setAttr ".hyp[3].nvs" 1920;
	setAttr ".hyp[4].x" 984.28570556640625;
	setAttr ".hyp[4].y" -281.42855834960937;
	setAttr ".hyp[4].nvs" 1920;
	setAttr ".hyp[5].x" 984.28570556640625;
	setAttr ".hyp[5].y" -177.14285278320312;
	setAttr ".hyp[5].nvs" 1920;
	setAttr ".hyp[6].x" 561.4285888671875;
	setAttr ".hyp[6].y" -72.857139587402344;
	setAttr ".hyp[6].nvs" 1920;
	setAttr ".hyp[7].x" 772.85711669921875;
	setAttr ".hyp[7].y" -72.857139587402344;
	setAttr ".hyp[7].nvs" 1920;
	setAttr ".hyp[8].x" 984.28570556640625;
	setAttr ".hyp[8].y" -72.857139587402344;
	setAttr ".hyp[8].nvs" 1920;
	setAttr ".hyp[9].nvs" 1920;
	setAttr ".hyp[10].nvs" 1920;
	setAttr ".hyp[11].nvs" 1920;
	setAttr ".anf" yes;
createNode displayLayer -n "BONES_REFERENCIA";
	setAttr ".do" 1;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -k on ".an";
	setAttr -k on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av ".dar";
	setAttr -av -k on ".ldar";
	setAttr -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -k on ".isu";
	setAttr -k on ".pdu";
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off ".eeaa";
	setAttr -k off ".engm";
	setAttr -k off ".mes";
	setAttr -k off ".emb";
	setAttr -av -k off ".mbbf";
	setAttr -k off ".mbs";
	setAttr -k off ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off ".twa";
	setAttr -k off ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
select -ne :defaultHardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".rp";
	setAttr -k on ".cai";
	setAttr -k on ".coi";
	setAttr -cb on ".bc";
	setAttr -av -k on ".bcb";
	setAttr -av -k on ".bcg";
	setAttr -av -k on ".bcr";
	setAttr -k on ".ei";
	setAttr -k on ".ex";
	setAttr -av -k on ".es";
	setAttr -av ".ef";
	setAttr -av -k on ".bf";
	setAttr -k on ".fii";
	setAttr -av -k on ".sf";
	setAttr -k on ".gr";
	setAttr -k on ".li";
	setAttr -k on ".ls";
	setAttr -k on ".mb";
	setAttr -k on ".ti";
	setAttr -k on ".txt";
	setAttr -k on ".mpr";
	setAttr -k on ".wzd";
	setAttr -k on ".if";
	setAttr ".res" -type "string" "ntsc_4d 646 485 1.333";
	setAttr -k on ".as";
	setAttr -k on ".ds";
	setAttr -k on ".lm";
	setAttr -k on ".fir";
	setAttr -k on ".aap";
	setAttr -k on ".gh";
	setAttr -cb on ".sd";
connectAttr "BONES_REFERENCIA.di" "R_ROOT.do";
connectAttr "R_ROOT.s" "R_COLUMNA_BAJA.is";
connectAttr "R_COLUMNA_BAJA.s" "R_COLUMNA_MEDIA.is";
connectAttr "R_COLUMNA_MEDIA.s" "R_COLUMNA_ALTA.is";
connectAttr "R_COLUMNA_ALTA.s" "R_CUELLO.is";
connectAttr "R_CUELLO.s" "R_CUELLO_SEC.is";
connectAttr "R_CUELLO_SEC.s" "R_CABEZA.is";
connectAttr "R_CABEZA.s" "R_CABEZA_ALTA.is";
connectAttr "R_CABEZA_ALTA.s" "R_OJO_DER.is";
connectAttr "R_CABEZA_ALTA.s" "R_OJO_IZQ.is";
connectAttr "R_CABEZA.s" "R_DIENTES_ARRIBA.is";
connectAttr "R_CABEZA.s" "R_MANDIBULA.is";
connectAttr "R_MANDIBULA.s" "R_BOCA_1.is";
connectAttr "R_BOCA_1.s" "R_BOCA_2.is";
connectAttr "R_BOCA_2.s" "R_DIENTES_BAJA.is";
connectAttr "R_MANDIBULA.s" "R_LENGUA_1.is";
connectAttr "R_LENGUA_1.s" "R_LENGUA_2.is";
connectAttr "R_LENGUA_2.s" "R_LENGUA_3.is";
connectAttr "R_COLUMNA_ALTA.s" "R_CLAVICULA_IZQ.is";
connectAttr "R_CLAVICULA_IZQ.s" "R_HOMBRO_IZQ.is";
connectAttr "R_HOMBRO_IZQ.s" "R_CODO_IZQ.is";
connectAttr "R_CODO_IZQ.s" "R_CODO_SEC_IZQ.is";
connectAttr "R_CODO_SEC_IZQ.s" "R_MANO_IZQ.is";
connectAttr "R_MANO_IZQ.s" "R_MIDDLE_IZQ_1.is";
connectAttr "R_MIDDLE_IZQ_1.s" "R_MIDDLE_IZQ_2.is";
connectAttr "R_MIDDLE_IZQ_2.s" "R_MIDDLE_IZQ_3.is";
connectAttr "R_MIDDLE_IZQ_3.s" "R_MIDDLE_IZQ_4.is";
connectAttr "R_MANO_IZQ.s" "R_PINKY_SEC_IZQ.is";
connectAttr "R_PINKY_SEC_IZQ.s" "R_PINKY_IZQ_1.is";
connectAttr "R_PINKY_IZQ_1.s" "R_PINKY_IZQ_2.is";
connectAttr "R_PINKY_IZQ_2.s" "R_PINKY_IZQ_3.is";
connectAttr "R_PINKY_IZQ_3.s" "R_PINKY_IZQ_4.is";
connectAttr "R_MANO_IZQ.s" "R_CANCEL_IZQ_1.is";
connectAttr "R_CANCEL_IZQ_1.s" "R_CANCEL_IZQ_2.is";
connectAttr "R_CANCEL_IZQ_2.s" "R_CANCEL_IZQ_3.is";
connectAttr "R_CANCEL_IZQ_3.s" "R_CANCEL_IZQ_4.is";
connectAttr "R_MANO_IZQ.s" "R_INDEX_IZQ_1.is";
connectAttr "R_INDEX_IZQ_1.s" "R_INDEX_IZQ_2.is";
connectAttr "R_INDEX_IZQ_2.s" "R_INDEX_IZQ_3.is";
connectAttr "R_INDEX_IZQ_3.s" "R_INDEX_IZQ_4.is";
connectAttr "R_MANO_IZQ.s" "R_THUMB_IZQ_1.is";
connectAttr "R_THUMB_IZQ_1.s" "R_THUMB_IZQ_2.is";
connectAttr "R_THUMB_IZQ_2.s" "R_THUMB_IZQ_3.is";
connectAttr "R_THUMB_IZQ_3.s" "R_THUMB_IZQ_4.is";
connectAttr "R_COLUMNA_ALTA.s" "R_CLAVICULA_DER.is";
connectAttr "R_CLAVICULA_DER.s" "R_HOMBRO_DER.is";
connectAttr "R_HOMBRO_DER.s" "R_CODO_DER.is";
connectAttr "R_CODO_DER.s" "R_CODO_SEC_DER.is";
connectAttr "R_CODO_SEC_DER.s" "R_MANO_DER.is";
connectAttr "R_MANO_DER.s" "R_MIDDLE_DER_1.is";
connectAttr "R_MIDDLE_DER_1.s" "R_MIDDLE_DER_2.is";
connectAttr "R_MIDDLE_DER_2.s" "R_MIDDLE_DER_3.is";
connectAttr "R_MIDDLE_DER_3.s" "R_MIDDLE_DER_4.is";
connectAttr "R_MANO_DER.s" "R_PINKY_SEC_DER.is";
connectAttr "R_PINKY_SEC_DER.s" "R_PINKY_DER_1.is";
connectAttr "R_PINKY_DER_1.s" "R_PINKY_DER_2.is";
connectAttr "R_PINKY_DER_2.s" "R_PINKY_DER_3.is";
connectAttr "R_PINKY_DER_3.s" "R_PINKY_DER_4.is";
connectAttr "R_MANO_DER.s" "R_CANCEL_DER_1.is";
connectAttr "R_CANCEL_DER_1.s" "R_CANCEL_DER_2.is";
connectAttr "R_CANCEL_DER_2.s" "R_CANCEL_DER_3.is";
connectAttr "R_CANCEL_DER_3.s" "R_CANCEL_DER_4.is";
connectAttr "R_MANO_DER.s" "R_INDEX_DER_1.is";
connectAttr "R_INDEX_DER_1.s" "R_INDEX_DER_2.is";
connectAttr "R_INDEX_DER_2.s" "R_INDEX_DER_3.is";
connectAttr "R_INDEX_DER_3.s" "R_INDEX_DER_4.is";
connectAttr "R_MANO_DER.s" "R_THUMB_DER_1.is";
connectAttr "R_THUMB_DER_1.s" "R_THUMB_DER_2.is";
connectAttr "R_THUMB_DER_2.s" "R_THUMB_DER_3.is";
connectAttr "R_THUMB_DER_3.s" "R_THUMB_DER_4.is";
connectAttr "R_ROOT.s" "R_CINTURA.is";
connectAttr "R_CINTURA.s" "R_PIERNA_IZQ.is";
connectAttr "R_PIERNA_IZQ.s" "R_RODILLA_IZQ.is";
connectAttr "R_RODILLA_IZQ.s" "R_TALON_IZQ.is";
connectAttr "R_TALON_IZQ.s" "R_DEDOS_PIE_IZQ.is";
connectAttr "R_DEDOS_PIE_IZQ.s" "R_PUNTA_PIE_IZQ.is";
connectAttr "R_CINTURA.s" "R_PIERNA_DER.is";
connectAttr "R_PIERNA_DER.s" "R_RODILLA_DER.is";
connectAttr "R_RODILLA_DER.s" "R_TALON_DER.is";
connectAttr "R_TALON_DER.s" "R_DEDOS_PIE_DER.is";
connectAttr "R_DEDOS_PIE_DER.s" "R_PUNTA_PIE_DER.is";
connectAttr "BONES_REFERENCIA.di" "R_REV_IZQ_1.do";
connectAttr "R_REV_IZQ_1.s" "R_REV_IZQ_2.is";
connectAttr "R_REV_IZQ_2.s" "R_REV_IZQ_3.is";
connectAttr "R_REV_IZQ_3.s" "R_REV_IZQ_4.is";
connectAttr "BONES_REFERENCIA.di" "R_REV_DER_1.do";
connectAttr "R_REV_DER_1.s" "R_REV_DER_2.is";
connectAttr "R_REV_DER_2.s" "R_REV_DER_3.is";
connectAttr "R_REV_DER_3.s" "R_REV_DER_4.is";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "hyperView1.msg" "nodeEditorPanel1Info.b[0]";
connectAttr "hyperLayout1.msg" "hyperView1.hl";
connectAttr "uiConfigurationScriptNode.msg" "hyperLayout1.hyp[158].dn";
connectAttr "sceneConfigurationScriptNode.msg" "hyperLayout1.hyp[159].dn";
connectAttr "hyperView2.msg" "nodeEditorPanel2Info.b[0]";
connectAttr "hyperLayout2.msg" "hyperView2.hl";
connectAttr "DRIVER_CABEZA1Shape.msg" "hyperLayout2.hyp[0].dn";
connectAttr "DRIVER_CABEZAShape.msg" "hyperLayout2.hyp[2].dn";
connectAttr "DRIVER_CABEZA.msg" "hyperLayout2.hyp[3].dn";
connectAttr "hyperView3.msg" "nodeEditorPanel2Info1.b[0]";
connectAttr "hyperLayout3.msg" "hyperView3.hl";
connectAttr "hyperView4.msg" "nodeEditorPanel2Info2.b[0]";
connectAttr "hyperLayout4.msg" "hyperView4.hl";
connectAttr "hyperView5.msg" "nodeEditorPanel1Info1.b[0]";
connectAttr "hyperLayout5.msg" "hyperView5.hl";
connectAttr ":persp.msg" "hyperLayout5.hyp[0].dn";
connectAttr ":perspShape.msg" "hyperLayout5.hyp[1].dn";
connectAttr ":top.msg" "hyperLayout5.hyp[2].dn";
connectAttr ":topShape.msg" "hyperLayout5.hyp[3].dn";
connectAttr ":front.msg" "hyperLayout5.hyp[4].dn";
connectAttr ":frontShape.msg" "hyperLayout5.hyp[5].dn";
connectAttr ":side.msg" "hyperLayout5.hyp[6].dn";
connectAttr ":sideShape.msg" "hyperLayout5.hyp[7].dn";
connectAttr ":lightLinker1.msg" "hyperLayout5.hyp[8].dn";
connectAttr "layerManager.dli[2]" "BONES_REFERENCIA.id";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr ":perspShape.msg" ":defaultRenderGlobals.sc";
// End of RIGG_BASE_I.ma
