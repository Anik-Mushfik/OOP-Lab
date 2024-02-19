name = input()
age = int(input())
syntoms = [0]*10
probability = 0

for i in range(10):
    response = input(f"Do you have symtom no {i+1}?")
    if response == "y" or response == "Y":
        syntoms[i] = 1
    
probability = (sum(syntoms) / 10) * 100

print(f"{name} has {probability:.2f}% chance of COVID-19")
