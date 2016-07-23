from colorama import Fore, init

init ()

BAD_THEMES_PATH = 'res/themes.json'
WPCONFIG_PATH = 'res/wpconfig.lst'
VERSION_FILE_PATH = 'version.json'

WPCONFIG_DB_REMOTE = 'https://raw.githubusercontent.com/doctorrabb/badtheme/master/res/wpconfig.lst'
THEMES_DB_REMOTE = 'https://raw.githubusercontent.com/doctorrabb/badtheme/master/res/themes.json'
VERSION_REMOTE = 'https://raw.githubusercontent.com/doctorrabb/badtheme/master/version.json'

WP_PAGES = ['wp-admin', 'wp-login.php', 'readme.html']

ERR = Fore.RED + '[!]' + Fore.RESET + ' '
OK = Fore.GREEN + '[+]' + Fore.RESET + ' '
NO = Fore.RED + '[-]' + Fore.RESET + ' '
INFO = Fore.CYAN + '[*]' + Fore.RESET + ' '