def init_option_parser ():
	from optparse import OptionParser

	op = OptionParser ('-t <url> [-T <file with targets> -v <verbose>')
	op.add_option ('-t', '--target', dest='target', type='string', help='use this option to set target\'s url')
	op.add_option ('-T', "--target-list", dest='targets', type='string', help='use this option to set file with targets')
	op.add_option ('-v', "--verbose", dest='verbose', default=False, action='store_true', help='use this option to set file with targets')
	(op, args) = op.parse_args ()

	return op

def url_pattern_exist (url, pattern):
	from requests import get
	if get (url + '/' + pattern + '/').status_code == 200:
		return True
	return False

def gettime ():
	from datetime import datetime 

	return str (datetime.now ().year) + '.' + str (datetime.now ().day) + ' - ' + str (datetime.now ().hour) + ':' + str (datetime.now ().minute)

def get_themes ():
	from json import loads
	from modules.const import BAD_THEMES_PATH

	str = ''

	with open (BAD_THEMES_PATH, 'r') as themes_file:
		for i in themes_file.readlines ():
			str += i
		themes_file.close ()

	return loads (str) ['list']

def get_wpconfigs ():
	from modules.const import WPCONFIG_PATH

	configs = list ()

	with open (WPCONFIG_PATH, 'r') as wpconfigs:
		for config in wpconfigs.readlines ():
			configs.append (config.strip ('\n').strip ('\r'))
		wpconfigs.close ()

	return configs

def getversion ():
	from modules.const import VERSION_FILE_PATH
	from json import loads

	str = ''

	with open (VERSION_FILE_PATH, 'r') as f:
		for i in f.readlines ():
			str += i
		f.close ()

	return loads (str)