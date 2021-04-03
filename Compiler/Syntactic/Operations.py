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
from WritingMachine.Compiler.Syntactic.Comparisons import *
from WritingMachine.Compiler.Syntactic.Atomic import *
import WritingMachine.Compiler.Syntactic.Parser as parser
from WritingMachine.Compiler.Semantic.OperationModels import *


def p_operation_random(p):
    'operation : Random LPAREN INTEGER RPAREN SEMICOLON'
    p[0] = Random(p[3])


def p_operation_sum(p):
    'operation : Sum LPAREN numerical COMMA numerical RPAREN SEMICOLON '
    p[0] = Sum(p[3], p[5])


def p_operation_substr(p):
    'operation : Substr LPAREN numerical COMMA numerical RPAREN SEMICOLON'
    p[0] = Substr(p[3], p[5])


def p_operation_mult(p):
    'operation : Mult LPAREN numerical COMMA numerical RPAREN SEMICOLON'
    p[0] = Mult(p[3], p[5])


def p_operation_div(p):
    'operation : Div LPAREN numerical COMMA numerical RPAREN SEMICOLON'
    p[0] = Div(p[3], p[5])


def p_operation_power(p):
    'operation : Power LPAREN INTEGER COMMA INTEGER RPAREN SEMICOLON'
    p[0] = Power(p[3], p[5])


def p_error(p):
    if p:
        error_message = "Syntax error in line: " + str(p.lineno)
        print(error_message)



