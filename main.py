# Francesco Carollo SM3201419


import LMC
import Assembler

def main():

    assembler = Assembler.Assembler()
    lmc = LMC.LMC()
    
    lmc.memory = assembler.assemble("test_programs/reverse.lmc")
    lmc.input = [5, 10, 15, 0] # Da scegliere in base a quale programma si vuole eseguire
    lmc.run()
 

    print(len(lmc.output))
    print(lmc.output)

if __name__ == "__main__":
    main()