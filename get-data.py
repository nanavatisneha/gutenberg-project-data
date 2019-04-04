import requests
import urllib2

#getting over proxy of college
proxy = urllib2.ProxyHandler({'http': 'proxy.iiit.ac.in:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

#url for the book
url = "http://www.gutenberg.org/files/36/36-0.txt"
#requesting the content from the URL
request = requests.get(url)
#storing the books content
book = request.content
#printing the content (> and crime_and_punishment.txt)
print(book)
