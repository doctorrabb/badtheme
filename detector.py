#!/usr/bin/python

from sys import argv
from modules.helpers.wpdetector import WordpressDetector

from modules.const import ERR, NO, OK, INFO

def main ():
	if len (argv) > 1:
		print INFO + 'Detecting wordpress...'
		wpd = WordpressDetector (argv [1])

		if wpd.detect_by_pages ():
			print OK + 'Wordpress Detected!'
			if raw_input ('Try to detect Wordpress version? (y/n): ') == 'y':
				print INFO + 'Detecting Wordpress version...'
				dec = wpd.detect_version ()
				if dec is not None:
					print OK + 'Wordpress Version Detected!' + dec
				else:
					print NO + 'Wordpress version getting failed!'

			exit (0)
		else:
			print NO + 'This is not Wordpress! :('
	else:
		print ERR + 'Example: ./detector.py http://blabla.com'


if __name__ == '__main__':
	main ()