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
from random import randint

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
    p[0] = p[3] ** p[5]

def p_reserved_greater(p):
    'reserved : Greater LPAREN INTEGER COMMA INTEGER RPAREN SEMICOLON'
    p[0] = p[3] > p[5]

def p_reserved_smaller(p):
    'reserved : Smaller LPAREN INTEGER COMMA INTEGER RPAREN SEMICOLON'
    p[0] = p[3] < p[5]

def p_reverved_random(p):
    'reserved : Random LPAREN INTEGER RPAREN SEMICOLON'
    p[0] = randint(0, p[3])

def p_reserved_def(p):
    'reserved : Def ID ASSIGN INTEGER SEMICOLON'
    p[2] = p[4]

def p_reserved_put(p):
    'reserved : Put ID ASSIGN INTEGER SEMICOLON'
    p[2] = p[4]

def p_reserved_add(p):
    'reserved : Add LPAREN INTEGER RPAREN SEMICOLON'
    p[3] += 1

def p_reserved_continueup(p):
    'reserved : ContinueUp LPAREN INTEGER RPAREN SEMICOLON'
    # Continuar N unidades hacia arriba
    print("Continuar", p[3], "cantidad de unidades hacia arriba")

def p_reserved_continuedown(p):
    'reserved : ContinueDown LPAREN INTEGER RPAREN SEMICOLON'
    # Continuar N unidades hacia abajo
    print("Continuar", p[3], "cantidad de unidades hacia abajo")

def p_reserved_continueleft(p):
    'reserved : ContinueLeft LPAREN INTEGER RPAREN SEMICOLON'
    # Continuar N unidades hacia izquierda
    print("Continuar", p[3], "cantidad de unidades hacia izquierda")

def p_reserved_continueright(p):
    'reserved : ContinueRight LPAREN INTEGER RPAREN SEMICOLON'
    # Continuar N unidades hacia derecha
    print("Continuar", p[3], "cantidad de unidades hacia derecha")

def p_reserved_up(p):
    'reserved : Up SEMICOLON'
    # Subir lápiz
    print("Subir lápiz")

def p_reserved_down(p):
    'reserved : Down SEMICOLON'
    # Bajar lápiz
    print("Bajar lápiz")

def p_reserved_equal(p):
    'reserved : Equal LPAREN INTEGER COMMA INTEGER RPAREN SEMICOLON'
    p[0] = p[3] == p[5]

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
