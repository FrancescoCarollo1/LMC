#SM3201419 Francesco Carollo

MEMORY_MIN = 0
MEMORY_MAX = 100
memory = [0] * MEMORY_MAX

def read_memory(adress):
    if adress >= MEMORY_MAX or adress < MEMORY_MIN:
        raise Exception("Memory out of bounds")
    return memory[adress]


def write_memory(adress, value):
    if adress >= MEMORY_MAX or adress < MEMORY_MIN:
        raise Exception("Memory out of bounds")
    memory[adress] = value
