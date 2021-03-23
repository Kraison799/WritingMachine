# ------------------------------------------------------------
# File: Lexer.py
# Developed by: Kevin Barrantes Cerdas
# Project: Writing Machine
# version: 0.1
#
# Description: A tokenizer for the writing machine language
# lexical analysis
# TEC 2021 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------


# Regular expression rules for simple tokens

# OPERATORS
t_ASSIGN = r'\='


# SYMBOLS
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSQRBRACKET = r'\['
t_RSQRBRACKET = r'\]'

# Reserved words

reserved = {
    'Def': 'Def',
    'Put' : 'PUT',
    'Add' : 'ADD',
    'ContinueUp' : 'ContinueUp',
    'ContinueDown' : 'ContinueDown',
    'ContinueRight' : 'ContinueRight',
    'ContinueLeft' : 'ContinueLeft',
    'Pos' : 'Pos',
    'PosX' : 'PosX',
    'PosY' : 'PosY',
    'UseColor' : 'UseColor',
    'Down' : 'Down',
    'Up' : 'Up',
    'Begin' : 'Begin',
    'Speed' : 'Speed',
    'Run' : 'Run',
    'Repeat' : 'Repeat',
    'If' : 'If',
    'IfElse' : 'IfElse',
    'Until' : 'Until',
    'While' : 'While',
    'Equal' : 'Equal',
    'And' : 'And',
    'Or' : 'Or',
    'Greater' : 'Greater',
    'Smaller' : 'Smaller',
    'Substr' : 'Substr',
    'Random' : 'Random',
    'Mult' : 'Mult',
    'Power' : 'Power',
    'Div' : 'Div',
    'Sum' : 'Sum'
}

# List of token names
tokens = ['ASSIGN', 'NUMBER', 'COMMA', 'SEMICOLON', 'LPAREN', 'RPAREN',
          'LSQRBRACKET', 'RSQRBRACKET', 'ID', 'RESERVED', 'INTEGER', 'COMMENT',
          'INVALID_ID'] + list(reserved.values())