# def p_reserved_random(p):
#     'reserved : Random LPAREN INTEGER RPAREN SEMICOLON'
#     p[0] = randint(0, p[3])
#
#
# def p_reserved_def(p):
#     'reserved : Def ID ASSIGN factor SEMICOLON'
#     SymbolTable["PROC_01"] = []
#     SymbolTable["PROC_01"].append([p[2], type(p[4]), p[4]])
#     p[0] = SymbolTable["PROC_01"][-1]
#
#
# def p_reserved_put(p):
#     'reserved : Put ID ASSIGN factor SEMICOLON'
#     line = p.lineno(2)
#     for id_list in SymbolTable[CurrentScope]:
#         if id_list[0] == p[2]:
#             if type(p[4]) == id_list[1]:
#                 id_list[2] = p[4]
#                 p[0] = SymbolTable[CurrentScope]
#             else:
#                 error_assignment(line)
#
#
# def p_reserved_put_operation(p):
#     'reserved : Put ID ASSIGN operation'
#     line = p.lineno(2)
#     for id_list in SymbolTable[CurrentScope]:
#         if id_list[0] == p[2]:
#             if type(p[4]) == id_list[1]:
#                 id_list[2] = p[4]
#                 p[0] = SymbolTable[CurrentScope]
#             else:
#                 error_assignment(line)
#
#
# def p_reserved_add_simple(p):
#     'reserved : Add LSQRBRACKET ID RSQRBRACKET SEMICOLON'
#     line = p.lineno(2)
#     for id_list in SymbolTable[CurrentScope]:
#         if id_list[0] == p[3]:
#             if id_list[1] == int:
#                 id_list[2] += 1
#                 p[0] = SymbolTable[CurrentScope]
#             else:
#                 error_assignment(line)
#
#
# def p_reserved_add_int(p):
#     'reserved : Add LSQRBRACKET ID numerical RSQRBRACKET SEMICOLON'
#     line = p.lineno(2)
#     if p[4] < 0:
#         print('Add toma unicamente valores positivos')
#     else:
#         for id_list in SymbolTable[CurrentScope]:
#             if id_list[0] == p[3]:
#                 if id_list[1] == int:
#                     id_list[2] += p[4]
#                     p[0] = SymbolTable[CurrentScope]
#                 else:
#                     error_assignment(line)
#
#
# def p_reserved_add_variable(p):
#     'reserved : Add LSQRBRACKET ID ID RSQRBRACKET SEMICOLON'
#     line = p.lineno(2)
#     for id_list in SymbolTable[CurrentScope]:
#         if id_list[0] == p[3]:
#             if id_list[1] == int:
#                 for id_search_list in SymbolTable[CurrentScope]:
#                     if id_search_list[0] == p[4]:
#                         if id_search_list[1] == int:
#                             if id_search_list[2] < 0:
#                                 print("Add toma unicamente valores positivos")
#                             else:
#                                 id_list[2] += id_search_list[2]
#                                 p[0] = SymbolTable[CurrentScope]
#                         else:
#                             error_assignment(line)
#             else:
#                 error_assignment(line)
#
#
# def p_reserved_continueup_units(p):
#     'reserved : ContinueUp numerical SEMICOLON'
#     # Continuar N unidades hacia arriba
#     if p[2] < 0:
#         print("ContinueRight solo admite valores positivos")
#     else:
#         print("Continuar", p[2], "unidades hacia arriba")
#         p[0] = ["y", p[2]]
#
#
# def p_reserved_continueup_operation(p):
#     'reserved : ContinueUp operation'
#     if p[2] < 0:
#         print("ContinueUp solo admite valores positivos")
#     else:
#         print("Continuar", p[2], "unidades hacia arriba")
#         p[0] = ["y", p[2]]
#
#
# def p_reserved_continueup_variable(p):
#     'reserved : ContinueUp ID SEMICOLON'
#     line = p.lineno(2)
#     for id_list in SymbolTable[CurrentScope]:
#         if id_list[0] == p[2]:
#             if id_list[1] == int:
#                 if id_list[2] < 0:
#                     print("ContinueUp solo admite valores positivos")
#                 else:
#                     print("Continuar", id_list[2], "unidades hacia arriba")
#                     p[0] = ["y", id_list[2]]
#             else:
#                 error_assignment(line)
#
#
# def p_reserved_continuedown_units(p):
#     'reserved : ContinueDown numerical SEMICOLON'
#     # Continuar N unidades hacia abajo
#     if p[2] < 0:
#         print("ContinueDown solo admite valores positivos")
#     else:
#         print("Continuar", p[2], "unidades hacia abajo")
#         p[0] = ["y", p[2] * -1]
#
#
# def p_reserved_continuedown_operation(p):
#     'reserved : ContinueDown operation'
#     if p[2] < 0:
#         print("ContinueDown solo admite valores positivos")
#     else:
#         print("Continuar", p[2], "unidades hacia abajo")
#         p[0] = ["y", p[2] * -1]
#
#
# def p_reserved_continuedown_variable(p):
#     'reserved : ContinueDown ID SEMICOLON'
#     line = p.lineno(2)
#     for id_list in SymbolTable[CurrentScope]:
#         if id_list[0] == p[2]:
#             if id_list[1] == int:
#                 if id_list[2] < 0:
#                     print("ContinueDown solo admite valores positivos")
#                 else:
#                     print("Continuar", id_list[2], "unidades hacia abajo")
#                     p[0] = ["y", id_list[2] * -1]
#             else:
#                 error_assignment(line)
#
#
# def p_reserved_continueleft_units(p):
#     'reserved : ContinueLeft numerical SEMICOLON'
#     # Continuar N unidades hacia arriba
#     if p[2] < 0:
#         print("ContinueLeft solo admite valores positivos")
#     else:
#         print("Continuar", p[2], "unidades hacia la izquierda")
#         p[0] = ["x", p[2] * -1]
#
#
# def p_reserved_continueleft_operation(p):
#     'reserved : ContinueLeft operation'
#     if p[2] < 0:
#         print("ContinueLeft solo admite valores positivos")
#     else:
#         print("Continuar", p[2], "unidades hacia la izquierda")
#         p[0] = ["x", p[2] * -1]
#
#
# def p_reserved_continueleft_variable(p):
#     'reserved : ContinueLeft ID SEMICOLON'
#     line = p.lineno(2)
#     for id_list in SymbolTable[CurrentScope]:
#         if id_list[0] == p[2]:
#             if id_list[1] == int:
#                 if id_list[2] < 0:
#                     print("ContinueLeft solo admite valores positivos")
#                 else:
#                     print("Continuar", id_list[2], "unidades hacia la izquierda")
#                     p[0] = ["x", id_list[2] * -1]
#             else:
#                 error_assignment(line)
#
#
# def p_reserved_continueright_units(p):
#     'reserved : ContinueRight numerical SEMICOLON'
#     # Continuar N unidades hacia arriba
#     if p[2] < 0:
#         print("ContinueRight solo admite valores positivos")
#     else:
#         print("Continuar", p[2], "unidades hacia la derecha")
#         p[0] = ["x", p[2]]
#
#
# def p_reserved_continueright_operation(p):
#     'reserved : ContinueRight operation'
#     if p[2] < 0:
#         print("ContinueRight solo admite valores positivos")
#     else:
#         print("Continuar", p[2], "unidades hacia la derecha")
#         p[0] = ["x", p[2]]
#
#
# def p_reserved_continueright_variable(p):
#     'reserved : ContinueRight ID SEMICOLON'
#     line = p.lineno(2)
#     for id_list in SymbolTable[CurrentScope]:
#         if id_list[0] == p[2]:
#             if id_list[1] == int:
#                 if id_list[2] < 0:
#                     print("ContinueRight solo admite valores positivos")
#                 else:
#                     print("Continuar", id_list[2], "unidades hacia la derecha")
#                     p[0] = ["x", id_list[2]]
#             else:
#                 error_assignment(line)
#
#
# def p_reserved_up(p):
#     'reserved : Up SEMICOLON'
#     # Subir lápiz
#     print("Subir lápiz")
#     p[0] = "u"
#
#
# def p_reserved_down(p):
#     'reserved : Down SEMICOLON'
#     # Bajar lápiz
#     print("Bajar lápiz")
#     p[0] = "d"
#
#
# def p_reserved_pos(p):
#     'reserved : Pos LSQRBRACKET numerical COMMA numerical RSQRBRACKET SEMICOLON'
#     p[0] = [p[3], p[5]]
#
#
# def p_reserved_posX(p):
#     'reserved : PosX numerical SEMICOLON'
#     p[0] = [p[2]]
#
#
# def p_reserved_posY(p):
#     'reserved : PosY numerical SEMICOLON'
#     p[0] = [p[2]]
#
#
# def p_reserved_UseColor(p):
#     'reserved : UseColor INTEGER SEMICOLON'
#     p[0] = ["color", p[2]]
#
#
# def p_reserved_Begin(p):
#     'reserved : Begin SEMICOLON'
#     p[0] = [1, 1]
#
#
# def p_reserved_Speed(p):
#     'reserved : Speed INTEGER SEMICOLON'
#     p[0] = p[2]
#
#
# def p_reserved_and_bool(p):
#     'reserved : And LPAREN bool COMMA bool RPAREN SEMICOLON'
#     if p[3] == "TRUE" and p[5] == "TRUE":
#         p[0] = "TRUE"
#     else:
#         p[0] = "FALSE"
#
#
# def p_reserved_and_comparison(p):
#     'reserved : And LPAREN comparison COMMA comparison RPAREN SEMICOLON'
#     if p[3] == "TRUE" and p[5] == "TRUE":
#         p[0] = "TRUE"
#     else:
#         p[0] = "FALSE"
#
#
# def p_reserved_or_bool(p):
#     'reserved : Or LPAREN bool COMMA bool RPAREN SEMICOLON'
#     if p[3] == "TRUE" or p[5] == "TRUE":
#         p[0] = "TRUE"
#     else:
#         p[0] = "FALSE"
#
#
# def p_reserved_or_comparison(p):
#     'reserved : Or LPAREN comparison COMMA comparison RPAREN SEMICOLON'
#     if p[3] == "TRUE" or p[5] == "TRUE":
#         p[0] = "TRUE"
#     else:
#         p[0] = "FALSE"


