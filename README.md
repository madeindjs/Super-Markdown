Super-Markdown
==============

a Python library to export a complex Markdown file into a standalone HTML file.


It will include:

* [Mermaid.js][mermaid.js] to create diagrams with javascript
* [graphviz][graphviz] to create Diagrams in [Dot language][Dot language]
* [Markdown-TOC][TOC] to create Table of Content 
* [markdown-checklist][markdown-checklist] to support create Checklists
* [Github Flavoured MarkdownStylesheet][GFM]


Instalation
-----------

### Old School

    git clone https://github.com/madeindjs/super-markdown.git
    cd super-markdown
    python setup.py install

### New School

    pip install supermarkdown


Usage
-----

### Command line usage

to export **one markdown file** in one **Html file**

    super-markdown -f README.md

to export **many markdown file** in one **Html file**

    super-markdown -d /home/alex/markdown_files/


### API usage

#### Hello World

~~~Python
    from SuperMarkdown import SuperMarkdown

    supermd = SuperMarkdown()
    content = "# Hello World\r\n"
    content += "[SuperMarkdown](https://github.com/madeindjs/Super-Markdown) is awesome!"

    supermd.add_content(text=content)
    supermd.export()
~~~




#### Add [Table of Content][TOC]

~~~Python
    supermd.add_TOC(text=content)
    content = "## Other title\r\n## Other title\r\n###sutitle\r\n## Other title"
    supermd.add_content(text=content)
    supermd.export()
~~~




#### Add [Dot Graph][Dot language]

~~~Python
    dotgraph = """~~~dotgraph
        digraph "pet-shop" {
            graph [rankdir=LR]
            node [shape=plaintext]
            edge [arrowhead=vee arrowsize=2]
            parrot
            dead
            parrot -> dead
        }
        ~~~"""
    supermd.add_content(text=dotgraph)
    supermd.export()
~~~




#### Convert markdown file(s)

##### one file

~~~Python
    supermd = SuperMarkdown()
    supermd.add_content('/home/alex/markdown_files/a_file.md')
    supermd.export()
~~~


##### many files

~~~Python
    files = os.listdir('/home/alex/markdown_files/')
    supermd = SuperMarkdown()
    supermd.add_content(*files)
    supermd.export()
~~~


Syntax
------

### Table of content

To create a [Table of content][TOC] you just need to insert `[TOC]` 
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

You can do it quickly with this command `pip install -r requirements.txt`


Author
------

[Rousseau Alexandre][madeindjs]

License
-------

[MIT](https://opensource.org/licenses/MIT)


[super-markdown]: https://github.com/madeindjs/Super-Markdown.git

[Python-Markdown]: https://pythonhosted.org/Markdown/
[graphviz]: https://pypi.python.org/pypi/graphviz
[TOC]: https://pythonhosted.org/Markdown/extensions/toc.html
[markdown-checklist]: https://github.com/FND/markdown-checklist
[mermaid.js]: https://github.com/knsv/mermaid
[GFM]: https://gist.github.com/andyferra/2554919
[Dot language]: https://en.wikipedia.org/wiki/DOT_(graph_description_language)

[madeindjs]: https://github.com/madeindjs/