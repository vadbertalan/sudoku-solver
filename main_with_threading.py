# Author: Vad Bertalan

from Sudoku import Sudoku
from SudokuSolver import SudokuSolver
from SudokuGen import SudokuGen
import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, sudoku_string):
        Thread.__init__(self)
        self.sudoku_string = sudoku_string
        self.sudoku = None
        self.solution = None
        self.nr_solution = 0

    def run(self):
        self.sudoku = Sudoku(self.sudoku_string[:-1] if self.sudoku_string[-1] == '\n' else self.sudoku_string)  # getting rid of '\n'
        ss = SudokuSolver(self.sudoku)
        ss.solve()
        if ss.nr_solution != 1:
            print(f'nr_solution != 1  <=>  nr_solution = {ss.nr_solution}')
        self.solution = ss.solution
        self.nr_solution = ss.nr_solution


def main():
    filename = input("filename = ")
    if not filename.endswith('.txt'):
        filename = 'in.txt'
    try:
        fo = open(filename, "r")
        nr_solved = 0
        threads = []
        start = time.time()
        for line in fo:
            th = MyThread(line)
            threads.append(th)
            th.start()
            nr_solved += 1

        print('** threads started **')
        end_th_start = time.time()
        print(f'starting threads finished: {end_th_start - start}')

        for th in threads:
            th.join()
        end_solve = time.time()

        for th in threads:
            print(th.sudoku)
            print(th.solution)
            print(th.nr_solution)
            print('=================================')
        print(f'\nresolved {nr_solved} sudokus in {end_solve - start} seconds.')

    except IOError:
        print("Couldn't open file: " + filename + ".")


    # SudokuGen.gen_sudoku()


main()
