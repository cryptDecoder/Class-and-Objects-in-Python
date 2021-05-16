from OperationsClass import operations
from UtilsClass import utilsWork


class ExecutorClass:
    date = utilsWork.dateTime()

    def sumNumbers(self):
        print("Performing Addition :")
        result = operations.addition(112, 222, 2, 2, 2, 2, )
        print(result)

    def doSub(self):
        result = operations.substraction(23, 2, 2, 45, 11, 232333, 1)
        print(self.date)

        print(result)


exc = ExecutorClass()
if __name__ == '__main__':
    exc.sumNumbers()
    exc.doSub()
