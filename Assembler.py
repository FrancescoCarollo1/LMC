#SM3201419 Francesco Carollo
# This is the Assembler.py file. It contains the Assembler class, which is used to assemble the LMC code into machine code.

'''
class Assembler():
    def __init__(self):
        self.instructions = {
            "ADD",
            "SUB",
            "STA",
            "LDA",
            "BRA",
            "BRZ",
            "BRP",
            "INP",
            "OUT",
            "HLT",
            "DAT",
            }
'''    
with open('test_programs/looping.lmc') as f:
    lines = []
    for line in f.readlines():
        line = line.split("//")[0].strip("\n ").split()
        line = [token.upper() for token in line]
        if line:
            lines.append(line)
    print(lines)

    