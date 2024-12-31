# Francesco Carollo SM3201419


import LMC
import Assembler

def main():

    assembler = Assembler.Assembler()
    lmc = LMC.LMC()
    
    lmc.memory = assembler.assemble("test_programs/counting.lmc")
    lmc.input = [14] # Da scegliere in base a quale programma si vuole eseguire
  
    lmc.run()

    print(len(lmc.output))
    print(lmc.output)

if __name__ == "__main__":
    main()