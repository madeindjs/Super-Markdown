#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import sys
import webbrowser

import markdown
from markdown.extensions.toc import TocExtension
from graphviz import  Source
from bs4 import BeautifulSoup



class SuperMarkdown(object):
	"""SuperMarkdown class"""

	def __init__(self):
		self.markdown_text = str()

		# create the main soup from the `snippert.html` file
		html_snippet = self._text_file('ressources/snippet.html')
		self.main_soup = BeautifulSoup(
			html_snippet.encode('utf-8'), 'html.parser')
		self.add_stylesheets('ressources/css/github_flavoured_markdown.css')
		self.add_stylesheets('ressources/css/toc.css')



	def add_content(self, *markdown_files):
		"""add the content of the file(s) in HTML body"""
		for markdown_file in markdown_files:
			self.markdown_text += self._text_file(markdown_file)



	def add_toc(self, markdown_file):
		"""add the table of content"""
		self.markdown_text += "\r\n[TOC]\r\n"



	def add_stylesheets(self, *css_files):
		"""add stylesheet files in HTML head"""
		for css_file in css_files:
			self.main_soup.style.append( self._text_file(css_file) )



	def add_javascripts(self, *js_files):
		"""add javascripts files in HTML body"""
		# create the script tag if don't exists
		if self.main_soup.script is None:
			script_tag = self.main_soup.new_tag('script')
			self.main_soup.body.append( script_tag)

		for js_file in js_files:
			self.main_soup.script.append( self._text_file(js_file) )



	def export(self, url='export.html'):
		"""return the object in a file"""
		with open(url,'w', encoding='utf-8') as file:
			file.write(self.build())
			webbrowser.open_new_tab(url)



	def _text_file(self, url):
		"""return the content of a file"""
		try:
			with open(url ,'r', encoding='utf-8') as file:
				return file.read()
		except FileNotFoundError :
			print('File `{}` not found'.format(url))
			sys.exit(0)



	def _add_mermaid_js(self):
		"""add js libraries and css files of mermaid js_file"""
		self.add_javascripts('ressources/js/jquery-1.11.3.min.js')
		self.add_javascripts('ressources/js/mermaid.min.js')
		self.add_stylesheets('ressources/css/mermaid.css')
		self.main_soup.script.append('mermaid.initialize({startOnLoad:true  });')



	def build(self):
		"""convert Markdown text as html. return the html file as string"""
		markdown_html = markdown.markdown(self.markdown_text, extensions=[
				TocExtension(), 'fenced_code', 'markdown_checklist.extension'])
		markdown_soup = BeautifulSoup(markdown_html, 'html.parser')

		# include jquery & mermaid.js only if there are Mermaid graph
		if markdown_soup.find('code', attrs={'class':'mermaid'}):
			self._add_mermaid_js()

		self.main_soup.body.append(markdown_soup)
		return self.main_soup.prettify()









if __name__ == '__main__':





	def text_to_graphiz(text):
		"""create a graphviz graph from text"""
		dot = Source( text, format='svg')
		return dot.pipe().decode('utf-8')




	


	superMarkdown = SuperMarkdown()


	# parse arg to find file(s)
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", 
		help="export the markdown file to export in HTML")
	parser.add_argument("-d", "--directory", 
		help="export the markdown files in the directory in HTML")
	args = parser.parse_args()



	if args.directory:# get all files from directory
		superMarkdown.add_toc()
		files=[file for file in os.listdir(args.directory) if not os.path.isdir(file)]
		superMarkdown.add_content(*files)

	elif args.file:# get the file from directory
		superMarkdown.add_content(args.file)

	else:# get the default markdown file `ressources/test.markdown`
		superMarkdown.add_content('ressources/test.markdown')



	# search in markdown html if there are Dot Graph & replace it with .svg result
	for dot_tag in superMarkdown.main_soup.find_all('code', attrs={'class':'dotgraph'}):
		graph_soup = BeautifulSoup( text_to_graphiz(dot_tag.string) , 'html.parser')
		dot_tag.parent.replaceWith( graph_soup )


	superMarkdown.export()



