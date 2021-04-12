# ------------------------------------------------------------
# File: OperationModels.py
# Developed by: Kevin Barrantes Cerdas
# Project: Writing Machine
# version: 0.1
#
# Description: Data models for
# in the Writing Machine language
# TEC 2021 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------
from random import randint

from WritingMachine.Compiler.Semantic.SemanticError import SemanticError
from WritingMachine.Compiler.Syntactic import Parser as parser


class Sum:
    def __init__(self, x, y, line):
        self.first_value = x
        self.second_value = y
        self.line = line

    def calculate(self):
        if isinstance(self.first_value, int) and isinstance(self.second_value, int):
            result = self.first_value + self.second_value
            return result

        elif isinstance(self.first_value, int) and isinstance(self.second_value, str):

            current_scope = parser.symbol_table[parser.current_scope]
            value = None
            for variable in current_scope:
                if variable[0] == self.second_value and variable[1] == int:
                    value = variable[2]
                    break
            if value:
                result = self.first_value + value
                return result
            else:
                for variable in parser.symbol_table["main"]:
                    if variable[0] == self.second_value and variable[1] == int:
                        value = variable[2]
                        break
                if value:
                    result = self.first_value + value
                    return result
                else:
                    error = SemanticError(4, self.line)
                    error.process()

        elif isinstance(self.first_value, str) and isinstance(self.second_value, int):

            current_scope = parser.symbol_table[parser.current_scope]
            value = None
            for variable in current_scope:
                if variable[0] == self.first_value and variable[1] == int:
                    value = variable[2]
                    break
            if value:
                result = value + self.second_value
                return result
            else:
                for variable in parser.symbol_table["main"]:
                    if variable[0] == self.first_value and variable[1] == int:
                        value = variable[2]
                        break
                if value:
                    result = value + self.second_value
                    return result
                else:
                    error = SemanticError(4, self.line)
                    error.process()

        elif isinstance(self.first_value, str) and isinstance(self.second_value,str):

            current_scope = parser.symbol_table[parser.current_scope]
            value_1 = None
            value_2 = None
            for variable in current_scope:
                if variable[0] == self.first_value and variable[1] == int:
                    value_1 = variable[2]
                    break

            for variable in current_scope:
                if variable[0] == self.second_value and variable[1] == int:
                    value_2 = variable[2]
                    break

            if value_1 and value_2:
                result = value_1 + value_2
                return result
            else:
                for variable in parser.symbol_table["main"]:
                    if variable[0] == self.first_value and variable[1] == int:
                        value_1 = variable[2]
                        break
                for variable in parser.symbol_table["main"]:
                    if variable[0] == self.second_value and variable[1] == int:
                        value_2 = variable[2]
                        break
                if value_1 and value_2:
                    result = value_1 + value_2
                    return result
                else:
                    error = SemanticError(4, self.line)
                    error.process()


class Substr:
    def __init__(self, x, y, line):
        self.first_value = x
        self.second_value = y
        self.line = line

    def calculate(self):
        if isinstance(self.first_value, int) and isinstance(self.second_value, int):
            result = self.first_value - self.second_value
            return result

        elif isinstance(self.first_value, int) and isinstance(self.second_value, str):

            current_scope = parser.symbol_table[parser.current_scope]
            value = None
            for variable in current_scope:
                if variable[0] == self.second_value and variable[1] == int:
                    value = variable[2]
                    break
            if value:
                result = self.first_value - value
                return result
            else:
                for variable in parser.symbol_table["main"]:
                    if variable[0] == self.second_value and variable[1] == int:
                        value = variable[2]
                        break
                if value:
                    result = self.first_value - value
                    return result
                else:
                    error = SemanticError(4, self.line)
                    error.process()

        elif isinstance(self.first_value, str) and isinstance(self.second_value, int):

            current_scope = parser.symbol_table[parser.current_scope]
            value = None
            for variable in current_scope:
                if variable[0] == self.first_value and variable[1] == int:
                    value = variable[2]
                    break
            if value:
                result = value - self.second_value
                return result
            else:
                for variable in parser.symbol_table["main"]:
                    if variable[0] == self.first_value and variable[1] == int:
                        value = variable[2]
                        break
                if value:
                    result = value - self.second_value
                    return result
                else:
                    error = SemanticError(4, self.line)
                    error.process()

        elif isinstance(self.first_value, str) and isinstance(self.second_value, str):

            current_scope = parser.symbol_table[parser.current_scope]
            value_1 = None
            value_2 = None
            for variable in current_scope:
                if variable[0] == self.first_value and variable[1] == int:
                    value_1 = variable[2]
                    break

            for variable in current_scope:
                if variable[0] == self.second_value and variable[1] == int:
                    value_2 = variable[2]
                    break

            if value_1 and value_2:
                result = value_1 - value_2
                return result
            else:
                for variable in parser.symbol_table["main"]:
                    if variable[0] == self.first_value and variable[1] == int:
                        value_1 = variable[2]
                        break
                for variable in parser.symbol_table["main"]:
                    if variable[0] == self.second_value and variable[1] == int:
                        value_2 = variable[2]
                        break
                if value_1 and value_2:
                    result = value_1 - value_2
                    return result
                else:
                    error = SemanticError(4, self.line)
                    error.process()


