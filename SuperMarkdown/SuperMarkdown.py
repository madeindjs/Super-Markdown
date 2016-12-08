#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import argparse
import webbrowser

import markdown
from markdown.extensions.toc import TocExtension
from graphviz import Source
from bs4 import BeautifulSoup


class SuperMarkdown(object):
    """SuperMarkdown class"""

    resources_path = '{}/ressources'.format(os.path.dirname(__file__))

    def __init__(self):
        self.markdown_text = str()

        # create the main soup from the `snippert.html` file
        html_snippet = self._text_file('{}/snippet.html'.format(self.resources_path))
        self.main_soup = BeautifulSoup(
            html_snippet.encode('utf-8'), 'html.parser')
        self.add_stylesheets('{}/css/github_flavoured_markdown.css'.format(self.resources_path))
        self.add_stylesheets('{}/css/toc.css'.format(self.resources_path))
        self.export_url = 'export.html'  # allow users to change it
        self.open_browser = True  # allow user to disable the opening of the web-browser

    def add_content(self, text=None, *markdown_files):
        """add the content of the file(s) (or the text in string) in HTML body"""
        for markdown_file in markdown_files:
            self.markdown_text += self._text_file(markdown_file)

        if text:
            self.markdown_text += text

    def add_toc(self):
        """add the table of content"""
        self.markdown_text += "\r\n \r\n [TOC] \r\n \r\n"

    def add_stylesheets(self, *css_files):
        """add stylesheet files in HTML head"""
        for css_file in css_files:
            self.main_soup.style.append(self._text_file(css_file))

    def add_javascripts(self, *js_files):
        """add javascripts files in HTML body"""
        # create the script tag if don't exists
        if self.main_soup.script is None:
            script_tag = self.main_soup.new_tag('script')
            self.main_soup.body.append(script_tag)

        for js_file in js_files:
            self.main_soup.script.append(self._text_file(js_file))

    def export(self):
        """return the object in a file"""

        with open(self.export_url, 'w', encoding='utf-8') as file:
            file.write(self.build())
            if self.open_browser:
                webbrowser.open_new_tab(self.export_url)

    def build(self):
        """convert Markdown text as html. return the html file as string"""
        markdown_html = markdown.markdown(self.markdown_text, extensions=[
                TocExtension(), 'fenced_code', 'markdown_checklist.extension',
                'markdown.extensions.tables'])
        markdown_soup = BeautifulSoup(markdown_html, 'html.parser')

        # include jquery & mermaid.js only if there are Mermaid graph
        if markdown_soup.find('code', attrs={'class': 'mermaid'}):
            self._add_mermaid_js()

        # search in markdown html if there are Dot Graph & replace it with .svg result
        for dot_tag in markdown_soup.find_all('code', attrs={'class': 'dotgraph'}):
            grap_svg = self._text_to_graphiz(dot_tag.string)
            graph_soup = BeautifulSoup(grap_svg, 'html.parser')
            dot_tag.parent.replaceWith(graph_soup)

        self.main_soup.body.append(markdown_soup)
        return self.main_soup.prettify()

    def _text_file(self, url):
        """return the content of a file"""
        try:
            with open(url, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print('File `{}` not found'.format(url))
            sys.exit(0)

    def _text_to_graphiz(self, text):
        """create a graphviz graph from text"""
        dot = Source(text, format='svg')
        return dot.pipe().decode('utf-8')

    def _add_mermaid_js(self):
        """add js libraries and css files of mermaid js_file"""
        self.add_javascripts('{}/js/jquery-1.11.3.min.js'.format(self.resources_path))
        self.add_javascripts('{}/js/mermaid.min.js'.format(self.resources_path))
        self.add_stylesheets('{}/css/mermaid.css'.format(self.resources_path))
        self.main_soup.script.append('mermaid.initialize({startOnLoad:true  });')


def main():
    """function to """
    # parse arg to find file(s)
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file",
                        help="convert the markdown file to HTML")
    parser.add_argument("-d", "--directory",
                        help="convert the markdown files in the directory to HTML")
    parser.add_argument("-o", "--output",
                        help="chose the output filename")
    parser.add_argument("--no_browser",  nargs='?', const=True,
                        help="if stated, will prevent browser from opening")
    args = parser.parse_args()

    print(args)

    superMarkdown = SuperMarkdown()

    if args.output:  # get the new output url
        superMarkdown.export_url = args.output

    if args.no_browser:
        superMarkdown.open_browser = False

    if args.directory:  # get all files from directory
        superMarkdown.add_toc()
        files = [file for file in os.listdir(args.directory) if not os.path.isdir(file)]
        superMarkdown.add_content(*files)

    elif args.file:  # get the file from directory
        superMarkdown.add_content(args.file)

    else:  # get the default markdown file `ressources/test.markdown`
        superMarkdown.add_content('SuperMarkdown/ressources/test.md')

    superMarkdown.export()
