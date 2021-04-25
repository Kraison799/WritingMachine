
import sys

from WritingMachine.Compiler.ErrorLog import ErrorLog
from WritingMachine.Compiler.Syntactic import Parser as parser



class SemanticError:

    def __init__(self, code, line = 0):
        self.code = code
        self.line = line
        self.error = ErrorLog()

    def process(self):

        if self.code == 0:
            err_message = "SEMANTIC ERROR 0. SYNTAX INCORRECT"
            parser.semantic_err = True
            self.error.log_error(err_message)

        if self.code == 1:
            parser.symbol_table.clear()
            err_message = "SEMANTIC ERROR: NO MAIN PROCEDURE DECLARED"
            parser.semantic_err = True
            self.error.log_error(err_message)

        if self.code == 2:
            parser.symbol_table.clear()
            err_message = "SEMANTIC ERROR: MULTIPLE MAIN PROCEDURES DECLARED"
            parser.semantic_err = True
            self.error.log_error(err_message)

        if self.code == 2.1:
            parser.symbol_table.clear()
            err_message = "SEMANTIC ERROR: MAIN CANNOT RECEIVE PARAMETERS"
            parser.semantic_err = True
            self.error.log_error(err_message)
        if self.code == 3:
            err_message = "SEMANTIC ERROR IN LINE " + str(self.line) + ": VARIABLE ALREADY DECLARED"
            parser.semantic_err = True
            self.error.log_error(err_message)
        if self.code == 4:
            err_message = "SEMANTIC ERROR IN LINE " + str(self.line) + ": NO SUCH VARIABLE OF INT TYPE EXIST"
            parser.semantic_err = True
            self.error.log_error(err_message)
        if self.code == 5:
            print("SEMANTIC ERROR IN LINE " + str(self.line) + ": TYPE ASSIGNATION ERROR")
            parser.semantic_err = True
        if self.code == 6:
            err_message = "SEMANTIC ERROR IN LINE " + str(self.line) + ": VARIABLE DOES NOT EXIST"
            parser.semantic_err = True
            self.error.log_error(err_message)
        if self.code == 7:
            err_message = "SEMANTIC ERROR IN LINE " + str(self.line) + ": GLOBAL VARIABLE DOES NOT EXIST"
            parser.semantic_err = True
            self.error.log_error(err_message)
        if self.code == 8:
            err_message = "SEMANTIC ERROR IN LINE " + str(self.line) + ": MAXIMUM RECURSION EXCEEDED"
            parser.semantic_err = True
            self.error.log_error(err_message)
        if self.code == 9:
            parser.symbol_table.clear()
            err_message = "SEMANTIC ERROR" + ": DUPLICATE PROCEDURE SIGNATURE"
            parser.semantic_err = True
            self.error.log_error(err_message)


