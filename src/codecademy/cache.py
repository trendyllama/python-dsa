import logging
from pathlib import Path
from random import randint

logger = logging.getLogger(__name__)


class Memory:
    def __init__(self, name="Memory", access_time=1):
        self.name = name
        self.access_time = access_time
        self.exec_time = 0
        self.output = ""

        logger.debug("Initialized %s with access time %.2f", name, access_time)

    def write(self, address, data):
        """Writes data to the memory at the specified address.
        Example:

        """
        self.exec_time += self.access_time

    def read(self, address, data=None):
        self.exec_time += self.access_time

    def get_exec_time(self):
        return self.exec_time


class ISA:
    def __init__(self):
        self._memory: Memory | None = None
        self.instructions = []
        self.output = ""
        logger.debug("Initialized ISA")

    @property
    def memory(self):
        if self._memory is None:
            msg = "Memory not set. Please set memory before accessing it."
            raise ValueError(msg)
        return self._memory

    def set_memory(self, memory: Memory):
        self._memory = memory

    def read_instructions(self, filename: Path):
        with filename.open() as file:
            for line in file:
                logger.debug("Reading instruction: %s", line.strip())
                instruction = line.strip()
                if instruction:
                    self.instructions.append(instruction)
                    self.execute_instruction(instruction)

    def execute_instruction(self, instruction):
        parts = instruction.split()
        command = parts[0].lower()
        if command == "write":
            address = int(parts[1])
            data = " ".join(parts[2:])
            self.memory.write(address, data)
        elif command == "read":
            address = int(parts[1])
            data = self.memory.read(address)
            if data is not None:
                self.output += f"Data at {address}: {data}\n"
            else:
                self.output += f"No data found at {address}\n"

    def get_exec_time(self):
        return self.memory.get_exec_time()


class MainMemory(Memory):
    def __init__(self):
        super().__init__(name="Main Memory", access_time=10)
        self.data = {}

    def write(self, address, data):
        super().write()
        self.data[address] = data

    def read(self, address):
        super().read()
        return self.data.get(address, None)

    def get_exec_time(self):
        return self.exec_time


class Cache(Memory):
    def __init__(self):
        super().__init__(name="Cache", access_time=0.5)
        self.main_memory = MainMemory()
        self.fifo_indices = [0, 0, 0, 0]
        self.sets = 1  # Set to 1, 2 or 4
        self.fifo_indices = [0, None, None, None]

        logger.debug("Initialized Cache with FIFO indices: %s", self.fifo_indices)
        logger.debug("Initialized Cache with sets: %s", self.sets)

        # Sets self.fifo_indicies based on
        # the number of sets in the cache
        if self.sets == 2:
            self.fifo_indices = [0, 2, None, None]
        elif self.sets == 4:
            self.fifo_indices = [0, 1, 2, 3]

        self.data = [
            {"tag": None, "data": ""},
            {"tag": None, "data": ""},
            {"tag": None, "data": ""},
            {"tag": None, "data": ""},
        ]

    def write(self, address, data):
        super().write()
        entry = self.get_entry(address)
        if entry is not None:
            entry["data"] = data
        else:
            self.replace_entry(address, data)

        self.main_memory.write(address, data)

    def read(self, address):
        super().read()
        data = None
        entry = self.get_entry(address)
        if entry is not None:
            data = entry["data"]
        else:
            data = self.main_memory.read(address)
            self.replace_entry(address, data)

        return data

    def replace_entry(self, address, data):
        index = 0
        set_number = address % self.sets
        index = self.fifo_policy(set_number)
        self.data[index] = {"tag": address, "data": data}

    def random_policy(self, set_number):
        if self.sets == 1:
            return randint(0, len(self.data) - 1)
        elif self.sets == 2:
            return randint(set_number * 2, set_number * 2 + 1)

        return set_number

    def fifo_policy(self, set_number):
        self.fifo_indices[set_number] += 1
        if self.fifo_indices[set_number] == len(self.data) / self.sets + (
            set_number * int(len(self.data) / self.sets)
        ):
            self.fifo_indices[set_number] = set_number * int(len(self.data) / self.sets)

        return self.fifo_indices[set_number]

    # Returns entry on cache hit
    # Returns None on cache miss
    def get_entry(self, address):
        entry = filter(lambda x: x["tag"] == address, self.data)

        match list(entry):
            case []:
                logger.info("Miss")
                return
            case _:
                logger.info("Hit")
                return entry

    def get_exec_time(self):
        exec_time = self.exec_time + self.main_memory.get_exec_time()
        return exec_time


if __name__ == "__main__":
    cache_arch = ISA()
    cache_arch.set_memory(Cache())

    # Architecture runs the instructions
    cache_arch.read_instructions("ex9_instructions")

    # This outputs the memory data and code execution time
    exec_time = cache_arch.get_exec_time()
    if exec_time > 0:
        logger.info("OUTPUT STRING: %s", cache_arch.output)
        logger.info("EXECUTION TIME: %.2f nanoseconds", exec_time)
