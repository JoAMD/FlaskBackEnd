str = 'None'
finalStr = None
if str :
	s = list(str)
	for idx,val in enumerate(s) :
		if val == 'o' :
			s[idx] = 'k'
			finalStr = "".join(s)

print(finalStr)