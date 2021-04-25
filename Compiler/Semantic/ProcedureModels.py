
class Procedure:

    def __init__(self, id, arguments, statements):
        self.id = id
        self.arguments = arguments
        self.statements = statements


class Run:

    def __init__(self, sequence):
        self.sequence = sequence

    def calculate(self):
        return self.sequence


class Repeat:

    def __init__(self, times, sequence, line):
        self.times = times
        self.sequence = sequence
        self.line = line
        self.count = 0

    def calculate(self):
        if self.count <\
                self.times:
            self.count += 1
            return self.sequence
        else:
            return None


class Chain:

    def __init__(self):
        self.chain = []

    def __del__(self):
        self.chain = []

