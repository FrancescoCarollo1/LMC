# Francesco Carollo SM3201419

class Assembler:
    def __init__(self):
        self.lines = []
        self.labels = {}
        self.memory = [0] * 100
        self.instructions = {
            "ADD" : 1,
            "SUB" : 2,
            "STA" : 3,
            "LDA" : 5,
            "BRA" : 6,
            "BRZ" : 7,
            "BRP" : 8,
            "INP" : 901,
            "OUT" : 902,
            "HLT" : 0,
            "COB" : 0, #COFFEE BREAK https://en.wikipedia.org/wiki/Little_man_computer#Instructions   
            "DAT" : "",
        }

    
    def assemble(self, filename):
        with open(filename) as f:
            for line in f.readlines():

                # Remove comments and excess whitespace, uppercase the line, split it into a list of tokens
                line = line.split("//")[0].strip("\n ").upper().split()

                # Check if the line is not empty
                if line:

                    # Labels detection
                    if line[0] not in self.instructions:
                        label = line[0]
                        self.labels[label] = len(self.lines) 
                        line = line[1:] # Remove the label from the line

                    self.lines.append(line)

            # Second pass
            for i, line in enumerate(self.lines):

                # Replace labels with their corresponding memory addresses
                if len(line) == 2 and line[1] in self.labels:
                    line[1] = self.labels[line[1]]

                # Retrieve the opcode using the instruction dictionary
                opcode = self.instructions[line[0]]
                
                # Format the operand if it exists, otherwise use an empty string
                operand = f"{int(line[1]):02d}" if len(line) == 2 else ""
                
                # Combine opcode and operand, convert to integer, append to memory
                if opcode or operand:
                    self.memory[i] = int(f"{opcode}{operand}")

        return self.memory           


    
