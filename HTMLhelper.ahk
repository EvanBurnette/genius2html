#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;ctrl shift = ^ +
^+T::Send,<sup class="chords"></sup>{Left down}{Left up}{Left down}{Left up}{Left down}{Left up}{Left down}{Left up}{Left down}{Left up}{Left down}{Left up}
return
^+U::Send,^x<span class="drums-mute">^v</span>{Left down}{Left up}{Left down}{Left up}{Left down}{Left up}{Left down}{Left up}{Left down}{Left up}{Left down}{Left up}{Left down}{Left up}
return