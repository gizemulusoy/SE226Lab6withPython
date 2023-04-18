from math import factorial

n = int(input("Enter n: "))
x = int(input("Enter x: "))

result = sum([n ** i / factorial(i) for i in range(x + 1)])
print(result)

print("--------------------------------------------------")


def sum_rec(n):

#Calculates the sum of (-1)^(k+1)/k from k=1 to n

    global y

    if n == 1:
        y = 1.0
        return y
    else:
        y = (-1) ** (n + 1) / n + sum_rec(n - 1)
        return y


n = int(input("enter the limit for calculation: "))
sum_rec(n)
print("result : ", y)