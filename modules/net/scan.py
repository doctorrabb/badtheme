from colorama import Fore
from modules.const import OK, INFO, NO
from modules.util import *

FULL_LIST = list ()

def check_once (target, verbose=False):

	print INFO + 'Checking ' + target + '...'
	th = check (target, verbose)
	if len (th) > 0:
		print OK + 'Bad themes were found at url ' + Fore.CYAN + target + Fore.RESET
		for good in th:
			print '\t|Bad Theme found ' + Fore.GREEN + good + Fore.RESET

	else:
		print NO + 'Bad themes were not found at url ' + Fore.CYAN + target + Fore.RESET + ' :('
			

def check (trg, verbose=False):

	goods = list ()
	global FULL_LIST

	for theme in get_themes ():
		print INFO + 'Checking theme ' + Fore.CYAN + theme ['name'] + Fore.RESET +' from database...'
		for conf in get_wpconfigs ():
			print '\t|Checking "wp-config.php" path ' + Fore.CYAN + conf + Fore.RESET + ' from database...'

			if verbose:
				print  '[VERBOSE]\t|Full path: ' + trg + theme ['path'] + conf

			if url_pattern_exist (trg, theme ['path'] + conf):
				goods.append (theme ['name'])
				FULL_LIST.append ({'name': theme ['name'], 'url': trg + theme ['path'] + conf, 'hackable': True})
			else:
				FULL_LIST.append ({'name': theme ['name'], 'url': trg + theme ['path'] + conf, 'hackable': False})

	return goods