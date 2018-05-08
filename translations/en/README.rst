Python SK website
####################

.. image:: https://d322cqt584bo4o.cloudfront.net/pythonsk-website/localized.svg

`Zobraziť README.rst v Slovenčine <https://github.com/pythonsk/python.sk-website/blob/master/README.rst>`_

Website `python.sk <https://www.python.sk>`_, built with `Flask <http://flask.pocoo.org/>`_ from which static HTML is generated.

Contributing
-----------

From community to the community. Website is managed by volunteers and we'll be happy if you'll join us. Contributions are welcome. Read our `contribution guide <https://github.com/pythonsk/python.sk-website/blob/master/translations/en/CONTRIBUTING.rst>`_ and feel free to join, we would love to hear from you!


Project structure
------------------

**1 branch**:

- ``master`` - the Flask app, templates, static files.

**Directories**

- ``root`` - Flask app is in root directory.
- ``docs`` - Generated static `website www.python.sk <https://www.python.sk>`_. **Do not edit files in this directory, because they will be re-generated!** Steps how to generate is written below.


Installation
----------

We use Python 3 for development. Commands are made for terminal in Linux, and should work in Mac OS.

- clone repository locally::

    git clone https://github.com/pythonsk/python.sk-website
    cd python.sk-website

- creates a virtual environment (module venv is part of Python 3) and installs all requirements::

    python3 -m venv envs3

- activate virtual environments::

    source envs3/bin/activate

- install requirements::

    pip install -r requirements.txt

- start flask server, and you can view it in the browser (http://127.0.0.1:5000)::

    python views.py


If you find some bug please do report it! Please create `issue on GitHube <https://github.com/pythonsk/python.sk-website/issues?template=Bug_report_en.md>`_. If you have an idea for an improvement, you can create a `issue on GitHube <https://github.com/pythonsk/python.sk-website/issues?template=Feature_request_en.md>`_ or visit us on our `public chat <https://riot.python.sk/#/room/#general:python.sk>`_ or write us an email: `info@python.sk <mailto:info@python.sk>`_.


Translations
--------

Help us to translate website in more languages. You don't need to know how to program in order to participate on translations, it is enought to know the language. Translations are done via `crowdin.com <https://crowdin.com/project/pythonsk-website>`_ service.


Generate static site
-----------------------------

`Frozen-Flask <https://pythonhosted.org/Frozen-Flask/>`_ freezes a Flask application into a set of static files. The result can be hosted without any server-side software other than a traditional web server.

- generate static files, and you can find them in ``docs`` directory::

    python freezer.py

- verify the generated result in browser (http://127.0.0.1:8000/en/index.html)::

    cd docs
    python -m SimpleHTTPServer 8000


Continuous Deployment
---------------------

Anything committed to master branch ``docs`` directory will be automatically deployed on live server. Live site contain only generated static site in ``docs`` directory.


Links
-------------

- web: `https://www.python.sk <https://www.python.sk/>`_, `https://www.micropython.sk <https://www.micropython.sk/>`_, `https://www.microbit.sk <https://www.microbit.sk/>`_
- chat: `https://riot.python.sk <https://riot.python.sk/#/room/#general:python.sk>`_
- email: `info@python.sk <mailto:info@python.sk>`_

License 
--------

MIT license for code (GitHub repo), CC-BY for content (if not stated otherwise). For more detail read the LICENSE file.
