def get_exploits ():
	from json import loads

	from modules.const import EXPLOITS_PATH

	str = ''

	with open (EXPLOITS_PATH, 'r') as f:
		for i in f.readlines ():
			str += i
		f.close ()

	return loads (str) ['exploits']

def exploit_validate (path, target):

	exploit = dict ()

	for i in get_exploits ():
		if i ['path'] == path:
			exploit = i
			break

	content = ''
	file = open (path, 'r')
	for i in file.readlines (): content += i
	file.close ()

	content = content.replace ('{{NAME}}', exploit ['name']).replace ('{{TARGET_URL}}', target).replace ('{{DESC}}', exploit ['description'])

	file = open (path + 'moded.html', 'w')
	file.write (content)
	file.close ()

def remove_tmp_exploits ():
	from modules.const import ALL_EXPLOITS_PATH
	import os

	for moded in os.listdir (ALL_EXPLOITS_PATH):
		if moded.endswith ('moded.html'):
			os.remove (ALL_EXPLOITS_PATH + moded)


def init_option_parser ():
	from optparse import OptionParser

	op = OptionParser ('-t <url> [-T <file with targets> -v <verbose> -o <output file>]')
	op.add_option ('-t', '--target', dest='target', type='string', help='use this option to set target\'s url')
	op.add_option ('-T', "--target-list", dest='targets', type='string', help='use this option to set file with targets')
	op.add_option ('-v', "--verbose", dest='verbose', default=False, action='store_true', help='use this option to enable verbose mode')
	op.add_option ('-o', "--output", dest='output', help='use this option to write goods at output file')
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