class Mult:
    def __init__(self, x, y, line):
        self.first_value = x
        self.second_value = y
        self.line = line

    def calculate(self):
        if isinstance(self.first_value, int) and isinstance(self.second_value, int):
            result = self.first_value * self.second_value
            return result

        elif isinstance(self.first_value, int) and isinstance(self.second_value, str):

            current_scope = parser.symbol_table[parser.current_scope]
            value = None
            for variable in current_scope:
                if variable[0] == self.second_value and variable[1] == int:
                    value = variable[2]
                    break
            if value:
                result = self.first_value * value
                return result
            else:
                for variable in parser.symbol_table["main"]:
                    if variable[0] == self.second_value and variable[1] == int:
                        value = variable[2]
                        break
                if value:
                    result = self.first_value * value
                    return result
                else:
                    error = SemanticError(4, self.line)
                    error.process()

        elif isinstance(self.first_value, str) and isinstance(self.second_value, int):

            current_scope = parser.symbol_table[parser.current_scope]
            value = None
            for variable in current_scope:
                if variable[0] == self.first_value and variable[1] == int:
                    value = variable[2]
                    break
            if value:
                result = value * self.second_value
                return result
            else:
                for variable in parser.symbol_table["main"]:
                    if variable[0] == self.first_value and variable[1] == int:
                        value = variable[2]
                        break
                if value:
                    result = value * self.second_value
                    return result
                else:
                    error = SemanticError(4, self.line)
                    error.process()

        elif isinstance(self.first_value, str) and isinstance(self.second_value, str):

            current_scope = parser.symbol_table[parser.current_scope]
            value_1 = None
            value_2 = None
            for variable in current_scope:
                if variable[0] == self.first_value and variable[1] == int:
                    value_1 = variable[2]
                    break

            for variable in current_scope:
                if variable[0] == self.second_value and variable[1] == int:
                    value_2 = variable[2]
                    break

            if value_1 and value_2:
                result = value_1 * value_2
                return result
            else:
                for variable in parser.symbol_table["main"]:
                    if variable[0] == self.first_value and variable[1] == int:
                        value_1 = variable[2]
                        break
                for variable in parser.symbol_table["main"]:
                    if variable[0] == self.second_value and variable[1] == int:
                        value_2 = variable[2]
                        break
                if value_1 and value_2:
                    result = value_1 * value_2
                    return result
                else:
                    error = SemanticError(4, self.line)
                    error.process()


class Div:
    def __init__(self, x, y, line):
        self.first_value = x
        self.second_value = y
        self.line = line

    def calculate(self):
        if isinstance(self.first_value, int) and isinstance(self.second_value, int):
            result = self.first_value // self.second_value
            return result

        elif isinstance(self.first_value, int) and isinstance(self.second_value, str):

            current_scope = parser.symbol_table[parser.current_scope]
            value = None
            for variable in current_scope:
                if variable[0] == self.second_value and variable[1] == int:
                    value = variable[2]
                    break
            if value:
                result = self.first_value // value
                return result
            else:
                for variable in parser.symbol_table["main"]:
                    if variable[0] == self.second_value and variable[1] == int:
                        value = variable[2]
                        break
                if value:
                    result = self.first_value // value
                    return result
                else:
                    error = SemanticError(4, self.line)
                    error.process()

        elif isinstance(self.first_value, str) and isinstance(self.second_value, int):

            current_scope = parser.symbol_table[parser.current_scope]
            value = None
            for variable in current_scope:
                if variable[0] == self.first_value and variable[1] == int:
                    value = variable[2]
                    break
            if value:
                result = value // self.second_value
                return result
            else:
                for variable in parser.symbol_table["main"]:
                    if variable[0] == self.first_value and variable[1] == int:
                        value = variable[2]
                        break
                if value:
                    result = value // self.second_value
                    return result
                else:
                    error = SemanticError(4, self.line)
                    error.process()

        elif isinstance(self.first_value, str) and isinstance(self.second_value, str):

            current_scope = parser.symbol_table[parser.current_scope]
            value_1 = None
            value_2 = None
            for variable in current_scope:
                if variable[0] == self.first_value and variable[1] == int:
                    value_1 = variable[2]
                    break

            for variable in current_scope:
                if variable[0] == self.second_value and variable[1] == int:
                    value_2 = variable[2]
                    break

            if value_1 and value_2:
                result = value_1 // value_2
                return result
            else:
                for variable in parser.symbol_table["main"]:
                    if variable[0] == self.first_value and variable[1] == int:
                        value_1 = variable[2]
                        break
                for variable in parser.symbol_table["main"]:
                    if variable[0] == self.second_value and variable[1] == int:
                        value_2 = variable[2]
                        break
                if value_1 and value_2:
                    result = value_1 // value_2
                    return result
                else:
                    error = SemanticError(4, self.line)
                    error.process()


class Power:
    def __init__(self, x, y, line):
        self.first_value = x
        self.second_value = y
        self.line = line

    def calculate(self):
        if isinstance(self.first_value, int) and isinstance(self.second_value, int):
            result = self.first_value ** self.second_value
            print(result)
            return result
        elif isinstance(self.first_value, int) and isinstance(self.second_value, str):
            print("VALIDATION")
        elif isinstance(self.first_value, str) and isinstance(self.second_value, int):
            print("VALIDATION_02")
        elif isinstance(self.first_value, str) and isinstance(self.second_value,str):
            print("VALIDATION_03")


class Random:
    def __init__(self, x, line):
        self.start_value = x
        self.line = line

    def calculate(self):
        random = randint(0, self.start_value)
        print(random)
        return random
