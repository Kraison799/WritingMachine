# ------------------------------------------------------------
# File: OrderModels.py
# Developed by: Kevin Barrantes Cerdas
# Project: Writing Machine
# version: 0.1
#
# Description: Data models for the order rules
# in the Writing Machine language
# TEC 2021 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------
from WritingMachine.Compiler.Semantic.ReservedModels import *


class Sequence:

    def __init__(self):
        self.actions = []

    def append_action(self, action):
        self.actions.insert(0, action)


class WritingIf:

    def __init__(self, comparison, sequence, line):
        self.comparison = comparison
        self.sequence = sequence
        self.line = line


    def calculate(self):
        if self.comparison.calculate().value == "TRUE":
            return self.sequence
        else:
            return None


class WritingIfElse:

    def __init__(self, comparison, if_seq, else_seq, line):
        self.comparison = comparison
        self.if_seq = if_seq
        self.else_seq = else_seq
        self.line = line



    def calculate(self):
        if self.comparison.calculate().value == "TRUE":
            return self.if_seq
        else:
            return self.else_seq


class WritingWhile:

    def __init__(self, comparison, sequence, line, count):
        self.comparison = comparison
        self.sequence = sequence
        self.line = line
        self.count = count

    def calculate(self):
        if self.count <= 985:
            if self.comparison.calculate().value == "TRUE":
                self.count += 1
                return self.sequence
            else:
                return None
        else:
            error = SemanticError(8, self.line)
            error.process()



class Until:

    def __init__(self, comparison, sequence):
        self.comparison = comparison
        self.sequence = sequence





