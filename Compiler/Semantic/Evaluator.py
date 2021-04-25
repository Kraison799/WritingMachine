import sys
import copy
from WritingMachine.Compiler.Semantic.OrderModels import Sequence, Def, WritingIf, WritingIfElse, WritingWhile
from WritingMachine.Compiler.Semantic.ProcedureModels import Chain, Procedure, Repeat, Run
from WritingMachine.Compiler.Semantic.ReservedModels import Put, AddSimple, AddInt, ContinueUp, ContinueDown, \
    ContinueLeft, ContinueRight, Pos, PosX, PosY, Up, Down, Speed, Begin
from WritingMachine.Compiler.Syntactic import Parser as parser
from WritingMachine.Compiler.Semantic.SemanticError import SemanticError


class Evaluate:

    def __init__(self, ast):
        self.ast = ast
        self.procedures = None
        self.main = None
        self.error = SemanticError(0)

    def __del__(self):
        self.ast = None
        self.procedures = None
        self.main = None
        self.error = SemanticError(0)


    def get_procedures(self):

        if self.ast:
            self.procedures = self.ast.chain
        else:
            self.error.process()

        if self.procedures:
            main_count = 0
            for procedure in self.procedures:
                if procedure.id == "main":
                    if procedure.arguments != []:
                        self.error = SemanticError(2.1)
                        self.error.process()
                    else:
                        main_count += 1
                        parser.symbol_table[procedure.id] = []
                        self.main = copy.deepcopy(procedure)
                        self.procedures.remove(procedure)


            if main_count == 0:
                self.error = SemanticError(1)
                self.error.process()
            elif main_count > 1:
                self.error = SemanticError(2)
                self.error.process()
            else:

                for procedure in self.procedures:
                    print("Evaluating procedure " + procedure.id)
                    parser.symbol_table[procedure.id] = []
                    print(parser.symbol_table)
                    # arg_amount = len(procedure.arguments)
                    # proc_name = procedure.id+str(arg_amount)
                    # print("evaluating proc name: ", proc_name)
                    # if proc_name in parser.symbol_table:
                    #     self.error = SemanticError(9)
                    #     self.error.process()
                    #     print(parser.symbol_table)
                    # else:
                    #     procedure.id = proc_name
                    #     parser.symbol_table[proc_name] = []
                    #     print(parser.symbol_table)
                    return 1


    def start(self):
        procedures = self.get_procedures()
        if procedures == 1:
            self.evaluate("start")


    def evaluate(self, element):

        if element == "start":
            self.evaluate(self.main)
            for procedure in self.procedures:
                self.evaluate(procedure)


        if isinstance(element, Procedure):
            parser.current_scope = element.id
            statements = element.statements
            for chunk in statements:
                self.evaluate(chunk)

        if isinstance(element, Sequence):
            actions = element.actions
            for action in actions:
                self.evaluate(action)

        if isinstance(element, Def):
            solve = element.calculate()
            if len(parser.symbol_table[parser.current_scope]) > 0:
                for variable in parser.symbol_table[parser.current_scope]:
                    if solve[0] in variable:
                        line = str(element.line)
                        self.error = SemanticError(3, line)
                        self.error.process()

                parser.symbol_table[parser.current_scope].append(solve)
                print(parser.symbol_table)

            else:
                parser.symbol_table[parser.current_scope].append(solve)
                print(parser.symbol_table)

        if isinstance(element, Put):
            solve = element.calculate()
            print(parser.symbol_table)

        if isinstance(element, AddSimple):
            solve = element.calculate()
            print(parser.symbol_table)

        if isinstance(element, AddInt):
            solve = element.calculate()
            print(parser.symbol_table)

        if isinstance(element, WritingIf):
            solve = element.calculate()
            self.evaluate(solve)
            print(parser.symbol_table)

        if isinstance(element, WritingIfElse):
            solve = element.calculate()
            self.evaluate(solve)
            print(parser.symbol_table)

        if isinstance(element, WritingWhile):
            solve = element.calculate()
            if isinstance(solve, Sequence):
                self.evaluate(solve)
                self.evaluate(element)

        if isinstance(element, Repeat):
            solve = element.calculate()
            if isinstance(solve, Sequence):
                self.evaluate(solve)
                self.evaluate(element)

        if isinstance(element, Run):
            solve = element.calculate()
            if solve:
                self.evaluate(solve)

        if isinstance(element, ContinueUp):
            solve = element.calculate()

        if isinstance(element, ContinueDown):
            solve = element.calculate()

        if isinstance(element, ContinueLeft):
            solve = element.calculate()

        if isinstance(element, ContinueRight):
            solve = element.calculate()

        if isinstance(element, Pos):
            solve = element.calculate()

        if isinstance(element, PosX):
            solve = element.calculate()

        if isinstance(element, PosY):
            solve = element.calculate()

        if isinstance(element, Up):
            solve = element.calculate()

        if isinstance(element, Down):
            solve = element.calculate()

        if isinstance(element, Begin):
            solve = element.calculate()

        if isinstance(element, Speed):
            solve = element.calculate()









