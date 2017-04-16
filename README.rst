Python SK Website
#################

Python SK Website, built with Flask from which static HTML is generated.


Contributing
------------

From community to the community. Contributions are welcome. Read our `contribution guide <https://github.com/pyconsk/www.python.sk/blob/master/doc/contributing.rst>`_ and feel free to join, we would love to hear from you.


Project structure
-----------------

**3 branches**:

- ``master`` - the Flask app, templates, static files.
- ``staging`` - static HTML, generated from the app in ``master`` branch (do NOT edit anything in here).
- ``live`` - static HTML, created by pushing the ``staging`` branch into ``live`` branch (do NOT edit anything in here).


Installation
------------

- clone repository locally::

    git clone https://github.com/pyconsk/www.python.sk.git
    cd python.sk

- creates a virtual environment (pyvenv is part of Python 3) and installs all requirements::

    pyvenv envs3

- activate virtual environments::

    source envs3/bin/activate

- install requirements::

    pip install -r doc/requirements.txt

- start flask server, and you can view it in browser (http://127.0.0.1:5000)::

    python views.py


If you find some bug please do report it! Feel free to submit suggestions as well, or join us in our `public chat <https://riot.python.sk/#/room/#general:python.sk>`_.


Links
-----

- web: https://www.python.sk
- chat: https://riot.python.sk/#/room/#general:python.sk


License
-------

MIT license for code (GitHub repo), CC-BY for content (if not stated otherwise). For more detail read the LICENSE file.
