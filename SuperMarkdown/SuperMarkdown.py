#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
import webbrowser
import tempfile

import markdown
from markdown.extensions.toc import TocExtension
from graphviz import  Source
from bs4 import BeautifulSoup



class SuperMarkdown(object):
	"""SuperMarkdown class"""

	resources_path = '{}/ressources'.format(os.path.dirname(__file__))
	export_url = '{}/export.html'.format(tempfile.gettempdir())


	def __init__(self):
		self.markdown_text = str()

		# create the main soup from the `snippert.html` file
		html_snippet = self._text_file('{}/snippet.html'.format(self.resources_path))
		self.main_soup = BeautifulSoup(
			html_snippet.encode('utf-8'), 'html.parser')
		self.add_stylesheets('{}/css/github_flavoured_markdown.css'.format(self.resources_path))
		self.add_stylesheets('{}/css/toc.css'.format(self.resources_path))



	def add_content(self, *markdown_files, text=None):
		"""add the content of the file(s) (or the text in string) in HTML body"""
		for markdown_file in markdown_files:
			self.markdown_text += self._text_file(markdown_file)

		if text: self.markdown_text += text



	def add_toc(self):
		"""add the table of content"""
		self.markdown_text += "\r\n \r\n [TOC] \r\n \r\n"



	def add_stylesheets(self, *css_files):
		"""add stylesheet files in HTML head"""
		for css_file in css_files:
			self.main_soup.style.append( self._text_file(css_file) )



	def add_javascripts(self, *js_files, text=None):
		"""add javascripts files in HTML body"""
		# create the script tag if don't exists
		if self.main_soup.script is None:
			script_tag = self.main_soup.new_tag('script')
			self.main_soup.body.append(	script_tag)

		for js_file in js_files:
			self.main_soup.script.append( self._text_file(js_file) )

		if text: self.main_soup.script.append(text)



	def export(self, url=export_url):
		"""return the object in a file"""

		with open(url,'w', encoding='utf-8') as file:
			file.write(self.build())
			webbrowser.open_new_tab(url)



	def build(self):
		"""convert Markdown text as html. return the html file as string"""
		markdown_html = markdown.markdown(self.markdown_text, extensions=[
				TocExtension(), 'fenced_code', 'markdown_checklist.extension'])
		markdown_soup = BeautifulSoup(markdown_html, 'html.parser')

		# include HighLight.js if there <code> tag anywhere
		if markdown_soup.find('code'):
			self._add_highlight()

		# include mermaid.js only if there are Mermaid graph
		if markdown_soup.find('code', attrs={'class':'mermaid'}):
			self._add_mermaid()

		# search in markdown html if there are Dot Graph & replace it with .svg result
		for dot_tag in markdown_soup.find_all('code', attrs={'class':'dotgraph'}):
			grap_svg = self._text_to_graphiz(dot_tag.string)
			graph_soup = BeautifulSoup( grap_svg, 'html.parser')
			dot_tag.parent.replaceWith( graph_soup )

		self.main_soup.body.append(markdown_soup)
		return self.main_soup.prettify()




	def _text_file(self, url):
		"""return the content of a file"""
		try:
			with open(url ,'r', encoding='utf-8') as file:
				return file.read()
		except FileNotFoundError :
			print('File `{}` not found'.format(url))
			sys.exit(0)



	def _text_to_graphiz(self, text):
		"""create a graphviz graph from text"""
		dot = Source( text, format='svg')
		return dot.pipe().decode('utf-8')



	def _add_mermaid(self):
		"""add js libraries and css files of mermaid.js"""
		self.add_javascripts(
			'{}/js/jquery-1.11.3.min.js'.format(self.resources_path),
			'{}/js/mermaid.min.js'.format(self.resources_path),
			text='mermaid.initialize({startOnLoad:true  });'
			)
		self.add_stylesheets('{}/css/mermaid.css'.format(self.resources_path))



	def _add_highlight(self):
		"""add js libraries and css files of Highlight.js"""
		self.add_javascripts(
			'{}/js/jquery-1.11.3.min.js'.format(self.resources_path),
			'{}/js/highlight.min.js'.format(self.resources_path),
			text="""$(document).ready(function() {
				  $('pre code').each(function(i, block) {
				    hljs.highlightBlock(block);
				  });
				});"""
			)
		self.add_stylesheets('{}/css/highlight.min.css'.format(self.resources_path))
