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
import Syntactic.Parser as syntactic
from Rules import *



# TEST

def lex_test():
    lexer = lex.lex()
    data = '''PARA proc01 [0,1,10]
                Run [
                    Def id05 = 4;
                    Def id06 = 5;
                    If(Greater(5,4))[
                        If(Equal(2,2))[
                            Mult(10,10);
                            ];
                        ];
                   ];
                FIN'''


    lexer.input(data)
    syntactic.parse(lexer)

    # while True:
    #     tok = lexer.token()
    #     if not tok:
    #         break
    #     print(tok)
    # print("---END OF TOKENS---")



if __name__ == '__main__':
    lex_test()
