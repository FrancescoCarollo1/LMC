#SM3201419 Francesco Carollo

import queue

MIN_INPUT = 0
MAX_INPUT = 999
input = queue.Queue()
output = queue.Queue()

def add_input(value):
    if value < MIN_INPUT or value > MAX_INPUT:
        raise Exception("Input out of bounds")
    input.put(value)
    
def read_input():
    return input.get()

def add_output(value):
    if value < MIN_INPUT or value > MAX_INPUT:
        raise Exception("Output out of bounds")
    output.put(value)

def read_output():
    return output.get()

