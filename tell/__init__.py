#!/usr/bin/env python3

from __future__ import print_function

from dbus.exceptions import DBusException
import notify2
import subprocess
import sys

def main():
	if len(sys.argv) <= 1 or sys.argv[1] in ('-h', '--help', '-help', '-?'):
		print('USAGE: tell COMMAND [args]')
		exit(0)

	# TODO: Prevent tell from running as root.

	try:
		notify2.init('Tell')
	except DBusException:
		print('\033[91mERROR\033[0m: Cannot connect to DBus. '  # red 'ERROR'
		      'Notificatons will not work.',
		      file=sys.stderr)
		print('Proceeding anyway.', file=sys.stderr)
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
	try:
		notify2.Notification(summary, body, icon).show()
	except notify2.UninittedError:
		print('Command complete. Could not notify due to DBus Error.',
		      file=sys.stderr)
		if return_value == 0:
			return_string = '\033[92m%d\033[0m' % return_value  # Green value
		else:
			return_string = '\033[91m%d\033[0m' % return_value  # Red value
		print('Return value was: %s' % return_string,
		      file=sys.stderr)
		exit(255)
	exit(return_value)


if __name__ == '__main__':
	main()
