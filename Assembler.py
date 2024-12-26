#SM3201419 Francesco Carollo
# This is the Assembler.py file. It contains the Assembler class, which is used to assemble the LMC code into machine code.
import LMC

class Assembler:
    def __init__(self):
        self.instructions = {
            "ADD": LMC.add,
            "SUB": LMC.sub,
            "STA": LMC.write_memory,
            "LDA": LMC.accum_read_in,
            "BRA": LMC.branch,
            "BRZ": LMC.branch_zero,
            "BRP": LMC.branch_positive,
            "INP": LMC.accum_read_in,
            "OUT": LMC.accum_add_out,
            "HLT": LMC.halt,
            "DAT": self.dat
            }
    
    