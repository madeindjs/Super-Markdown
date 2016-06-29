Super-Markdown
==============

a Python library to export a complex Markdown file into a standalone HTML file.


It will include:

* [Mermaid.js][mermaid.js] to create diagrams with javascript
* [graphviz][graphviz] to create Diagrams in 
 [Dot language](https://en.wikipedia.org/wiki/DOT_(graph_description_language))
* [Markdown-TOC][Markdown-TOC] to create Table of Content 
* [markdown-checklist][markdown-checklist] to support create Checklists
* [Github Flavoured MarkdownStylesheet][GFM]


Instalation
-----------

    git clone https://github.com/madeindjs/super-markdown.git
    cd super-markdown
    pip install -r requirements.txt


Usage
-----

### Basic usage

to export **one markdown file** in one **Html file**

    python markdown-exporter.py -f README.md

to export **many markdown file** in one **Html file**

    python markdown-exporter.py -d /home/alex/markdown_files/


Syntax
------

### Table of content

To create a [Table of content][Markdown-TOC] you just need to insert `[TOC]` 
in your markdown file


### Markdown

[Markdown-Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)


### Mermaid.js

[Mermaid.js Basic Syntax](https://knsv.github.io/mermaid/#flowcharts-basic-syntax)


### Dot Language

[Dot Language Cheatsheet](http://www.graphviz.org/content/dot-language)



    

Requirements
------------

First you need to install [graphviz](http://www.graphviz.org/Download..php) on
your computer

Then you need to install these python librairy

* [Python-Markdown][Python-Markdown] 
* [markdown-checklist][Python-Markdown]
* [graphviz][graphviz]
* [beautifulsoup4](https://pypi.python.org/pypi/beautifulsoup4)

You can do it quickly with this command


Author
------

[Rousseau Alexandre][madeindjs]

License
-------

[MIT](https://opensource.org/licenses/MIT)


[super-markdown]: https://github.com/madeindjs/Super-Markdown.git

[Python-Markdown]: https://pythonhosted.org/Markdown/
[graphviz]: https://pypi.python.org/pypi/graphviz
[Markdown-TOC]: https://pythonhosted.org/Markdown/extensions/toc.html
[markdown-checklist]: https://github.com/FND/markdown-checklist
[mermaid.js]: https://github.com/knsv/mermaid
[GFM]: https://gist.github.com/andyferra/2554919

[madeindjs]: https://github.com/madeindjs/