import requests
from bs4 import BeautifulSoup

site_map = 'https://www.pngmart.com/sitemap.xml'
response = requests.get(site_map)
soup = BeautifulSoup(response.text, 'xml')
sitemapslist=[]
for loc in soup.find_all('loc'):
    url=loc.text
    if 'posts' in url:
        sitemapslist.append(url)

imgurllist=[]
response=requests.get(sitemapslist)
soup = BeautifulSoup(response.text, 'xml')
for loc in soup.find_all('loc'):
    url=loc.text
    if 'files' not in url:
        imgurllist.append(url)



for pngurl in imgurllist:
    response = requests.get(pngurl)
    soup = BeautifulSoup(response.text, 'html.parser')
    d_url = soup.find('a',{'class':'download'})['href']
    img = requests.get(d_url)
    img_title = 'E:/python-projects/scrapping/' + pngurl.split('/')[-1] + '-' + d_url.split('/')[-1]
    with open(img_title, 'wb') as f:
                f.write(img.content)
    

