
class Procedure:

    def __init__(self, id, arguments, statements):
        self.id = id
        self.arguments = arguments
        self.statements = statements


class Run:

    def __init__(self, sequence):
        self.sequence = sequence


class Repeat:

    def __init__(self, times, sequence):
        self.times = times
        self.sequence = sequence


class Chain:

    def __init__(self):
        self.chain = []

