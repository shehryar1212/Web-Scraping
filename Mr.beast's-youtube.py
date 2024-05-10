from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get('https://www.youtube.com/@MrBeast/videos')

actions = ActionChains(driver)

# Wait for the page to load dynamically
time.sleep(5)

# Get the page source
page_source = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find the elements 
videos = soup.find_all('div', {'id': 'dismissible'})
masterlist=[]
for video in videos:
    datadict={}
    datadict['title']     = video.find('a', {'id': 'video-title-link'}).text
    datadict['url']       = 'https://www.youtube.com/'+video.find('a', {'id': 'video-title-link'})['href']
    meta                  = video.find('div', {'id': 'metadata-line'}).find_all('span')
    datadict['views']     = meta[0].text
    datadict['video_age'] = meta[1].text
    masterlist.append(datadict)

youtube_df=pd.DataFrame(masterlist) 
print(youtube_df)
