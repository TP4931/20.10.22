a=int(input("введите a"))
b=int(input("введите b"))
c=int(input("введите c"))
D=b**2-4*a*c
if D<0:
    print("корней нет")
if D==0:
    x = (-b + D ** 0.5) / (2 * a)
    print(x)
if D>0:
    x=(-b+D**0.5)/(2*a)
    y=(-b-D**0.5)/(2*a)
    print(x,y)