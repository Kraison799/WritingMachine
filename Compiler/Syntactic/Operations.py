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

SymbolTable = {'PROC_01': [['id01', int, 2], ['id02', str, "FALSE"], ['id03', int, 10]]}
# SymbolTable = {}
CurrentScope = "PROC_01"

start = 'reserved'


def p_operation_sum(p):
    'operation : Sum LPAREN INTEGER COMMA INTEGER RPAREN SEMICOLON'
    p[0] = p[3] + p[5]


def p_operation_substr(p):
    'operation : Substr LPAREN INTEGER COMMA INTEGER RPAREN SEMICOLON'
    p[0] = p[3] - p[5]


def p_operation_mult(p):
    'operation : Mult LPAREN INTEGER COMMA INTEGER RPAREN SEMICOLON'
    p[0] = p[3] * p[5]


def p_operation_div(p):
    'reserved : Div LPAREN INTEGER COMMA INTEGER RPAREN SEMICOLON'
    p[0] = p[3] // p[5]


def p_operation_power(p):
    'operation : Power LPAREN INTEGER COMMA INTEGER RPAREN SEMICOLON'
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
    'reserved : Def ID ASSIGN factor SEMICOLON'
    SymbolTable["PROC_01"] = []
    SymbolTable["PROC_01"].append([p[2], type(p[4]), p[4]])
    p[0] = SymbolTable["PROC_01"][-1]


def p_reserved_put(p):
    'reserved : Put ID ASSIGN factor SEMICOLON'
    line = p.lineno(2)
    for id_list in SymbolTable[CurrentScope]:
        if id_list[0] == p[2]:
            if type(p[4]) == id_list[1]:
                id_list[2] = p[4]
                p[0] = SymbolTable[CurrentScope]
            else:
                error_assignment(line)


def p_reserved_put_operation(p):
    'reserved : Put ID ASSIGN operation'
    line = p.lineno(2)
    for id_list in SymbolTable[CurrentScope]:
        if id_list[0] == p[2]:
            if type(p[4]) == id_list[1]:
                id_list[2] = p[4]
                p[0] = SymbolTable[CurrentScope]
            else:
                error_assignment(line)


def p_reserved_add_simple(p):
    'reserved : Add LSQRBRACKET ID RSQRBRACKET SEMICOLON'
    line = p.lineno(2)
    for id_list in SymbolTable[CurrentScope]:
        if id_list[0] == p[3]:
            if id_list[1] == int:
                id_list[2] += 1
                p[0] = SymbolTable[CurrentScope]
            else:
                error_assignment(line)


def p_reserved_add_int(p):
    'reserved : Add LSQRBRACKET ID INTEGER RSQRBRACKET SEMICOLON'
    line = p.lineno(2)
    for id_list in SymbolTable[CurrentScope]:
        if id_list[0] == p[3]:
            if id_list[1] == int:
                id_list[2] += p[4]
                p[0] = SymbolTable[CurrentScope]
            else:
                error_assignment(line)


def p_reserved_add_variable(p):
    'reserved : Add LSQRBRACKET ID ID RSQRBRACKET SEMICOLON'
    line = p.lineno(2)
    for id_list in SymbolTable[CurrentScope]:
        if id_list[0] == p[3]:
            if id_list[1] == int:
                for id_search_list in SymbolTable[CurrentScope]:
                    if id_search_list[0] == p[4]:
                        if id_search_list[1] == int:
                            id_list[2] += id_search_list[2]
                            p[0] = SymbolTable[CurrentScope]
                        else:
                            error_assignment(line)
            else:
                error_assignment(line)


def p_reserved_continueup_units(p):
    'reserved : ContinueUp INTEGER SEMICOLON'
    # Continuar N unidades hacia arriba
    print("Continuar", p[2], "unidades hacia arriba")
    p[0] = ["y", p[2]]


def p_reserved_continueup_operation(p):
    'reserved : ContinueUp operation'
    if p[2] < 0:
        print("ContinueUp solo admite valores positivos")
    else:
        print("Continuar", p[2], "unidades hacia arriba")
        p[0] = ["y", p[2]]


def p_reserved_continueup_variable(p):
    'reserved : ContinueUp ID SEMICOLON'
    line = p.lineno(2)
    for id_list in SymbolTable[CurrentScope]:
        if id_list[0] == p[2]:
            if id_list[1] == int:
                print("Continuar", id_list[2], "unidades hacia arriba")
                p[0] = ["y", id_list[2]]
            else:
                error_assignment(line)


def p_reserved_continuedown_units(p):
    'reserved : ContinueDown INTEGER SEMICOLON'
    # Continuar N unidades hacia abajo
    print("Continuar", p[2], "unidades hacia abajo")
    p[0] = ["y", p[2] * -1]

def p_reserved_continuedown_operation(p):
    'reserved : ContinueDown operation'
    if p[2] < 0:
        print("ContinueDown solo admite valores positivos")
    else:
        print("Continuar", p[2], "unidades hacia abajo")
        p[0] = ["y", p[2]*-1]

def p_reserved_continuedown_variable(p):
    'reserved : ContinueDown ID SEMICOLON'
    line = p.lineno(2)
    for id_list in SymbolTable[CurrentScope]:
        if id_list[0] == p[2]:
            if id_list[1] == int:
                print("Continuar", id_list[2], "unidades hacia abajo")
                p[0] = ["y", id_list[2]*-1]
            else:
                error_assignment(line)

def p_reserved_continueleft_units(p):
    'reserved : ContinueLeft INTEGER SEMICOLON'
    # Continuar N unidades hacia arriba
    print("Continuar", p[2], "unidades hacia la izquierda")
    p[0] = ["x", p[2]*-1]


def p_reserved_continueleft_operation(p):
    'reserved : ContinueLeft operation'
    if p[2] < 0:
        print("ContinueLeft solo admite valores positivos")
    else:
        print("Continuar", p[2]*-1, "unidades hacia la izquierda")
        p[0] = ["x", p[2]]


def p_reserved_continueleft_variable(p):
    'reserved : ContinueLeft ID SEMICOLON'
    line = p.lineno(2)
    for id_list in SymbolTable[CurrentScope]:
        if id_list[0] == p[2]:
            if id_list[1] == int:
                print("Continuar", id_list[2], "unidades hacia la izquierda")
                p[0] = ["x", id_list[2]*-1]
            else:
                error_assignment(line)


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
    p[0] = [p[3], p[5]]


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
    p[0] = [1, 1]


def p_reserved_Speed(p):
    'reserved : Speed INTEGER SEMICOLON'
    p[0] = p[2]


def p_factor_num(p):
    'factor : INTEGER'
    p[0] = p[1]


def p_factor_false(p):
    'factor : False'
    p[0] = p[1]


def p_factor_true(p):
    'factor : True'
    p[0] = p[1]


# Error rule for syntax errors
def p_error(p):
    if p:
        error_message = "Syntax error in line: " + str(p.lineno)
        print(error_message)


def error_assignment(lineno):
    error_message = "SEMANTIC ERROR in line " + str(lineno) + " Assigned value does not match variable type."
    print(error_message)
