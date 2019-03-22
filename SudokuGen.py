# Author: Vad Bertalan

import random
from Sudoku import Sudoku
from SudokuSolver import SudokuSolver
import copy


class SudokuGen:
    @staticmethod
    def gen_sudoku():
        # creating a sudoku object
        value_matrix = [['.' for x in range(9)] for x in range(9)]
        sud = Sudoku(value_matrix=value_matrix)

        # cycle ends when we find a sudoku with 1 solution
        while True:
            # generating 3 random sequences in range(1, 10)
            temp = [str(x) for x in range(1, 10)]
            random.shuffle(temp)
            l1 = temp.copy()
            random.shuffle(temp)
            l2 = temp.copy()
            random.shuffle(temp)
            l3 = temp

            # inserting the shuffled lists into the diagonal squares <=> they do not affect each other
            for i in range(3):
                for j in range(3):
                    sud.matrix[i][j].value = l1.pop()
            for i in range(3, 6):
                for j in range(3, 6):
                    sud.matrix[i][j].value = l2.pop()
            for i in range(6, 9):
                for j in range(6, 9):
                    sud.matrix[i][j].value = l3.pop()

            print(f'before insertion: \n{sud}')
            # generating a few random values
            count = 0
            nr_insert = 10#random.randint(13, 16)
            while count < nr_insert:
                i = random.randint(0, 8)
                j = random.randint(0, 8)
                value = str(random.randint(1, 9))
                while sud.matrix[i][j].value != '.' or not SudokuGen.__valid(sud.matrix, i, j, value):
                    i = random.randint(0, 8)
                    j = random.randint(0, 8)
                sud.matrix[i][j].value = value
                print(sud)
                count += 1
            print(f'after insertion: \n{sud}')

            # solving the sudoku
            ss = SudokuSolver(sud)
            ss.solve()
            print(ss.solution)
            # if it has only 1 solution, cycle ends
            if ss.nr_solution == 1:
                break
            else:
                print(f'Sudoku created having solution count 0 or more than 1  ({ss.nr_solution}). Recreating sudoku.')

            # recreating the sudoku
            value_matrix = [['.' for x in range(9)] for x in range(9)]
            sud = Sudoku(value_matrix=value_matrix)

        print(f'value_matrix: \n{sud}')
        print(ss.solution)

        final_sud_solution = ss.solution

        while True:
            print('extracting')
            # creating the final sudoku puzzle extracting 30-50 items randomly
            final_sud = copy.deepcopy(final_sud_solution)
            count = 0
            nr_extract = random.randint(35, 45)
            while count < nr_extract:
                i = random.randint(0, 8)
                j = random.randint(0, 8)
                while final_sud.matrix[i][j].value == '.':
                    i = random.randint(0, 8)
                    j = random.randint(0, 8)
                final_sud.matrix[i][j].value = '.'

                count += 1

            ss2 = SudokuSolver(final_sud)
            ss2.solve()
            if ss2.nr_solution == 1:
                break
            else:
                print(f'{ss2.nr_solution} > 1 after extraction. extracting again.')

        print(f'final sudoku: \n{final_sud}')
        print(ss2.solution)
        print(ss2.nr_solution)

    @staticmethod
    def __valid(m, I, J, item):
        # row
        for cell in m[I]:
            if cell.j != J and cell.value == item:
                return False

        # column
        for i in range(9):
            if m[i][J].value == item:
                return False

        temp_i = I - I % 3
        temp_j = J - J % 3
        for i in range(3):
            for j in range(3):
                if m[i + temp_i][j + temp_j].value == item:
                    return False
        return True

