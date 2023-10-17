number, height = map(int, input().split())
min_heights = [int(i) for i in input().split()]

count = 0
for min_height in min_heights:
    if height >= min_height:
        count += 1

print(count)


import time
def funcion_con_timeout():
    start_time = time.time()
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
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time
    
tiempo_transcurrido = funcion_con_timeout()
print(f"El pcoeso tomo {tiempo_transcurrido} segundos")
