# coding: utf8

from modules.util import *
from modules.const import ERR, OK, NO, INFO
from colorama import Fore
from sys import stdout

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
		print INFO + 'Started at ' + gettime ()
		print '-'*50
	elif op.target:
		TRG = op.target
		print INFO + 'Started at ' + gettime ()
		print '-'*50
	else:
		print ERR + 'Error getting target!'
		exit (-1)
	

	if not 'str' in str (type (TRG)):
		for i in TRG.readlines ():
			try:
				net.scan.check_once (i.strip ('\n').strip ('\r'), os.verbose)
			except KeyboardInterrupt:
				print '-'*50
				print INFO + 'Exiting... Finished at ' + gettime ()
				exit (0)
	else:
		try:
			net.scan.check_once (TRG, op.verbose)
		except KeyboardInterrupt:
			print '-'*50
			print INFO + 'Exiting... Finished at ' + gettime ()
			exit (0)

	if op.output is not None:
		from modules.fileop import save_output_file
		fileop.save_output_file (op.output, net.scan.FULL_LIST)


if __name__ == '__main__':
	main ()