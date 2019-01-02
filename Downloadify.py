#Author: Soumya Jagdev
#Date: 01/01/19

import requests
import sys
import os
from bs4 import BeautifulSoup
import subprocess
import popen
from shutil import copy2

#if a direcotry is provided, then work in that directory
#else work in current directory
if (len(sys.argv) > 2):
    working_path = sys.argv[2]
else:
    #had to do this as the program is listed in Desktop, making it download songs in Desktop
    working_path =  subprocess.check_output(['pwd']).strip() + "/"

#List of songs that already exist on cloud
list = []
for root, dirs, files in os.walk('/home/shiv/googledrive/Music'): 
    for file in files:  
        if file.endswith('.mp3'): 
            list.append(str(file))

#Get spotify webpage
page = requests.get(sys.argv[1])
soup = BeautifulSoup(page.content, 'html.parser')
tags = soup.find_all(class_="top-align track-name-wrapper")
print "Parsed list"

count = 0
for songs in tags:
    name = songs.find_all('span')[0].string 
    #Download song if not in list
    if (name + ".mp3" not in list):
        count += 1
        author = songs.find_all('span')[2].string
        #This is the search link 
        url = "https://www.youtube.com/results?search_query=" + name + " by " + author
        #Youtube webpage
        html = requests.get(url)
        meat = BeautifulSoup(html.content, 'html.parser')
        #Take the first link 
        vid = (meat.findAll(attrs={'class':'yt-uix-tile-link'})[0])
        url = "https://www.youtube.com" + vid['href']
        #Extract mp3 from youtube link
        bashCommand = "youtube-dl -f 'bestaudio' --extract-audio --audio-format mp3 --audio-quality 0 --embed-thumbnail --add-metadata --output '" +  name + ".%(ext)s\' " + url
        print "Downloading " + name
        #Execute bash command in bash
        subprocess.Popen(bashCommand,shell=True,cwd=working_path).wait()
        #Copy from local source to cloud 
        copy2(working_path+"/"+name+".mp3",'/home/shiv/googledrive/Music')
        print "DOWNLOADED " + name
    else:
        print "File already exists: " + name
        
print "Downloaded " + str(count) + " songs"

# Notes to self:
#     --> get spotify song list
#     --> go to youtube and download the mp3 file of the first youtube link
#     --> store it on working directory, and then copy it to google drive