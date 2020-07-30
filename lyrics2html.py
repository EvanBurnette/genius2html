import os
import sys

def Lyrics2html(filename, trackNumber, artist, album, prevSong, nextSong):

    textFile = open(filename + ".txt", mode='r')
    
    fileHTML = open(filename + '.html', mode='w')

    fileHTML.write("""<!DOCTYPE HTML>
    <html>

    <head>
        <link rel="stylesheet" href="../../songMapStyle.css">
    </head>""")
    fileHTML.write("<h1>" + str(trackNumber) + " " + filename.upper() + " " + artist.upper() + " " + album.upper() + "</h1>")

    for line in textFile:
        if line[-1] == '\n':
            line = line[:-1]
        else:
            pass
        
        if line == '':
            fileHTML.write(line + '\n');
        elif (line[0] == '[' and line[-1] ==']'):
            fileHTML.write("</div><h2><span>" + line[1:-1].upper() + """</span>\n
                <span class="drums">DRUMS</span>
                <span class="synth">SYNTH</span>
                <span class="chords">CHORDS</span>
                <span class="bass">BASS</span></h2>\n<div>""")
        else:
            fileHTML.write("<span>" + line + "</span><br>\n")

    fileHTML.write('''<span class="bottom-nav"><a href="''' + prevSong + '''.html">Previous Song</a><a href="trackList.html">TrackList</a>
                    <a href="''' + nextSong + '''.html">Next Song</a></span></body></html>''')

    textFile.close()

    fileHTML.close()

def trackList2html(tracks, artist, album):
    trackListHTML = open("trackList.html", mode='w')
    trackListHTML.write("""<!DOCTYPE HTML>
    <html>

    <head>
        <link rel="stylesheet" href="../../songMapStyle.css">
    </head>""")
    trackListHTML.write("<h1>" + artist.upper() + " " + album.upper() + " SONG MAPS</h1>")
    for track in tracks:
        trackListHTML.write('''<a href="''' + track + '''.html">''' + track + '''</a><br>''')
    trackListHTML.write("</body></html>")
    trackListHTML.close()
        

albumDir = sys.argv[1]
os.chdir(albumDir)

workingDir = os.getcwd().split('\\')
print(workingDir)
artist = workingDir[-2]
album = workingDir[-1]    
    
trackFile = open("trackList.txt", mode='r')
tracks = trackFile.read().split("\n")
trackFile.close()

prevSong = ""
nextSong = ""

for i in range(len(tracks)):
    if i+1 == len(tracks):
        nextSong = "#"
    else:
        nextSong = tracks[i+1]
    if i == 0:
        prevSong = "#"
    else:
        prevSong = tracks[i-1]
    
    Lyrics2html(tracks[i], i+1, artist, album, prevSong, nextSong)

trackList2html(tracks, artist, album)
