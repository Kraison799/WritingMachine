# ------------------------------------------------------------
# File: Loops.py
# Developed by: Kevin Barrantes Cerdas
# Project: Writing Machine
# version: 0.1
#
# Description: Context free grammar for loops
# in the Writing Machine language
# TEC 2021 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------
from WritingMachine.Compiler.Syntactic.Comparisons import *
from WritingMachine.Compiler.Syntactic.Atomic import *
import WritingMachine.Compiler.Syntactic.Parser as parser

def p_loop_Until(p):
    'loop : Until LSQRBRACKET sequence RSQRBRACKET LSQRBRACKET comparison RSQRBRACKET'

def p_loop_While(p):
    'loop : While LSQRBRACKET comparison RSQRBRACKET LSQRBRACKET sequence RSQRBRACKET'

def p_loop_Repeat(p):
    'loop : Repeat INTEGER LSQRBRACKET sequence RSQRBRACKET'