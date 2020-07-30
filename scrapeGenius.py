from selenium import webdriver
import time
import sys
import os
import tkinter as tk
from tkinter import simpledialog

if len(sys.argv) == 3:
    artist = sys.argv[1]
    album = sys.argv[2]
else:
    root = tk.Tk()
    root.withdraw()        

    artist = simpledialog.askstring("tk", "Enter Artist Name")
    album = simpledialog.askstring("tk", "Enter Album Name")
    artist = artist.replace(" ", "-")
    album = album.replace(" ", "-")

## TODO: santaize inputs
    
##Create folders for Artist and album and change directory into those folders
try:
    os.mkdir(artist)
except:
    pass

os.chdir(artist)

try:
    os.mkdir(album)
except:
    pass

os.chdir(album)

##Search for album on Genius based on Genius.com organization
##https://genius.com/albums/Johanna-warren/Numun

profile = webdriver.FirefoxProfile()
profile.set_preference("javascript.enabled", False);
browser = webdriver.Firefox(profile)

albumFormat = "http://genius.com/albums" + "/" + artist + "/" + album
print(albumFormat)
browser.get(albumFormat)

##TODO: Click through each link in album tracklist page on Genius.com

allLinks = browser.find_elements_by_tag_name('a')

trackDict = {}

for link in allLinks:
    linkText = link.text
    if "Lyrics" in linkText:
        for char in ["'","?","(",")","❦"," Lyrics",".",'/']: #TODO: Sanitize input without micromanaging 
            linkText = linkText.replace(char, "")

        trackDict[linkText] = link.get_attribute("href")
    else:
        pass

print(trackDict)
trackListFile = open("trackList.txt", "w")

newline = ''

for track in trackDict:
    trackListFile.write(newline + track)
    newline = "\n"
    
trackListFile.close()

for track in trackDict:
    print(trackDict[track])
    browser.get(trackDict[track])
    #TODO: See if we can detect when page load is complete
    time.sleep(5)
    try:
        lyrics = browser.find_element_by_tag_name("p")
    except:
        print("Failed to scrape " + track)
        pass
    ##Save lyrics text content to a text file
    newFile = open(track + ".txt", mode="w")
    newFile.write(lyrics.text)
    newFile.close()
    
browser.quit()
