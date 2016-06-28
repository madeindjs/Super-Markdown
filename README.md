# Markdown Exporter

An Markdown exporter that will include more libraries in one standalone html 
file. It will include:

* [Mermaid.js][mermaid.js] to create beautifull diagrams
* [graphviz][graphviz] to create Diagrams in Dot languge
* [Markdown-TOC][Markdown-TOC] to create Table of Content, you just have to add
 a `[TOC]` a the right place in your Markdown file
* [markdown-checklist][markdown-checklist], a library to support Checklists
* [Github Flavoured Markdown][GFM], the Github Markdown Stylesheet

## Usage

to export **one markdown file** in one **Html file**

    python markdown-exporter.py -f README.md


to export **many markdown file** in one **Html file**

    python markdown-exporter.py -d /home/alex/markdown_files/

    

## Requirements

* [Python-Markdown][Python-Markdown] 
* [markdown-checklist][Python-Markdown]
* [graphviz][graphviz]
* [beautifulsoup4](https://pypi.python.org/pypi/beautifulsoup4)

Also, you need to install [graphviz](http://www.graphviz.org/Download..php)

## Author

[Rousseau Alexandre][madeindjs]

## License

[MIT](https://opensource.org/licenses/MIT)


[Python-Markdown]: https://pythonhosted.org/Markdown/
[graphviz]: https://pypi.python.org/pypi/graphviz
[Markdown-TOC]: https://pythonhosted.org/Markdown/extensions/toc.html
[markdown-checklist]: https://github.com/FND/markdown-checklist
[mermaid.js]: https://github.com/knsv/mermaid
[GFM]: https://gist.github.com/andyferra/2554919

[madeindjs]: https://github.com/madeindjs/