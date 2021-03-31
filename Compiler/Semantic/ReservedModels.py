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
from WritingMachine.Compiler.Semantic.TypeModels import *
from WritingMachine.Compiler.Semantic.OperationModels import *


class Def:
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def calculate(self):
        if isinstance(self.value, BooleanValue):
            # SYMBOL TABLE LOGIC
            print(self.id, self.value.value)
        if isinstance(self.value, int):
            print(self.id, self.value)

        if isinstance(self.value, str):
            print(self.id, self.value)
            # Possible pointer management

        if isinstance(self.value, Sum):
            sumResult = self.value.calculate()
            print(self.id, sumResult)

        if isinstance(self.value, Substr):
            subsResult = self.value.calculate()
            print(self.id, subsResult)

        if isinstance(self.value, Mult):
            multResult = self.value.calculate()
            print(self.id, multResult)

        if isinstance(self.value, Div):
            divResult = self.value.calculate()
            print(self.id, divResult)

        if isinstance(self.value, Random):
            randResult = self.value.calculate()
            print(self.id, randResult)

        if isinstance(self.value, Power):
            powResult = self.value.calculate()
            print(self.id, powResult)


class ContinueUp:
    def __init__(self, x):
        self.value = x

    def calculate(self):
        if isinstance(self.value, int):
            if self.value > 0:
                print("Continue up: " + str(self.value))
                return ["Y", self.value]

        elif isinstance(self.value, str):
            print("Continue up: " + self.value)

        elif isinstance(self.value, Sum):
            sumResult = self.value.calculate()
            if sumResult > 0:
                print("Continue up: " + str(sumResult))
                return ["Y", sumResult]

        elif isinstance(self.value, Substr):
            subsResult = self.value.calculate()
            if subsResult > 0:
                print("Continue up: " + str(subsResult))
                return ["Y", subsResult]

        elif isinstance(self.value, Mult):
            multResult = self.value.calculate()
            if multResult > 0:
                print("Continue up: " + str(multResult))
                return ["Y", multResult]

        elif isinstance(self.value, Div):
            divResult = self.value.calculate()
            if divResult > 0:
                print("Continue up: " + str(divResult))
                return ["Y", divResult]

        elif isinstance(self.value, Random):
            randResult = self.value.calculate()
            if randResult > 0:
                print("Continue up: " + str(randResult))
                return ["Y", randResult]

        elif isinstance(self.value, Power):
            powResult = self.value.calculate()
            if powResult > 0:
                print("Continue up: " + str(powResult))
                return ["Y", powResult]

        else:
            print("Err: Invalid input")
            return None


class ContinueDown:
    def __init__(self, x):
        self.value = x

    def calculate(self):
        if isinstance(self.value, int):
            if self.value > 0:
                print("Continue down: " + str(self.value * -1))
                return ["Y", self.value * -1]

        elif isinstance(self.value, str):
            print("Continue down: " + self.value)

        elif isinstance(self.value, Sum):
            sumResult = self.value.calculate()
            if sumResult > 0:
                print("Continue down: " + str(sumResult * -1))
                return ["Y", sumResult * -1]

        elif isinstance(self.value, Substr):
            subsResult = self.value.calculate()
            if subsResult > 0:
                print("Continue down: " + str(subsResult * -1))
                return ["Y", subsResult * -1]

        elif isinstance(self.value, Mult):
            multResult = self.value.calculate()
            if multResult > 0:
                print("Continue down: " + str(multResult * -1))
                return ["Y", multResult * -1]

        elif isinstance(self.value, Div):
            divResult = self.value.calculate()
            if divResult > 0:
                print("Continue down: " + str(divResult * -1))
                return ["Y", divResult * -1]

        elif isinstance(self.value, Random):
            randResult = self.value.calculate()
            if randResult > 0:
                print("Continue down: " + str(randResult * -1))
                return ["Y", randResult * -1]

        elif isinstance(self.value, Power):
            powResult = self.value.calculate()
            if powResult > 0:
                print("Continue down: " + str(powResult * -1))
                return ["Y", powResult * -1]

        else:
            print("Err: Invalid input")
            return None


