from selenium import webdriver
import time
import pyautogui
import sys
import os

if len(sys.argv) == 3:
    artist = sys.argv[1]
    album = sys.argv[2]
else:
    artist = "Nada-surf"
    album = "let-go"

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

browser = webdriver.Firefox()
albumFormat = "http://genius.com/albums" + "/" + artist + "/" + album
print(albumFormat)
browser.get(albumFormat)

##TODO: Click through each link in album tracklist page on Genius.com

elements = browser.find_elements_by_tag_name('a')

i = 0

trackList = []

for element in elements:
    if "Lyrics" in element.text:
        trackList.append(element.text)
    else:
        pass

print(trackList)
trackListFile = open("trackList.txt", 'w')
for track in trackList:
    for char in ["'","?","(",")","❦"]: #TODO: combine w below
        track = track.replace(char, "")
    if track == trackList[-1]:
        trackListFile.write(track)
    else:
        trackListFile.write(track + '\n')
trackListFile.close()

for track in trackList:
    print(track)
    for char in ["'","?","(",")","❦"]:
        track = track.replace(char, "")
    filteredTrack = track.strip().replace(" ","-").replace("&","and").lower()
    browser.get("http://genius.com/" + artist + "-" + filteredTrack)
    time.sleep(1) #TODO: see if we can detect when page load is complete
    lyrics = browser.find_element_by_tag_name('p')
    ##Save lyrics text content to a text file
    newFile = open(track + ".txt", mode='w')
    newFile.write(lyrics.text)
    newFile.close()
    
browser.quit()
