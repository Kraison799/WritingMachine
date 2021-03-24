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
import Compiler.ply.lex as lex
import Compiler.Syntactic.Parser as syntactic
from Rules import *



# TEST

def lex_test():
    lexer = lex.lex()
    data = '''Speed 10;'''
    lexer.input(data)
    print("---END OF TOKENS---")
    syntactic.parse(lexer)
    # while True:
    #     tok = lexer.token()
    #     if not tok:
    #         break
    #     print(tok)



if __name__ == '__main__':
    lex_test()
