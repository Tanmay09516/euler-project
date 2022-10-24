import math
def largestPrimeFactor(number):
    # largestPrime = 0
    # while number % 2 == 0:
    #     largestPrime = 2
    #     number = number / 2
    # for i in range(3, int(math.sqrt(number)) + 1, 2):
    #     while number % i == 0:
    #         largestPrime = i
    #         number = number / i
    # if number > 2:
    #     largestPrime = number
    # return largestPrime
    arr1=[]
    highest=0
    for i in range(3,math.ceil(number/2)):
        arr2=[]
        for j in range(3,number-1):
            if i%j==0:
                arr2.append(i)
        if arr2==[]:
            arr1.append(i)
    for k in arr1:
        if(number%k==0):
            highest=k
    return highest


print(largestPrimeFactor(8))


