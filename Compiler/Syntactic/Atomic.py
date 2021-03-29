# ------------------------------------------------------------
# File: Atomic.py
# Developed by: Kevin Barrantes Cerdas
# Project: Writing Machine
# version: 0.1
#
# Description: Context free grammar for simple atomic expressions
# in the Writing Machine language
# TEC 2021 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------
import Compiler.Syntactic.Parser as parser

#BOOLEAN VALUES
def p_bool_true(p):
    'bool : True'
    p[0] = p[1]


def p_bool_false(p):
    'bool : False'
    p[0] = p[1]

#NUMERICAL VALUES
def p_numerical_positive(p):
    'numerical : INTEGER'
    p[0] = p[1]


def p_numerical_negative(p):
    'numerical : MINUS INTEGER %prec UMINUS'
    p[0] = -p[2]


# SIMPLE FACTORS
def p_factor_num(p):
    'factor : numerical'
    p[0] = p[1]


def p_factor_bool(p):
    'factor : bool'
    p[0] = p[1]