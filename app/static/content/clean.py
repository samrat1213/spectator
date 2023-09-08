def clean(strng):
	new=""
	s=strng.split()
	for w in s:
		if w[0]!="#":
			new=new+" "+w
	return new
		
