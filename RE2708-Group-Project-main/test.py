# sum = 0
# for i in [0,1,2,3]:
#     f = i**2 + 4
#     sum += f

# print(sum)
# print(f"{(1/sum)=}")

def func(x):
    return x-((x**3)/3)

def sub(lower, upper):
    return (3/4)*(func(upper)-func(lower))

ans = sub(-1, -0.25) + sub(0.25, 1)
print(ans)