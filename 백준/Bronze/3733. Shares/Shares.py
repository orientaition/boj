while 1:
	try:
    		a,b=map(int,input().split())
	except EOFError:
    		break
	else:
    		print(b//(a+1))
