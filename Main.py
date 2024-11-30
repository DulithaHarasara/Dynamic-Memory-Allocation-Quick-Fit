class QuickFitAllocator:
    
    def __init__(self,common_sizes):
        self.freeLists = {size: [] for size in common_sizes}
        self.memoryPool = []

    def allocate(self,size):

        if size in self.freeLists:
            if self.freeLists[size]:
                return self.freeLists[size].pop()
            else:
                print(f"Allocating new block of size {size}")
                return f"Block-{size}-{len(self.freeLists[size]) + 1}"
                
        else:
            print(f"Allocating from general memory pool: Size {size}")
            block = f"Block-{size}-{len(self.memoryPool) + 1}"
            self.memoryPool.append(block)
            return block

    def deallocate(self,block,size):
        if size in self.freeLists:
            print(f"Returning block to free list of size {size}")
            self.freeLists[size].append(block)
        else:
            print(f"Removing block of size {size} from memory pool")
            self.memoryPool.remove(block)

    def displayState(self):
        print("Free LIst: ")

        for size,block in self.freeLists.items():
            print(f"Size {size} : {block}")

        print(f"General Memory pool: {self.memoryPool}")


allocator = QuickFitAllocator(common_sizes=[64, 128, 256])

# Allocate memory
block1 = allocator.allocate(64)
# block2 = allocator.allocate(128)
block3 = allocator.allocate(64)

# # Deallocate memory
allocator.deallocate(block1, 64)
# allocator.deallocate(block2, 128)

# # Display the state
# allocator.displayState()

# # Allocate an uncommon size
# block4 = allocator.allocate(1024)
allocator.displayState()