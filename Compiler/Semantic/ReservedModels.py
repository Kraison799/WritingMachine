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
from Compiler.Gcode import gcode
from Compiler.Semantic.SemanticError import SemanticError
from Compiler.Semantic.TypeModels import *
from Compiler.Semantic.OperationModels import *
from Compiler.Syntactic import Parser as parser



class Def:
    def __init__(self, id, value, line):
        self.id = id
        self.value = value
        self.line = line

    def calculate(self):

        if isinstance(self.value, BooleanValue):
            if self.value.value == "TRUE":
                self.value = True
            else:
                self.value = False
            return [self.id, bool, self.value]

        if isinstance(self.value, int):
            return [self.id, int, self.value]

        if isinstance(self.value, str):
            value = None
            var_type = None
            for variable in parser.symbol_table[parser.current_scope]:
                if self.value in variable:
                    value = variable[2]
                    var_type = variable[1]
                    break
            if value:
                return [self.id, var_type, value]
            else:
                for variable in parser.symbol_table["main"]:
                    if self.value in variable:
                        value = variable[2]
                        var_type = variable[1]
                        break
                if value:
                    return [self.id, var_type, value]
                else:
                    error = SemanticError(4)
                    error.process()



        if isinstance(self.value, Sum):
            sumResult = self.value.calculate()
            return [self.id, int, sumResult]

        if isinstance(self.value, Substr):
            subsResult = self.value.calculate()
            return [self.id, int, subsResult]

        if isinstance(self.value, Mult):
            multResult = self.value.calculate()
            return [self.id, int, multResult]

        if isinstance(self.value, Div):
            divResult = self.value.calculate()
            return [self.id, int, divResult]

        if isinstance(self.value, Random):
            randResult = self.value.calculate()
            return [self.id, int, randResult]

        if isinstance(self.value, Power):
            powResult = self.value.calculate()
            return [self.id, int, powResult]



class Put:
    def __init__(self, id, value, line, glovar = False):
        self.id = id
        self.value = value
        self.line = line
        self.glovar = glovar

    def calculate(self):
        found = False
        if isinstance(self.value, BooleanValue):
            if self.value.value == "TRUE":
                self.value = True
            else:
                self.value = False

            if self.glovar:
                for variable in parser.symbol_table["main"]:
                    if self.id == variable[0]:
                        found = True
                        if variable[1] == bool:
                            variable[2] = self.value
                        else:
                            error = SemanticError(5, self.line)
                            error.process()
                if found:
                    return
                else:
                    error = SemanticError(7, self.line)
                    error.process()

            for variable in parser.symbol_table[parser.current_scope]:
                if self.id == variable[0]:
                    found = True
                    if variable[1] == bool:
                        variable[2] = self.value
                    else:
                        error = SemanticError(5, self.line)
                        error.process()
            if found:
                return
            else:
                for variable in parser.symbol_table["main"]:
                    if self.id == variable[0]:
                        found = True
                        if variable[1] == bool:
                            variable[2] = self.value
                        else:
                            error = SemanticError(5, self.line)
                            error.process()
                if found:
                    return
                else:
                    error = SemanticError(6, self.line)
                    error.process()

        if isinstance(self.value, int):

            if self.glovar:
                for variable in parser.symbol_table["main"]:
                    if self.id == variable[0]:
                        found = True
                        if variable[1] == int:
                            variable[2] = self.value
                        else:
                            error = SemanticError(5, self.line)
                            error.process()
                if found:
                    return
                else:
                    error = SemanticError(7, self.line)
                    error.process()

            for variable in parser.symbol_table[parser.current_scope]:
                if self.id == variable[0]:
                    found = True
                    if variable[1] == int:
                        variable[2] = self.value
                    else:
                        error = SemanticError(5, self.line)
                        error.process()
            if found:
                return
            else:
                for variable in parser.symbol_table["main"]:
                    if self.id == variable[0]:
                        found = True
                        if variable[1] == int:
                            variable[2] = self.value
                        else:
                            error = SemanticError(5, self.line)
                            error.process()
                if found:
                    return
                else:
                    error = SemanticError(6, self.line)
                    error.process()

        if isinstance(self.value, Sum):
            sumResult = self.value.calculate()
            self.value = sumResult
            self.calculate()

        if isinstance(self.value, Substr):
            subsResult = self.value.calculate()
            self.value = subsResult
            self.calculate()

        if isinstance(self.value, Mult):
            multResult = self.value.calculate()
            self.value = multResult
            self.calculate()

        if isinstance(self.value, Div):
            divResult = self.value.calculate()
            self.value = divResult
            self.calculate()

        if isinstance(self.value, Random):
            randResult = self.value.calculate()
            self.value = randResult
            self.calculate()

        if isinstance(self.value, Power):
            powResult = self.value.calculate()
            self.value = powResult
            self.calculate()


