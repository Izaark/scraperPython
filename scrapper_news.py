from bs4 import BeautifulSoup
import requests
import threading


Google_news = 'https://news.google.com.mx/'
Custome_target = 'www.milenio.com'

def get_beautiful_soup(href):
	re = requests.get(href)
	if re.status_code==200:
		return BeautifulSoup(re.text, 'html.parser')

def set_robot(article):
	title = article.find('span',{'class':'titletext'}).getText()
	href = article.find('a').get('href')
	
	if Custome_target in href:
		soup = get_beautiful_soup(href)
		if soup is not None:
			container = soup.find('div',{'itemprop':"articleBody", 'class':"mce-body mce"})
			paragraphs = container.find_all('p')

			final_article = ''
			for paragraph in paragraphs:
				final_article = '{} {}'.format(final_article, paragraph)
				print final_article

def scraping_site():
	soup = get_beautiful_soup(Google_news)
	if soup is not None:
		articles = soup.find_all('h2',{'class':'esc-lead-article-title'})
		for article in articles:
			robot = threading.Thread(name='set_robot',target=set_robot, args =(article,))
			robot.start()			
	else:
		print 'error !!'

if __name__ == '__main__':
	scraping_site()