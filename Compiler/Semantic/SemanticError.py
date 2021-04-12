import sys


class SemanticError:

    def __init__(self, code, line = 0):
        self.code = code
        self.line = line

    def process(self):

        if self.code == 0:
            print("SEMANTIC ERROR 0. SYNTAX INCORRECT")
            sys.exit(1)
        if self.code == 1:
            print("SEMANTIC ERROR: NO MAIN PROCEDURE DECLARED")
            sys.exit(1)
        if self.code == 2:
            print("SEMANTIC ERROR: MULTIPLE MAIN PROCEDURES DECLARED")
            sys.exit(1)
        if self.code == 3:
            print("SEMANTIC ERROR IN LINE " + str(self.line) + ": VARIABLE ALREADY DECLARED")
            #MANDAR AL IDE
            sys.exit(1)
        if self.code == 4:
            print("SEMANTIC ERROR IN LINE " + str(self.line) + ": NO SUCH VARIABLE OF INT TYPE EXIST")
            sys.exit(1)
        if self.code == 5:
            print("SEMANTIC ERROR IN LINE " + str(self.line) + ": TYPE ASSIGNATION ERROR")
            sys.exit(1)
        if self.code == 6:
            print("SEMANTIC ERROR IN LINE " + str(self.line) + ": VARIABLE DOES NOT EXIST")
            # sys.exit(1)
        if self.code == 7:
            print("SEMANTIC ERROR IN LINE " + str(self.line) + ": GLOBAL VARIABLE DOES NOT EXIST")
            # sys.exit(1)
        if self.code == 8:
            print("SEMANTIC ERROR IN LINE " + str(self.line) + ": MAXIMUM RECURSION EXCEEDED")
            sys.exit(1)


