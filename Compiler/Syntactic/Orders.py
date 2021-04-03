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
from WritingMachine.Compiler.Syntactic.Reserved import *
from WritingMachine.Compiler.Semantic.OrderModels import *
import copy
seq = Sequence()
else_seq = Sequence()
if_seq = Sequence()



# Multiple orders
def p_sequence(p):
    'sequence : order sequence'
    seq.append_action(p[1])
    p[0] = seq


def p_sequence_if(p):
    'sequence_if : order sequence_if'
    if_seq.append_action(p[1])
    p[0] = if_seq


def p_sequence_else(p):
    'sequence_else : order sequence_else'
    else_seq.append_action(p[1])
    p[0] = else_seq

# Singular orders
def p_order_reserved(p):
    'order : reserved'
    p[0] = p[1]


def p_order_operation(p):
    'order : operation'
    p[0] = p[1]


def p_order_conditional(p):
    'order : conditional'
    p[0] = p[1]


def p_conditional_if(p):
    'conditional : If LPAREN comparison RPAREN LSQRBRACKET sequence RSQRBRACKET SEMICOLON'
    inner_sequence = copy.deepcopy(seq)
    seq.actions.clear()
    p[0] = WritingIf(p[3], inner_sequence)



def p_conditional_ifelse(p):
    'conditional : IfElse LPAREN comparison RPAREN LSQRBRACKET sequence_if RSQRBRACKET LSQRBRACKET sequence_else RSQRBRACKET SEMICOLON'
    if_sequence = copy.deepcopy(if_seq)
    if_seq.actions.clear()
    else_sequence = copy.deepcopy(else_seq)
    else_seq.actions.clear()
    p[0] = WritingIfElse(p[3], if_sequence, else_sequence)


# Empty productions
def p_sequence_empty(p):
    'sequence :'
    pass


def p_sequence_else_empty(p):
    'sequence_else :'
    pass


def p_sequence_if_empty(p):
    'sequence_if :'
    pass



