from bs4 import BeautifulSoup
import requests
import threading
Google_news = 'https://news.google.com.mx/'

def set_robot():
	pass
def scraping_site():
	re = requests.get(Google_news)
	if re.status_code==200:
		soup = BeautifulSoup(re.text, 'html.parser')
		if soup is not None:
			articles = soup.find_all('h2',{'class':'esc-lead-article-title'})
			for article in articles:
				title = article.find('span',{'class':'titletext'}).getText()
				print title
	else:
		print 'error !!'

if __name__ == '__main__':
	scraping_site()