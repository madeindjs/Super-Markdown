#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import sys
import webbrowser

import markdown
from markdown.extensions.toc import TocExtension
from graphviz import Digraph
from bs4 import BeautifulSoup



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


	# create the main soup from the `snippert.html` file
	text = get_text_file('ressources/snippet.html')
	soup = BeautifulSoup(text.encode('utf-8'), 'html.parser')

	# insert css files and js files
	soup.script.append( get_ressources('ressources/js') )
	soup.style.append( get_ressources('ressources/css') )

	# insert all files ressources in text
	graph = search_replace_graphiz()
	text = text.replace('<<graphiz_here>>',graph )


	# parse arg to find file(s)
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", 
		help="export the markdown file to export in HTML")
	parser.add_argument("-d", "--directory", 
		help="export the markdown files in the directory in HTML")
	args = parser.parse_args()


	# Get the markdown text from file(s)
	markdown_text = str()

	if args.directory:# get all files from directory
		markdown_text = "\r\n[TOC]\r\n"
		files=[file for file in os.listdir(args.directory) if not os.path.isdir(file)]
		for file in files:
			markdown_text+=get_text_file('{}\{}'.format(args.directory, file))
			markdown_text += "{rn}{sep}{rn}".format(rn="\r\n", sep="---------")

	elif args.file:# get the file from directory
		markdown_text = get_text_file( args.file )

	else:# get the default markdown file `ressources/test.markdown`
		markdown_text = get_text_file( 'ressources/test.markdown' )


	markdown_html = markdown.markdown(markdown_text, 
		extensions=[
			TocExtension(), 'fenced_code', 'markdown_checklist.extension'] )


	soup.body.append( BeautifulSoup(markdown_html, 'html.parser') )

	export_url = 'export.html'

	try:
		file = open(export_url,'w', encoding='utf-8')
		file.write(soup.prettify())
		webbrowser.open_new_tab(export_url)
	except FileNotFoundError :
		print('Can\'t open/create `export.html` file (maybe already opened?)')
	finally:
		file.close()

	