#
# def p_conditional_if(p):
#     'conditional : If LPAREN comparison RPAREN LSQRBRACKET sequence RSQRBRACKET SEMICOLON'
#     if p[3] == "TRUE":
#         result = parser.results
#         print(result)
#         p[0] = "TRUE"
#
#     if p[3] == "FALSE":
#         p[0] = "FALSE"
#
#
# def p_conditional_ifelse(p):
#     'conditional : IfElse LPAREN comparison RPAREN LSQRBRACKET sequence RSQRBRACKET LSQRBRACKET sequence RSQRBRACKET SEMICOLON'
#
#
# def p_order_reserved(p):
#     'order : reserved'
#     p[0] = p[1]
#
#
# def p_order_operation(p):
#     'order : operation'
#     p[0] = p[1]
#
#
# def p_order_conditional(p):
#     'order : conditional'
#     p[0] = p[1]
#
#
# def p_sequence(p):
#     'sequence : order sequence'
#     parser.results.insert(0, p[1])
#     p[0] = p[1]


# def p_numerical_positive(p):
#     'numerical : INTEGER'
#     p[0] = p[1]
#
#
# def p_numerical_negative(p):
#     'numerical : MINUS INTEGER %prec UMINUS'
#     p[0] = -p[2]


# def p_factor_num(p):
#     'factor : numerical'
#     p[0] = p[1]
#
#
# def p_factor_bool(p):
#     'factor : bool'
#     p[0] = p[1]

# def p_argument_simple(p):
#     'argument : factor'
#     p[0] = p[1]
#
#
# def p_argument_multiple(p):
#     'argument : factor COMMA argument'
#     p[0] = p[1]
#
# def p_argument_empty(p):
#     'argument :'
#     pass


# def p_bool_true(p):
#     'bool : True'
#     p[0] = p[1]
#
#
# def p_bool_false(p):
#     'bool : False'
#     p[0] = p[1]
# def p_sequence_empty(p):
#     'sequence :'
#     pass
#



