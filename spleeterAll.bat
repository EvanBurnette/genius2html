PUSHD "C:\\USERS\\EVANB\\DESKTOP\\ALT-J\\AN AWESOME WAVE"
FOR %%A in (*.WAV) DO (spleeter separate -o stems -p spleeter:4stems -i "%%A")
ECHO DONE!
PAUSE