def trail_0(n):
# 0 in factorial depends on how many 5 we have in no 
#so first we'll count 5 in no we'll get to know about 0
    c=0
    while n!=0:
        n=n//5
        c+=n
    return c
n=int(input())
print(trail_0(n))
 