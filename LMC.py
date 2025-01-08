# Francesco Carollo SM3201419

import logging
logger = logging.getLogger("LMC")

# Input and accumulator value range
VALUE_MIN = 0
VALUE_MAX = 1000

MEM_SIZE = 100

class LMC:
    def __init__(self):
       
        self.input = []
        self.output = []
        self.memory = [0] * MEM_SIZE
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
        logger.debug(f"ADD: accumulatore <- {self.accumulatore}+{self.memory[address]}")        
        self.accumulatore += self.memory[address]
        self.flag = self.accumulatore >= VALUE_MAX
        self.accumulatore %= VALUE_MAX
        
    def Sottrazione(self, address):
        logger.debug(f"SUB: accumulatore <- {self.accumulatore}-{self.memory[address]}")        
        self.accumulatore -= self.memory[address]
        self.flag = self.accumulatore < VALUE_MIN
        self.accumulatore %= VALUE_MAX
            
    def Store(self, address):
        logger.debug(f"STA: mem[{address}] <- {self.accumulatore}")        
        self.memory[address] = self.accumulatore

    def Load(self, address):
        logger.debug(f"LDA: accumulatore <- {self.memory[address]}")
        self.accumulatore = self.memory[address]
        
    def Branch(self, address):
        logger.debug(f"BRA: program counter <- {address}")
        self.program_counter = address
    
    def Branch_if_zero(self, address):
        if self.accumulatore == 0 and not self.flag:
            logger.debug(f"BRZ: program counter <- {address}")
            self.program_counter = address
        else:
            logger.debug(f"BRZ: Continue")
        
    
    def Branch_if_positive(self, address):
        if not self.flag:
            logger.debug(f"BRP: program counter <- {address}")
            self.program_counter = address
        else:
            logger.debug(f"BRP: Continue")
        
    #  Questa funzione gestisce sia Input che Output
    def Input_Output(self, operand):    
        if operand == 1:
            logger.debug(f"INP: accumulatore <- {self.input[0]}")
            if VALUE_MIN > self.input[0] or self.input[0] >= VALUE_MAX:
                raise ValueError("Input out of range")
            self.accumulatore = self.input.pop(0)

        elif operand == 2:
            logger.debug(f"OUT: <- {self.accumulatore}") 
            self.output.append(self.accumulatore)

        else:
            raise ValueError("Invalid instruction")
        

    def run(self, interactive):
        while True:
            opcode = int(f'{self.memory[self.program_counter]:03d}'[:1])
            if opcode == 0:
                break
            if opcode not in self.instructions:
                raise ValueError("Invalid instruction")

            operand = int(f'{self.memory[self.program_counter]:03d}'[1:])

            self.program_counter += 1
            self.program_counter %= MEM_SIZE
            
            self.instructions[opcode](operand)
            if interactive:
                input("Press Enter to continue, press Ctrl+C to stop")
                
                