def multiplesOf3and5(number):
    sum=0
    for i in range(1,number):
        if i%3==0 or i%5==0:
            sum=sum+i
    return sum

x=multiplesOf3and5(1000)
print(x)