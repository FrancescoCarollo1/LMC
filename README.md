# LMC
progetto in python per il corso di Programmazione avanzata e parallela


INPUT USATI PER FARE I TEST:
- Counting: `[10]` 
- Exec: `[901, 902, 705, 600, 0, 4, 5, 6, 7, 8, 9, 0]`
- Looping non richiede input.
- Multiplication: `[6, 7]`
- Quine non richiede input.
- Reverse: `[5, 10, 15, 0]`
- Squares: `[1, 2, 3, 4, 5, 0]`

```python
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

```