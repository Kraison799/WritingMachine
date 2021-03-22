# ------------------------------------------------------------
# File: Lexer.py
# Developed by: Kevin Barrantes Cerdas
# Project: Writing Machine
# version: 0.1
#
# Description: The PLY lexer implementation that initiates
# lexical analysis
# TEC 2021 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------
import ply.lex as lex
from Rules import *


# TEST
def lex_test():
    lexer = lex.lex()
    data = '''
    ;,[]()=
    dAs&@f
    Arr2%
    aRr2&
    Arr
    se
    While
    while
    Def
    Run
    If
    IfElse
    **    *
    
    $
    iDentify
    '''
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


if __name__ == '__main__':
    lex_test()
