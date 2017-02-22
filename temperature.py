#!/usr/bin/python 

# Output a clickable URL.

import os, sys, string, cgi, urllib, time

sourceurl = "http://aws.mq.edu.au/awsProcess.php?variable=TD&day=%d&output=graph"

def main():
	write("Content-type: text/html\r\n\r\n")
	#try:
	#	data = urllib.urlopen(sourceurl).read()
	#except:
	#	error()
	#	return 1
	try:
		write_info(int(cgi.FieldStorage().getfirst("date", str(time.time()))))
	except:
		write_info(int(time.time()))
	return 0

def write_info(date):
	day = 24*60*60
	date = date - (date % day) + 11*60*60
	sourceaddr = sourceurl % date
	write("<html>\n")
	write(" <head>\n")
	write("  <title>Temperature</title>\n")
	write(" </head>\n")
	write("<body>\n")
	write("<center>\n")
	write('<h1><a href="temperature.cgi" style="text-decoration: none">Temperature</a></h1>\n')
	write('<a href="temperature.cgi?date=%d" style="text-decoration: none">&lt; Previous</a>' % (date - day))
	write(" " + ("&nbsp;" * 10) + " ")
	write('<a href="temperature.cgi?date=%d" style="text-decoration: none">Next &gt;</a>' % (date + day))
	write("<p />\n")
	write('<img src="%s" border="0">\n' % sourceaddr)
	write("</center>\n")
	write("</html>\n")

def error(msg=''):
	write("<html>\n")
	write(" <head>\n")
	write("  <title>Temperature</title>\n")
	write(" </head>\n")
	write("<body>\n")
	write("<H1>Temperature</H1>\n")
	write("Sorry, an error occurred " + msg)
	write("</html>\n")

def write(msg):
	sys.stdout.write(msg)
	sys.stdout.flush()

if __name__ == "__main__":
	sys.exit(main())

