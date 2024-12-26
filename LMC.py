#SM3201419 Francesco Carollo
import sys

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
            3: self.write_memory,
            5: self.accum_read_in,
            6: self.branch,
            7: self.branch_zero,
            8: self.branch_positive,
            901: self.accum_read_in,
            902: self.accum_add_out,
            0: self.halt
        }
    

    def add_input(self, value):
        if value < self.MIN_INPUT or value > self.MAX_INPUT:
            raise Exception("Input out of bounds")
        self.input.append(value)
        pass

    def read_input(self):
        return self.input.pop(0)
        pass
    
    def add_output(self, value):
        if value < self.MIN_INPUT or value > self.MAX_INPUT:
            raise Exception("Output out of bounds")
        self.output.append(value)
        pass

    def read_output(self):
        return self.output.pop(0)
        pass

    def accum_read_in(self, address):
        self.accumulatore = self.read_input(address)
        pass

    def accum_add_out(self):
        self.add_output(self.accumulatore)

    def read_memory(self, adress):
        if adress >= self.MEMORY_MAX or adress < self.MEMORY_MIN:
            raise Exception("Memory out of bounds")
        return self.memory[adress]
        pass

    def write_memory(self, adress):
        if adress >= self.MEMORY_MAX or adress < self.MEMORY_MIN:
            raise Exception("Memory out of bounds")
        self.memory[adress] = self.accumulatore
        pass

    def branch(self, adress):
        self.program_counter = adress
        pass
    
    def branch_zero(self, adress):
        if self.accumulatore == 0 & self.flag:
            self.program_counter = adress
        pass
    
    def branch_positive(self, adress):
        if self.flag:
            self.program_counter = adress
        pass

    def add(self, adress):
        self.accumulatore += self.read_memory(adress) % 1000
        if self.accumulatore >= 1000:
            self.falg = True
        pass

    def sub(self, adress):
        self.accumulatore -= self.read_memory(adress) % 1000
        if self.accumulatore >= 1000:
            self.flag = True
        pass

    def halt(self):
        exit(0)
        pass