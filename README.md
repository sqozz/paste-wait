## What is this?
A small script which uses one device from /dev/input/ and waits until "ctrl + v" is pressed. Then it exits.
`~/scripts/paste_wait/paste_wait.py -d /dev/input/event5`

## Why?
It's intendet to run after i requested a new password from my password manager. Technically speaking I want 
to request the username for a stored password frist. After that, wait until "ctrl + v" (aka. "paste") is pressed - 
hence the username is not anymore required. After that, copy the password out of the password manager. Finally
wait until a second paste and clear the clipboard.

## Features
* tiny
* pretty solid

## Credits
The whole original code is from here: http://seclist.us/event_sniffer-linux-keylogger-based-on-devinputevent-devices.html OR https://github.com/your-favorite-hacker/event_sniffer.
