#SM3201419 Francesco Carollo

class LMC:
    def __init__(self):
        self.MIN_INPUT = 0
        self.MAX_INPUT = 999
        self.input = []
        self.output = []
        self.MEMORY_MIN = 0
        self.MEMORY_MAX = 100
        self.memory = [0] * self.MEMORY_MAX
        self.accumulatore = 0
        self.program_counter = 0
        self.flag = False
        self.instructions = {
            1: self.add,
            2: self.sub,
            3: self.store,
            5: self.load,
            6: self.branch,
            7: self.branch_zero,
            8: self.branch_positive,
            901: self.porcodio,
            902: self.porcamadona,
            0: self.halt
        }

   
    def add_input(self, value):
        if value < self.MIN_INPUT or value > self.MAX_INPUT:
            raise Exception("Input out of bounds")
        self.input.append(value)

    def read_input(self):
        return self.input.pop(0)
    
    def porcodio(self):
        self.accumulatore = self.read_input(self)


    def add_output(self, value):
        if value < self.MIN_INPUT or value > self.MAX_INPUT:
            raise Exception("Output out of bounds")
        self.output.append(value)

    def read_output(self):
        return self.output.pop(0)
    
    def porcamadona(self):
        self.add_output(self.accumulatore)

    def read_memory(self, adress):
        if adress >= self.MEMORY_MAX or adress < self.MEMORY_MIN:
            raise Exception("Memory out of bounds")
        return self.memory[adress]

    def write_memory(self, adress, value):
        if adress >= self.MEMORY_MAX or adress < self.MEMORY_MIN:
            raise Exception("Memory out of bounds")
        self.memory[adress] = value

    