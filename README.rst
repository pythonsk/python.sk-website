Python SK webstránka
#####################

`Webová stranka Python SK <https://www.python.sk>`_, založená na frameworku `Flask <http://flask.pocoo.org/>`_, z ktorého sa vygeneruje statické HTML.


Ako pomôct?
-----------

Od komunity pre komunity. Príspevky su viac než vítané. Prečítaj si našu `prispievateľskú príručku <https://github.com/pyconsk/www.python.sk/blob/master/doc/contributing.rst>`_ a pridaj sa k nám, radi budeme o tebe počuť!


Štruktúra projektu
------------------

**1 branch**:

- ``master`` - Flask aplikácia, šablony, statické súbory.

Inštalácia
----------

- Naklonujeme si repozitár lokálne ku sebe::

    git clone https://github.com/pyconsk/www.python.sk.git
    cd python.sk

- Vytvoríme si Python virtualné prostredie (pyvenv je súčasť Python 3) a nainštalujeme všetky potrebné závislosti::

    pyvenv envs3

- Aktivujeme Python virtuálne prostredie::

    source envs3/bin/activate

- Nainsštalujeme závislosti::

    pip install -r doc/requirements.txt

- Spustíme Flask server a prípadne otvoríme vo webovom prehliadači (http://127.0.0.1:5000)::

    python views.py


Pokiaľ nájdete chyby, prosím nahláste ich! Taktiež uvítame podnety od Vás, prípadne nás navštívte na našom verejnom chate
`<https://riot.python.sk/#/room/#general:python.sk>`_.


Webové odkazy
-------------

- web: `https://www.python.sk <https://www.python.sk/>`_
- chat: `https://riot.python.sk <https://riot.python.sk/#/room/#general:python.sk>`_

Licencia 
--------

MIT licencia pre kód (GitHub repo), CC-BY pre ostatný obsah (pokiaľ nie je stanovené ináč). Viac informácií o licenciách je v súbore LICENSE.

-----------------

Python SK Website
#################

`Python SK Website <https://www.python.sk>`_, built with `Flask <http://flask.pocoo.org/>`_ from which static HTML is generated.


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

- web: `https://www.python.sk <https://www.python.sk/>`_
- chat: `https://riot.python.sk <https://riot.python.sk/#/room/#general:python.sk>`_


License
-------

MIT license for code (GitHub repo), CC-BY for content (if not stated otherwise). For more detail read the LICENSE file.

