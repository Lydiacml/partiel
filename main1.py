
def polynome(x):
	return ((x*x*x)-(1.5*(x*x))-(6*x)+5)

def factorielle(n):
	if n==0 :
		return 1
	else : 
		i=1
		f=1
		while i<=n :
			f=f*i
			i=i+1
		return f
print (polynome(5))
print (factorielle(5))

def fibonacci(n):
	a=[0,1]
	if n==0 : 
	    print('0')
	elif n==1 :
	    print('0,1')
	else:
	    while (len(a)<n):
	        a.append(0)
	    if (n==0 or n==1):
	        return 1 
	    else :
	        a[0]=0
	        a[1]=1
	        for i in range (2,n):
	            a[i]=a[i-1]+a[i-2]
	        print (a)

fibonacci(6)
