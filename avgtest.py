a=int(input("test1="))
b=int(input("test2="))
c=int(input("test3="))
avg=(a+b+c)/3
print("the avg of tests is="+str(avg))
#to take avg of best 2 out of 3
#using ternary operator

big1 =a if a>b else b
print(big1)

big2= b if b>c and a>c else c
print(big2)

AVG=(big1+big2)/2

print("Average of best of 2 out of 3 is (using ternary operator):"+str(AVG))

if a<b:

   if a<c:
       large1=b
       large2=c
       print(large1)
       print(large2)
   else:
       large1=a
       large2=b
       print(large1)
       print(large2)
else:
    if(b<c):
        large1=a
        large2=c
        print(large1)
        print(large2)
    else:
        large1=a
        large2=b
        print(large1)
        print(large2)

Average=(large1+large2)/2
print("Average of 2 numbers out of 3(using nested if-else):"+str(Average))





