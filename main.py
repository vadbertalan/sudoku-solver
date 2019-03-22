# Author: Vad Bertalan

from Sudoku import Sudoku
from SudokuSolver import SudokuSolver
from SudokuGen import SudokuGen
import time


def main():
    filename = input("filename = ")
    if not filename.endswith('.txt'):
        filename = 'in.txt'
    try:
        fo = open(filename, "r")
        nr_solved = 0
        start = time.time()
        for line in fo:
            sud = Sudoku(line[:-1] if line[-1] == '\n' else line)  # getting rid of '\n'
            print(sud)
            ss = SudokuSolver(sud)
            ss.solve()
            if ss.nr_solution == 1:
                print(ss.solution)
            else:
                print(f'nr_solution != 1  <=>  nr_solution = {ss.nr_solution}')
            nr_solved += 1
            print('=================================')
        end = time.time()
        print(f'\nresolved {nr_solved} sudokus in {end - start} seconds.')

    except IOError:
        print("Couldn't open file: " + filename + ".")

    # SudokuGen.gen_sudoku()


main()