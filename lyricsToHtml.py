import os

filename = sys.argv[1]

openFile = open(filename, mode='r')

filenameHtml = filename[:-4] + '.html'

newFile = open(filenameHtml, mode='w')

newFile.write("""<!DOCTYPE HTML>
<html>

<head>
    <link rel="stylesheet" href="songMapStyle.css">
    </style>
</head>""")

for line in openFile:
    if line[-1] == '\n':
        line = line[:-1]
    else:
        pass
    
    if line == '':
        newFile.write(line + '\n');
    elif (len(line) > 2 and line[0] == '[' and line[-1] ==']'):
        newFile.write("</div><h2><span>" + line[1:7].upper() + """</span>\n
            <span class="drums">DRUMS</span>
            <span class="synth">SYNTH</span>
            <span class="chords">CHORDS</span>
            <span class="bass">BASS</span></h2>\n<div>""")
    else:
        newFile.write("<span>" + line + "</span><br>\n")

newFile.write("""<a href="#">Previous Song</a><a href="#">Next Song</a>

</body>

</html>""")

openFile.close()
newFile.close()
