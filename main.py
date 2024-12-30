#SM3201419 Francesco Carollo
import LMC
import Assembler

def main():
    assembler = Assembler.Assembler()
    assembler.assemble("test_programs/counting.lmc")
    machine_code = assembler.memory
    lmc = LMC.LMC()
    #lmc.input = [901, 902, 705, 600, 0, 4, 5, 6, 7, 8, 9, 0]
    lmc.input = [42]
    lmc.load_memory(machine_code)
    lmc.run()

if __name__ == "__main__":
    main()