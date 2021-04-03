# ------------------------------------------------------------
# File: Procedures.py
# Developed by: Kevin Barrantes Cerdas
# Project: Writing Machine
# version: 0.1
#
# Description: Context free grammar for procedures
# in the Writing Machine language
# TEC 2021 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------
import WritingMachine.Compiler.Syntactic.Parser as parser
from WritingMachine.Compiler.Syntactic.Orders import *
from copy import deepcopy
from WritingMachine.Compiler.Semantic.ProcedureModels import *
arguments = []
statements = []

def p_procedure(p):
    'procedure : Para ID LSQRBRACKET argument RSQRBRACKET statements Fin'
    args = copy.deepcopy(arguments)
    arguments.clear()
    stats = copy.deepcopy(statements)
    statements.clear()
    seq.actions.clear()
    result = Procedure(p[2], args, stats)
    p[0] = result


def p_statements_01(p):
    'statements : body statements'
    statements.insert(0,p[1])
    p[0] = statements


def p_statements_02(p):
    'statements : sequence statements'
    statements.insert(0,p[1])
    p[0] = statements


def p_statements_empty(p):
    'statements : '
    pass


def p_body_run(p):
    'body : Run LSQRBRACKET sequence RSQRBRACKET SEMICOLON'
    sequence = copy.deepcopy(p[3])
    p[3].actions.clear()
    result = Run(sequence)
    p[0] = result


def p_body_repeat(p):
    'body : Repeat INTEGER LSQRBRACKET sequence RSQRBRACKET SEMICOLON'
    sequence = copy.deepcopy(p[4])
    p[4].actions.clear()
    result = Repeat(p[2], sequence)
    p[0] = result


def p_argument_simple(p):
    'argument : factor'
    arguments.insert(0,p[1])
    p[0] = arguments


def p_argument_multiple(p):
    'argument : factor COMMA argument'
    arguments.insert(0,p[1])
    p[0] = arguments

def p_argument_empty(p):
    'argument :'
    pass