class AddSimple:
    def __init__(self, id, line, glovar = False):
        self.id = id
        self.line = line
        self.glovar = glovar

    def calculate(self):
        found = False
        if self.glovar:
            for variable in parser.symbol_table["main"]:
                if self.id == variable[0]:
                    if variable[1] == int:
                        variable[2] += 1
                        found = True
                        break
                    else:
                        error = SemanticError(5, self.line)
                        error.process()
            if found:
                return
            else:
                error = SemanticError(7, self.line)
                error.process()
        else:
            for variable in parser.symbol_table[parser.current_scope]:
                if self.id == variable[0]:
                    if variable[1] == int:
                        variable[2] += 1
                        found = True
                        break
                    else:
                        error = SemanticError(5, self.line)
                        error.process()
            if found:
                return
            else:
                for variable in parser.symbol_table["main"]:
                    if self.id == variable[0]:
                        if variable[1] == int:
                            variable[2] += 1
                            found = True
                            break
                        else:
                            error = SemanticError(5, self.line)
                            error.process()
                if found:
                    return
                else:
                    error = SemanticError(7, self.line)
                    error.process()

class AddInt:
    def __init__(self, id, value, line, glovar = False):
        self.id = id
        self.value = value
        self.line = line
        self.glovar = glovar

    def calculate(self):
        found = False
        if self.glovar:
            for variable in parser.symbol_table["main"]:
                if self.id == variable[0]:
                    if variable[1] == int:
                        variable[2] += self.value
                        found = True
                        break
                    else:
                        error = SemanticError(5, self.line)
                        error.process()
            if found:
                return
            else:
                error = SemanticError(7, self.line)
                error.process()
        else:
            for variable in parser.symbol_table[parser.current_scope]:
                if self.id == variable[0]:
                    if variable[1] == int:
                        variable[2] += self.value
                        found = True
                        break
                    else:
                        error = SemanticError(5, self.line)
                        error.process()
            if found:
                return
            else:
                for variable in parser.symbol_table["main"]:
                    if self.id == variable[0]:
                        if variable[1] == int:
                            variable[2] += self.value
                            found = True
                            break
                        else:
                            error = SemanticError(5, self.line)
                            error.process()
                if found:
                    return
                else:
                    error = SemanticError(7, self.line)
                    error.process()


class ContinueUp:
    def __init__(self, x, line):
        self.value = x
        self.line = line

    def calculate(self):
        if isinstance(self.value, int):
            if self.value > 0:
                print("Continue up: " + str(self.value))
                gt = gcode()
                gt.moverypositivo(self.value)
                return ["Y", self.value]

        elif isinstance(self.value, str):
            print("Continue up: " + str(self.get_var(self.value)))
            gt = gcode()
            gt.moverypositivo(self.get_var(self.value))


        elif isinstance(self.value, Sum):
            sumResult = self.value.calculate()
            if sumResult > 0:
                print("Continue up: " + str(sumResult))
                gt = gcode()
                gt.moverypositivo(sumResult)
                return ["Y", sumResult]

        elif isinstance(self.value, Substr):
            subsResult = self.value.calculate()
            if subsResult > 0:
                print("Continue up: " + str(subsResult))
                gt = gcode()
                gt.moverypositivo(subsResult)
                return ["Y", subsResult]

        elif isinstance(self.value, Mult):
            multResult = self.value.calculate()
            if multResult > 0:
                print("Continue up: " + str(multResult))
                gt = gcode()
                gt.moverypositivo(multResult)
                return ["Y", multResult]

        elif isinstance(self.value, Div):
            divResult = self.value.calculate()
            if divResult > 0:
                print("Continue up: " + str(divResult))
                gt = gcode()
                gt.moverypositivo(divResult)
                return ["Y", divResult]

        elif isinstance(self.value, Random):
            randResult = self.value.calculate()
            if randResult > 0:
                print("Continue up: " + str(randResult))
                gt = gcode()
                gt.moverypositivo(randResult)
                return ["Y", randResult]

        elif isinstance(self.value, Power):
            powResult = self.value.calculate()
            if powResult > 0:
                print("Continue up: " + str(powResult))
                gt = gcode()
                gt.moverypositivo(powResult)
                return ["Y", powResult]

        else:
            print("Err: Invalid input")
            return None

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


