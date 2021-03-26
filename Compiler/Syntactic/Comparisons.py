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
import Syntactic.Parser as parser
from Syntactic.Atomic import *

def p_comparison_smaller(p):
    'comparison : Smaller LPAREN numerical COMMA numerical RPAREN'
    if p[3] < p[5]:
        p[0] = "TRUE"
    else:
        p[0] = "FALSE"


def p_comparison_equal(p):
    'comparison : Equal LPAREN numerical COMMA numerical RPAREN'
    if p[3] == p[5]:
        p[0] = "TRUE"
    else:
        p[0] = "FALSE"

def p_comparison_greater(p):
    'comparison : Greater LPAREN numerical COMMA numerical RPAREN'
    if p[3] > p[5]:
        p[0] = "TRUE"
    else:
        p[0] = "FALSE"