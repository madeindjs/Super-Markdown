import os
import markdown
from markdown.extensions.toc import TocExtension



os.chdir('C:/Users/rousseaua/! Projets/Sketchup/FAQ')


try:
	file = open('_header.part','r')
	text = file.read()

	file = open('sketchup-faq.markdown', 'r', encoding='utf-8')
	text += file.read() 

	html = markdown.markdown(text, extensions=[TocExtension()] )

	file = open( 'sketchup-faq.html','w')   # Trying to create a new file or open one

	file.write(html + '</body></html>')

	file.close()

except:
	print('Something went wrong! Can\'t tell what?')
	sys.exit(0) # quit Python


md = markdown.Markdown(extensions=['markdown.extensions.toc'])
html = md.convert(text)