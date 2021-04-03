# ------------------------------------------------------------
# File: Reserved.py
# Developed by: Kevin Barrantes Cerdas
# Project: Writing Machine
# version: 0.1
#
# Description: Context free grammar for reserved functions
# in the Writing Machine language
# TEC 2021 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------

from random import randint
from WritingMachine.Compiler.Syntactic.Operations import *
from WritingMachine.Compiler.Semantic.ReservedModels import *
SymbolTable = {'PROC_01': [['id01', int, 2], ['id02', str, "FALSE"], ['id03', int, -10]]}
# SymbolTable = {}
CurrentScope = "PROC_01"


def p_reserved_def(p):
    '''reserved : Def ID ASSIGN factor SEMICOLON
                | Def ID ASSIGN operation'''
    p[0] = Def(p[2], p[4])




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
    'reserved : Add LSQRBRACKET ID numerical RSQRBRACKET SEMICOLON'
    line = p.lineno(2)
    if p[4] < 0:
        print('Add toma unicamente valores positivos')
    else:
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
                            if id_search_list[2] < 0:
                                print("Add toma unicamente valores positivos")
                            else:
                                id_list[2] += id_search_list[2]
                                p[0] = SymbolTable[CurrentScope]
                        else:
                            error_assignment(line)
            else:
                error_assignment(line)


def p_reserved_continueup_units(p):
    'reserved : ContinueUp numerical SEMICOLON'
    p[0] = ContinueUp(p[2])


def p_reserved_continueup_operation(p):
    'reserved : ContinueUp operation'
    p[0] = ContinueUp(p[2])


def p_reserved_continueup_variable(p):
    'reserved : ContinueUp ID SEMICOLON'
    line = p.lineno(2)
    p[0] = ContinueUp(p[2])


def p_reserved_continuedown_units(p):
    'reserved : ContinueDown numerical SEMICOLON'
    p[0] = ContinueDown(p[2])


def p_reserved_continuedown_operation(p):
    'reserved : ContinueDown operation'
    p[0] = ContinueDown(p[2])


def p_reserved_continuedown_variable(p):
    'reserved : ContinueDown ID SEMICOLON'
    line = p.lineno(2)
    p[0] = ContinueDown(p[2])


def p_reserved_continueleft_units(p):
    'reserved : ContinueLeft numerical SEMICOLON'
    p[0] = ContinueLeft(p[2])


def p_reserved_continueleft_operation(p):
    'reserved : ContinueLeft operation'
    p[0] = ContinueLeft(p[2])


def p_reserved_continueleft_variable(p):
    'reserved : ContinueLeft ID SEMICOLON'
    line = p.lineno(2)
    p[0] = ContinueLeft(p[2])


def p_reserved_continueright_units(p):
    'reserved : ContinueRight numerical SEMICOLON'
    p[0] = ContinueRight(p[2])


def p_reserved_continueright_operation(p):
    'reserved : ContinueRight operation'
    p[0] = ContinueRight(p[2])


def p_reserved_continueright_variable(p):
    'reserved : ContinueRight ID SEMICOLON'
    p[0] = ContinueRight(p[2])


def p_reserved_up(p):
    'reserved : Up SEMICOLON'
    p[0] = Up()


def p_reserved_down(p):
    'reserved : Down SEMICOLON'
    p[0] = Down()


def p_reserved_pos(p):
    'reserved : Pos LSQRBRACKET numerical COMMA numerical RSQRBRACKET SEMICOLON'
    p[0] = Pos(p[3], p[5])


def p_reserved_posX(p):
    'reserved : PosX numerical SEMICOLON'
    p[0] = PosX(p[2])


def p_reserved_posY(p):
    'reserved : PosY numerical SEMICOLON'
    p[0] = PosY(p[2])


def p_reserved_UseColor(p):
    'reserved : UseColor INTEGER SEMICOLON'
    p[0] = UseColor(p[2])


def p_reserved_Begin(p):
    'reserved : Begin SEMICOLON'
    p[0] = Begin()


def p_reserved_Speed(p):
    'reserved : Speed INTEGER SEMICOLON'
    p[0] = Speed(p[2])


def p_reserved_and_bool(p):
    'reserved : And LPAREN bool COMMA bool RPAREN SEMICOLON'
    p[0] = And(p[3], p[5])


def p_reserved_and_comparison(p):
    'reserved : And LPAREN comparison COMMA comparison RPAREN SEMICOLON'
    p[0] = And(p[3], p[5])


def p_reserved_or_bool(p):
    'reserved : Or LPAREN bool COMMA bool RPAREN SEMICOLON'
    p[0] = Or(p[3], p[5])


def p_reserved_or_comparison(p):
    'reserved : Or LPAREN comparison COMMA comparison RPAREN SEMICOLON'
    p[0] = Or(p[3], p[5])

def error_assignment(lineno):
    error_message = "SEMANTIC ERROR in line " + str(lineno) + " Assigned value does not match variable type."
    print(error_message)