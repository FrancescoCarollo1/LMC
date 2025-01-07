# Francesco Carollo SM3201419


import LMC
import Assembler
import argparse
import logging
import sys

def main():

    assembler = Assembler.Assembler()
    lmc = LMC.LMC()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="nome del file da eseguire")
    parser.add_argument("--input", help="input del programma" , type = int, nargs="*",  default = [])
    parser.add_argument("--interactive", help="modalità di esecuzione", action="store_true")
    args = parser.parse_args()

    lmc.memory = assembler.assemble(args.filename)
    lmc.input = args.input

    if  args.interactive:
        logging.basicConfig(level=logging.DEBUG, stream=sys.stdout, format="%(message)s")
    else:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout, format="%(message)s")

    lmc.run(args.interactive)    

    print("Output del programma: ", lmc.output)

if __name__ == "__main__":
    main()