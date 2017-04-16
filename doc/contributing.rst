Contributors Guide
==================

We are happy with any volunteers involvement in `python.sk <https://github.com/pyconsk/www.python.sk>`_ website. If you would like to help us, there are multiple ways to do so. Depending on your skills and type of work you would like to do (doesn’t have to be development), we encourage you to start with any of the following:

Write a blog, get involved on social media or make a talk
---------------------------------------------------------

You can help out by spreading the word about `python.sk <https://github.com/pyconsk/www.python.sk>`_, or joining `public chat <https://riot.python.sk/#/room/#general:python.sk>`_ (if there is Slovak chatter, don't worry just start in English) to help others or share your ideas and experiences with people in community.

Update documentation
--------------------

`GitHub wiki <https://github.com/pyconsk/www.python.sk/wiki>`_ is used to guide people and developers the right way. **Currently it is empty and we have to start somehow...** If you don't know how to do something, we probably missed it in our wiki. Documentation is a never ending process so we welcome any improvement suggestions, feel free to create issues in our bug tracker.

If you feel that our documentation needs to be modified or we missed something, feel free to submit PR, or get in touch with us at our `public chat <https://riot.python.sk/#/room/#general:python.sk>`_ (if there is Slovak chatter, don't worry just start in English).

Suggest an improvement or report bug
------------------------------------

All issues are handled by `Github issue tracker <https://github.com/pyconsk/www.python.sk/issues>_`, if you've found a bug please create an issue for it.

If there is something you are missing, and wish to be implemented in `Github issue tracker <https://github.com/pyconsk/www.python.sk/issues>_`, feel free to create an issue and mark it as an enhancement.

Update python.sk
----------------

All development is done on `Github <https://github.com/pyconsk/www.python.sk>`_. If you decide to work on existing issue, **please mention in the issue comment that you are working on it so other people do not work on the same issue**. Create your `fork <https://github.com/pyconsk/www.python.sk/fork>`_ and **in new branch update code**. Once you are happy with your changes create `pull request <https://help.github.com/articles/using-pull-requests>`_ and we will review and merge it as soon as we can. To make the life easier please do all your work in a `separate branch <https://git-scm.com/book/en/v1/Git-Branching>`_ (if there are multiple commits we do `squash merge <https://github.com/blog/2141-squash-your-commits>`_), if there is a issue for your change should include the issue number in the branch name and merge request description so they are linked on GitHub.

Getting help
------------

If you look for help, visit our `monthly meetups in Bratislava <https://pycon.sk/sk/meetup.html>`_ or give us a shout at `public chat <https://riot.python.sk/#/room/#general:python.sk>`_ (if there is Slovak chatter, don't worry just start in English).

Developer's HowTo
=================

Development standards
---------------------

* We do use standard PEP8, with extended line to 119 characters.

Development setup
-----------------

This is standard Flask app. Follow steps in (in Linux, or Mac):

1. ``git clone git@github.com:YOUR-GITHUB-ACCOUNT/www.python.sk.git`` make a clone of your fork of python.sk
2. ``cd www.python.sk`` lets go inside the project directory
3. ``pyvenv envs3`` this will create virtual environments for you, where you can install all requirements needed
4. ``source envs3/bin/activate`` activate virtual environments
5. ``pip doc/requirements.txt`` install out main dependency
6. ``python views.py`` start development server, and check the app in browser

Development methodology
-----------------------

1. You create a `fork <https://github.com/pyconsk/www.python.sk/fork>`_ of the project (you do this only once. Afterwards you already have it in your GitHub, it is your repo in which you are doing all the development).
2. Clone your fork locally ``git clone git@github.com:YOUR-GITHUB-ACCOUNT/www.python.sk.git`` add upstream remote to be able to download updated into your fork ``git remote add upstream https://github.com/pyconsk/www.python.sk.git``. You don't have the right to push to upstream, but do regularly pull and push to your fork to keep it up-to-date and prevent conflicts.
3. Pick up a `issue <https://github.com/pyconsk/www.python.sk/issues>`_, and make a comment that you are working on it.
4. In your local git copy you create a branch: ``git checkout -b XX-new-feature`` (where XX is issue number).
5. Coding time:

   * Do commit how often you need. At this point doesn't matter if code is broken between commits.
   * Store your change in your repo at GitHub. You can push to server how many times you want: ``git push origin XX-new-feature``.
   * Merge the code from upstream as often as you can: ``git pull upstream master``. At this point we don't care about merge message, or rebase to get rid of it. We will do `squash merge <https://github.com/blog/2141-squash-your-commits>`_ (in upstream master it will looks like one commit).

6. Once you are happy with your code, you click on `pull request <https://help.github.com/articles/using-pull-requests>`_ button, and select master branch in upstream and XX-new-feature branch from your repo. At this point automated tests will be run if everything is OK, if you see some errors please fix them and push your fix into your branch. This way the pull request is updated with fixes and tests are run again.
7. In case reviewer asks for changes you can do all the things mentioned in point 5. Once happy with the changes make a note in pull request to review again.
8. Your feature is approved and merged to master of upstream, so you can check out master at your local copy: ``git checkout master`` and pull the newly approved changes from upstream ``git pull upstream master``. Pull from upstream will download your work (as one commit into master) that has been done in branch. Now you can delete your local branch ``git branch --delete XX-new-feature``, and also remote one ``git push origin :XX-new-feature``

Seems complicated? Dont worry once you start using this setup you will find out that it is easy get to used to. Besides similar setup is used in almost all large open source projects, and you might found similar setup in corporate environments as well. If you feel lost jump into our `public chat <https://riot.python.sk/#/room/#general:python.sk>`_ and ask for help.
