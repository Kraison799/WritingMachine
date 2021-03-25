# ------------------------------------------------------------
# File: Rules.py
# Developed by: Kevin Barrantes Cerdas
# Project: Writing Machine
# version: 0.1
#
# Description: Rules for complex regular expressions
#
# TEC 2021 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------

from Tokenizer import *


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


#Defines a rule that ignores lines that start with --
def t_COMMENT(t):
    r'\--.*'
    t.value = str(t.value) + str(t.lexer.lineno)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


def t_ID(t):
    r'[a-z][a-zA-Z_0-9&@]*'
    if 3 <= len(t.value) < 11:
        t.type = reserved.get(t.value, 'ID')  # Check for reserved words
        return t
    else:
        t.type = "length_err"
        t_error(t)

def t_INVALID_ID(t):
    r'[A-Z][a-zA-Z_0-9@&]*'
    token = reserved.get(t.value)
    if token:
        t.type = token
        return t
    else:
        t_error(t)



def t_RESERVED(t):
    r'[A-Z][a-zA-Z]*'
    token = reserved.get(t.value)
    if token:
        t.type = token
        return t


# Error handling rule
def t_error(t):
    if t.type == "length_err":
        print ("Lexical error at line "+str(t.lexer.lineno)+": ID length must be between 3 and 11")
        t.lexer.skip(1)
    elif t.type == "INVALID_ID":
        print ("Lexical error at line "+str(t.lexer.lineno)+": Identifiers cannot start with Upper case")
    else:
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