class ContinueDown:
    def __init__(self, x, line):
        self.value = x
        self.line = line

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

    def calculate(self):
        if isinstance(self.value, int):
            if self.value > 0:
                print("Continue down: " + str(self.value * -1))
                gt = gcode()
                gt.moverynegativo(self.value)
                return ["Y", self.value * -1]

        elif isinstance(self.value, str):
            print("Continue down: " + str(self.get_var(self.value)))
            gt = gcode()
            gt.moverynegativo(self.get_var(self.value))

        elif isinstance(self.value, Sum):
            sumResult = self.value.calculate()
            if sumResult > 0:
                print("Continue down: " + str(sumResult * -1))
                gt = gcode()
                gt.moverynegativo(sumResult)
                return ["Y", sumResult * -1]

        elif isinstance(self.value, Substr):
            subsResult = self.value.calculate()
            if subsResult > 0:
                print("Continue down: " + str(subsResult * -1))
                gt = gcode()
                gt.moverynegativo(subsResult)
                return ["Y", subsResult * -1]

        elif isinstance(self.value, Mult):
            multResult = self.value.calculate()
            if multResult > 0:
                print("Continue down: " + str(multResult * -1))
                gt = gcode()
                gt.moverynegativo(multResult)
                return ["Y", multResult * -1]

        elif isinstance(self.value, Div):
            divResult = self.value.calculate()
            if divResult > 0:
                print("Continue down: " + str(divResult * -1))
                gt = gcode()
                gt.moverynegativo(divResult)
                return ["Y", divResult * -1]

        elif isinstance(self.value, Random):
            randResult = self.value.calculate()
            if randResult > 0:
                print("Continue down: " + str(randResult * -1))
                gt = gcode()
                gt.moverynegativo(randResult)
                return ["Y", randResult * -1]

        elif isinstance(self.value, Power):
            powResult = self.value.calculate()
            if powResult > 0:
                print("Continue down: " + str(powResult * -1))
                gt = gcode()
                gt.moverynegativo(powResult)
                return ["Y", powResult * -1]

        else:
            print("Err: Invalid input")
            return None


class ContinueLeft:
    def __init__(self, x, line):
        self.value = x
        self.line = line

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

    def calculate(self):
        if isinstance(self.value, int):
            if self.value > 0:
                print("Continue left: " + str(self.value * -1))
                gt = gcode()
                gt.moverXnegativo(self.value)
                return ["X", self.value * -1]

        elif isinstance(self.value, str):
            print("Continue left: " + str(self.get_var(self.value)))
            gt = gcode()
            gt.moverXnegativo(self.get_var(self.value))

        elif isinstance(self.value, Sum):
            sumResult = self.value.calculate()
            if sumResult > 0:
                print("Continue left: " + str(sumResult * -1))
                gt = gcode()
                gt.moverXnegativo(sumResult)
                return ["X", sumResult * -1]

        elif isinstance(self.value, Substr):
            subsResult = self.value.calculate()
            if subsResult > 0:
                print("Continue left: " + str(subsResult * -1))
                gt = gcode()
                gt.moverXnegativo(subsResult)
                return ["X", subsResult * -1]

        elif isinstance(self.value, Mult):
            multResult = self.value.calculate()
            if multResult > 0:
                print("Continue left: " + str(multResult * -1))
                gt = gcode()
                gt.moverXnegativo(multResult)
                return ["X", multResult * -1]

        elif isinstance(self.value, Div):
            divResult = self.value.calculate()
            if divResult > 0:
                print("Continue left: " + str(divResult * -1))
                gt = gcode()
                gt.moverXnegativo(divResult)
                return ["X", divResult * -1]

        elif isinstance(self.value, Random):
            randResult = self.value.calculate()
            if randResult > 0:
                print("Continue left: " + str(randResult * -1))
                gt = gcode()
                gt.moverXnegativo(randResult)
                return ["X", randResult * -1]

        elif isinstance(self.value, Power):
            powResult = self.value.calculate()
            if powResult > 0:
                print("Continue left: " + str(powResult * -1))
                gt = gcode()
                gt.moverXnegativo(powResult)
                return ["X", powResult * -1]

        else:
            print("Err: Invalid input")
            return None


