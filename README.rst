Super-Markdown
==============

a Python library to export a complex Markdown file into a standalone HTML file.


It will include:

* `Mermaid.js <https://github.com/knsv/mermaid>`_ to create diagrams with javascript
* `graphviz <https://pypi.python.org/pypi/graphviz>`_ to create Diagrams in [Dot language][Dot language]
* `Markdown-TOC <https://pythonhosted.org/Markdown/extensions/toc.html>`_ to create Table of Content 
* markdown-checklist_ [markdown-checklist] to support create Checklists
* `Github Flavoured MarkdownStylesheet <https://gist.github.com/andyferra/2554919>`__





Instalation
-----------

Old School
``````````
you can install it with clone this repo::

    git clone https://github.com/madeindjs/super-markdown.git
    cd super-markdown
    python setup.py install


New School
``````````
Or you can install it with pip::

    pip install supermarkdown

Usage
-----

Command line usage
``````````````````

to export **one markdown file** in one **Html file**::

    super-markdown -f README.md

to export **many markdown file** in one **Html file**::

    super-markdown -d /home/alex/markdown_files/


API usage
`````````

Hello World
''''''''''''

::

    from SuperMarkdown import SuperMarkdown

    supermd = SuperMarkdown()
    content = "# Hello World\r\n"
    content += "[SuperMarkdown](https://github.com/madeindjs/Super-Markdown) is awesome!"

    supermd.add_content(text=content)
    supermd.export()


Add Table of Content
''''''''''''''''''''
::

    supermd.add_TOC(text=content)
    content = "## Other title\r\n## Other title\r\n###sutitle\r\n## Other title"
    supermd.add_content(text=content)
    supermd.export()



Add Dot Graph
'''''''''''''
::

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



Convert markdown file(s)
''''''''''''''''''''''''


one file
^^^^^^^^

::

    supermd = SuperMarkdown()
    supermd.add_content('/home/alex/markdown_files/a_file.md')
    supermd.export()



many files
^^^^^^^^^^

::

    files = os.listdir('/home/alex/markdown_files/')
    supermd = SuperMarkdown()
    supermd.add_content(*files)
    supermd.export()




Syntax
------

Table of content
````````````````

To create a [Table of content][TOC] you just need to insert `[TOC]` 
in your markdown file


Markdown
````````

`Markdown-Cheatsheet <https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>`_


Mermaid.js
``````````

`Mermaid.js Basic Syntax <https://knsv.github.io/mermaid/#flowcharts-basic-syntax>`_


Dot Language
````````````

`Dot Language Cheatsheet <http://www.graphviz.org/content/dot-language>`_

    

Requirements
------------

First you need to `download graphviz <http://www.graphviz.org/Download..php>`_ & install on your computer

Then you need to install these python libraries

* `Python-Markdown <https://pythonhosted.org/Markdown/>`_
* `markdown-checklist <https://github.com/FND/markdown-checklist>`_
* graphviz_
* `beautifulsoup4 <https://pypi.python.org/pypi/beautifulsoup4>`_

You can do it quickly with this command `pip install -r requirements.txt`


Author
------

`Rousseau Alexandre <https://github.com/madeindjs/>`_.

License
-------

`MIT <https://opensource.org/licenses/MIT>`_


.. _super-markdown: https://github.com/madeindjs/Super-Markdown.git
.. _graphviz: https://pypi.python.org/pypi/graphviz
.. _toc: https://pythonhosted.org/Markdown/extensions/toc.html
.. _python: http://www.python.org/
.. _markdown-checklist: https://github.com/FND/markdown-checklist
.. _mermaid-js: https://github.com/knsv/mermaid
.. _gfm: https://gist.github.com/andyferra/2554919
.. _dot-language: https://en.wikipedia.org/wiki/DOT_(graph_description_language)
.. _madeindjs: https://github.com/madeindjs/