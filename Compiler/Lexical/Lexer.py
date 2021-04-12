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
    # data = '''  --Initial comment
    #             PARA proc01 [3,4]
    #             Repeat 4[
    #             Def id02 = Div(3,5);
    #             IfElse(Greater(3,5))
    #               [
    #                 Random(4);
    #               ]
    #               [
    #                 Mult(2,2);
    #                 If(Equal(2,2))[
    #                     Mult(20,20);
    #                     Def id02 = 44;
    #                     If(Smaller(3,6))[
    #                        Sum(3,6);
    #                     ];
    #                 If(Greater(2,3))[
    #                     Sum(3,3);
    #                     ];
    #                 ];
    #               ];
    #               Sum(4,4);
    #               ];
    #               Run[ Mult(6,4);];
    #               Def id04 = Sum(4,4);
    #               Sum(4,6);
    #                 FIN
    #
    #             PARA main []
    #                 Def id05 = Mult(2,2);
    #                 While [ Greater(3,1) ]
    #                     [
    #                         Sum(6,1);
    #                         While [ Equal(2,2)]
    #                             [
    #                                 Div(2,2);
    #                                 Until
    #                                     [ Power(2,3);]
    #                                 [Smaller(2,1)];
    #                             ];
    #                     ];
    #             FIN
    #
    #             PARA proc02[4,6]
    #             FIN
    #           '''
    data = '''-- First comment
            PARA main [arg1,arg2]
                Def var01 = 10;
                Def var02 = 20;
                
            FIN
            
            PARA proc01[]
                Def var01 = 35;
                Def var02 = 25;
                Run
                [
                    Add[Global var01];
                ];
                Repeat 2
                [
                    Add[var02];
                    ContinueRight var02;
                ];
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
