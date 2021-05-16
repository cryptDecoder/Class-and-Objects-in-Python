# This is my mathematical operation class
from functools import reduce
from operator import sub

from UtilsClass import utilsWork


class OperationsClass:
    date = utilsWork.dateTime()

    @classmethod
    def addition(cls, *args):
        return sum(args)

    @classmethod
    def substraction(cls, *args):
        print(f"date is {cls.date}")

        return reduce(sub, args)


operations = OperationsClass()
