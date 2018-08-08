import re
import urllib.request

url="https://www.weather-forecast.com/locations/"
city=input("Enter name of the city:")
url=url+city
data=urllib.request.urlopen(url).read()
data1=data.decode("utf-8")
new=re.search('<span class="phrase">',data1)
start=new.end()
k=re.search("</span></p>",data1)
end=k.start()
print(data1[start:end])