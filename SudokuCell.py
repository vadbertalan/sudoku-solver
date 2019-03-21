class SudokuCell:
    def __init__(self, i, j, value) -> None:
        assert(0 <= i < 9)
        assert(0 <= j < 9)
        assert(value == '.' or 1 <= int(value) <= 9)
        self.i = i
        self.j = j
        self.value = value
        self.done = True if value != '.' else False
        self.sector = self.decide_sector(i, j)

    @staticmethod
    def decide_sector(i, j):
        if 0 <= i <= 2:
            if 0 <= j <= 2:
                return 'a'
            elif 3 <= j <= 5:
                return 'b'
            else:
                return 'c'
        elif  3 <= i <= 5:
            if 0 <= j <= 2:
                return 'd'
            elif 3 <= j <= 5:
                return 'e'
            else:
                return 'f'
        else:
            if 0 <= j <= 2:
                return 'g'
            elif 3 <= j <= 5:
                return 'h'
            else:
                return 'i'

    def __str__(self):
        return '(' + str(self.i) + ', ' + str(self.j) + ') ' + self.value + ' ' + self.sector
