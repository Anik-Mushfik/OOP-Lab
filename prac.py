# print("Givemetwonumbers,andI'lldividethem.")
# print("Enter'q'toquit.")
# while True:
#     first_number=input("\nFirstnumber:")
#     if first_number=='q':
#         break
#     second_number=input("Secondnumber:")
#     try:
#         answer=int(first_number)/int(second_number)
#     except ZeroDivisionError:
#         print("Youcan'tdivideby0!")
#     else: print(answe

# print("hello")
# try:
#     print("Data")
#     print("science")
#     print(5/0)
# except ZeroDivisionError:
#     print("learn math first")
# else:
#     print('NO exeption')
# finally:
#     print("bye")
# print("world")


# try:
#     print("Hello")
# except:
#     print("world!")
# finally:
#     print("Whatever")
#     try:
#         print(0/0)
#     except:
#         print("hi")
#         try:
#             print(7/0)
#         except:
#             print("Bye")


# try:
#     x= int(input())
#     y = int(input())
#     print(x/y)
#     file = open("my_file.txt","r")
#     file.read()

# except ValueError:
#     print("Input type is not integer")

# except ZeroDivisionError:
#     print("Can't divide by Zero")

# except FileNotFoundError:
#     print("File doesn't exist on the given path!")



def __add__(self, other):
    if not isinstance(other, type(1)):
        raise ValueError("Operand is not an integer")
    
x = input()
y = input()
__add__(x,y)
if type(x) != type(1):
    raise FileNotFoundError("Kaisa Laga Mera Majak!!!")
