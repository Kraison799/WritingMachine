# ------------------------------------------------------------
# File: ComparisonModels.py
# Developed by: Kevin Barrantes Cerdas
# Project: Writing Machine
# version: 0.1
#
# Description: Data models for
# in the Writing Machine language
# TEC 2021 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------
from WritingMachine.Compiler.Semantic.SemanticError import SemanticError
from WritingMachine.Compiler.Semantic.TypeModels import *
from WritingMachine.Compiler.Syntactic import Parser as parser


class Smaller:
    def __init__(self, x, y, line):
        self.first_value = x
        self.second_value = y
        self.line = line

    def calculate(self):

        if isinstance(self.first_value, int) and isinstance(self.second_value, int):
            if self.first_value < self.second_value:
                return BooleanValue("TRUE")
            else:
                return BooleanValue("FALSE")

        if isinstance(self.first_value, str) and isinstance(self.second_value, str):

            values = [self.get_var(self.first_value), self.get_var(self.second_value)]

            if values[0] < values[1]:
                return BooleanValue("TRUE")
            else:
                return BooleanValue("FALSE")

        if isinstance(self.first_value, str) and isinstance(self.second_value, int):

            values = [self.get_var(self.first_value), self.second_value]

            if values[0] < values[1]:
                return BooleanValue("TRUE")
            else:
                return BooleanValue("FALSE")

        if isinstance(self.first_value, int) and isinstance(self.second_value, str):

            values = [self.first_value, self.get_var(self.second_value)]

            if values[0] < values[1]:
                return BooleanValue("TRUE")
            else:
                return BooleanValue("FALSE")


    def get_var(self, id):
        found = False

        for variable in parser.symbol_table[parser.current_scope]:
            if id == variable[0]:
                if variable[1] == int:
                    return variable[2]
                else:
                    error = SemanticError(5, self.line)
                    error.process()

        for variable in parser.symbol_table["main"]:
            if id == variable[0]:
                if variable[1] == int:
                    return variable[2]
                else:
                    error = SemanticError(5, self.line)
                    error.process()
        if not found:
            error = SemanticError(6, self.line)
            error.process()


class Equal:
    def __init__(self, x, y, line):
        self.first_value = x
        self.second_value = y
        self.line = line

    def calculate(self):
        if isinstance(self.first_value, int) and isinstance(self.second_value, int):
            if self.first_value == self.second_value:
                return BooleanValue("TRUE")
            else:
                return BooleanValue("FALSE")

        if isinstance(self.first_value, str) and isinstance(self.second_value, str):

            values = [self.get_var(self.first_value), self.get_var(self.second_value)]

            if values[0] == values[1]:
                return BooleanValue("TRUE")
            else:
                return BooleanValue("FALSE")

        if isinstance(self.first_value, str) and isinstance(self.second_value, int):

            values = [self.get_var(self.first_value), self.second_value]

            if values[0] == values[1]:
                return BooleanValue("TRUE")
            else:
                return BooleanValue("FALSE")

        if isinstance(self.first_value, int) and isinstance(self.second_value, str):

            values = [self.first_value, self.get_var(self.second_value)]

            if values[0] == values[1]:
                return BooleanValue("TRUE")
            else:
                return BooleanValue("FALSE")

    def get_var(self, id):
        found = False

        for variable in parser.symbol_table[parser.current_scope]:
            if id == variable[0]:
                if variable[1] == int:
                    return variable[2]
                else:
                    error = SemanticError(5, self.line)
                    error.process()

        for variable in parser.symbol_table["main"]:
            if id == variable[0]:
                if variable[1] == int:
                    return variable[2]
                else:
                    error = SemanticError(5, self.line)
                    error.process()
        if not found:
            error = SemanticError(6, self.line)
            error.process()


class Greater:
    def __init__(self, x, y, line):
        self.first_value = x
        self.second_value = y
        self.line = line

    def calculate(self):
        if isinstance(self.first_value, int) and isinstance(self.second_value, int):
            if self.first_value > self.second_value:
                return BooleanValue("TRUE")
            else:
                return BooleanValue("FALSE")

        if isinstance(self.first_value, str) and isinstance(self.second_value, str):

            values = [self.get_var(self.first_value), self.get_var(self.second_value)]

            if values[0] > values[1]:
                return BooleanValue("TRUE")
            else:
                return BooleanValue("FALSE")

        if isinstance(self.first_value, str) and isinstance(self.second_value, int):

            values = [self.get_var(self.first_value), self.second_value]

            if values[0] > values[1]:
                return BooleanValue("TRUE")
            else:
                return BooleanValue("FALSE")

        if isinstance(self.first_value, int) and isinstance(self.second_value, str):

            values = [self.first_value, self.get_var(self.second_value)]

            if values[0] > values[1]:
                return BooleanValue("TRUE")
            else:
                return BooleanValue("FALSE")

    def get_var(self, id):
        found = False

        for variable in parser.symbol_table[parser.current_scope]:
            if id == variable[0]:
                if variable[1] == int:
                    return variable[2]
                else:
                    error = SemanticError(5, self.line)
                    error.process()

        for variable in parser.symbol_table["main"]:
            if id == variable[0]:
                if variable[1] == int:
                    return variable[2]
                else:
                    error = SemanticError(5, self.line)
                    error.process()
        if not found:
            error = SemanticError(6, self.line)
            error.process()
