from modules.const import BAD_THEMES_PATH, WPCONFIG_PATH
from requests import get

from modules.const import INFO, OK, ERR

def update_databases (wpconfig_url, themes_url):
	print INFO + 'Update started!'
	try:
		print INFO + 'Updating vulnerability themes database...'
		with open (BAD_THEMES_PATH, 'w') as out:
			out.write (get (themes_url).text)
		out.close ()

		print OK + 'Vulnerability themes database updated successfully!'

		print INFO + 'Updating wp-config.php pathes database...'
		with open (WPCONFIG_PATH, 'w') as out:
			out.write (get (wpconfig_url).text)
		out.close

		print OK + 'wp-config.php pathes database updated successfully!'

		print OK + 'Databases update complete!'
	except:
		print ERR + 'Error updating databases!'
		exit (-1)