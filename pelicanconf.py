#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import functools
import os
import posixpath
import random
from collections import OrderedDict
from hashlib import md5

AUTHOR = 'Comunidade Python MG'
SITENAME = 'Python-MG'
SITEURL = ''
THEME = 'malt'
PATH = 'content'
META_DESCRIPTION = '''A Python-MG é uma comunidade de usuários
(profissionais e amadores) da linguagem Python, onde prezamos pela troca de
conhecimento, respeito mútuo e diversidade (tanto de opinião
quanto de tecnologias).'''
META_KEYWORDS = ['python-mg', 'python', 'Belo Horizonte', 'desenvolvimento']
TIMEZONE = 'America/Sao_Paulo'
MALT_BASE_COLOR = 'red'
DEFAULT_LANG = 'pt'
SITE_LOGO = 'images/logo/logo.png'
SITE_LOGO_MOBILE = 'images/logo/logo.png'


WELCOME_TITLE = 'Seja bem vindo ao {}!'.format(SITENAME)
WELCOME_TEXT = 'Grupo de usuários da linguagem Python em Minas Gerais.'
SITE_BACKGROUND_IMAGE = 'images/banners/bh-pampulha.jpg'
FOOTER_ABOUT = '''A Python-MG é uma comunidade de usuários (profissionais e
                  amadores) da linguagem Python, onde prezamos pela troca de
                  conhecimento, respeito mútuo e diversidade (tanto de opinião
                  quanto de tecnologias).'''

ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

CATEGORIES_URL = 'blog/categorias'
CATEGORIES_SAVE_AS = 'blog/categorias/index.html'
CATEGORY_URL = 'blog/categorias/{slug}'
CATEGORY_SAVE_AS = 'blog/categorias/{slug}/index.html'

TAG_URL = 'blog/tags/{slug}'
TAG_SAVE_AS = 'blog/tags/{slug}/index.html'
TAGS_URL = 'blog/tags'
TAGS_SAVE_AS = 'blog/tags/index.html'

AUTHOR_URL = 'blog/autores/{slug}'
AUTHOR_SAVE_AS = 'blog/autores/{slug}/index.html'
AUTHORS_URL = 'blog/autores'
AUTHORS_SAVE_AS = 'blog/autores/index.html'

INDEX_SAVE_AS = "blog/index.html"

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['./.plugins']
PLUGINS = [
    'better_figures_and_images',
    'sitemap',
]

RESPONSIVE_IMAGES = True
PYGMENTS_STYLE = "perldoc"
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.2,
        'pages': 0.7
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    },
}

GITHUB_REPO = 'http://github.com/pythonmg/pythonmg.github.io'
GITHUB_BRANCH = 'pelican'
TWITTER = "@PythonMG"
OPEN_GRAPH_IMAGE = "/images/logo/logo.png"

# Navbar Links
NAVBAR_HOME_LINKS = [
    {
        "title": "Comunidade",
        "href": "comunidade",
    },
    {
        "title": "Membros",
        "href": "membros",
    },
    {
        "title": "Blog",
        "href": "blog",
    },
]

NAVBAR_BLOG_LINKS = NAVBAR_HOME_LINKS + [
    {
        "title": "Categorias",
        "href": "blog/categorias",
    },
    {
        "title": "Autores",
        "href": "blog/autores",
    },
    {
        "title": "Tags",
        "href": "blog/tags",
    },
]

SOCIAL_LINKS = (
    {
        "href": "https://github.com/pythonmg",
        "icon": "fa-github",
        "text": "GitHub",
    },
    {
        "href": "https://twitter.com/PythonMG",
        "icon": "fa-twitter",
        "text": "Twitter",
    },
    {
        "href": "https://www.facebook.com/uaipython",
        "icon": "fa-facebook",
        "text": "Facebook",
    },
    {
        "href": "https://groups.google.com/forum/#!forum/python-mg",
        "icon": "fa-envelope",
        "text": "Mailing List",
    },
    {
        "href": "https://telegram.me/joinchat/ADyifgM5UvBM95seWv33pA",
        "icon": "fa-paper-plane",
        "text": "Telegram",
    },
)

MEMBROS = OrderedDict((
    ("Cássio Botaro", {
        "email": "cassiobotaro@gmail.com",
        "twitter": "@cassiobotaro",
        "github": "cassiobotaro",
        "site": {
            "nome": "Import None",
            "href": "https://cassiobotaro.github.io",
        }
    }),
))

