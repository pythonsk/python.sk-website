Prispievateľská príručka
========================

`Switch CONTRIBUTING.rst to English <https://github.com/pythonsk/python.sk-website/blob/master/translations/en/CONTRIBUTING.rst>`_

Sme vďační za každého dobrovoľníka, ktorý sa zapojí do práce na na web stránke `www.python.sk <https://www.python.sk>`_. Ak nám chceš pomôcť, je viacero možností. Podľa toho, čo vieš robiť a tiež čo by si chcel/a robiť (nemusí to byť vývoj), môžeš si vybrať jednu z nasledujúcich aktivít:

Napíš blog, buď aktívny/a na sociálnych médiách alebo urob prednášku
--------------------------------------------------------------------

Veľmi pomôže, ak budeš šíriť informácie o `www.python.sk <https://github.com/pythonsk/python.sk-website>`_, alebo sa pripoj k `verejnému chatu <https://riot.python.sk/#/room/#general:python.sk>`_ a môžeš pomáhať ostatným či zdieľať svoje nápady a skúsenosti s ďalšími ľuďmi z komunity. Kontaktovať nás môžeš aj prostredníctvom emailu: `info@python.sk <mailto:info@python.sk>`_.

Aktualizuj dokumentáciu
-----------------------

`GitHub wiki <https://github.com/pythonsk/python.sk-website/wiki>`_ používame, aby sme usmernili ľudí a developerov. **Momentálne je prázdna, ale nejako začať musíme...** Ak nevieš, ako niečo urobiť, pravdepodobne sme to zabudli zapísať do wiki. Dokumentácia je nekonečný proces, takže vítame akékoľvek návrhy na zlepšenie, a preto pokojne vytváraj "issues" (problémy) v našom issue trackeri.

Ak sa ti zdá, že naša dokumentácia by mala byť upravená, alebo se na niečo zabudli, kľudne vytvor "pull request", alebo nás kontaktuj prostedníctvom nášho `verejného chatu <https://riot.python.sk/#/room/#general:python.sk>`_. Kontaktovať nás môžeš aj emailom: `info@python.sk <mailto:info@python.sk>`_.

Navrhuj zlepšenia alebo oznamuj chyby
--------------------------------------

Všetky issues/problémy sú vedené v `issue trackeri na Githube <https://github.com/pythonsk/python.sk-website/issues?template=Bug_report.md>`_, ak nájdeš bug, prosím vytvor na to issue, kde v krátkosti popíšeš, v čom je problém.

Ak je niečo, čo ti chýba a chcel/a by si, aby sme to implementovali, choď do `issue trackera na Githube <https://github.com/pythonsk/python.sk-website/issues?template=Feature_request.md>`_, vytvor issue a označ ju ako "enhancement" = vylepšenie. Ideálne ak na novej funkcionalite začneš aj pracovať (nezabudni to napísať do komentára). Pokiaľ si si neni istý či je funkcionality potrebná, alebo potrebuješ poradiť s implementáciou, kontaktuj prostedníctvom nášho `verejného chatu <https://riot.python.sk/#/room/#general:python.sk>`_. Kontaktovať nás môžeš aj emailom: `info@python.sk <mailto:info@python.sk>`_. Viac o vývoji sa dočítaš nižšie...


Aktualizuj python.sk
----------------------

Celý vývoj sa robí na `Githube <https://github.com/pythonsk/python.sk-website>`_. Ak sa rozhodneš pracovať na existujúcom probléme, **prosím napíš do issue komentár, že na tom pracuješ, aby neriešilo viac ľudí rovnakoý problém**. Vytvor si vlastný `fork <https://github.com/pythonsk/python.sk-website/fork>`_ a **v novej vetve aktualizuj kód**. Keď budeš spokojný/á so svojimi úpravami, vytvor `pull request <https://help.github.com/articles/using-pull-requests>`_ a my ho skontrolujeme a pridáme (merge) do existujúceho kódu hneď, ako to bude možné. Aby sme si uľahčili život, prosím rob všetku svoju prácu v `samostatnej vetve <https://git-scm.com/book/en/v1/Git-Branching>`_ (ak je tam viacero commitov, použijeme `squash merge <https://github.com/blog/2141-squash-your-commits>`_), ak tvoja zmena rieši nejakú issue, v názve vetvy a popise merge requestu by malo byť číslo problému/issue, aby boli na GitHube prelinkované.

Ak hľadáš pomoc
---------------

Ak potrebuješ s niečím pomôcť, navštív náš `každomesačný meetup v Bratislave <https://pycon.sk/sk/meetup.html>`_ alebo nám daj vedieť na `verejnom chate <https://riot.python.sk/#/room/#general:python.sk>`_. Kontaktovať nás môžeš aj emailom: `info@python.sk <mailto:info@python.sk>`_.

