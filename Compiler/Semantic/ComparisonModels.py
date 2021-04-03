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
from WritingMachine.Compiler.Semantic.TypeModels import *


class Smaller:
    def __init__(self, x, y):
        self.first_value = x
        self.second_value = y

    def calculate(self):
        if self.first_value < self.second_value:
            print("TRUE")
            return BooleanValue("TRUE")
        else:
            print("FALSE")
            return BooleanValue("FALSE")


class Equal:
    def __init__(self, x, y):
        self.first_value = x
        self.second_value = y

    def calculate(self):
        if self.first_value == self.second_value:
            print("TRUE")
            return BooleanValue("TRUE")
        else:
            print("FALSE")
            return BooleanValue("FALSE")


class Greater:
    def __init__(self, x, y):
        self.first_value = x
        self.second_value = y

    def calculate(self):
        if self.first_value > self.second_value:
            print("TRUE")
            return BooleanValue("TRUE")
        else:
            print("FALSE")
            return BooleanValue("FALSE")