class ContinueLeft:
    def __init__(self, x):
        self.value = x

    def calculate(self):
        if isinstance(self.value, int):
            if self.value > 0:
                print("Continue left: " + str(self.value * -1))
                return ["X", self.value * -1]

        elif isinstance(self.value, str):
            print("Continue left: " + self.value)

        elif isinstance(self.value, Sum):
            sumResult = self.value.calculate()
            if sumResult > 0:
                print("Continue left: " + str(sumResult * -1))
                return ["X", sumResult * -1]

        elif isinstance(self.value, Substr):
            subsResult = self.value.calculate()
            if subsResult > 0:
                print("Continue left: " + str(subsResult * -1))
                return ["X", subsResult * -1]

        elif isinstance(self.value, Mult):
            multResult = self.value.calculate()
            if multResult > 0:
                print("Continue left: " + str(multResult * -1))
                return ["X", multResult * -1]

        elif isinstance(self.value, Div):
            divResult = self.value.calculate()
            if divResult > 0:
                print("Continue left: " + str(divResult * -1))
                return ["X", divResult * -1]

        elif isinstance(self.value, Random):
            randResult = self.value.calculate()
            if randResult > 0:
                print("Continue left: " + str(randResult * -1))
                return ["X", randResult * -1]

        elif isinstance(self.value, Power):
            powResult = self.value.calculate()
            if powResult > 0:
                print("Continue left: " + str(powResult * -1))
                return ["X", powResult * -1]

        else:
            print("Err: Invalid input")
            return None


class ContinueRight:
    def __init__(self, x):
        self.value = x

    def calculate(self):
        if isinstance(self.value, int):
            if self.value > 0:
                print("Continue right: " + str(self.value))
                return ["X", self.value]

        elif isinstance(self.value, str):
            print("Continue right: " + self.value)

        elif isinstance(self.value, Sum):
            sumResult = self.value.calculate()
            if sumResult > 0:
                print("Continue right: " + str(sumResult))
                return ["X", sumResult]

        elif isinstance(self.value, Substr):
            subsResult = self.value.calculate()
            if subsResult > 0:
                print("Continue right: " + str(subsResult))
                return ["X", subsResult]

        elif isinstance(self.value, Mult):
            multResult = self.value.calculate()
            if multResult > 0:
                print("Continue right: " + str(multResult))
                return ["X", multResult]

        elif isinstance(self.value, Div):
            divResult = self.value.calculate()
            if divResult > 0:
                print("Continue right: " + str(divResult))
                return ["X", divResult]

        elif isinstance(self.value, Random):
            randResult = self.value.calculate()
            if randResult > 0:
                print("Continue right: " + str(randResult))
                return ["X", randResult]

        elif isinstance(self.value, Power):
            powResult = self.value.calculate()
            if powResult > 0:
                print("Continue right: " + str(powResult))
                return ["X", powResult]

        else:
            print("Err: Invalid input")
            return None


class Up:

    def calculate(self):
        result = ["u"]
        print("UP")
        return result


class Down:

    def calculate(self):
        result = ["d"]
        print("DOWN")
        return result


class Pos:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate(self):
        result = ["Pos", self.x, self.y]
        print(result)
        return result


class PosX:

    def __init__(self, x):
        self.x = x

    def calculate(self):
        result = ["X", self.x]
        print(result)
        return result


class PosY:

    def __init__(self, x):
        self.x = x

    def calculate(self):
        result = ["Y", self.x]
        print(result)
        return result


class UseColor:

    def __init__(self, x):
        self.x = x

    def calculate(self):

        if self.x == 1:
            print(["Color", "BLACK"])
            return ["Color", 'BLACK']
        if self.x == 2:
            print(["Color", "BLUE"])
            return ["Color", 'BLUE']
        if self.x == 3:
            print(["Color", "RED"])
            return ["Color", 'RED']
        else:
            print("Err: invalid value")
            return ["Err01"]


class Begin:

    def calculate(self):
        print([1, 1])
        return [1, 1]

class Speed:

    def __init__(self, x):
        self.x = x


    def calculate(self):
        print(["Speed", self.x])
        return ["Speed", self.x]


class And:

    def __init__(self,x,y):
        self.x = x
        self.y = y


    def calculate(self):
        if isinstance(self.x,BooleanValue) and isinstance(self.y, BooleanValue):
            if self.x.value == "TRUE" and self.y.value == "TRUE":
                print("TRUE")
                return BooleanValue("TRUE")
            else:
                print("FALSE")
                return BooleanValue("FALSE")
        else:
            first_value = self.x.calculate()
            second_value = self.y.calculate()
            if first_value.value == "TRUE" and second_value.value == "TRUE":
                print("TRUE")
                return BooleanValue("TRUE")
            else:
                print("FALSE")
                return BooleanValue("FALSE")