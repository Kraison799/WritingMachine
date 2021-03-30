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


class Sum:
    def __init__(self, x, y):
        self.first_value = x
        self.second_value = y

    def calculate(self):
        if isinstance(self.first_value, int) and isinstance(self.second_value, int):
            result = self.first_value + self.second_value
            print(result)
            return result
        elif isinstance(self.first_value, int) and isinstance(self.second_value, str):
            print("VALIDATION")
        elif isinstance(self.first_value, str) and isinstance(self.second_value, int):
            print("VALIDATION_02")
        elif isinstance(self.first_value, str) and isinstance(self.second_value,str):
            print("VALIDATION_03")


class Substr:
    def __init__(self, x, y):
        self.first_value = x
        self.second_value = y

    def calculate(self):
        if isinstance(self.first_value, int) and isinstance(self.second_value, int):
            result = self.first_value - self.second_value
            print(result)
            return result
        elif isinstance(self.first_value, int) and isinstance(self.second_value, str):
            print("VALIDATION")
        elif isinstance(self.first_value, str) and isinstance(self.second_value, int):
            print("VALIDATION_02")
        elif isinstance(self.first_value, str) and isinstance(self.second_value,str):
            print("VALIDATION_03")


class Mult:
    def __init__(self, x, y):
        self.first_value = x
        self.second_value = y

    def calculate(self):
        if isinstance(self.first_value, int) and isinstance(self.second_value, int):
            result = self.first_value * self.second_value
            print(result)
            return result
        elif isinstance(self.first_value, int) and isinstance(self.second_value, str):
            print("VALIDATION")
        elif isinstance(self.first_value, str) and isinstance(self.second_value, int):
            print("VALIDATION_02")
        elif isinstance(self.first_value, str) and isinstance(self.second_value,str):
            print("VALIDATION_03")


class Div:
    def __init__(self, x, y):
        self.first_value = x
        self.second_value = y

    def calculate(self):
        if isinstance(self.first_value, int) and isinstance(self.second_value, int):
            result = self.first_value // self.second_value
            print(result)
            return result
        elif isinstance(self.first_value, int) and isinstance(self.second_value, str):
            print("VALIDATION")
        elif isinstance(self.first_value, str) and isinstance(self.second_value, int):
            print("VALIDATION_02")
        elif isinstance(self.first_value, str) and isinstance(self.second_value,str):
            print("VALIDATION_03")


class Power:
    def __init__(self, x, y):
        self.first_value = x
        self.second_value = y

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
    def __init__(self, x):
        self.start_value = x

    def calculate(self):
        random = randint(0, self.start_value)
        print(random)
        return random
