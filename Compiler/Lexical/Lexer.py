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
from WritingMachine.Compiler.Lexical.Rules import *


# TEST


def lex_test(codeEditor):
    lexer = lex.lex()
    print(codeEditor.toPlainText())
    data = codeEditor.toPlainText()
    lexer.input(data)
    return syntactic.build(lexer)



