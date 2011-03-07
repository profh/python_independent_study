import sys, os
import zlib, base64 #for storing icons as strings within py file.


def file_get_contents(filename):
	if not os.path.exists(filename):
		print "Can not access",filename
		return
	
	f = open(filename, "r")
	
	rawdata = f.read()
	f.close()
	return rawdata

def imageCompressionStats(filename):
	raw = file_get_contents(filename)
	print "Raw size is",len(raw),"bytes"
	print "Base64 encoded size is",len(base64.encodestring(raw)),"bytes"
	print "Compressed raw size is",len(zlib.compress(raw,9)),"bytes"
	print "base64 encoded compressed size is",len(base64.encodestring(zlib.compress(raw,9))),"bytes"
	print "Compressed base64 string size is",len((zlib.compress(base64.encodestring(raw),9))),"bytes"
	for i in range(1,10):
		print "Compressed (level "+str(i)+") of base64 string size is",len((zlib.compress(base64.encodestring(raw),i))),"bytes"
		
	return


def main():
	print "Takes images and zips them and then base64 encodes them"
	print
	if len(sys.argv) == 1:
		print "You must provide at least one file to process"
	else:
		skip = True
		for argument in sys.argv:
			if skip == True:
				skip = False
				continue
			print "String version of",argument
			print "---------------------------------------"
			data = base64.encodestring(file_get_contents(argument))
			linelength = 80
			curcount = 0
			outline = ""
			firstline = True
			outstr = ""
			outstr += "ico = \"\"\"\r\n"
			for i in range(0, len(data)):
				if (data[i] == "\n"):
					continue
				if (curcount+1 > linelength):
					outstr += outline + "\r\n"
					curcount = 0
					outline = ""
				outline = outline + data[i]
				curcount = curcount + 1
			outstr += outline
			outstr += "\r\n\"\"\""
			print outstr
			print "---------------------------------------"
			print 



main()
