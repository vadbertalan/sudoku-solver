from SudokuCell import SudokuCell

class Sudoku:
    def __init__(self, sudokuString = '', value_matrix = []) -> None:
        assert len(sudokuString) == 81 or value_matrix != []
        self.sudokuString = sudokuString
        self.matrix = []
        self.value_matrix = value_matrix
        self.__convert()

    def __convert(self):
        if self.sudokuString != '':
            i, j = 0, 9
            self.value_matrix = []
            while not i == 81:
                self.value_matrix.append(self.sudokuString[i:j])
                i, j = j, j + 9

        for i in range(9):
            self.matrix.append([])

        for i in range(9):
            for j in range(9):
                self.matrix[i].append(SudokuCell(i, j, self.value_matrix[i][j]))


    def __str__(self):
        ret = ''
        for i in range(9):
            if i != 0 and i % 3 == 0:
                ret += '- ' * 11 + '\n'
            for j in range(9):
                if j != 0 and j % 3 == 0: ret += '| '
                ret += self.matrix[i][j].value + ' '
            ret += '\n'
        return ret





