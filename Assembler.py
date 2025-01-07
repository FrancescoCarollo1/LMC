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
            "COB" : 0, 
            "DAT" : "",
        }

    
    def assemble(self, filename):
        with open(filename) as f:
            for line in f.readlines():

                # Rimuove i commenti e gli spazi di troppo, scrive la riga in stampatello la separa in una lista di token
                line = line.split("//")[0].strip("\n ").upper().split()

                # Controlla che la linea non sia vuota
                if line:

                    # Labels detection
                    if line[0] not in self.instructions:
                        label = line[0]
                        self.labels[label] = len(self.lines) 
                        line = line[1:] # Rimuove il label dalla riga

                    self.lines.append(line)

            # Secondo ciclo
            for i, line in enumerate(self.lines):

                # Rimpiazza i label con i rispettivi indirizzi
                if len(line) == 2 and line[1] in self.labels:
                    line[1] = self.labels[line[1]]

                # Ottiene l'opcode dalla lista di istruzioni
                opcode = self.instructions[line[0]]
                
                # Formatta l'operando se presente, altrimenti lascia vuoto
                operand = f"{int(line[1]):02d}" if len(line) == 2 else ""
                
                # Combina opcode e operando, converte ad intero, aggiunge a memory
                if opcode or operand:
                    self.memory[i] = int(f"{opcode}{operand}")

        return self.memory           


    
