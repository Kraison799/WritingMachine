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
    line = p.lineno(1)
    args = copy.deepcopy(arguments)
    arguments.clear()
    stats = copy.deepcopy(statements)
    statements.clear()
    seq.actions.clear()
    result = Procedure(p[2], args, stats)
    p[0] = result

def p_proc_call(p):
    'proc_call : ID LSQRBRACKET'


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
    'body : Run LSQRBRACKET body_seq RSQRBRACKET SEMICOLON'
    sequence = copy.deepcopy(body_seq)
    body_seq.actions.clear()
    result = Run(sequence)
    p[0] = result


def p_body_repeat(p):
    'body : Repeat INTEGER LSQRBRACKET body_seq RSQRBRACKET SEMICOLON'
    line = p.lineno(1)
    sequence = copy.deepcopy(body_seq)
    body_seq.actions.clear()
    result = Repeat(p[2], sequence, line)
    p[0] = result


def p_argument_simple(p):
    'argument : ID'
    arguments.insert(0,p[1])
    p[0] = arguments


def p_argument_multiple(p):
    'argument : ID COMMA argument'
    arguments.insert(0,p[1])
    p[0] = arguments

def p_argument_empty(p):
    'argument :'
    pass


