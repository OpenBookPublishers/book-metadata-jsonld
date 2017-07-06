"""
This file contains the definition of a book needed to produce JSON-LD
scripts following the http://schema.org/Book format.

(c) Javier Arias, Open Book Publishers, June 2017
Use of this software is governed by the terms of the GPLv3 -- see LICENSE
"""

formats = [ "Paperback", "Hardback", "PDF", "Epub", "Mobi" ]
roles = [ "Author", "Editor", "Foreword", "Introduction",
          "Music editor", "Preface", "Translator" ]

class Contributor(object):
    def __init__(self, name, surname, role):
        self.name = name
        self.surname = surname
        self.role = role

class Publisher(object):
    def __init__(self, name, shortname, url, logo, description):
        self.name = name
        self.shortname = shortname
        self.url = url
        self.logo = logo
        self.description = description

class Book(object):
    def __init__(self, title, isbn, doi, desc, url, keyw, cover, genre, lang, pages, pubdate):
        self.title = title
        self.isbn = isbn
        self.doi = doi
        self.desc = desc
        self.url = url
        self.keyw = keyw
        self.cover = cover
        self.genre = genre
        self.lang = lang
        self.pages = pages
        self.pubdate = pubdate
        self.formats = {}
        self.contributors = []

    def add_contributor(self, name, surname, role):
        contributor = Contributor(name, surname, role)
        assert contributor not in self.contributors
        assert role in roles
        self.contributors.append(contributor)

    def add_format(self, isbn, fmt):
        assert fmt not in self.formats
        self.formats[fmt] = isbn

    def add_publisher(self, name, shortname, url, logo, description):
        self.publisher = Publisher(name, shortname, url, logo, description)

    def to_json_ld(self):
        output = """{
        "@context": "http://schema.org",
        "@type": "Book",
        "name": "%s",
        "isbn": "%s",
        "url": "%s",
        "image": "%s",
        "genre": "%s",
        "keywords": "%s",
        "inLangugage": "%s",
        "publisher": {
            "@type": "Organization",
            "name": "%s",
            "alternateName": "%s",
            "url": "%s",
            "logo": "%s",
            "description": "%s"
        },""" % (self.title, self.isbn, self.url, self.cover, self.genre,
                 self.keyw, self.lang, self.publisher.name,
                 self.publisher.shortname, self.publisher.url,
                 self.publisher.logo, self.publisher.description)

        if self.pages:
            output += """
        "numberOfPages": %d,""" % (int(self.pages))

        if self.pubdate:
            output += """
        "datePublished": "%s",""" % (self.pubdate)

        if self.desc:
            output += """
        "description": "%s",""" % self.desc

        # remove last comma (purely cosmetic) and add the closing bracket
        output = output[:-1] + "\n}"
        return output

