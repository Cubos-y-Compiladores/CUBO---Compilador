
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'SLR'

_lr_signature = 'rightIDIFWHILETYPErightASSIGNleftLTLTEGTGTEleftPLUSMINUSleftMODDIVENTTIMESDIVIDEleftEXPleftLPARENTRPARENTASSIGN BLINK BOOKED COMMA CONST DELETE DIVENT DIVIDE DOT ELSE EXP F FALSE FOR GLOBAL GT GTE ID IF INSERT INT LCORCH LEN LENGHTERROR LPARENT LT LTE MINUS MOD NE NEG PARENTCL PARENTCR PLUS PROCEDURE RANGE RCORCH RPARENT SEMICOLON T TIMES TP TRUE TYPE VARERROR WHILEprogram : statement statement : assignment functionassignment : simpleAssignment doubleAssignment simpleAssignment : ID ASSIGN term SEMICOLON statementsimpleAssignment : emptydoubleAssignment : ID COMMA ID ASSIGN term COMMA term SEMICOLON statementdoubleAssignment : emptyfunction : typefunction : emptytype : TYPE LPARENT ID RPARENT SEMICOLON statementterm : FALSEterm : TRUEterm : factorfactor : IDfactor : INTempty : '
    
_lr_action_items = {'ID':([0,3,4,6,7,8,9,11,13,14,15,16,25,27,28,29,31,32,34,35,],[5,-16,12,-5,-2,-8,-9,-3,-7,17,23,24,5,17,-4,5,-10,17,5,-6,]),'TYPE':([0,3,4,6,7,8,9,11,13,25,28,29,31,34,35,],[-16,10,-16,-5,-2,-8,-9,-3,-7,-16,-4,-16,-10,-16,-6,]),'$end':([0,1,2,3,4,6,7,8,9,11,13,25,28,29,31,34,35,],[-16,0,-1,-16,-16,-5,-2,-8,-9,-3,-7,-16,-4,-16,-10,-16,-6,]),'ASSIGN':([5,24,],[14,27,]),'LPARENT':([10,],[15,]),'COMMA':([12,17,19,20,21,22,30,],[16,-14,-11,-12,-13,-15,32,]),'FALSE':([14,27,32,],[19,19,19,]),'TRUE':([14,27,32,],[20,20,20,]),'INT':([14,27,32,],[22,22,22,]),'SEMICOLON':([17,18,19,20,21,22,26,33,],[-14,25,-11,-12,-13,-15,29,34,]),'RPARENT':([23,],[26,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,25,29,34,],[2,28,31,35,]),'assignment':([0,25,29,34,],[3,3,3,3,]),'simpleAssignment':([0,25,29,34,],[4,4,4,4,]),'empty':([0,3,4,25,29,34,],[6,9,13,6,6,6,]),'function':([3,],[7,]),'type':([3,],[8,]),'doubleAssignment':([4,],[11,]),'term':([14,27,32,],[18,30,33,]),'factor':([14,27,32,],[21,21,21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement','program',1,'p_program','Parser.py',21),
  ('statement -> assignment function','statement',2,'p_statement','Parser.py',25),
  ('assignment -> simpleAssignment doubleAssignment','assignment',2,'p_assignment','Parser.py',29),
  ('simpleAssignment -> ID ASSIGN term SEMICOLON statement','simpleAssignment',5,'p_simpleAssignment','Parser.py',33),
  ('simpleAssignment -> empty','simpleAssignment',1,'p_simpleAssignmentEmp','Parser.py',37),
  ('doubleAssignment -> ID COMMA ID ASSIGN term COMMA term SEMICOLON statement','doubleAssignment',9,'p_doubleAssignment','Parser.py',41),
  ('doubleAssignment -> empty','doubleAssignment',1,'p_doubleAssignmentEmp','Parser.py',45),
  ('function -> type','function',1,'p_function','Parser.py',49),
  ('function -> empty','function',1,'p_functionEmp','Parser.py',53),
  ('type -> TYPE LPARENT ID RPARENT SEMICOLON statement','type',6,'p_type','Parser.py',56),
  ('term -> FALSE','term',1,'p_term0','Parser.py',60),
  ('term -> TRUE','term',1,'p_term1','Parser.py',64),
  ('term -> factor','term',1,'p_term2','Parser.py',68),
  ('factor -> ID','factor',1,'p_factor0','Parser.py',72),
  ('factor -> INT','factor',1,'p_factor1','Parser.py',76),
  ('empty -> <empty>','empty',0,'p_empty','Parser.py',80),
]
