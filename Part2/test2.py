from time import time

ITERATIONS = 5_000_000

def conversion_method(x):
    if x < 0: return False
        
    return True if int(str(x)[::-1]) == x else False

def int_method(x):
    if x < 0: return False
    x_copy = x
    
    x_list = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

    i = 0
    while x > 0:
        x_list[i] = x%10
        x //= 10
        i += 1


    x_reverse = 0
    for idx in range(i):
        x_reverse += x_list[idx] * (10 ** (i-1-idx))

    return True if x_reverse == x_copy else False

t0 = time()
for i in range(ITERATIONS):
    conversion_method(878738)

print(time() - t0)


t0 = time()
for i in range(ITERATIONS):
    int_method(878738)

print(time()-t0)

