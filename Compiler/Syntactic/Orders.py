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
import Compiler.Syntactic.Parser as parser
from Compiler.Syntactic.Reserved import *


# Multiple orders
def p_sequence(p):
    'sequence : order sequence'
    parser.results.insert(0, p[1])
    p[0] = p[1]


# Singular orders
def p_order_reserved(p):
    'order : reserved'
    p[0] = p[1]


def p_order_operation(p):
    'order : operation'
    p[0] = p[1]


# Conditional orders
def p_order_conditional(p):
    'order : conditional'
    p[0] = p[1]

# Loop orders
def p_order_loop(p):
    'order : loop'


def p_conditional_if(p):
    'conditional : If LPAREN comparison RPAREN LSQRBRACKET sequence RSQRBRACKET SEMICOLON'
    if p[3] == "TRUE":
        p[0] = "TRUE"

    if p[3] == "FALSE":
        p[0] = "FALSE"


def p_conditional_ifelse(p):
    'conditional : IfElse LPAREN comparison RPAREN LSQRBRACKET sequence RSQRBRACKET LSQRBRACKET sequence RSQRBRACKET SEMICOLON'

# Empty productions
def p_sequence_empty(p):
    'sequence :'
    pass