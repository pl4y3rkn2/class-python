for i in range(1, 101):
	if i % 3 == 0 and i % 5 == 0:
		print("SiteHost")
	elif i % 5 == 0:
		print("Host")
	elif i % 3 == 0:
		print("Site")
	else:
		print(i)
	i+=1