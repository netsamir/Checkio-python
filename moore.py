#!/usr/bin/env python
# encoding: utf-8

"""
You are given a state for a rectangular board game grid with chips in a binary
matrix, where 1 is a cell with a chip and 0 is an empty cell. You are also
given the coordinates for a cell in the form of row and column numbers
(starting from 0). You should determine how many chips are close to this cell.
Every cell interacts with its eight neighbours; those cells that are
horizontally, vertically, or diagonally adjacent.
"""


class Moore(object):
    """docstring for Moore"""
    def __init__(self, grid, row, col):
        "return the number of neighbours"
        # Extract the data from the argument
        # There are always the last two elements
        # of tuple
        self.matrix = self.__chg2list(grid)
        self.coor = self.__fndcoor((row, col))

    def __chg2list(self, grid):
        line = []
        matrix = []
        try:
            for row in grid:
                for el in row:
                    line.append(el)
                matrix.append(line)
                line = []
        except TypeError:
            pass
        return matrix

    def __fndcoor(self, coor):
        # print "Row is:", coor[0]
        # print "Col is:", coor[1]
        return (coor[0], coor[1])

    def __valid(self, row, col):
        # 3 ≤ len(grid) ≤ 10
        # all(len(grid[0]) == len(row) for row in grid)
        # Define bondary - Specification says that
        # print self.matrix
        lcol = len(self.matrix[0])
        lrow = len(self.matrix)
        # print "Num of col", lcol
        # print "Num of row", lrow
        return (-1 < col) and (col < lcol) and (-1 < row) and (row < lrow)

    def neighboor(self):
        col = self.coor[0]
        row = self.coor[1]
        colm1 = col - 1
        colp1 = col + 1
        rowm1 = row - 1
        rowp1 = row + 1
        # We will have to check if there is a number
        # in line corr[0] - 1 < corr[0] < corr[0] + 1
        # and in column corr[1] - 1 < corr[1] < corr[1] + 1

        # print colm1, row
        result = 0
        if self.__valid(colm1, rowm1):
            result += self.matrix[colm1][rowm1]
        if self.__valid(colm1, row):
            result += self.matrix[colm1][row]
        if self.__valid(colm1, rowp1):
            result += self.matrix[colm1][rowp1]
        if self.__valid(col, rowm1):
            result += self.matrix[col][rowm1]
        if self.__valid(col, rowp1):
            result += self.matrix[col][rowp1]
        if self.__valid(colp1, rowm1):
            result += self.matrix[colp1][rowm1]
        if self.__valid(colp1, row):
            result += self.matrix[colp1][row]
        if self.__valid(colp1, rowp1):
            result += self.matrix[colp1][rowp1]

        return result
