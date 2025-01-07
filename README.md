# LMC
### Breve introduzione
Progetto in python per il corso di Programmazione avanzata e parallela.  
Lo scopo del progetto è simulare l'esecuzione di un programma assembly per Little Man Computer (LMC).  
Sono state implementate due classi: LMC ed Assembler.
### Assembler
Traduce il codice assembly in istruzioni interpretabili dal LMC.  
È stata aggiunta l'istruzione ```COB``` (Coffee Break), che ha lo stesso significato di ```HLT``` e sebbene non sia utilizzata in nessun file di prova, è presente nella documentazione del LMC.  
https://en.wikipedia.org/wiki/Little_man_computer#Instructions






INPUT USATI PER FARE I TEST:
- Counting: `[10]` 
- Exec: `[901, 902, 705, 600, 0, 4, 5, 6, 7, 8, 9, 0]`
- Looping non richiede input.
- Multiplication: `[6, 7]`
- Quine non richiede input.
- Reverse: `[5, 10, 15, 0]`
- Squares: `[1, 2, 3, 4, 5, 0]`

