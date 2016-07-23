from colorama import Fore, init

init ()

BAD_THEMES_PATH = 'res/themes.json'
WPCONFIG_PATH = 'res/wpconfig.lst'
VERSION_FILE_PATH = 'version.json'

ERR = Fore.RED + '[!]' + Fore.RESET + ' '
OK = Fore.GREEN + '[+]' + Fore.RESET + ' '
NO = Fore.RED + '[-]' + Fore.RESET + ' '
INFO = Fore.CYAN + '[*]' + Fore.RESET + ' '