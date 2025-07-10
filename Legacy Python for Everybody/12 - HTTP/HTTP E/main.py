import urllib.request
fhand = urllib.request.urlopen('http://www.pythonlearn.com/code/intro-short.txt')
for line in fhand:
    print(line.decode().strip())
