import urllib.request
cnt=0
for i in range(100,10000):
	print("getting image "+str(cnt))
	urllib.request.urlretrieve("https://webmail.iitg.ac.in/plugins/captcha/backends/watercap/image_generator.php?sq="+str(i),"images/" +  str(i)+".png")
	cnt=cnt+1