class ContinueRight:
    def __init__(self, x, line):
        self.value = x
        self.line = line

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


    def calculate(self):
        if isinstance(self.value, int):
            if self.value > 0:
                print("Continue right: " + str(self.value))
                gt = gcode()
                gt.moverXpositivo(self.value)
                return ["X", self.value]

        elif isinstance(self.value, str):
            print("Continue right: " + str(self.get_var(self.value)))
            gt = gcode()
            gt.moverXpositivo(self.get_var(self.value))

        elif isinstance(self.value, Sum):
            sumResult = self.value.calculate()
            if sumResult > 0:
                print("Continue right: " + str(sumResult))
                gt = gcode()
                gt.moverXpositivo(sumResult)
                return ["X", sumResult]

        elif isinstance(self.value, Substr):
            subsResult = self.value.calculate()
            if subsResult > 0:
                print("Continue right: " + str(subsResult))
                gt = gcode()
                gt.moverXpositivo(subsResult)
                return ["X", subsResult]

        elif isinstance(self.value, Mult):
            multResult = self.value.calculate()
            if multResult > 0:
                print("Continue right: " + str(multResult))
                gt = gcode()
                gt.moverXpositivo(multResult)
                return ["X", multResult]

        elif isinstance(self.value, Div):
            divResult = self.value.calculate()
            if divResult > 0:
                print("Continue right: " + str(divResult))
                gt = gcode()
                gt.moverXpositivo(divResult)
                return ["X", divResult]

        elif isinstance(self.value, Random):
            randResult = self.value.calculate()
            if randResult > 0:
                print("Continue right: " + str(randResult))
                gt = gcode()
                gt.moverXpositivo(randResult)
                return ["X", randResult]

        elif isinstance(self.value, Power):
            powResult = self.value.calculate()
            if powResult > 0:
                print("Continue right: " + str(powResult))
                gt = gcode()
                gt.moverXpositivo(powResult)
                return ["X", powResult]

        else:
            print("Err: Invalid input")
            return None


class Up:

    def calculate(self):
        result = ["u"]
        print("UP")
        gt = gcode()
        gt.subir()
        return result


class Down:

    def calculate(self):
        result = ["d"]
        print("DOWN")
        gt = gcode()
        gt.bajar()
        return result


class Pos:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate(self):
        result = ["Pos", self.x, self.y]
        print(result)
        gt = gcode()
        gt.posxy(self.x,self.y)
        return result


class PosX:

    def __init__(self, x):
        self.x = x

    def calculate(self):
        result = ["X", self.x]
        print(result)
        gt = gcode()
        gt.posx(self.x)
        return result


class PosY:

    def __init__(self, x):
        self.x = x

    def calculate(self):
        result = ["Y", self.x]
        print(result)
        gt = gcode()
        gt.posy(self.x)
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
        gt = gcode()
        gt.puntosIniciales()
        return [1, 1]

class Speed:

    def __init__(self, x):
        self.x = x


    def calculate(self):
        print(["Speed", self.x])
        gt = gcode()
        gt.velocidad(self.x)
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


class Or:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def calculate(self):
        if isinstance(self.x, BooleanValue) and isinstance(self.y, BooleanValue):
            if self.x.value == "TRUE" or self.y.value == "TRUE":
                print("TRUE")
                return BooleanValue("TRUE")
            else:
                print("FALSE")
                return BooleanValue("FALSE")
        else:
            first_value = self.x.calculate()
            second_value = self.y.calculate()
            if first_value.value == "TRUE" or second_value.value == "TRUE":
                print("TRUE")
                return BooleanValue("TRUE")
            else:
                print("FALSE")
                return BooleanValue("FALSE")
