for takrorlanish operatori 

1 msiol 
n=int(input("n : "))
import math
s = 1
for i in range(0,n+1):
    s+=1/math.factorial(i)
print("s = " , s)

2 misol

n=int(input("n : "))
x=int(input("x : "))
import math
s = 1
for i in range(1,n+1):
    s+=(x**i)/math.factorial(i)
print("s = " , s)

3 misol 

n=int(input("n : "))
x=int(input("x : "))
import math
s = 0
for i in range(0,n+1):
    s+=pow(-1,i)*(x**(2*i+1))/math.factorial(2*i+1)
print("s = " , s)

4 misol

n=int(input("n : "))
x=int(input("x : "))
import math
s = 0
for i in range(0,n+1):
    s+=pow(-1,i)*(x**(2*i))/math.factorial(2*i)
print("s = " , s)

5 misol 

n=int(input("n : "))
x=float(input("x : "))
import math
s = 0
if n>0 and abs(x)<1 :
    for i in range(1,n+1):
        s-=pow(-1,i)*pow(x,i)/i
    print('s = ' , s)
else :
    print("xato son kiritinlid")

6-misol 

n=int(input("n : "))
x=float(input("x : "))
import math
s = 0
if n>0 and abs(x)<1 :
    for i in range(1,n+1):
        s-=pow(-1,i)*pow(x,2*i+1)/(2*i+1)
    print('s = ' , s)
else :
    print("xato son kiritinlid")

