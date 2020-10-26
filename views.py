#!/usr/bin/python
# -*- coding: utf8 -*-
import os
from datetime import datetime
from os.path import isfile, join, exists
from datetime import datetime

import markdown
from flask import Flask, g, request, render_template, abort, make_response, url_for, send_from_directory
from flask_babel import Babel

app = Flask(__name__, static_url_path='/static')
app.config['BABEL_DEFAULT_LOCALE'] = 'sk'
app.config['FREEZER_DESTINATION'] = 'docs'
app.jinja_options = {'extensions': ['jinja2.ext.with_', 'jinja2.ext.i18n']}
babel = Babel(app)

SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
LOGO_PYCON = 'logo/pycon.svg'

LANGS = ('en', 'sk')
TIME_FORMAT = '%Y-%m-%dT%H:%M:%S+00:00'
NOW = datetime.utcnow().strftime(TIME_FORMAT)


def get_mtime(filename):
    mtime = datetime.fromtimestamp(os.path.getmtime(filename))
    return mtime.strftime(TIME_FORMAT)


SITEMAP_DEFAULT = {'prio': '0.1', 'freq': 'weekly'}
SITEMAP = {
    'sitemap.xml': {'prio': '0.9', 'freq': 'daily', 'lastmod': get_mtime(__file__)},
    'index.html': {'prio': '1', 'freq': 'daily'},
}
LDJSON = {
    "@context": "http://schema.org",
    "@type": "Organization",
    "name": "SPy o.z.",
    "url": "https://python.sk",
    "logo": "https://python.sk/static/img/logo/python.svg",
    "sameAs": [
        "https://facebook.com/pyconsk",
        "https://twitter.com/pyconsk",
        "https://www.linkedin.com/company/spy-o--z-",
        "https://github.com/pyconsk",
    ]
}


@app.before_request
def before():
    if request.view_args and 'lang_code' in request.view_args:
        g.current_lang = request.view_args['lang_code']
        request.view_args.pop('lang_code')


@babel.localeselector
def get_locale():
    # try to guess the language from the user accept
    # header the browser transmits. The best match wins.
    # return request.accept_languages.best_match(['de', 'sk', 'en'])
    return g.get('current_lang', app.config['BABEL_DEFAULT_LOCALE'])


def _get_template_variables(**kwargs):
    variables = {
        'title': 'Python.SK',
        'logo': LOGO_PYCON,
        'ld_json': LDJSON
    }
    variables.update(kwargs)

    if 'current_lang' in g:
        variables['lang_code'] = g.current_lang

        if g.current_lang not in LANGS:
            return abort(404)
    else:
        variables['lang_code'] = app.config['BABEL_DEFAULT_LOCALE']

    return variables


@app.route('/')
def landing_page():
    template_variables = _get_template_variables(li_index='active')
    template_variables['title'] += " - Slovak Python User Group"

    return render_template('index.html', **template_variables)


@app.route('/daruj/')
def daruj_page():
    template_variables = _get_template_variables(li_index='active')
    template_variables['title'] += " - Daruj"

    return render_template('daruj.html', **template_variables)


@app.route('/o_nas/')
def o_nas_page():
    template_variables = _get_template_variables(li_index='active')
    template_variables['title'] += " - O nás"

    return render_template('o_nas.html', **template_variables)


@app.route('/ucimepython/')
def ucimepython_page():
    template_variables = _get_template_variables(li_index='active')
    template_variables['title'] += " - Učíme Python"

    return render_template('ucimepython.html', **template_variables)


@app.route('/zapojsa/')
def zapojsa_page():
    template_variables = _get_template_variables(li_index='active')
    template_variables['title'] += " - Zapoj sa!"

    return render_template('zapojsa.html', **template_variables)


@app.route('/navody/')
def navody_page():
    template_variables = _get_template_variables(li_index='active')
    template_variables['title'] += " - Python návody"

    return render_template('navody.html', **template_variables)


