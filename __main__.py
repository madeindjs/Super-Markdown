#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os
import webbrowser

from SuperMarkdown.SuperMarkdown import SuperMarkdown


__all__ = ['SuperMarkdown']

if __name__ == '__main__':

	# parse arg to find file(s)
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", 
		help="export the markdown file to export in HTML")
	parser.add_argument("-d", "--directory", 
		help="export the markdown files in the directory in HTML")
	args = parser.parse_args()


	superMarkdown = SuperMarkdown()


	if args.directory:# get all files from directory
		superMarkdown.add_toc()
		files=[file for file in os.listdir(args.directory) if not os.path.isdir(file)]
		superMarkdown.add_content(*files)

	elif args.file:# get the file from directory
		superMarkdown.add_content(args.file)

	else:# get the default markdown file `ressources/test.markdown`
		superMarkdown.add_content('SuperMarkdown/ressources/test.md')


	superMarkdown.export()

