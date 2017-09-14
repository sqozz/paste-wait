#!/usr/bin/env python2
#
# ufh 2015
# original version: http://seclist.us/event_sniffer-linux-keylogger-based-on-devinputevent-devices.html
# many thanks!
# heavy modifications (mostly removal of features)
# sqozz 2017
#

import os
import sys
import evdev
import argparse

def run(args):
	dList = evdev.list_devices()
	try:
		dList.index(args.device)

	except ValueError as e:
		print('Problem opening input: ' + e)
		sys.exit(1)

	dev = evdev.InputDevice(args.device)
	name = dev.name
	phys = dev.phys

	for e in dev.read_loop():
		if e.type == evdev.ecodes.EV_KEY:

			# get the categorzied object
			ek = evdev.categorize(e)
			data = "%s" % ek.keycode
			# key_down
			if ek.keystate == 1:
				if data == "KEY_LEFTCTRL":
					leftPressed = True

				if data == "KEY_V" and leftPressed:
					sys.exit(1)

			if ek.keystate == 0:
				if data == "KEY_LEFTCTRL":
					leftPressed = False



def main():
	parser_desc = 'wait until paste'
	prog_desc = 'paste_wait.py'
	parser = argparse.ArgumentParser( prog = prog_desc, description = parser_desc)
	parser.add_argument('-d','--device',dest='device',required=False,action='store',help='different event device to sniff')
	args = parser.parse_args()
	if not args.device:
		devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
		for device in devices:
			if "keyboard" in device.name:
				args.device = device.fn
		if not args.device:
			args.device = '/dev/input/event0'

	run(args)

if __name__ == '__main__':
	main()
