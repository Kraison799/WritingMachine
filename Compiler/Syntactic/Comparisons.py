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
    'comparison : Smaller LPAREN numerical COMMA numerical RPAREN'
    p[0] = Smaller(p[3], p[5])


def p_comparison_equal(p):
    'comparison : Equal LPAREN numerical COMMA numerical RPAREN'
    p[0] = Equal(p[3], p[5])

def p_comparison_greater(p):
    'comparison : Greater LPAREN numerical COMMA numerical RPAREN'
    p[0] = Greater(p[3], p[5])