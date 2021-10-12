import time

# constant color :
B = 1
N = 0

class ArrayConsole:
    def __init__(self, array):
        self.array = array
        self.size = 20*30
        self.width = 20
        self.height = 30

    def _printArray(self):
        for i in range(self.width):
            for j in range(self.height):
                if (self.array[i][j] == 0):
                    print(' ')
                else:
                    print('O')
        print()

    def update(self):
        self._printArray()
        time.sleep(0.5)

