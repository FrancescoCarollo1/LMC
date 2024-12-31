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
            9: self.Input_Output
        }
    
    def Addizione(self, address):
        print(f"ADD: accumulatore <- {self.accumulatore}+{self.memory[address]}")        
        self.accumulatore += self.memory[address]
        self.flag = self.accumulatore >= VALUE_MAX
        self.accumulatore %= VALUE_MAX
        
    def Sottrazione(self, address):
        print(f"SUB: accumulatore <- {self.accumulatore}-{self.memory[address]}")        
        self.accumulatore -= self.memory[address]
        self.flag = self.accumulatore < VALUE_MIN
        self.accumulatore %= VALUE_MAX
        
        
    def Store(self, address):
        print(f"STA: mem[{address}] <- {self.accumulatore}")        
        self.memory[address] = self.accumulatore

    def Load(self, address):
        print(f"LDA: accumulatore <- {self.memory[address]}")
        self.accumulatore = self.memory[address]
        

    def Branch(self, address):
        print(f"BRA: program counter <- {address}")
        self.program_counter = address
        
    
    def Branch_if_zero(self, address):

        if self.accumulatore == 0 and not self.flag:
            print(f"BRZ: program counter <- {address}")
            self.program_counter = address
        else:
            print(f"BRZ: skipped")
        
    
    def Branch_if_positive(self, address):
        if not self.flag:
            print(f"BRP: program counter <- {address}")
            self.program_counter = address
        else:
            print(f"BRP: skipped")
        

    def Input_Output(self, address):
        if address == 1:
            print(f"INP: accumulatore <- {self.input[0]}")
            if VALUE_MIN > self.input[0] or self.input[0] >= VALUE_MAX:
                raise ValueError("Input out of range")
            self.accumulatore = self.input.pop(0)
        elif address == 2:
            print(f"OUT <- {self.accumulatore}") 
            self.output.append(self.accumulatore)

        else:
            raise ValueError("Invalid instruction")
        

    def load_memory(self, machine_code):
        self.memory = machine_code

    def run(self):
        while True:
            opcode = self.memory[self.program_counter] // 100
            operand = self.memory[self.program_counter] % 100
            pre = self.program_counter
            if opcode == 0:
                break

            if opcode == 4:
                raise ValueError("Invalid instruction")

            self.instructions[opcode](operand)
            
            if pre == self.program_counter:
                self.program_counter += 1
                
            self.program_counter %= MEMORY_MAX
            
            
           
        