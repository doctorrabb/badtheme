from modules.const import WP_PAGES
import requests

class WordpressDetector (object):
	def __init__ (self, url):
		self.url = url

	def detect_by_pages (self):

		for i in WP_PAGES:
			if requests.get (self.url + '/' + i).status_code != 404:
				return True

		return False

	def detect_version (self):
		req = requests.get (self.url + '/readme.html')

		if req.status_code != 404:
			from bs4 import BeautifulSoup

			bs = BeautifulSoup (req.text, 'lxml')
			return bs.find ('h1', id='logo').text

		return None