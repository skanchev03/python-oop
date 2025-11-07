class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        args = args[1:]
        for num in args:
            result *= num
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        args = args[1:]
        for num in args:
            result /= num
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        args = args[1:]
        for num in args:
            result -= num
        return result
