#!/usr/bin/python
# coding: utf8

from modules.net.scan import *

from modules.const import ERR, OK, NO, INFO
from colorama import Fore

FULL_GOODS_LIST = list ()


def main ():

	print '''{0}
		__________             .______________.__                           
		\______   \_____     __| _/\__    ___/|  |__   ____   _____   ____  
		 |    |  _/\__  \   / __ |   |    |   |  |  \_/ __ \ /     \_/ __ \ 
		 |    |   \ / __ \_/ /_/ |   |    |   |   Y  \  ___/|  Y Y  \  ___/ 
		 |______  /(____  /\____ |   |____|   |___|  /\___  >__|_|  /\___  >
		        \/      \/      \/                 \/     \/      \/     \/ 
{1}
		  [DEVELOPER] {2}{3}{1}
		  [VERSION] {2}{4}{1}
		  [CODENAME] {2}{5}{1}

		  Follow me on GitHub: {6}
	'''.format (Fore.RED, Fore.RESET, Fore.CYAN, 
				getversion () ['developer'], 
				getversion () ['release'], 
				getversion () ['codename'], 
				getversion () ['github']
			)

	op = init_option_parser ()

	TRG = None

	if op.targets:
		TRG = open (op.targets, 'r')
	elif op.target:
		TRG = op.target
	else:
		print ERR + 'Error getting target!'
		exit (-1)

	print INFO + 'Started at ' + gettime ()
	print '-'*50

	try:
		if not 'str' in str (type (TRG)):
			for i in TRG.readlines ():
				if not is_good_response (TRG):
					print ERR + 'Site ' + i.strip ('\n').strip ('\r') + ' is unavailable! :('
				check_once (i.strip ('\n').strip ('\r'), os.verbose)
		else:
				if not is_good_response (TRG):
					print ERR + 'Site is unavailable! :('
					exit (-1)
				check_once (TRG, op.verbose)
		if op.output is not None:
			from modules.fileop import save_output_file
			save_output_file (op.output, FULL_LIST)
	except KeyboardInterrupt:
			print '-'*50
			print INFO + 'Exiting... Finished at ' + gettime ()
			exit (0)


if __name__ == '__main__':
	main ()