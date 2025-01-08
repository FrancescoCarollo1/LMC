# LMC
### Breve introduzione
Questo progetto Python, sviluppato per il corso di **Programmazione avanzata e parallela**, simula l'esecuzione di un programma assembly per il Little Man Computer (LMC).  
Il progetto implementa due classi principali: **LMC** e **Assembler**.

--- 

### Assembler
L'assembler si occupa di tradurre il codice assembly in istruzioni comprensibili per il simulatore LMC.  
Inoltre, è stata aggiunta l'istruzione `COB` (Coffee Break), equivalente a `HLT` (Halt), presente nella documentazione ufficiale del LMC ma non utilizzata nei file di prova.  

Documentazione ufficiale: [Little Man Computer - Wikipedia](https://en.wikipedia.org/wiki/Little_man_computer#Instructions)

### LMC
La classe **LMC** simula l'esecuzione delle istruzioni leggendole dalla memoria.

---

### Sintassi
Per eseguire correttamente il programma è necessario utilizzare il seguente formato:

```bash
python main.py programma.lmc [--input num1 num2 ...] [--interactive]
```
- *programma.lmc*: percorso al file con il programma assembly da eseguire.
- *--input*: (opzionale) specifica una sequenza di valori numerici come input per il programma.
- *--interactive*: (opzionale) flag che abilita l'esecuzione step by step.  
*Note*: 
- assicurarsi che il percorso del file sia corretto.
- secondo la sintassi di argparse, gli argomenti preceduti da "-" sono opzionali.  

# Esempio di utilizzo
### Esecuzione con flag disattivato

```bash
python main.py test_programs/counting.lmc --input 10  
```
### Esecuzione con flag attivato
```bash
python main.py test_programs/counting.lmc -- input 10 --interactive
```
**Nota**: sarà necessario premere Invio per proseguire nell'esecuizoone del programma, o Crl + C per arrestarla.






**Input utilizzati nei test:**
- Counting: `[10]`. 
- Exec: `[901, 902, 705, 600, 0, 4, 5, 6, 7, 8, 9, 0]`.
- Looping non richiede input.
- Multiplication: `[6, 7]`.
- Quine non richiede input.
- Reverse: `[5, 10, 15, 0]`.
- Squares: `[1, 2, 3, 4, 5, 0]`.

