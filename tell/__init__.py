#!/usr/bin/env python3

import notify2
import subprocess
import sys

def main():
	if len(sys.argv) <= 1 or sys.argv[1] in ('-h', '--help', '-help', '-?'):
		print('USAGE: tell COMMAND [args]')
		exit(0)

	# TODO: Prevent tell from running as root.

	notify2.init('Tell')
	command_string = ' '.join(sys.argv[1:])
	return_value = subprocess.call(command_string, shell=True)
	if return_value == 0:
		summary = 'Command completed successfully'
		body = 'Success running %s' % sys.argv[1]
		icon = 'dialog-information'
	else:
		summary = 'Command completed with error'
		body = 'Exit code %d from %s' % (return_value, sys.argv[1])
		icon = 'dialog-error'
	notify2.Notification(summary, body, icon).show()


if __name__ == '__main__':
	main()