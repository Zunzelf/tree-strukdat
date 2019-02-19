a = {
	'val' : "makan",
	'state' : "end",
	'next' : ["ayam", "soto"]
}
b = {
	'val' : "ayam",
	'state' : "end",
	'next' : []
}
c = {
	'val' : "soto",
	'state' : "end",
	'next' : ["ayam"]
}

kms = [a, b, c]

def checks(inp):
	pnt = inp.pop()
	res = find(pnt, kms)
	rsl = False
	if len(res) > 0 :
		rs = res[0]
		if len(inp) == 0:
			if rs["state"] == "end":
				rsl = True
		else:
			pnt = inp.pop()
			res = [x for x in rs["next"] if x == pnt]
			if len(res) > 0 :
				inp.append(pnt)
				rsl = checks(inp)
			else:
				rsl = False
	return rsl

def check(inp):
	txt = inp.split(" ")
	res = checks(txt[::-1])
	return res

def find(inp, ls):
	return [x for x in ls if x['val'] == inp]

if __name__ == '__main__':
	print(check("makan soto"))
	print(check("makan soto ayam"))
	print(check("makan ayam"))
	print(check("makan"))
	print(check("maka"))