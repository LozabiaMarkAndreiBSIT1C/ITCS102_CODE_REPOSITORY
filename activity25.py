def taga_triangle(number):
    for x in range(number, 0, -1):
        for y in range(1, x +1):
            print("*", end= " ")
        print()
def sum(x,y):
    return x+y

taga_triangle(7)
taga_triangle(4)
taga_triangle(23)

print(sum(30,2))
print(sum(14, 3)* 100)