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
import Syntactic.Parser as parser
from Syntactic.Orders import *


def p_procedure(p):
    'procedure : Para ID LSQRBRACKET argument RSQRBRACKET statements Fin'
    p[0] = p[1]

def p_function_body(p):
    'function : body '
    p[0] = p[1]


def p_function_sequence(p):
    'function : sequence'
    p[0] = p[1]

def p_statements(p):
    'statements : function statements'
    p[0] = p[1]

def p_body_run(p):
    'body : Run LSQRBRACKET sequence RSQRBRACKET SEMICOLON'
    p[0] = p[1]

def p_body_repeat(p):
    'body : Repeat INTEGER LSQRBRACKET sequence RSQRBRACKET SEMICOLON'

def p_argument_simple(p):
    'argument : factor'
    p[0] = p[1]


def p_argument_multiple(p):
    'argument : factor COMMA argument'
    p[0] = p[1]

def p_argument_empty(p):
    'argument :'
    pass

def p_statements_empty(p):
    'statements :'
    pass