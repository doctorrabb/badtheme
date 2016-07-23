# coding: utf8

from modules.util import *
from modules.const import ERR, OK, NO, INFO
from colorama import Fore


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
	'''.format (Fore.RED, Fore.RESET, Fore.CYAN, getversion () ['developer'], getversion () ['release'], getversion () ['codename'], getversion () ['github'])

	print INFO + 'Started at ' + gettime ()
	print '-'*50

	FULL_GOODS_LIST = list ()

	op = init_option_parser ()

	TRG = None

	if op.targets:
		TRG = open (op.targets, 'r')
	elif op.target:
		TRG = op.target
	else:
		print ERR + 'Error getting target!'
		exit (-1)
	

	if not 'str' in str (type (TRG)):
		for i in TRG.readlines ():
			try:
				check_once (i.strip ('\n').strip ('\r'), os.verbose)
			except KeyboardInterrupt:
				print '-'*50
				print INFO + 'Exiting... Finished at ' + gettime ()
				exit (0)
	else:
		try:
			check_once (TRG, op.verbose)
		except KeyboardInterrupt:
				print '-'*50
				print INFO + 'Exiting... Finished at ' + gettime ()
				exit (0)
			

def check_once (target, verbose=False):
	print INFO + 'Checking ' + target + '...'
	th = check (target, verbose)
	if len (th) > 0:
		print OK + 'Bad themes were found at url ' + Fore.CYAN + target + Fore.RESET
		for good in th:
			print '\t|Bad Theme found ' + Fore.GREEN + good + Fore.RESET

			FULL_GOODS_LIST.append ({"url": check (target), "goods": th})
	else:
		print NO + 'Bad themes were not found at url ' + Fore.CYAN + target + Fore.RESET + ' :('
			

def check (trg, verbose=False):

	goods = list ()

	for theme in get_themes ():
		print INFO + 'Checking theme ' + Fore.CYAN + theme ['name'] + Fore.RESET +' from database...'
		for conf in get_wpconfigs ():
			print '\t|Checking "wp-config.php" path ' + Fore.CYAN + conf + Fore.RESET + ' from database...'

			if verbose:
				print  '[VERBOSE]\t|Full path: ' + trg + theme ['path'] + conf

			if url_pattern_exist (trg, theme ['path'] + conf):
				goods.append (theme ['name'])

	return goods

if __name__ == '__main__':
	main ()