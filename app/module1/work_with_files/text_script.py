import urllib.request
import codecs

'''
The following code reads the USA Declaration of Independence as a text file. 
This code streams the document and reads it line-by-line. 
This code could handle a very large file.
'''

url = "https://www.constitution.org/usdeclar.txt"
with urllib.request.urlopen(url) as urlstream:
    for line in codecs.iterdecode(urlstream, 'utf-8'):
        print(line.rstrip())
