combinations = int(input())
binaries = [int(i) for i in input().split()]
print(binaries)
possibleCombinations = []

for i in range(0, combinations):
    for j in range(0, combinations - i):
        possibleCombinations.append(j)
        print(i, j)
    print("************")
print(possibleCombinations)
possibleCombinations = [21, 22, 2]
print(possibleCombinations.index(max(possibleCombinations)))