@app.route('/navody/flappy/')
def navody_flappy_page():
    template_variables = _get_template_variables(li_index='active')
    template_variables['title'] += " - Hra Flappy Bird v PyGame Zero"

    return render_template('navody/flappy.html', **template_variables)


@app.route('/navody/scraping/')
def navody_scraping_page():
    template_variables = _get_template_variables(li_index='active')
    template_variables['title'] += " - Web Scraping v Pythone - BeautifulSoup a Requests"

    return render_template('navody/scraping.html', **template_variables)


@app.route('/navody/scraping/blog/')
def navody_scraping_blog_page():
    return render_template('navody/scraping_blog.html')


@app.route('/blog/')
def blog_page():
    template_variables = _get_template_variables(li_index='active')
    template_variables['title'] += " - Blog"

    blog_dir_path = join(os.getcwd(), "blog")

    template_variables['articles'] = []

    for filename in os.listdir(blog_dir_path):
        if filename.endswith(".md") and isfile(join(blog_dir_path, filename)):
            with open(join(blog_dir_path, filename), "r") as md_file:
                md = markdown.Markdown(extensions=['meta'])
                article_html = md.convert(md_file.read())
                article_link = filename.split(".")[0]

                article_meta = md.Meta

                if len(article_meta.get("title")):
                    article_title = " ".join(article_meta.get("title"))

                if len(article_meta.get("summary")):
                    article_summary = " ".join(article_meta.get("summary"))

                if len(article_meta.get("author")):
                    article_author = article_meta.get("author")[0]

                if len(article_meta.get("date")):
                    article_date = article_meta.get("date")[0]

                if article_meta.get("hidden"):
                    continue

                template_variables['articles'] += [
                    {'title': article_title,
                     'summary': article_summary,
                     'author': article_author, 'date': article_date, 'link': article_link},
                ]

    template_variables['articles'] = sorted(template_variables['articles'], key=lambda k: datetime.strptime(k['date'], '%d.%m.%Y'), reverse=True)

    return render_template('blog.html', **template_variables)


@app.route('/blog/images/<image_url>')
def blog_image(image_url):
    blog_dir_path = join(os.getcwd(), "blog", "images")

    if exists(join(blog_dir_path, image_url)):
        return send_from_directory(join(blog_dir_path), image_url, mimetype='image/gif')
    else:
        return "No IMG"


@app.route('/blog/<article_url>/')
def blog_detail_page(article_url):
    template_variables = _get_template_variables(li_index='active')

    blog_dir_path = os.getcwd() + "/blog"

    filename = f"{article_url}.md"

    if exists(join(blog_dir_path, filename)):
        with open(join(blog_dir_path, filename), "r") as md_file:

            extension_configs = {
                'smarty': {
                    'substitutions': {
                        'left-double-quote': '&bdquo;',
                        'right-double-quote': '&ldquo;'
                    }
                }
            }

            md = markdown.Markdown(extensions=['meta', 'markdown_captions', 'smarty'],extension_configs=extension_configs)

            article_html = md.convert(md_file.read())
            article_html = article_html.replace("<img src=\"", "<img src=\"/blog/")
            article_html = article_html.replace("<img ", "<img class='img-fluid' ")
            article_html = article_html.replace("<figure", "<figure class='mt-5 mb-5'")
            article_html = article_html.replace("<figcaption", "<figcaption class='text-center text-muted font-italic'")
            article_html = article_html.replace("<h1", "<h1 class='mt-5 mb-2'")
            article_html = article_html.replace("<h2", "<h2 class='mt-4 mb-2'")

            article_link = filename.split(".")[0]

            article_meta = md.Meta

            if len(article_meta.get("title")):
                article_title = " ".join(article_meta.get("title"))

            if len(article_meta.get("summary")):
                article_summary = " ".join(article_meta.get("summary"))

            if article_meta.get("bio"):
                article_bio = " ".join(article_meta.get("bio"))
            else:
                article_bio = None

            if len(article_meta.get("author")):
                article_author = article_meta.get("author")[0]

            if len(article_meta.get("date")):
                article_date = article_meta.get("date")[0]

            template_variables['article'] = {
                'title': article_title,
                'summary': article_summary,
                'author': article_author,
                'date': article_date,
                'link': article_link,
                'html': article_html,
                'bio': article_bio,
            }

            template_variables['title'] += f" - {article_title}"

    return render_template('blog_detail.html', **template_variables)


