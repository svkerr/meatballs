

d
d={}
flag = 0; 
fp = open("datasource.dat")
for line in fp: 
	try:
		if line[1] != '#':
			clean_line = line.strip(); 
			key,val = tuple(clean_line.split("::"))
			if key == 'record':
				if val == 'start':
					flag = 1
				if val == 'stop':
					flag = 0; 

		if flag == 1:
			d[key] = val
		if flag == 0:
			print d
			d={}		

	except:
		pass	
