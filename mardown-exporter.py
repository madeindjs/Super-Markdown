import argparse
import os
import webbrowser
# I haven't internet conection to install now :(
# import markdown
# from markdown.extensions.toc import TocExtension



if __name__ == '__main__':

	def get_text_file(url):
		"""return the content of all files"""
		with open(url ,'r') as file:
			return file.read()
		return False



	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", help="Specify the file to export in HTML")
	args = parser.parse_args()

	if args.file:

		# os.chdir('C:/Users/rousseaua/! Projets/Sketchup/FAQ')

		text = get_text_file('ressources/snippet.html')

		stylesheets = str()
		stylesheets += get_text_file('ressources/github_flavoured_markdown.css')
		stylesheets += get_text_file('ressources/toc.css')
		text = text.replace('<<styles_here>>', stylesheets)

		markdown_text = get_text_file('ressources/test.markdown')
		text = text.replace('<<content>>', markdown_text)

		export_url = 'export.html'
		file = open( export_url,'w')   # Trying to create a new file or open one
		file.write(text)
		file.close()
		webbrowser.open_new_tab(export_url)


		# md = markdown.Markdown(extensions=['markdown.extensions.toc'])
		# html = md.convert(text)

	else: print('Please specify a file to open')