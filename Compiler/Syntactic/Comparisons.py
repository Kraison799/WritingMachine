# ------------------------------------------------------------
# File: Comparisons.py
# Developed by: Kevin Barrantes Cerdas
# Project: Writing Machine
# version: 0.1
#
# Description: Context free grammar for comparison functions
# in the Writing Machine language
# TEC 2021 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------
import WritingMachine.Compiler.Syntactic.Parser as parser
from WritingMachine.Compiler.Syntactic.Atomic import *
from WritingMachine.Compiler.Semantic.ComparisonModels import *

def p_comparison_smaller(p):
    '''comparison : Smaller LPAREN numerical COMMA numerical RPAREN
                  | Smaller LPAREN ID COMMA ID RPAREN
                  | Smaller LPAREN ID COMMA numerical RPAREN
                  | Smaller LPAREN numerical COMMA ID RPAREN'''
    line = p.lineno(1)
    p[0] = Smaller(p[3], p[5], line)


def p_comparison_equal(p):
    '''comparison : Equal LPAREN numerical COMMA numerical RPAREN
                  | Equal LPAREN ID COMMA ID RPAREN
                  | Equal LPAREN ID COMMA numerical RPAREN
                  | Equal LPAREN numerical COMMA ID RPAREN'''
    line = p.lineno(1)
    p[0] = Equal(p[3], p[5], line)

def p_comparison_greater(p):
    '''comparison : Greater LPAREN numerical COMMA numerical RPAREN
                  | Greater LPAREN ID COMMA ID RPAREN
                  | Greater LPAREN ID COMMA numerical RPAREN
                  | Greater LPAREN numerical COMMA ID RPAREN'''
    line = p.lineno(1)
    p[0] = Greater(p[3], p[5], line)