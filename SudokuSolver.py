# Author: Vad Bertalan

from SudokuCell import SudokuCell
import copy


class SudokuSolver:
    def __init__(self, sudoku) -> None:
        self.sudoku = sudoku
        self.__solution = sudoku
        self.possibilities = self.__init_possibilities()
        self.nr_solution = 0
        self.solution = None

    def __init_possibilities(self):
        temp = range(1, 10)
        pos = []
        for i in range(9):
            pos.append([])
            for j in range(9):
                pos[i].append({str(x) for x in range(1, 10)})
        return pos  # returning empty possibility map

    def __minimize_possibilities(self):
        for i in range(9):
            for j in range(9):
                if not self.__solution.matrix[i][j].done and len(self.possibilities[i][j]) == 1:
                    value = self.possibilities[i][j].pop()
                    self.__solution.matrix[i][j] = SudokuCell(i, j, value)
                    self.__affect_vicinity(SudokuCell(i, j, value))

    def solve(self):
        for row in self.sudoku.matrix:
            for item in row:
                if item.done:
                    self.__affect_vicinity(item)

        self.__minimize_possibilities()
        self.__backtracking(0)
        if self.nr_solution == 0:
            print('no solution')

    def __valid(self, I, J, item):
        # row
        for cell in self.__solution.matrix[I]:
            if cell.j != J and cell.value == item:
                return False

        # column
        for i in range(9):
            if self.__solution.matrix[i][J].value == item:
                return False

        temp_i = I - I % 3
        temp_j = J - J % 3
        for i in range(3):
            for j in range(3):
                if self.__solution.matrix[i + temp_i][j + temp_j].value == item:
                    return False
        return True

    def __backtracking(self, level):
        i = level // 9
        j = level % 9
        if self.__solution.matrix[i][j].value == '.':
            for item in self.possibilities[i][j].copy():
                if self.__valid(i, j, item):

                    # trying out the new value
                    self.__solution.matrix[i][j].value = item
                    # self.__affect_vicinity(self.solution.matrix[i][j])

                    # if we arrived to the last cell
                    if level == 80:
                        # print('YAY')
                        # print(self.__solution)
                        self.nr_solution += 1
                        self.solution = copy.deepcopy(self.__solution)
                        # print(self.solution)
                        if self.nr_solution > 1:
                            # print('Multiple solutions!')
                            self.solution = None
                    else:
                        self.__backtracking(level + 1)  # going to next level

                    # extraction the value from the value => it did not work out
                    # self.__push_vicinity(self.solution.matrix[i][j])
                    self.__solution.matrix[i][j].value = '.'
        else:
            # if we arrived to the last cell
            if level == 80:
                self.nr_solution += 1
                self.solution = copy.deepcopy(self.__solution)
                if self.nr_solution > 1:
                    self.solution = None
            else:
                self.__backtracking(level + 1)  # going to next level

    def __push_vicinity(self, cell):
        for row_neighbour in self.possibilities[cell.i]:
            row_neighbour.add(cell.value)

        for col_neighbour in [row[cell.j] for row in self.possibilities]:
            col_neighbour.add(cell.value)

    def __affect_vicinity(self, cell):
        for row_neighbour in self.possibilities[cell.i]:
            row_neighbour.discard(cell.value)

        for col_neighbour in [row[cell.j] for row in self.possibilities]:
            col_neighbour.discard(cell.value)

        start_i, end_i, start_j, end_j = SudokuSolver.get_sector_indexes(cell.sector)
        for i in range(start_i, end_i):
            for j in range(start_j, end_j):
                self.possibilities[i][j].discard(cell.value)


    @staticmethod
    def get_sector_indexes(sector):
        assert(sector in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])

        if sector == 'a':
            start_i = 0
            end_i = 3
            start_j = 0
            end_j = 3
        elif sector == 'b':
            start_i = 0
            end_i = 3
            start_j = 3
            end_j = 6
        elif sector == 'c':
            start_i = 0
            end_i = 3
            start_j = 6
            end_j = 9
        elif sector == 'd':
            start_i = 3
            end_i = 6
            start_j = 0
            end_j = 3
        elif sector == 'e':
            start_i = 3
            end_i = 6
            start_j = 3
            end_j = 6
        elif sector == 'f':
            start_i = 3
            end_i = 6
            start_j = 6
            end_j = 9
        elif sector == 'g':
            start_i = 6
            end_i = 9
            start_j = 0
            end_j = 3
        elif sector == 'h':
            start_i = 6
            end_i = 9
            start_j = 3
            end_j = 6
        else:  # 'i'
            start_i = 6
            end_i = 9
            start_j = 6
            end_j = 9

        return start_i, end_i, start_j, end_j
