stack_tiring = []

d, c, r = map(int, input().split())

for i in range(c):
    stack_tiring.append(int(input()))

for i in range(r):
    d += int(input())

count = r
for val in stack_tiring:
    if(d >= val):
        count+=1
        d -= val
    else:
        break
print(count)

