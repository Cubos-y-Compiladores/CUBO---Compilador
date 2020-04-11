
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIDIFWHILETYPELENBLINKDELAYFORrightASSIGNleftLTLTEGTGTEleftPLUSMINUSleftMODDIVENTTIMESDIVIDEleftEXPleftLPARENTRPARENTASSIGN BEGIN BLINK BOOKED CALL COMMA COMPARE CONST CUBO DEL DELAY DELETE DIMCOLUMNAS DIMFILAS DIVENT DIVIDE DOT ELSE END EXP F FALSE FOR GLOBAL GT GTE ID IF IN INSERT INT LCORCH LEN LENGHTERROR LPARENT LT LTE MAIN MIL MIN MINUS MOD NE NEG PARENTCL PARENTCR PLUS PROCEDURE QUOTES RANGE RANGOTIMER RCORCH RPARENT SEG SEMICOLON SHAPEA SHAPEC SHAPEF STEP T TIMER TIMES TP TRUE TYPE VARERROR WHILEprogram : const_block main_procconst_block : const const const const const blockblock : procedure blockblock : global blockblock : emptyalt_block : alt_content alt_blockalt_block : emptyalt_content : instructionalt_content : assignment instruction : function  instruction : consult SEMICOLON instruction : cycle instruction : statement global : GLOBAL assignment assignment : identifier ASSIGN a_content SEMICOLON assignment : identifier COMMA identifier ASSIGN a_content COMMA a_content SEMICOLON function : type function : insertfunction : delfunction : lenfunction : negfunction : t_ffunction : blinkfunction : delayfunction : shapefunction : deletefunction : calltype : TYPE LPARENT identifier RPARENT SEMICOLON a_content : RANGE LPARENT INT COMMA value RPARENTinsert : identifier DOT INSERT LPARENT i_content RPARENT SEMICOLON  del : identifier DOT DEL LPARENT INT RPARENT SEMICOLON  len : LEN LPARENT ID RPARENT SEMICOLON  neg :  identifier DOT NEG SEMICOLON t_f : identifier DOT tf SEMICOLON  blink : BLINK LPARENT b_content RPARENT SEMICOLON delay : DELAY LPARENT d_content RPARENT SEMICOLON shape_arg : SHAPEFshape_arg : SHAPECshape_arg : SHAPEAshape : identifier DOT shape_arg SEMICOLON delete : identifier DOT DELETE LPARENT indice COMMA INT RPARENT SEMICOLON call : CALL proc_dec SEMICOLONcycle : forfor : FOR ID IN iterable step LCORCH alt_block RCORCH SEMICOLON step : STEP INTstep : emptystatement : IF LPARENT iterable relation bif_value RPARENT LCORCH alt_block RCORCH SEMICOLON opt_statement opt_statement : ELSE LCORCH alt_block RCORCH SEMICOLON opt_statement : empty procedure : PROCEDURE proc_dec LCORCH body RCORCH SEMICOLON proc_dec : proc_name LPARENT parameter RPARENTproc_name : IDparameter : proc_paramparameter : proc_param COMMA parameterparameter : emptyproc_param : IDbody : BEGIN alt_block END SEMICOLON main_proc : MAIN LPARENT RPARENT LCORCH main_body RCORCH SEMICOLON blockmain_body : BEGIN main_block END SEMICOLONmain_block : instruction main_blockmain_block : empty arithmetic : termarithmetic : adding_operator term arithmetic : arithmetic adding_operator termterm : factorterm : term multiplying_operator factorfactor : INTfactor : IDfactor : LPARENT arithmetic RPARENTconst : TIMER ASSIGN INT SEMICOLONconst : RANGOTIMER ASSIGN time_mes SEMICOLONconst : dimension ASSIGN INT SEMICOLONconst : CUBO ASSIGN INT SEMICOLONa_content : valuea_content : arithmetica_content : lista_content : mata_content : 3dmata_content : consultb_content : list_consult COMMA INT COMMA time_mes COMMA valueb_content : list_consult COMMA valued_content : emptyd_content : INT COMMA time_mestf : Ttf : Fi_content : INT COMMA valuei_content : list COMMA INT i_indlist : PARENTCL list_term PARENTCRlist : PARENTCL empty PARENTCRlist_term : list_value COMMA list_termlist_term : list_valuelist_value : valuemat : PARENTCL mat_term PARENTCRmat_term : mat_value COMMA mat_termmat_term : mat_valuemat_value : list3dmat : PARENTCL 3dmat_term PARENTCR3dmat_term : 3dmat_value COMMA 3dmat_term3dmat_term : 3dmat_value3dmat_value : matconsult : list_consult consult : mat_consult consult : 3dmat_consultlist_consult : ID list_consultT list_consultT : PARENTCL indice PARENTCRlist_consultT : PARENTCL indice TP indice PARENTCR mat_consult : ID mat_consultT mat_consultT : PARENTCL indice COMMA indice PARENTCRmat_consultT : PARENTCL TP COMMA indice PARENTCR mat_consultT : PARENTCL TP PARENTCR list_consultT mat_consultT : PARENTCL indice PARENTCR list_consultT3dmat_consult : ID 3dmat_consultT3dmat_consultT : PARENTCL indice COMMA indice COMMA indice PARENTCR3dmat_consultT : PARENTCL indice PARENTCR mat_consultTindice : INTindice : IDi_ind : COMMA INTi_ind : emptydimension : DIMFILASdimension : DIMCOLUMNAStime_mes : QUOTES MIL QUOTEStime_mes : QUOTES MIN QUOTEStime_mes : QUOTES SEG QUOTESadding_operator : PLUSadding_operator : MINUSmultiplying_operator : TIMESmultiplying_operator : EXPmultiplying_operator : DIVIDEmultiplying_operator : DIVENTmultiplying_operator : MODvalue : FALSEvalue : TRUEbif_value : valuebif_value : arithmeticrelation : ASSIGNrelation : NErelation : LTrelation : GTrelation : LTErelation : GTErelation : COMPAREidentifier : IDidentifier : consultiterable : identifieriterable : INTempty : '
    
