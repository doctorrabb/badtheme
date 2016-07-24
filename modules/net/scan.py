from colorama import Fore
from modules.const import OK, INFO, NO
from modules.util import *

FULL_LIST = list ()

def check_once (target, verbose=False):

	print INFO + 'Checking ' + target + '...'
	th = check (target, verbose)
	if len (th) > 0:
		print OK + 'Bad items were found at url ' + Fore.CYAN + target + Fore.RESET
		for good in th:
			print '\t|Bad item found ' + Fore.GREEN + good + Fore.RESET

	else:
		print NO + 'Bad items were not found at url ' + Fore.CYAN + target + Fore.RESET + ' :('
			

def check (trg, verbose=False):

	from json import loads

	goods = list ()
	global FULL_LIST

	for theme in get_themes ():
		print INFO + 'Checking item ' + Fore.CYAN + theme ['name'] + Fore.RESET +' from database...'
		if url_pattern_exist (trg, theme ['path']):
				print OK + 'Bad item ' + Fore.CYAN + theme ['name'] + Fore.RESET + ' found! Explotation url: ' + Fore.RED + trg + theme ['path'] + Fore.RESET

				for exploit in get_exploits ():
					if theme ['type'] == exploit ['type-name']:
						if raw_input ('Run exploit ' + exploit ['name'] + ' for ' + theme ['name'] + '? (y/n): ') == 'y':
							print INFO + 'Preparing exploit...'
							exploit_validate (exploit ['path'], trg + theme ['path'])
							import webbrowser
							import os

							webbrowser.open (os.path.abspath (exploit ['path'] + 'moded.html'))
							exit (0)

				goods.append (theme ['name'])
				FULL_LIST.append ({'name': theme ['name'], 'url': trg + theme ['path'], 'hackable': True})
		else:
				FULL_LIST.append ({'name': theme ['name'], 'url': trg + theme ['path'], 'hackable': False})

			

	return goods

def is_good_response (url):
	from requests import get

	try:
		if get (url).status_code == 200:
			return True
	except: pass

	return False