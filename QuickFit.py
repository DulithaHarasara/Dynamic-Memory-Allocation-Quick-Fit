class QuickFit:
    def __init__(self):
        self.memory = {50:{"block1":50,"block2":50},100:{"block3":100,"block4":100},200:{"block5":200}}
        #self.processSize = processSize

    def allocate(self,processSize):

        # check input is in or not in the memory
        if processSize in self.memory:
            #print(self.memory[processSize])

            for key,value in self.memory[processSize].items():
                if value >= processSize and value != 0:
                    self.memory[processSize][key] = 0
                    return "ok"

        else:
            sorted_key = sorted(self.memory.keys())
            
            for key in sorted_key:
                print(self.memory[key])

                for keyele,value in self.memory[key].items():
                    if value != 0 and processSize <= value:
                        (self.memory[key])[keyele] = value - processSize
                        return "Add"
                
            return "No Space in the memory"

    def viewMemory(self):
        print(self.memory)

x = QuickFit()

isRun = True
while isRun:
    sizeOfAllocate = int(input("Enter the size: "))
    response = x.allocate(sizeOfAllocate)
    print(response)
    x.viewMemory()