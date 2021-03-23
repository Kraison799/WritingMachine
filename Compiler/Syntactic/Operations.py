# ------------------------------------------------------------
# File: Operations.py
# Developed by: Kevin Barrantes Cerdas
# Project: Writing Machine
# version: 0.1
#
# Description: Context free grammar for mathematical operations
# in the Writing Machine language
# TEC 2021 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------
start = 'reserved'


def p_reserved_sum(p):
    'reserved : Sum LPAREN INTEGER COMMA INTEGER RPAREN SEMICOLON'
    p[0] = p[3] + p[5]

def p_reserved_substr(p):
    'reserved : Substr LPAREN INTEGER COMMA INTEGER RPAREN SEMICOLON'
    p[0] = p[3] - p[5]

def p_reserved_mult(p):
    'reserved : Mult LPAREN INTEGER COMMA INTEGER RPAREN SEMICOLON'
    p[0] = p[3] * p[5]

def p_reserved_div(p):
    'reserved : Div LPAREN INTEGER COMMA INTEGER RPAREN SEMICOLON'
    p[0] = p[3] // p[5]

def p_reserved_power(p):
    'reserved : Power LPAREN INTEGER COMMA INTEGER RPAREN SEMICOLON'
    p[0] = p[3]**p[5]

def p_reserved_pos(p):
    'reserved : Pos LSQRBRACKET INTEGER COMMA INTEGER RSQRBRACKET SEMICOLON'
    p[0] = [p[3],p[5]]


def p_reserved_posX(p):
    'reserved : PosX INTEGER SEMICOLON'
    p[0] = [p[2]]

def p_reserved_posY(p):
    'reserved : PosY INTEGER SEMICOLON'
    p[0] = [p[2]]

def p_reserved_UseColor(p):
    'reserved : UseColor INTEGER SEMICOLON'
    p[0] = p[2]

def p_reserved_Begin(p):
    'reserved : Begin SEMICOLON'
    p[0] = [1,1]

def p_reserved_Speed(p):
    'reserved : Speed INTEGER SEMICOLON'
    p[0] = p[2]


def p_factor_num(p):
    'factor : INTEGER'
    p[0] = p[1]


# Error rule for syntax errors
def p_error(p):
    if p:
        error_message = "Syntax error in line: " + str(p.lineno)
        print(error_message)
