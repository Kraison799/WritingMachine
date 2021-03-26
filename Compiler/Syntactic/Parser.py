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

import ply.yacc as yacc
from Syntactic.Procedures import*
from Lexical.Tokenizer import tokens

results = []
precedence = (('right', 'UMINUS'),)
start = 'procedure'



# Build the parser
def parse(lex):
    parser = yacc.yacc()
    result = parser.parse(lexer=lex)
    print(results)



