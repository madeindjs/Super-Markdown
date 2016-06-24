import argparse
import os
import sys
import webbrowser
# I haven't internet conection to install now :(
import markdown
from markdown.extensions.toc import TocExtension



if __name__ == '__main__':

	def get_text_file(url):
		"""return the content of all files"""
		try:
			with open(url ,'r', encoding='utf-8') as file:
				return file.read()
		except FileNotFoundError :
			print('File `{}` not found'.format(url))
			sys.exit(0)

	def get_ressources(directory):
		"""return all files content in a directory in a big big string"""
		ret = str()
		for file in os.listdir(directory):
			ret += get_text_file('{}/{}'.format(directory, file))

		return ret



	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", help="Specify the markdown file to export in HTML")
	args = parser.parse_args()

	css_dir = 'ressources/css'
	js_dir = 'ressources/js'
	url_md_file = str()

	if args.file: 
		url_md_file = args.file
	else: 
		url_md_file = 'ressources/test.markdown'


	text = get_text_file('ressources/snippet.html')

	# insert all files ressources in text
	text = text.replace('<<styles_here>>', get_ressources('ressources/css'))
	text = text.replace('<<scripts_here>>', get_ressources('ressources/js'))


	markdown_text = get_text_file( url_md_file )
	markdown_html = markdown.markdown(markdown_text, 
		extensions=[
			TocExtension(), 
			'fenced_code', 
			'markdown_checklist.extension'] )
	text = text.replace('<<content>>', markdown_html)

	export_url = 'export.html'

	try:
		file = open(export_url,'w', encoding='utf-8')
		file.write(text)
		webbrowser.open_new_tab(export_url)
	except FileNotFoundError :
		print('Can\'t open/create `export.html` file (maybe already opened?)')
	finally:
		file.close()
