def fiboEvenSum(n):
    x=0#first value of fibonaci sequence
    y=1#second value of fibonaci sequence
    sum=x
    for i in range(2,int(n/2)):
        x=x+y #in first iteration x becomes the third element
        y=y+x #in first iteration y becomes the fourth element
        if y>n:
            break
        if (x%2==0):
            sum=sum+x
        if (y%2==0):
            sum=sum+y
    return sum

x=fiboEvenSum(4000000)
print(x)