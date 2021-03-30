# ------------------------------------------------------------
# File: Parser.py
# Developed by: Kevin Barrantes Cerdas
# Project: Writing Machine
# version: 0.1
#
# Description: A parsing class that generates an AST
# for syntactical analysis
# in the Writing Machine language
# TEC 2021 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------

import Compiler.ply.yacc as yacc
from Compiler.Syntactic.Procedures import*
from Compiler.Lexical.Tokenizer import tokens
from Compiler.TreeStructure.Node import *

results = []
ast = TreeNode("ROOT")
precedence = (('right', 'UMINUS'),)
start = 'sequence'


def p_structure(p):
    '''structure : COMMENT\
    chain'''
    p[0] = p[1]

def p_chain(p):
    'chain : procedure chain'
    p[0] = p[1]

def p_chain_empty(p):
    'chain :'
    pass


# Build the parser
def parse(lex):
    parser = yacc.yacc()
    result = parser.parse(lexer=lex)
    result.calculate()