@app.route('/stity_seniorom/')
def stity_seniorom():
    template_variables = _get_template_variables(li_index='active')
    template_variables['title'] += " - Výzva pre domovy sociálnych služieb"

    return render_template('covid/stity_seniorom.html', **template_variables)


@app.route('/stity_seniorom/ziadost/')
def stity_seniorom_dss():
    template_variables = _get_template_variables(li_index='active')
    template_variables['title'] += " - Získaj ochranné štíty"
    template_variables['menu_items'] = [
        {"title": "Napíš list seniorom", "link": url_for('stity_seniorom_list')}]

    return render_template('covid/dss.html', **template_variables)


@app.route('/stity_seniorom/list/')
def stity_seniorom_list():
    template_variables = _get_template_variables(li_index='active')
    template_variables['title'] += " - Napíš Májový list seniorom"
    template_variables['menu_items'] = [
        {"title": "Požiadaj o ochranné štíty", "link": url_for('stity_seniorom_dss')}]

    return render_template('covid/list.html', **template_variables)


@app.route('/stity_seniorom/gdpr/')
def stity_seniorom_gdpr():
    template_variables = _get_template_variables(li_index='active')
    template_variables['title'] += " - Spracúvanie osobných údajov"
    template_variables['menu_items'] = [
        {"title": "Požiadaj o ochranné štíty", "link": url_for('stity_seniorom_dss')},
        {"title": "Napíš list seniorom", "link": url_for('stity_seniorom_list')},
    ]

    return render_template('covid/gdpr.html', **template_variables)


@app.route('/CNAME')
def gh_cname():
    return 'python.sk'


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    """Generate sitemap.xml. Makes a list of urls and date modified."""
    domain = 'https://python.sk'
    pages = []

    # static pages
    for rule in app.url_map.iter_rules():

        if "GET" not in rule.methods:
            raise Exception

        if 'lang_code' in rule.arguments:
            indx = rule.rule.replace('/<lang_code>/', '')

            for lang in LANGS:
                alternate = []

                for alt_lang in LANGS:
                    if alt_lang != lang:
                        alternate.append({
                            'lang': alt_lang,
                            'url': domain + rule.rule.replace('<lang_code>', alt_lang)
                        })

                sitemap_data = SITEMAP.get(indx, SITEMAP_DEFAULT)
                pages.append({
                    'loc': domain + rule.rule.replace('<lang_code>', lang),
                    'alternate': alternate,
                    # 'lastmod': get_lastmod(rule, sitemap_data),
                    'freq': sitemap_data['freq'],
                    'prio': sitemap_data['prio'],
                })
        elif rule.rule == '/sitemap.xml':
            indx = rule.rule.replace('/', '')
            sitemap_data = SITEMAP.get(indx, SITEMAP_DEFAULT)
            pages.append({
                'loc': domain + rule.rule,
                # 'lastmod': get_lastmod(rule, sitemap_data),
                'freq': sitemap_data['freq'],
                'prio': sitemap_data['prio'],
            })

    sitemap_xml = render_template('sitemap_template.xml', pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "text/xml"

    return response


if __name__ == "__main__":
    app.run(debug=True, host=os.environ.get('FLASK_HOST', '127.0.0.1'), port=int(os.environ.get('FLASK_PORT', 5100)))
