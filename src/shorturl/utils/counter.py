class Counter:
    def __init__(self) -> None:
        self._counter = 0

    def getCounter(self) -> int:
        self._counter += 1
        return self._counter

if __name__ == '__main__':
    counter = Counter()
    for i in range(10):
        print(counter.getCounter())