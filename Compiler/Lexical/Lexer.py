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
import WritingMachine.Compiler.ply.lex as lex
import WritingMachine.Compiler.Syntactic.Parser as syntactic
from Rules import *



# TEST

def lex_test():
    lexer = lex.lex()
    # data = '''--This is a comment!
    #             PARA proc01 [0,1,10]
    #                 Run [
    #                     Def id05 = 4;
    #                     Def id06 = 5;
    #                     If(Greater(5,4))[
    #                         If(Equal(2,2))[
    #                             Mult(10,10);
    #                             ];
    #                         ];
    #                     ];
    #                     Sum(2,2)
    #             FIN
    #             PARA proc02 [12,TRUE]
    #                 Run [
    #                     Def id05 = 4;
    #                     Def id06 = 5;
    #                     If(Greater(5,4))[
    #                         If(Equal(2,2))[
    #                             Mult(20,20);
    #                             ];
    #                         ];
    #                     ];
    #             FIN
    #             '''
    data = '''  --MANDATORY COMMENT
                PARA proc01 [3,4]
                Repeat 4[
                Def id02 = Div(3,5);
                IfElse(Greater(3,5))
                  [
                    Random(4);
                  ]
                  [  
                    Mult(2,2);
                    If(Equal(2,2))[
                        Mult(20,20);
                        Def id02 = 44;
                        If(Smaller(3,6))[
                           Sum(3,6);
                        ];
                    ];
                  ];
                  Sum(4,4);
                  ];
                  Run[ Mult(4,4);];
                  Def id04 = Sum(4,4);
                  Sum(4,6);
                    FIN
                    
                PARA proc02 []
                    Def id05 = Mult(2,2);
                FIN
                
                
              '''
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
