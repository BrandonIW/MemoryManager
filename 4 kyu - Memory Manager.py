class Node:
    def __init__(self, idex, allocated=False, data=None):
        self.idex = idex
        self.allocated = allocated
        self.data = data
        self.next = None

class MemoryManager:
    def __init__(self, memory):
        self.memory = memory
        self.memory_block = [Node(idex) for idex,_ in enumerate(memory)]
        for idex,node in enumerate(self.memory_block):
            try: node.next = self.memory_block[idex+1]
            except IndexError: node.next = None
        self.allocated_mem = []

    def calc_free_mem(self):
        return sum(1 for node in self.memory_block if node.allocated is False)

    def allocate(self, size):
        if size <= self.calc_free_mem():
            allocated_block = [self.memory_block[num] for num in range(size)]
            for node in allocated_block:
                node.allocated = True
            self.allocated_mem.append(allocated_block)
            return self.allocated_mem.index(allocated_block)

        if size > self.calc_free_mem():
            raise Exception("Cannot allocate more memory than exists")

    def release(self, pointer):
        try:
            for node in self.allocated_mem[pointer]:
                node.allocated = False
        except IndexError:
            raise Exception("Memory block does not exist")

    def read(self, pointer):
        try:
            if self.memory_block[pointer].allocated:
                return self.memory[pointer]
            else:
                raise Exception("Memory address is not allocated")
        except IndexError:
            raise Exception("Memory block does not exist")

    def write(self, pointer, value):
        try:
            if self.memory_block[pointer].allocated:
                self.memory[pointer] = value
            else:
                raise Exception("Memory address is not allocated")
        except IndexError:
            raise Exception("Memory location does not exist")



