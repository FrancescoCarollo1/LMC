#SM3201419 Francesco Carollo
import LMC_memory
import LMC_queues 

print("Hello World!")

# Read and write memory

LMC_memory.write_memory(99, 42)
print(LMC_memory.read_memory(99))
LMC_queues.add_output(42)
print(LMC_queues.read_output())
