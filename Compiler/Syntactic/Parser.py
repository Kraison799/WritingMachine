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
import WritingMachine.Compiler.ply.yacc as yacc
from WritingMachine.Compiler.Syntactic.Procedures import*
from WritingMachine.Compiler.Lexical.Tokenizer import tokens
from WritingMachine.Compiler.Semantic.Evaluator import *

symbol_table = {}
current_scope = None
chain = Chain()
precedence = (('right', 'UMINUS'),)
start = 'structure'
syntax_err = False
semantic_err = False
Err_log = ""





def p_structure(p):
    '''structure : COMMENT\
    chain'''
    p[0] = p[2]


def p_chain(p):
    'chain : procedure chain'
    chain.chain.insert(0,p[1])
    p[0] = chain

def p_chain_comment(p):
    'chain : COMMENT chain'
    p[0] = p[2]

def p_chain_empty(p):
    'chain :'
    pass




# Build the parser
def build(lex):

    syntactic = yacc.yacc()
    if not syntax_err:
        semantic = Evaluate(syntactic.parse(lexer=lex))
        semantic.start()
        if semantic_err:
            print("SEMANTIC ERROR")
            parser.symbol_table = {}
            parser.current_scope = None
            parser.Err_log = ""
            parser.semantic_err = False
            parser.syntax_err = False
            del semantic
            chain.chain = []
            return False
        else:
            parser.symbol_table = {}
            parser.current_scope = None
            parser.Err_log = ""
            parser.semantic_err = False
            parser.syntax_err = False
            chain.chain = []
            del semantic
            return True
    else:
        parser.symbol_table = {}
        parser.current_scope = None
        parser.Err_log = ""
        parser.semantic_err = False
        parser.syntax_err = False
        chain.chain = []
        return False








