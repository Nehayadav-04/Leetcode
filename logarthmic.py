def myPow(x, n):
    if x==0:
        return 0
    if n==0:
        return 1
    a=myPow(x*x,n//2)
    if n%2==0:
        return a
    else:
        return a*x
           
x=float(input())
n=int(input())
a=myPow(x,abs(n))
if n>=0:
    print(a)
else:
    print(1/a)    
# class Solution:
# def myPow(self,x : float,n : int) -> float:
#     def helper(x,n):
#         if x==0 : return 0
#         if n==0: return 1
#         res = helper(x*x,n//2)
#         return x*res if (n%2) else res 
#     res=helper(x,abs(n))
#     return res if n>=0 else 1/res
# x=float(input())
# n=int(input())
# print(helper(x,n))     