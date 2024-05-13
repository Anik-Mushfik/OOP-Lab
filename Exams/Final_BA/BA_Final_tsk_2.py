class InvalidArgsException(Exception):
    pass


def validate_agrs(func):
    def wrapper(*args):
        for i in args:
            if i <= 0:
                raise InvalidArgsException("The given Arguments are invalid!!!")
        return func(*args)
    return wrapper


@validate_agrs
def area(length, width):
    area = length * width
    print(f"The area of the rectangle is: {area}")


area(5,4)
# area(5, -4)
area(-4, 5)