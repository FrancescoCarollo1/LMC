#SM3201419 Francesco Carollo
import LMC
import Assembler

def main():
    assembler = Assembler.Assembler()
    assembler.assemble("test_programs/squares.lmc")
    machine_code = assembler.memory
    lmc = LMC.LMC()
    lmc.input = [1, 2, 3, 4, 5, 0]
    lmc.load_memory(machine_code)
    lmc.run()
    print(lmc.output)
    print(len(lmc.output))

if __name__ == "__main__":
    main()