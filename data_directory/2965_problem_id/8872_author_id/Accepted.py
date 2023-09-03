string =input()
rotation =int(input())
start =string[0]
cstart =start
end =string[2]
if rotation%2 == 0:
	print ("undefined")
	quit()
if rotation > 4:rotation =rotation%4
for i in range(rotation):
	if start == ">":start ="v"
	elif start == "v":start ="<"
	elif start == "<":start ="^"
	elif start == "^":start =">"
if start == end:
	print ("cw")
	quit()
start =cstart
for i in range(rotation):
	if start == ">":start ="^"
	elif start == "v":start =">"
	elif start == "<":start ="v"
	elif start == "^":start ="<"
if start == end:
	print ("ccw")
	quit()
print ("undefined")