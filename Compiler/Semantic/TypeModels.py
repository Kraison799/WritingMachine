# ------------------------------------------------------------
# File: Reserved.py
# Developed by: Kevin Barrantes Cerdas, Victor Castrillo
# Project: Writing Machine
# version: 0.1
#
# Description: Context free grammar for reserved functions
# in the Writing Machine language
# TEC 2021 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------

class BooleanValue:
    def __init__(self, value):
        self.value = value

    def validate(self):
        if self.value == "TRUE" or self.value == "FALSE":
            print(self.value)
            return self.value

