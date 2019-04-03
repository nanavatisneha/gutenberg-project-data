import requests
import urllib2

#getting over proxy of college
proxy = urllib2.ProxyHandler({'http': 'proxy.iiit.ac.in:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

#url for the book
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
#requesting the content from the URL
request = requests.get(url)
#storing the books content
crime_and_punishment = request.content
#printing the content (> and crime_and_punishment.txt)
print(request.content)
