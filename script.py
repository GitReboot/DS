f = open("graph7.txt","r")
l = f.readlines()
for line in l:
	G = Graph(line.strip())
	G.show()