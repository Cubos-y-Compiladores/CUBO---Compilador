import ply.yacc as yacc
import os,codecs,re
from Lexer import tokens
from sys import stdin

precedence=(
    ('right','ASSIGN'),
    ('left','LT','LTE','GT','GTE'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE','DIVENT','MOD'),
    ('left','EXP'),
    ('left','LPARENT','RPARENT'),
    )