#!/usr/bin/env python
# encoding: utf-8

"""
Test for moore.py
"""


from unittest import TestCase
from moore import Moore


class TestMoore(TestCase):
    def setUp(self):
        # input for the function
        y0 = (0, 0, 1, 0, 0)
        y1 = (0, 1, 0, 0, 0)
        y2 = (0, 1, 1, 0, 0)
        y3 = (0, 1, 0, 0, 1)
        y4 = (0, 0, 1, 0, 1)
        matrix = (y0, y1, y2, y3, y4,)
        self.moore = Moore(matrix, 1, 2)

    def test_chg2list(self):
        # intermediary result
        rine1 = [0, 0, 1, 0, 0]
        rine2 = [0, 1, 0, 0, 0]
        rine3 = [0, 1, 1, 0, 0]
        rine4 = [0, 1, 0, 0, 1]
        rine5 = [0, 0, 1, 0, 1]
        ratrix = [rine1, rine2, rine3, rine4, rine5]
        self.assertEqual(self.moore.matrix, ratrix)

    def test_fndcoor(self):
        coor = (1, 2)
        self.assertEqual(self.moore.coor, coor)

    def test_neighboor(self):
        self.assertEqual(self.moore.neighboor(), 4)

    def test_neighboor_0(self):
        y0 = (0, 0, 0, 0, 0)
        y1 = (0, 0, 0, 0, 0)
        y2 = (0, 0, 0, 0, 0)
        y3 = (0, 0, 0, 0, 0)
        y4 = (0, 0, 0, 0, 0)
        matrix = (y0, y1, y2, y3, y4,)
        moore = Moore(matrix, 1, 2)
        self.assertEqual(moore.neighboor(), 0)

    def test_neighboor_1(self):
        y0 = (1, 1, 1, 1, 1)
        y1 = (1, 1, 1, 1, 1)
        y2 = (1, 1, 1, 1, 1)
        y3 = (1, 1, 1, 1, 1)
        y4 = (1, 1, 1, 1, 1)
        matrix = (y0, y1, y2, y3, y4,)
        moore = Moore(matrix, 1, 2)
        self.assertEqual(moore.neighboor(), 8)

    def test_neighboor_c(self):
        y0 = (1, 1, 0, 1, 0)
        y1 = (1, 0, 0, 1, 1)
        y2 = (0, 1, 0, 0, 0)
        y3 = (1, 0, 0, 1, 1)
        y4 = (1, 0, 0, 1, 0)
        matrix = (y0, y1, y2, y3, y4,)
        moore = Moore(matrix, 0, 0)
        self.assertEqual(moore.neighboor(), 2)

    def test_neighboor_c1(self):
        y0 = (1, 1, 0, 1, 0)
        y1 = (1, 0, 0, 1, 1)
        y2 = (0, 1, 0, 0, 0)
        y3 = (1, 0, 0, 1, 1)
        y4 = (1, 0, 0, 1, 0)
        matrix = (y0, y1, y2, y3, y4,)
        moore = Moore(matrix, 4, 4)
        self.assertEqual(moore.neighboor(), 3)

    def test_neighboor_c2(self):
        y0 = (1, 1, 0, 1, 0)
        y1 = (1, 0, 0, 1, 1)
        y2 = (0, 1, 0, 0, 0)
        y3 = (1, 0, 0, 1, 1)
        y4 = (1, 0, 0, 1, 0)
        matrix = (y0, y1, y2, y3, y4,)
        moore = Moore(matrix, 0, 4)
        self.assertEqual(moore.neighboor(), 3)

    def test_neighboor_c3(self):
        y0 = (1, 1, 0, 1, 0)
        y1 = (1, 0, 0, 1, 1)
        y2 = (0, 1, 0, 0, 0)
        y3 = (1, 0, 0, 1, 1)
        y4 = (1, 0, 0, 1, 0)
        matrix = (y0, y1, y2, y3, y4,)
        moore = Moore(matrix, 4, 0)
        self.assertEqual(moore.neighboor(), 1)

    def test_neighboor_c4(self):
        y0 = (1, 1, 0)
        y1 = (1, 0, 0)
        y2 = (0, 1, 0)
        matrix = (y0, y1, y2,)
        moore = Moore(matrix, 2, 0)
        self.assertEqual(moore.neighboor(), 2)

    def test_neighboor_c5(self):
        y0 = (1, 0, 1, 0, 1)
        y1 = (0, 1, 0, 1, 0)
        y2 = (1, 0, 1, 0, 1)
        y3 = (0, 1, 0, 1, 0)
        y4 = (1, 0, 1, 0, 1)
        y5 = (0, 1, 0, 1, 0)
        matrix = (y0, y1, y2, y3, y4, y5,)
        moore = Moore(matrix, 5, 4)
        self.assertEqual(moore.neighboor(), 2)
