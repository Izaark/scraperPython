import urllib

def get_page(file_path):
	open_file = open(file_path,'w')
	html_file = urllib.urlopen('http://econpy.pythonanywhere.com/ex/001.html')
	html_file = html_file.read()

	open_file.write(html_file)
	open_file.close()

def get_tittle(file_path):
	open_file = open(file_path,'r')
	regex = '<div title="buyer-name">'
	regex_end = '</div>'

	for line in open_file.readlines():
		sentence = line.strip('\n')
		if regex in sentence:
			initial_post = sentence.find(regex)
			initial_post = initial_post + len(regex)
			final_post = sentence.find(regex_end)
			print sentence[initial_post:final_post]

if __name__ == '__main__':
	file_path = 'econpy.html'
	get_page(file_path)
	get_tittle(file_path)