# @staticmethod
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Cannot Divide By Zero')
