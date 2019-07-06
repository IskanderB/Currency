

import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()

def parse(html):
	soup = BeautifulSoup(html)
	table = soup.find('div', class_ = 'finance-currency-table__body')
	projects = []
	for row in table.find_all('a'):
		cols = row.find_all('div')

		projects.append({
			'title': cols[0].text.strip(),
			'par': cols[1].text.strip(),
			'currency': cols[2].text.strip(),
			'rate': cols[3].text.strip(),
			'changes': cols[4].text.strip(),
			'persent': cols[5].text.strip(),

			})
	return projects

def main():
	return parse(get_html('https://finance.rambler.ru/currencies/'))

if __name__ == '__main__':
	main()

