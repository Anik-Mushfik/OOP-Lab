try:
    x= int(input())
    y= int(input())

    print(x/y)

    x = {
        "name" : "x"
    }
    print(x["age"])

    file = open("myfile.txt", "r")
    file.readline()

except FileNotFoundError:
    print("No File Found")

except ValueError:
    print("Value can not be converted")

except ZeroDivisionError:
    print("Learn Math you STUPID!")

# except Exception:
#     print("Kichu ekta hoise")

# except KeyError:
#     print("Eta print hobe na karon eta Exception er pore ase!")