#to print fib series b/w lb and ub
def gen_fib(l,u,a=0,b=1):
    if l==0:
        print(a,end=" ")
    if l==1:
        print(b,end=" ")
    c=0
    while c<=u:
        c=a+b
        if c>=l and c<=u:
            print(c,end=" ")
        a=b
        b=c