_lr_action_items = {'TIMER':([0,3,12,18,25,26,27,31,32,],[4,4,4,4,4,-70,-71,-72,-73,]),'RANGOTIMER':([0,3,12,18,25,26,27,31,32,],[5,5,5,5,5,-70,-71,-72,-73,]),'CUBO':([0,3,12,18,25,26,27,31,32,],[7,7,7,7,7,-70,-71,-72,-73,]),'DIMFILAS':([0,3,12,18,25,26,27,31,32,],[8,8,8,8,8,-70,-71,-72,-73,]),'DIMCOLUMNAS':([0,3,12,18,25,26,27,31,32,],[9,9,9,9,9,-70,-71,-72,-73,]),'$end':([1,10,41,42,43,78,79,83,87,107,199,250,311,],[0,-1,-146,-146,-5,-3,-4,-14,-146,-58,-15,-50,-16,]),'MAIN':([2,26,27,31,32,34,40,41,42,43,78,79,83,199,250,311,],[11,-70,-71,-72,-73,-146,-2,-146,-146,-5,-3,-4,-14,-15,-50,-16,]),'ASSIGN':([4,5,6,7,8,9,51,65,66,67,84,85,86,95,96,97,109,110,111,162,179,196,235,236,240,273,275,276,278,294,307,],[13,14,15,16,-119,-120,-143,-101,-102,-103,105,-142,-143,-104,-107,-112,164,-144,-145,222,-105,105,-111,-114,-110,-106,-108,-109,-105,-105,-113,]),'LPARENT':([11,69,70,72,74,75,81,82,105,113,114,118,144,145,156,159,160,163,164,165,166,167,168,169,170,203,204,205,206,207,208,209,222,287,],[17,91,92,94,99,100,104,-52,145,172,173,177,200,145,145,-124,-125,145,-135,-136,-137,-138,-139,-140,-141,145,145,-126,-127,-128,-129,-130,145,145,]),'INT':([13,15,16,91,98,100,105,136,145,156,159,160,163,164,165,166,167,168,169,170,172,173,177,180,181,182,185,186,200,203,204,205,206,207,208,209,222,234,248,269,271,274,287,295,302,],[19,22,23,111,127,134,146,111,146,146,-124,-125,146,-135,-136,-137,-138,-139,-140,-141,228,231,127,127,127,127,242,127,254,146,146,-126,-127,-128,-129,-130,146,127,280,291,293,127,146,127,313,]),'QUOTES':([14,28,29,30,188,277,],[21,35,36,37,21,21,]),'RPARENT':([17,35,36,37,65,66,67,85,86,95,96,97,100,104,112,124,129,132,133,139,140,141,142,146,153,154,155,158,179,198,201,202,210,223,224,225,227,231,235,236,240,243,246,253,255,256,257,273,275,276,278,290,291,293,294,299,303,304,307,313,315,],[24,-121,-122,-123,-101,-102,-103,-142,-143,-104,-107,-112,-146,-146,171,178,184,187,-82,197,-53,-55,-56,-67,-131,-132,-62,-65,-105,-146,255,-68,-63,266,-133,-134,267,270,-111,-114,-110,-81,-83,-54,-69,-64,-66,-106,-108,-109,-105,-86,-146,305,-105,310,-87,-118,-113,-117,-80,]),'SEMICOLON':([19,20,22,23,35,36,37,46,51,65,66,67,88,95,96,97,101,115,116,117,119,120,121,122,123,143,146,147,148,149,150,151,152,153,154,155,158,161,171,178,179,184,187,190,197,202,210,235,236,240,251,255,256,257,258,259,260,261,267,270,273,275,276,278,294,300,305,307,309,310,312,323,],[26,27,31,32,-121,-122,-123,87,90,-101,-102,-103,108,-104,-107,-112,135,174,175,176,-84,-85,-37,-38,-39,199,-67,-74,-75,-76,-77,-78,-79,-131,-132,-62,-65,-68,226,233,-105,241,245,250,-51,-68,-63,-111,-114,-110,281,-69,-64,-66,-88,-89,-93,-97,289,292,-106,-108,-109,-105,-105,311,314,-113,316,-29,317,324,]),'MIL':([21,],[28,]),'MIN':([21,],[29,]),'SEG':([21,],[30,]),'LCORCH':([24,65,66,67,80,85,86,95,96,97,110,111,179,189,197,235,236,240,247,249,266,273,275,276,278,280,294,307,319,],[33,-101,-102,-103,103,-142,-143,-104,-107,-112,-144,-145,-105,-146,-51,-111,-114,-110,279,-46,288,-106,-108,-109,-105,-45,-105,-113,321,]),'PROCEDURE':([26,27,31,32,34,41,42,83,87,199,250,311,],[-70,-71,-72,-73,44,44,44,-14,44,-15,-50,-16,]),'GLOBAL':([26,27,31,32,34,41,42,83,87,199,250,311,],[-70,-71,-72,-73,45,45,45,-14,45,-15,-50,-16,]),'BEGIN':([33,103,],[39,138,]),'COMMA':([35,36,37,51,65,66,67,84,85,86,95,96,97,125,126,127,128,130,134,140,142,146,147,148,149,150,151,152,153,154,155,158,161,179,196,202,210,216,217,218,219,220,221,228,229,232,235,236,238,240,242,254,255,256,257,258,259,260,261,265,272,273,275,276,278,291,294,297,307,310,],[-121,-122,-123,-143,-101,-102,-103,106,-142,-143,-104,-107,-112,181,182,-115,-116,185,188,198,-56,-67,-74,-75,-76,-77,-78,-79,-131,-132,-62,-65,-68,-105,106,-68,-63,262,263,264,-92,-96,-100,268,269,271,-111,-114,274,-110,277,282,-69,-64,-66,-88,-89,-93,-97,287,295,-106,-108,-109,-105,302,-105,308,-113,-29,]),'RCORCH':([38,50,52,53,54,55,56,57,58,59,60,61,62,63,64,68,90,108,135,137,174,175,176,192,193,194,195,199,226,233,241,245,252,279,281,288,289,292,298,301,311,314,316,317,318,320,321,322,324,],[46,-10,-12,-13,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-43,-11,-59,-42,190,-33,-34,-40,-146,-7,-8,-9,-15,-28,-32,-35,-36,-6,-146,-57,-146,-30,-31,309,312,-16,-41,-44,-146,-47,-49,-146,323,-48,]),'END':([39,47,48,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,68,89,90,135,138,174,175,176,191,192,193,194,195,199,226,233,241,245,252,289,292,311,314,316,317,318,320,324,],[-146,88,-146,-61,-10,-12,-13,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-43,-60,-11,-42,-146,-33,-34,-40,251,-146,-7,-8,-9,-15,-28,-32,-35,-36,-6,-30,-31,-16,-41,-44,-146,-47,-49,-48,]),'IF':([39,48,50,52,53,54,55,56,57,58,59,60,61,62,63,64,68,90,135,138,174,175,176,192,194,195,199,226,233,241,245,279,288,289,292,311,314,316,317,318,320,321,324,],[69,69,-10,-12,-13,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-43,-11,-42,69,-33,-34,-40,69,-8,-9,-15,-28,-32,-35,-36,69,69,-30,-31,-16,-41,-44,-146,-47,-49,69,-48,]),'TYPE':([39,48,50,52,53,54,55,56,57,58,59,60,61,62,63,64,68,90,135,138,174,175,176,192,194,195,199,226,233,241,245,279,288,289,292,311,314,316,317,318,320,321,324,],[70,70,-10,-12,-13,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-43,-11,-42,70,-33,-34,-40,70,-8,-9,-15,-28,-32,-35,-36,70,70,-30,-31,-16,-41,-44,-146,-47,-49,70,-48,]),'LEN':([39,48,50,52,53,54,55,56,57,58,59,60,61,62,63,64,68,90,135,138,174,175,176,192,194,195,199,226,233,241,245,279,288,289,292,311,314,316,317,318,320,321,324,],[72,72,-10,-12,-13,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-43,-11,-42,72,-33,-34,-40,72,-8,-9,-15,-28,-32,-35,-36,72,72,-30,-31,-16,-41,-44,-146,-47,-49,72,-48,]),'BLINK':([39,48,50,52,53,54,55,56,57,58,59,60,61,62,63,64,68,90,135,138,174,175,176,192,194,195,199,226,233,241,245,279,288,289,292,311,314,316,317,318,320,321,324,],[74,74,-10,-12,-13,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-43,-11,-42,74,-33,-34,-40,74,-8,-9,-15,-28,-32,-35,-36,74,74,-30,-31,-16,-41,-44,-146,-47,-49,74,-48,]),'DELAY':([39,48,50,52,53,54,55,56,57,58,59,60,61,62,63,64,68,90,135,138,174,175,176,192,194,195,199,226,233,241,245,279,288,289,292,311,314,316,317,318,320,321,324,],[75,75,-10,-12,-13,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-43,-11,-42,75,-33,-34,-40,75,-8,-9,-15,-28,-32,-35,-36,75,75,-30,-31,-16,-41,-44,-146,-47,-49,75,-48,]),'CALL':([39,48,50,52,53,54,55,56,57,58,59,60,61,62,63,64,68,90,135,138,174,175,176,192,194,195,199,226,233,241,245,279,288,289,292,311,314,316,317,318,320,321,324,],[76,76,-10,-12,-13,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-43,-11,-42,76,-33,-34,-40,76,-8,-9,-15,-28,-32,-35,-36,76,76,-30,-31,-16,-41,-44,-146,-47,-49,76,-48,]),'ID':([39,44,45,48,50,52,53,54,55,56,57,58,59,60,61,62,63,64,68,76,77,90,91,92,94,98,99,104,105,106,135,136,138,145,156,159,160,163,164,165,166,167,168,169,170,174,175,176,177,180,181,182,186,192,194,195,198,199,203,204,205,206,207,208,209,222,226,233,234,241,245,274,279,287,288,289,292,295,311,314,316,317,318,320,321,324,],[73,82,85,73,-10,-12,-13,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-43,82,102,-11,85,85,124,128,131,142,161,85,-42,85,85,202,202,-124,-125,202,-135,-136,-137,-138,-139,-140,-141,-33,-34,-40,128,128,128,128,128,85,-8,-9,142,-15,202,202,-126,-127,-128,-129,-130,161,-28,-32,128,-35,-36,128,85,161,85,-30,-31,128,-16,-41,-44,-146,-47,-49,85,-48,]),'FOR':([39,48,50,52,53,54,55,56,57,58,59,60,61,62,63,64,68,90,135,138,174,175,176,192,194,195,199,226,233,241,245,279,288,289,292,311,314,316,317,318,320,321,324,],[77,77,-10,-12,-13,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-43,-11,-42,77,-33,-34,-40,77,-8,-9,-15,-28,-32,-35,-36,77,77,-30,-31,-16,-41,-44,-146,-47,-49,77,-48,]),'DOT':([51,65,66,67,71,73,85,95,96,97,179,196,235,236,240,273,275,276,278,294,307,],[-143,-101,-102,-103,93,-142,-142,-104,-107,-112,-105,93,-111,-114,-110,-106,-108,-109,-105,-105,-113,]),'NE':([65,66,67,85,86,95,96,97,109,110,111,179,235,236,240,273,275,276,278,294,307,],[-101,-102,-103,-142,-143,-104,-107,-112,165,-144,-145,-105,-111,-114,-110,-106,-108,-109,-105,-105,-113,]),'LT':([65,66,67,85,86,95,96,97,109,110,111,179,235,236,240,273,275,276,278,294,307,],[-101,-102,-103,-142,-143,-104,-107,-112,166,-144,-145,-105,-111,-114,-110,-106,-108,-109,-105,-105,-113,]),'GT':([65,66,67,85,86,95,96,97,109,110,111,179,235,236,240,273,275,276,278,294,307,],[-101,-102,-103,-142,-143,-104,-107,-112,167,-144,-145,-105,-111,-114,-110,-106,-108,-109,-105,-105,-113,]),'LTE':([65,66,67,85,86,95,96,97,109,110,111,179,235,236,240,273,275,276,278,294,307,],[-101,-102,-103,-142,-143,-104,-107,-112,168,-144,-145,-105,-111,-114,-110,-106,-108,-109,-105,-105,-113,]),'GTE':([65,66,67,85,86,95,96,97,109,110,111,179,235,236,240,273,275,276,278,294,307,],[-101,-102,-103,-142,-143,-104,-107,-112,169,-144,-145,-105,-111,-114,-110,-106,-108,-109,-105,-105,-113,]),'COMPARE':([65,66,67,85,86,95,96,97,109,110,111,179,235,236,240,273,275,276,278,294,307,],[-101,-102,-103,-142,-143,-104,-107,-112,170,-144,-145,-105,-111,-114,-110,-106,-108,-109,-105,-105,-113,]),'STEP':([65,66,67,85,86,95,96,97,110,111,179,189,235,236,240,273,275,276,278,294,307,],[-101,-102,-103,-142,-143,-104,-107,-112,-144,-145,-105,248,-111,-114,-110,-106,-108,-109,-105,-105,-113,]),'PARENTCL':([73,85,105,131,157,161,172,179,183,211,222,263,264,286,287,294,],[98,98,157,186,211,98,230,234,186,230,157,230,286,230,157,186,]),'INSERT':([93,],[113,]),'DEL':([93,],[114,]),'NEG':([93,],[115,]),'DELETE':([93,],[118,]),'T':([93,],[119,]),'F':([93,],[120,]),'SHAPEF':([93,],[121,]),'SHAPEC':([93,],[122,]),'SHAPEA':([93,],[123,]),'TP':([98,125,127,128,234,244,272,],[126,180,-115,-116,126,180,180,]),'IN':([102,],[136,]),'RANGE':([105,222,287,],[144,144,144,]),'FALSE':([105,157,163,164,165,166,167,168,169,170,185,211,222,230,262,268,282,287,308,],[153,153,153,-135,-136,-137,-138,-139,-140,-141,153,153,153,153,153,153,153,153,153,]),'TRUE':([105,157,163,164,165,166,167,168,169,170,185,211,222,230,262,268,282,287,308,],[154,154,154,-135,-136,-137,-138,-139,-140,-141,154,154,154,154,154,154,154,154,154,]),'PLUS':([105,145,146,148,155,158,161,163,164,165,166,167,168,169,170,201,202,210,222,225,255,256,257,287,],[159,159,-67,159,-62,-65,-68,159,-135,-136,-137,-138,-139,-140,-141,159,-68,-63,159,159,-69,-64,-66,159,]),'MINUS':([105,145,146,148,155,158,161,163,164,165,166,167,168,169,170,201,202,210,222,225,255,256,257,287,],[160,160,-67,160,-62,-65,-68,160,-135,-136,-137,-138,-139,-140,-141,160,-68,-63,160,160,-69,-64,-66,160,]),'PARENTCR':([125,126,127,128,153,154,157,211,212,213,214,215,216,217,218,219,220,221,230,237,238,239,244,258,259,260,272,283,284,285,296,306,],[179,183,-115,-116,-131,-132,-146,-146,258,259,260,261,-91,-95,-99,-92,-96,-100,-146,273,275,276,278,-88,-89,-93,294,-90,-94,-98,307,275,]),'TIMES':([146,155,158,161,202,210,255,256,257,],[-67,205,-65,-68,-68,205,-69,205,-66,]),'EXP':([146,155,158,161,202,210,255,256,257,],[-67,206,-65,-68,-68,206,-69,206,-66,]),'DIVIDE':([146,155,158,161,202,210,255,256,257,],[-67,207,-65,-68,-68,207,-69,207,-66,]),'DIVENT':([146,155,158,161,202,210,255,256,257,],[-67,208,-65,-68,-68,208,-69,208,-66,]),'MOD':([146,155,158,161,202,210,255,256,257,],[-67,209,-65,-68,-68,209,-69,209,-66,]),'ELSE':([317,],[319,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'const_block':([0,],[2,]),'const':([0,3,12,18,25,],[3,12,18,25,34,]),'dimension':([0,3,12,18,25,],[6,6,6,6,6,]),'main_proc':([2,],[10,]),'time_mes':([14,188,277,],[20,246,297,]),'main_body':([33,],[38,]),'block':([34,41,42,87,],[40,78,79,107,]),'procedure':([34,41,42,87,],[41,41,41,41,]),'global':([34,41,42,87,],[42,42,42,42,]),'empty':([34,39,41,42,48,87,100,104,138,157,189,192,198,211,230,279,288,291,317,321,],[43,49,43,43,49,43,133,141,193,213,249,193,141,213,213,193,193,304,320,193,]),'main_block':([39,48,],[47,89,]),'instruction':([39,48,138,192,279,288,321,],[48,48,194,194,194,194,194,]),'function':([39,48,138,192,279,288,321,],[50,50,50,50,50,50,50,]),'consult':([39,45,48,91,92,105,106,136,138,192,222,279,287,288,321,],[51,86,51,86,86,152,86,86,51,51,152,51,152,51,51,]),'cycle':([39,48,138,192,279,288,321,],[52,52,52,52,52,52,52,]),'statement':([39,48,138,192,279,288,321,],[53,53,53,53,53,53,53,]),'type':([39,48,138,192,279,288,321,],[54,54,54,54,54,54,54,]),'insert':([39,48,138,192,279,288,321,],[55,55,55,55,55,55,55,]),'del':([39,48,138,192,279,288,321,],[56,56,56,56,56,56,56,]),'len':([39,48,138,192,279,288,321,],[57,57,57,57,57,57,57,]),'neg':([39,48,138,192,279,288,321,],[58,58,58,58,58,58,58,]),'t_f':([39,48,138,192,279,288,321,],[59,59,59,59,59,59,59,]),'blink':([39,48,138,192,279,288,321,],[60,60,60,60,60,60,60,]),'delay':([39,48,138,192,279,288,321,],[61,61,61,61,61,61,61,]),'shape':([39,48,138,192,279,288,321,],[62,62,62,62,62,62,62,]),'delete':([39,48,138,192,279,288,321,],[63,63,63,63,63,63,63,]),'call':([39,48,138,192,279,288,321,],[64,64,64,64,64,64,64,]),'list_consult':([39,45,48,91,92,99,105,106,136,138,192,222,279,287,288,321,],[65,65,65,65,65,130,65,65,65,65,65,65,65,65,65,65,]),'mat_consult':([39,45,48,91,92,105,106,136,138,192,222,279,287,288,321,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'3dmat_consult':([39,45,48,91,92,105,106,136,138,192,222,279,287,288,321,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'for':([39,48,138,192,279,288,321,],[68,68,68,68,68,68,68,]),'identifier':([39,45,48,91,92,106,136,138,192,279,288,321,],[71,84,71,110,112,162,110,196,196,196,196,196,]),'proc_dec':([44,76,],[80,101,]),'proc_name':([44,76,],[81,81,]),'assignment':([45,138,192,279,288,321,],[83,195,195,195,195,195,]),'list_consultT':([73,85,131,161,179,183,294,],[95,95,95,95,235,240,235,]),'mat_consultT':([73,85,161,179,],[96,96,96,236,]),'3dmat_consultT':([73,85,161,],[97,97,97,]),'iterable':([91,136,],[109,189,]),'tf':([93,],[116,]),'shape_arg':([93,],[117,]),'indice':([98,177,180,181,182,186,234,274,295,],[125,232,237,238,239,244,272,296,306,]),'b_content':([99,],[129,]),'d_content':([100,],[132,]),'body':([103,],[137,]),'parameter':([104,198,],[139,253,]),'proc_param':([104,198,],[140,140,]),'a_content':([105,222,287,],[143,265,300,]),'value':([105,157,163,185,211,222,230,262,268,282,287,308,],[147,219,224,243,219,147,219,219,290,299,147,315,]),'arithmetic':([105,145,163,222,287,],[148,201,225,148,148,]),'list':([105,157,172,211,222,263,286,287,],[149,220,229,220,149,220,220,149,]),'mat':([105,157,222,264,287,],[150,221,150,221,150,]),'3dmat':([105,222,287,],[151,151,151,]),'term':([105,145,156,163,203,222,287,],[155,155,210,155,256,155,155,]),'adding_operator':([105,145,148,163,201,222,225,287,],[156,156,203,156,203,156,203,156,]),'factor':([105,145,156,163,203,204,222,287,],[158,158,158,158,158,257,158,158,]),'relation':([109,],[163,]),'alt_block':([138,192,279,288,321,],[191,252,298,301,322,]),'alt_content':([138,192,279,288,321,],[192,192,192,192,192,]),'multiplying_operator':([155,210,256,],[204,204,204,]),'list_term':([157,211,230,262,],[212,212,212,283,]),'mat_term':([157,211,263,286,],[214,214,284,214,]),'3dmat_term':([157,264,],[215,285,]),'list_value':([157,211,230,262,],[216,216,216,216,]),'mat_value':([157,211,263,286,],[217,217,217,217,]),'3dmat_value':([157,264,],[218,218,]),'bif_value':([163,],[223,]),'i_content':([172,],[227,]),'step':([189,],[247,]),'i_ind':([291,],[303,]),'opt_statement':([317,],[318,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> const_block main_proc','program',2,'p_program','Parser.py',19),
  ('const_block -> const const const const const block','const_block',6,'p_constB','Parser.py',26),
  ('block -> procedure block','block',2,'p_block0','Parser.py',32),
  ('block -> global block','block',2,'p_block1','Parser.py',37),
  ('block -> empty','block',1,'p_blockEmp','Parser.py',42),
  ('alt_block -> alt_content alt_block','alt_block',2,'p_altBlock','Parser.py',52),
  ('alt_block -> empty','alt_block',1,'p_emptyaltBlock','Parser.py',57),
  ('alt_content -> instruction','alt_content',1,'p_altContent0','Parser.py',62),
  ('alt_content -> assignment','alt_content',1,'p_altContent1','Parser.py',67),
  ('instruction -> function','instruction',1,'p_instruction0','Parser.py',77),
  ('instruction -> consult SEMICOLON','instruction',2,'p_instruction1','Parser.py',82),
  ('instruction -> cycle','instruction',1,'p_instruction2','Parser.py',87),
  ('instruction -> statement','instruction',1,'p_instruction3','Parser.py',92),
  ('global -> GLOBAL assignment','global',2,'p_globalAssignment','Parser.py',102),
  ('assignment -> identifier ASSIGN a_content SEMICOLON','assignment',4,'p_simpleAssignment','Parser.py',113),
  ('assignment -> identifier COMMA identifier ASSIGN a_content COMMA a_content SEMICOLON','assignment',8,'p_doubleAssignment','Parser.py',118),
  ('function -> type','function',1,'p_function0','Parser.py',128),
  ('function -> insert','function',1,'p_function1','Parser.py',133),
  ('function -> del','function',1,'p_function2','Parser.py',138),
  ('function -> len','function',1,'p_function3','Parser.py',143),
  ('function -> neg','function',1,'p_function4','Parser.py',148),
  ('function -> t_f','function',1,'p_function5','Parser.py',153),
  ('function -> blink','function',1,'p_function6','Parser.py',158),
  ('function -> delay','function',1,'p_function7','Parser.py',163),
  ('function -> shape','function',1,'p_function8','Parser.py',168),
  ('function -> delete','function',1,'p_function9','Parser.py',173),
  ('function -> call','function',1,'p_function10','Parser.py',178),
  ('type -> TYPE LPARENT identifier RPARENT SEMICOLON','type',5,'p_type','Parser.py',183),
  ('a_content -> RANGE LPARENT INT COMMA value RPARENT','a_content',6,'p_range','Parser.py',188),
  ('insert -> identifier DOT INSERT LPARENT i_content RPARENT SEMICOLON','insert',7,'p_insert','Parser.py',193),
  ('del -> identifier DOT DEL LPARENT INT RPARENT SEMICOLON','del',7,'p_del','Parser.py',198),
  ('len -> LEN LPARENT ID RPARENT SEMICOLON','len',5,'p_len','Parser.py',203),
  ('neg -> identifier DOT NEG SEMICOLON','neg',4,'p_neg','Parser.py',208),
  ('t_f -> identifier DOT tf SEMICOLON','t_f',4,'p_tf','Parser.py',213),
  ('blink -> BLINK LPARENT b_content RPARENT SEMICOLON','blink',5,'p_blink','Parser.py',218),
  ('delay -> DELAY LPARENT d_content RPARENT SEMICOLON','delay',5,'p_delay','Parser.py',223),
  ('shape_arg -> SHAPEF','shape_arg',1,'p_shapeArg0','Parser.py',228),
  ('shape_arg -> SHAPEC','shape_arg',1,'p_shapeArg1','Parser.py',233),
  ('shape_arg -> SHAPEA','shape_arg',1,'p_shapeArg2','Parser.py',238),
  ('shape -> identifier DOT shape_arg SEMICOLON','shape',4,'p_shape','Parser.py',243),
  ('delete -> identifier DOT DELETE LPARENT indice COMMA INT RPARENT SEMICOLON','delete',9,'p_delete','Parser.py',248),
  ('call -> CALL proc_dec SEMICOLON','call',3,'p_call','Parser.py',253),
  ('cycle -> for','cycle',1,'p_cycle','Parser.py',263),
  ('for -> FOR ID IN iterable step LCORCH alt_block RCORCH SEMICOLON','for',9,'p_for','Parser.py',268),
  ('step -> STEP INT','step',2,'p_step','Parser.py',273),
  ('step -> empty','step',1,'p_stepEmp','Parser.py',278),
  ('statement -> IF LPARENT iterable relation bif_value RPARENT LCORCH alt_block RCORCH SEMICOLON opt_statement','statement',11,'p_statement','Parser.py',288),
  ('opt_statement -> ELSE LCORCH alt_block RCORCH SEMICOLON','opt_statement',5,'p_optStatment','Parser.py',293),
  ('opt_statement -> empty','opt_statement',1,'p_EmptyOptStatment','Parser.py',298),
  ('procedure -> PROCEDURE proc_dec LCORCH body RCORCH SEMICOLON','procedure',6,'p_procedure','Parser.py',308),
  ('proc_dec -> proc_name LPARENT parameter RPARENT','proc_dec',4,'p_procDec','Parser.py',312),
  ('proc_name -> ID','proc_name',1,'p_procName','Parser.py',317),
  ('parameter -> proc_param','parameter',1,'p_parameter0','Parser.py',322),
  ('parameter -> proc_param COMMA parameter','parameter',3,'p_parameter1','Parser.py',327),
  ('parameter -> empty','parameter',1,'p_emptyParameter','Parser.py',332),
  ('proc_param -> ID','proc_param',1,'p_procParam','Parser.py',337),
  ('body -> BEGIN alt_block END SEMICOLON','body',4,'p_body','Parser.py',342),
  ('main_proc -> MAIN LPARENT RPARENT LCORCH main_body RCORCH SEMICOLON block','main_proc',8,'p_mainProcedure','Parser.py',347),
  ('main_body -> BEGIN main_block END SEMICOLON','main_body',4,'p_mainBody','Parser.py',353),
  ('main_block -> instruction main_block','main_block',2,'p_mainBlock','Parser.py',358),
  ('main_block -> empty','main_block',1,'p_EmptyMainblok','Parser.py',364),
  ('arithmetic -> term','arithmetic',1,'p_arithmetic0','Parser.py',374),
  ('arithmetic -> adding_operator term','arithmetic',2,'p_arithmetic1','Parser.py',378),
  ('arithmetic -> arithmetic adding_operator term','arithmetic',3,'p_arithmetic2','Parser.py',383),
  ('term -> factor','term',1,'p_term0','Parser.py',393),
  ('term -> term multiplying_operator factor','term',3,'p_term1','Parser.py',398),
  ('factor -> INT','factor',1,'p_factor0','Parser.py',408),
  ('factor -> ID','factor',1,'p_factor1','Parser.py',413),
  ('factor -> LPARENT arithmetic RPARENT','factor',3,'p_factor2','Parser.py',418),
  ('const -> TIMER ASSIGN INT SEMICOLON','const',4,'p_const0','Parser.py',428),
  ('const -> RANGOTIMER ASSIGN time_mes SEMICOLON','const',4,'p_const1','Parser.py',433),
  ('const -> dimension ASSIGN INT SEMICOLON','const',4,'p_const2','Parser.py',438),
  ('const -> CUBO ASSIGN INT SEMICOLON','const',4,'p_const3','Parser.py',443),
  ('a_content -> value','a_content',1,'p_Acont0','Parser.py',453),
  ('a_content -> arithmetic','a_content',1,'p_Acont1','Parser.py',458),
  ('a_content -> list','a_content',1,'p_Acont2','Parser.py',463),
  ('a_content -> mat','a_content',1,'p_Acont3','Parser.py',468),
  ('a_content -> 3dmat','a_content',1,'p_Acont4','Parser.py',473),
  ('a_content -> consult','a_content',1,'p_Acont5','Parser.py',478),
  ('b_content -> list_consult COMMA INT COMMA time_mes COMMA value','b_content',7,'p_Fcont0','Parser.py',487),
  ('b_content -> list_consult COMMA value','b_content',3,'p_Fcont1','Parser.py',492),
  ('d_content -> empty','d_content',1,'p_Fcont2','Parser.py',497),
  ('d_content -> INT COMMA time_mes','d_content',3,'p_Fcont3','Parser.py',502),
  ('tf -> T','tf',1,'p_Fcont4','Parser.py',507),
  ('tf -> F','tf',1,'p_Fcont5','Parser.py',512),
  ('i_content -> INT COMMA value','i_content',3,'p_Fcont6','Parser.py',517),
  ('i_content -> list COMMA INT i_ind','i_content',4,'p_Fcont7','Parser.py',522),
  ('list -> PARENTCL list_term PARENTCR','list',3,'p_list','Parser.py',532),
  ('list -> PARENTCL empty PARENTCR','list',3,'p_EmptyList','Parser.py',537),
  ('list_term -> list_value COMMA list_term','list_term',3,'p_listT0','Parser.py',542),
  ('list_term -> list_value','list_term',1,'p_listT1','Parser.py',547),
  ('list_value -> value','list_value',1,'p_listV','Parser.py',552),
  ('mat -> PARENTCL mat_term PARENTCR','mat',3,'p_mat','Parser.py',557),
  ('mat_term -> mat_value COMMA mat_term','mat_term',3,'p_matT0','Parser.py',562),
  ('mat_term -> mat_value','mat_term',1,'p_matT1','Parser.py',567),
  ('mat_value -> list','mat_value',1,'p_matV','Parser.py',572),
  ('3dmat -> PARENTCL 3dmat_term PARENTCR','3dmat',3,'p_3dmat','Parser.py',577),
  ('3dmat_term -> 3dmat_value COMMA 3dmat_term','3dmat_term',3,'p_3dmatT0','Parser.py',582),
  ('3dmat_term -> 3dmat_value','3dmat_term',1,'p_3dmatT1','Parser.py',587),
  ('3dmat_value -> mat','3dmat_value',1,'p_3dmatV','Parser.py',592),
  ('consult -> list_consult','consult',1,'p_consult0','Parser.py',597),
  ('consult -> mat_consult','consult',1,'p_consult1','Parser.py',602),
  ('consult -> 3dmat_consult','consult',1,'p_consult2','Parser.py',607),
  ('list_consult -> ID list_consultT','list_consult',2,'p_Listconsult','Parser.py',612),
  ('list_consultT -> PARENTCL indice PARENTCR','list_consultT',3,'p_ListconsultT0','Parser.py',617),
  ('list_consultT -> PARENTCL indice TP indice PARENTCR','list_consultT',5,'p_LstconsultT1','Parser.py',622),
  ('mat_consult -> ID mat_consultT','mat_consult',2,'p_Matconsult','Parser.py',627),
  ('mat_consultT -> PARENTCL indice COMMA indice PARENTCR','mat_consultT',5,'p_MatconsultT0','Parser.py',632),
  ('mat_consultT -> PARENTCL TP COMMA indice PARENTCR','mat_consultT',5,'p_MatconsultT1','Parser.py',637),
  ('mat_consultT -> PARENTCL TP PARENTCR list_consultT','mat_consultT',4,'p_MatconsultT2','Parser.py',642),
  ('mat_consultT -> PARENTCL indice PARENTCR list_consultT','mat_consultT',4,'p_MatconsultT3','Parser.py',647),
  ('3dmat_consult -> ID 3dmat_consultT','3dmat_consult',2,'p_3dMatconsult','Parser.py',652),
  ('3dmat_consultT -> PARENTCL indice COMMA indice COMMA indice PARENTCR','3dmat_consultT',7,'p_3dMatconsultT0','Parser.py',657),
  ('3dmat_consultT -> PARENTCL indice PARENTCR mat_consultT','3dmat_consultT',4,'p_3dMatconsultT1','Parser.py',662),
  ('indice -> INT','indice',1,'p_indice0','Parser.py',670),
  ('indice -> ID','indice',1,'p_indice1','Parser.py',675),
  ('i_ind -> COMMA INT','i_ind',2,'p_Insind0','Parser.py',680),
  ('i_ind -> empty','i_ind',1,'p_InsindEmp','Parser.py',685),
  ('dimension -> DIMFILAS','dimension',1,'p_dim0','Parser.py',693),
  ('dimension -> DIMCOLUMNAS','dimension',1,'p_dim1','Parser.py',698),
  ('time_mes -> QUOTES MIL QUOTES','time_mes',3,'p_timeM0','Parser.py',708),
  ('time_mes -> QUOTES MIN QUOTES','time_mes',3,'p_timeM1','Parser.py',713),
  ('time_mes -> QUOTES SEG QUOTES','time_mes',3,'p_timeM2','Parser.py',718),
  ('adding_operator -> PLUS','adding_operator',1,'p_addingOp0','Parser.py',728),
  ('adding_operator -> MINUS','adding_operator',1,'p_addingOp1','Parser.py',733),
  ('multiplying_operator -> TIMES','multiplying_operator',1,'p_multiplyingOp0','Parser.py',738),
  ('multiplying_operator -> EXP','multiplying_operator',1,'p_multiplyingOp1','Parser.py',742),
  ('multiplying_operator -> DIVIDE','multiplying_operator',1,'p_multiplyingOp2','Parser.py',747),
  ('multiplying_operator -> DIVENT','multiplying_operator',1,'p_multiplyingOp3','Parser.py',752),
  ('multiplying_operator -> MOD','multiplying_operator',1,'p_multiplyingOp4','Parser.py',757),
  ('value -> FALSE','value',1,'p_value0','Parser.py',767),
  ('value -> TRUE','value',1,'p_value1','Parser.py',772),
  ('bif_value -> value','bif_value',1,'p_Bifvalue0','Parser.py',777),
  ('bif_value -> arithmetic','bif_value',1,'p_Bifvalue1','Parser.py',782),
  ('relation -> ASSIGN','relation',1,'p_relation0','Parser.py',792),
  ('relation -> NE','relation',1,'p_relation1','Parser.py',797),
  ('relation -> LT','relation',1,'p_relation2','Parser.py',802),
  ('relation -> GT','relation',1,'p_relation3','Parser.py',807),
  ('relation -> LTE','relation',1,'p_relation4','Parser.py',812),
  ('relation -> GTE','relation',1,'p_relation5','Parser.py',817),
  ('relation -> COMPARE','relation',1,'p_relation6','Parser.py',822),
  ('identifier -> ID','identifier',1,'p_identifier0','Parser.py',830),
  ('identifier -> consult','identifier',1,'p_identifier1','Parser.py',835),
  ('iterable -> identifier','iterable',1,'p_iterable0','Parser.py',845),
  ('iterable -> INT','iterable',1,'p_iterable1','Parser.py',850),
  ('empty -> <empty>','empty',0,'p_empty','Parser.py',860),
]
