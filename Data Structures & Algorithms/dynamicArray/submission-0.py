class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        if capacity <1 :
            raise CustomException("capacity needs to be greater than 0")
        self.array = [None]*capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i]=n

    def pushback(self, n: int) -> None:
        if self.capacity == self.length:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        value = self.array[self.length-1]
        self.array[self.length-1] = None
        self.length -= 1
        return value


    def resize(self) -> None:
        self.array += [None]*self.capacity
        self.capacity *= 2

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity