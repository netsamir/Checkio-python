#!/usr/bin/env python
# encoding: utf-8

import collections


class Subject(object):

    """Docstring for Subject. """

    def __init__(self):
        """TODO: to be defined1. """
        self._grades = []

    def report_grade(self, score, weight):
        """ """
        Grades = collections.namedtuple('Grade', ('score', 'weight'))
        self._grades.append(Grades(score, weight))


class Student(object):

    """Docstring for Student. """

    def __init__(self):
        """TODO: to be defined1. """
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]


class Gradebook(object):

    """Docstring for BookGrade. """

    def __init__(self):
        """TODO: to be defined1. """
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]
