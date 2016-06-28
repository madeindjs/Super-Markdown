import argparse
import os
import sys
import webbrowser
# I haven't internet conection to install now :(
import markdown
from markdown.extensions.toc import TocExtension

from graphviz import Digraph



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


	def search_replace_graphiz():
		dot = Digraph(comment='The Round Table', format='svg')
		dot.node('A', 'King Arthur')
		dot.node('B', 'Sir Bedevere the Wise')
		dot.node('L', 'Sir Lancelot the Brave')

		dot.edges(['AB', 'AL'])
		dot.edge('B', 'L', constraint='false')
		return dot.pipe().decode('utf-8')




	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", 
		help="export the markdown file to export in HTML")
	parser.add_argument("-d", "--directory", 
		help="export the markdown files in the directory in HTML")
	args = parser.parse_args()



	text = get_text_file('ressources/snippet.html')

	# insert all files ressources in text
	graph = search_replace_graphiz()
	print(graph)
	text = text.replace('<<graphiz_here>>',graph )

	text = text.replace('<<styles_here>>', get_ressources('ressources/css'))
	text = text.replace('<<scripts_here>>', get_ressources('ressources/js'))



	markdown_text = str()

	if args.directory:
		markdown_text = "\r\n[TOC]\r\n"
		files=[file for file in os.listdir(args.directory) if not os.path.isdir(file)]

		for file in files:
			markdown_text+=get_text_file('{}\{}'.format(args.directory, file))
			markdown_text += "{rn}{sep}{rn}".format(rn="\r\n", sep="---------")

	elif args.file: 
		markdown_text = get_text_file( args.file )

	else:
		markdown_text = get_text_file( 'ressources/test.markdown' )


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

	
