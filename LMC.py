#SM3201419 Francesco Carollo
import sys

VALUE_MIN = 0
VALUE_MAX = 1000
MEMORY_MIN = 0
MEMORY_MAX = 100

class LMC:
    def __init__(self):
       
        self.input = []
        self.output = []
        self.memory = [0] * MEMORY_MAX
        self.accumulatore = 0
        self.program_counter = 0
        self.flag = False
        self.instructions = {
            1: self.Addizione,
            2: self.Sottrazione,
            3: self.Store,
            5: self.Load,
            6: self.Branch,
            7: self.Branch_if_zero,
            8: self.Branch_if_positive,
            9: self.Input_Output,
        }
    
    def Addizione(self, address):
        self.accumulatore += self.memory[address]
        self.flag = self.accumulatore >= VALUE_MAX
        self.accumulatore %= VALUE_MAX
        
        
    def Sottrazione(self, address):
        self.accumulatore -= self.memory[address]
        self.flag = self.accumulatore <= VALUE_MIN
        self.accumulatore %= VALUE_MAX
        
        
    def Store(self, address):
        self.memory[address] = self.accumulatore
        

    def Load(self, address):
        self.accumulatore = self.memory[address]
        

    def Branch(self, address):
        self.program_counter = address
        
    
    def Branch_if_zero(self, address):
        if self.accumulatore == 0 and not self.flag:
            self.program_counter = address
        
    
    def Branch_if_positive(self, address):
        if not self.flag:
            self.program_counter = address
        

    def Input_Output(self, address):
        if address == 1:
            if VALUE_MIN >= self.input[0] or self.input[0] >= VALUE_MAX:
                raise ValueError("Input out of range")
            self.accumulatore = self.input.pop(0)
        elif address == 2: 
            self.output.append(self.accumulatore)

        else:
            raise ValueError("Invalid instruction")

    def load_memory(self, machine_code):
        self.memory = machine_code

    def run(self):
        while True:
            opcode = self.memory[self.program_counter] // 100
            operand = self.memory[self.program_counter] % 100
            print("Eseguendo istruzione: ", opcode, operand)
            print(f"PC: {self.program_counter}, ACC: {self.accumulatore}, MEM: {self.memory}")
            if opcode == 0:
                break
            pre = self.program_counter

            self.instructions[opcode](operand)
            
            if pre == self.program_counter:
                self.program_counter += 1
                
            self.program_counter %= MEMORY_MAX
            
            
           
        