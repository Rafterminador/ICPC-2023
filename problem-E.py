n, k = map(int, input().split())
f = [int(i) for i in input().split()]

def add_digits(number):
    return int(number//(10**(len(str(number))-1))) + number%(10**(len(str(number))-1))

for i in range(k):

    f = sorted(f)
    if(f[-1] == 0):
        print(0)
        break

    if(i == k-1):
        print(add_digits(f[-1]))
        break
    
    f[-1] -= add_digits(f[-1])
    if(f[-1] == 0 and len(f) != 1):
        f.pop()