Návod pre developerov
=====================

Štandardy vývoja
----------------

* Používame PEP8 štandard s predĺženými riadkami na 119 znakov.

Nastavenie vývojového prostredia
--------------------------------

Toto je štandardná Flasková aplikácia. Postupuj podľa týchto krokov (na Linuxe, alebo Macu):

1. ``git clone git@github.com:YOUR-GITHUB-ACCOUNT/python.sk-website.git`` naklonuj si vlastný fork repozitára python.sk-website
2. ``cd python.sk-website`` vojdi do adresára projektu
3. ``python3 -m venv envs3`` vytvor virtuálne prostredie, kde môžeš inštalovať všetko potrebné
4. ``source envs3/bin/activate`` aktivuj virtuálne prostredie
5. ``pip install -r requirements.txt`` nainštaluj požadované knižnice
6. ``python views.py`` spusti lokálne vývojový server a skontroluj ho v prehliadači

Metodika vývoja
---------------

1. Vytvoríš `fork <https://github.com/pythonsk/python.sk-website/fork>`_ projektu (toto urobíš iba raz. Neskôr už fork budeš mať vo svojom GitHube, všetok vývoj budeš robiť vo svojom repozitári).
2. Naklonuj si lokálne vlastný fork ``git clone git@github.com:YOUR-GITHUB-ACCOUNT/python.sk-website.git``, pridaj si upstream remote, aby si mohol/mohla sťahovať aktualizácie do vlastného forku ``git remote add upstream https://github.com/pythonsk/python.sk-website.git``. Na push do upstreamu nebudeš mať oprávnenie, ale pravidelným sťahovaním ("pull") z upstreamu a pushom do vlastného forku budeš udržovať svoj kód aktuálny a predídeš konfliktom.
3. Vyber si `chybu/issue <https://github.com/pythonsk/python.sk-website/issues>`_ a do komentárov napíš, že budeš na nej pracovať.
4. Vo svojej lokálne kópii vytvor vetvu: ``git checkout -b XX-nova-funkcia`` (kde XX je číslo chyby).
5. Kódovanie:

   * Commituj, ako často potrebuješ. Je úplne jedno, či je kód medzi commitmi rozbitý.
   * Ulož svoju zmenu vo svojom repozitári na GitHube. Na server môžeš pushnúť svoj kód koľkokrát len chceš: ``git push origin XX-nova-funkcia``.
   * Merguj kód z upstreamu, kedykoľvek chceš: ``git pull upstream master``. Tu nás nezaujímajú správy o mergovaní, prípadne použi rebase, aby si sa ich zbavil. Nakoniec urobíme `squash merge <https://github.com/blog/2141-squash-your-commits>`_ (v hlavnej vetve na upstreame to bude vyzerať ako jeden commit).

6. Keď si so svojím kódom spokojný/á, klikni na tlačítko `pull request <https://help.github.com/articles/using-pull-requests>`_ a vyber si z upstreamu vetvu master a XX-nova-funkcia zo svojho repozitára. Potom sa spustia automatické testy, ktoré overia, či je všetko OK. Ak uvidíš nejké chyby, oprav ich a pushni opravu do svojej vetvy. Takto sa pull request zaktualizuje o opravy a testy sa spustia znova.
7. Ak niekto kontroluje tvoj kód a požiada ťa o zmenu, môžeš postupovať podľa bodu 5. Ak si so zmenami hotový/á, urob do pull requestu poznámku, aby sa mohla opäť urobiť revízia.
8. Tvoja funkcionalita je schválená a zmergovaná do mastra v upstreame, takže si môžeš otvorit vetvu master vo svojej lokálnej kópii: ``git checkout master`` a stiahnuť si novo schválené zmeny z upstreamu ``git pull upstream master``. Stiahnutie z upstreamu stiahne tvoju prácu (ako jeden commit do mastra) ktorú si urobil/a v samostatnej vetve. Teraz môžeš zmazať svoju lokálnu vetvu ``git branch --delete XX-nova-funkcia`` a aj vzdialenú ``git push origin :XX-nova-funkcia``

Zdá sa ti to príliš zložité? Netráp sa tým, keď budeš postupovať podľa vyššie uvedených krokov, uvidíš, že si na to ľahko zvykneš. Okrem toho, podobný postup sa používa v takmer každom väčšom open source projekte a podobne to chodí aj v korporátnom prostredí. Ak si nevieš rady, neváhaj a poď na náš `verejný chat <https://riot.python.sk/#/room/#general:python.sk>`_ a požiadaj o pomoc. Kontaktovať nás môžeš aj emailom: `info@python.sk <mailto:info@python.sk>`_.
