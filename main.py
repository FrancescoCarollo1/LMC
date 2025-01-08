# Francesco Carollo SM3201419

import LMC
import Assembler
import argparse
import sys

# Questa funzione controlla che il programma passato come argomento abbia l'output atteso
def test_program(program_filename, program_input, expected_output):
    assembler = Assembler.Assembler()
    lmc = LMC.LMC(False)

    lmc.memory = assembler.assemble(program_filename)
    lmc.input = program_input

    try:
        lmc.run()
    except ValueError as e: 
        print(f'FAIL: {program_filename}\t\t{e}')
        return

    if lmc.output == expected_output:
        print(f'PASS: {program_filename}')
    else:
        print(f'FAIL: {program_filename}\t\toutput: {lmc.output} != {expected_output}')


def run_all_tests():
    test_program("test_programs/counting.lmc",          [10],                                           [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    test_program("test_programs/exec.lmc",              [901, 902, 705, 600, 0, 4, 5, 6, 7, 8, 9, 0],   [4, 5, 6, 7, 8, 9, 0])
    test_program("test_programs/looping.lmc",           [],                                             list(range(0,100))*100)
    test_program("test_programs/multiplication.lmc",    [6, 7],                                         [42])
    test_program("test_programs/quine.lmc",             [],                                             [500, 902, 208, 708, 500, 108, 300, 600, 1])
    test_program("test_programs/reverse.lmc",           [5, 10, 15, 0],                                 [15, 10, 5])
    test_program("test_programs/squares.lmc",           [1, 2, 3, 4, 5, 0],                             [1, 4, 9, 16, 25])


def main():

    if '--run-tests' in sys.argv: 
        run_all_tests()
        exit()

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="nome del file da eseguire")
    parser.add_argument("--input", help="input del programma" , type = int, nargs="*",  default = [])
    parser.add_argument("--interactive", help="modalità di esecuzione: flag presente per esecuzione interattiva, assente per esecuzione normale", action="store_true")
    # --run-tests è inutilizzato, controllato dall'if soprastante. Inserito per il messaggio di help
    parser.add_argument("--run-tests", help="testa tutti i programmi e termina (risultati hard-coded)", action="store_true") 
    args = parser.parse_args()

    assembler = Assembler.Assembler()
    lmc = LMC.LMC(args.interactive)

    lmc.memory = assembler.assemble(args.filename)
    lmc.input = args.input
    lmc.run()    
    print("Output del programma: ", lmc.output)

if __name__ == "__main__":
    main()