MALT_HOME = [
    {
        "color": "blue-grey lighten-5",
        "title": "O que Fazemos?",
        "items": [
            {
                "title": "Comunidade",
                "icon": "fa-comments",
                "text": "A Python MG se comunica através de " +
                "mailing lists e do grupo no telegram mas frequentemente são" +
                " promovidos encontros diversos, como almoços, " +
                "<em>coding dojos</em> e palestras. ",
                "buttons": [
                    {
                        "text": "Saiba Mais",
                        "href": "comunidade",
                    },
                ],
            },
            {
                "title": "Membros",
                "icon": "fa-users",
                "text": "A Python MG, " +
                        "apesar de extensa possui alguns " +
                        "colaboradores principais, " +
                        "responsáveis por organizar " +
                        "eventos, manter a comunicação ativa, " +
                        "divulgar eventos, " +
                        "redes sociais e etc. ",
                "buttons": [
                    {
                        "text": "Conheça",
                        "href": "membros",
                    },
                ],
            },
            {
                "title": "Projetos",
                "icon": "fa-briefcase",
                "text": "Atualmente a Python MG  possui poucos projetos " +
                        "em andamento:" +
                        "Traduções do Django-docs e Python on Campus.",
                "buttons": [
                    {
                        "text": "Mais detalhes",
                        "href": "projetos",
                    },
                ],
            },
        ]
    },
]


MALT_COMUNITY = [
    {
        'title': 'Mídias Sociais',
        'text': 'Siga a Python-MG  nas mídias sociais para ficar por dentro' +
        ' dos encontros, novidades e postagens do nosso blog.',
        'buttons': [
            {
                'text': '<i class="fa fa-twitter fa-2x"></i> Twitter',
                'href': 'https://twitter.com/PythonMG'
            },
            {
                'text': '<i class="fa fa-facebook fa-2x"></i> Facebook',
                'href': 'https://facebook.com/uaipython'
            },
            {
                'text': '<i class="fa fa-paper-plane fa-2x"></i> Telegram',
                'href': 'https://telegram.me/joinchat/ADyifgM5UvBM95seWv33pA'
            },
        ],
    },
    {
        'title': 'Meetup',
        'text': 'Nos encontramos duas vezes ao mês para trocar conhecimento.' +
        ' Veja nossa agenda de eventos.',
        'buttons': [
            {
                'text': '<i class="fa fa-calendar fa-2x"></i> Meetup',
                'href': 'http://www.meetup.com/' +
                'Belo-Horizonte-Python-User-Group/'
            },
        ],
    },
    {
        'title': 'Lista de emails',
        'text': 'Para quem curte o bom e velho email, ' +
        'temos a lista de discussão oficial da Python MG no google groups.',
        'buttons': [
            {
                'text': '<i class="fa fa-envelope fa-2x"></i> Lista',
                'href': 'https://groups.google.com/forum/#!forum/python-mg'
            },
        ],
    },
]


def GET_AVATAR(autor, membros):
    if autor in membros:
        if 'github' in membros[autor]:
            formatter = "https://avatars.githubusercontent.com/{}?size=250"
            username = membros[autor]['github']
        elif 'email' in membros[autor]:
            formatter = "http://www.gravatar.com/avatar/{}?s=250"
            username = md5(membros[autor]['email'].strip().lower()).hexdigest()
        elif 'twitter' in membros[autor]:
            formatter = "http://avatars.io/twitter/{}"
            username = membros[autor]['twitter']
            if username.startswith("@"):
                username = username[1:]
        else:
            formatter = "/theme/img/{}"
            username = "default_avatar.png"
    else:
        formatter = "/theme/img/{}"
        username = "default_avatar.gif"
    return formatter.format(username)


def GET_ARTICLE_IMAGE(article, root):
    if hasattr(article, 'image'):
        img = article.image
        if img.startswith('/'):
            img = img[1:]
        return img

    if not root:
        return ""

    base = os.path.join('content', root)
    banners = map(functools.partial(os.path.join, root),
                  os.walk(base).next()[2])
    random.seed(article.date)
    return random.choice(banners)


def GET_ARTICLE_AT_GITHUB(article, repo, branch):
    base = posixpath.relpath(article.source_path, os.getcwd())
    return posixpath.join(repo, 'tree/', branch, base)


def GET_LINK(link):
    if link.startswith('http://') or link.startswith('https://'):
        return link
    else:
        return '/' + link
