# Task 2: Fibonacci Generator 
def ficonacci_geneerator(limit):
    num_1 = 0
    num_2 = 1
    for i in range(limit):
        yield num_1
        num_1, num_2 = num_2, (num_1 + num_2)


gen = ficonacci_geneerator(limit=10)
for num in gen:
    print(num)