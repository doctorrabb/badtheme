#!/usr/bin/python

from modules.net.validate import update_databases
from modules.const import THEMES_DB_REMOTE, WPCONFIG_DB_REMOTE, VERSION_REMOTE, EXPLOITS_REMOTE

if __name__ == '__main__':
	update_databases (WPCONFIG_DB_REMOTE, THEMES_DB_REMOTE, VERSION_REMOTE, EXPLOITS_REMOTE)
