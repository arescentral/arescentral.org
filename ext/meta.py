import html5lib
import re
import time

def setup(app):
    app.connect('html-page-context', add_byline)

def add_byline(app, docname, templatename, ctx, doctree):
    date = None
    author = None
    author_email = None
    if "meta" in ctx:
        meta = ctx["meta"]
        if "author" in meta:
            author = meta["author"]
            m = re.match("\s*(.*\S)\s*<(.+)>\s*", author)
            if m:
                author = m.group(1)
                author_email = m.group(2)
        if "date" in meta:
            date = time.strptime(meta["date"], "%Y-%m-%d")
            date = date_string(date)
    if not (date or author):
        return

    tree_builder = html5lib.treebuilders.getTreeBuilder("dom")
    parser = html5lib.html5parser.HTMLParser(tree = tree_builder)
    dom = parser.parse(ctx["body"])

    h1 = dom.getElementsByTagName("h1")[0]
    div = dom.createElement("div")
    div.setAttribute("class", "meta")
    h1.parentNode.insertBefore(div, h1.nextSibling)

    if author:
        span = dom.createElement("span")
        span.setAttribute("class", "author")
        span.appendChild(dom.createTextNode("By: "))
        if author_email:
            a = dom.createElement("a")
            a.setAttribute("href", "mailto:%s" % author_email)
            a.appendChild(dom.createTextNode(author))
            span.appendChild(a)
        else:
            span.appendChild(dom.createTextNode(author))
        div.appendChild(span)

    if date:
        span = dom.createElement("span")
        span.setAttribute("class", "date")
        span.appendChild(dom.createTextNode("On: %s" % date))
        div.appendChild(span)

    body = dom.getElementsByTagName("body")[0]
    tree_walker = html5lib.treewalkers.getTreeWalker("dom")
    html_serializer = html5lib.serializer.htmlserializer.HTMLSerializer()
    ctx["body"] = u"".join(html_serializer.serialize(tree_walker(body)))

def date_string(t):
    year = time.strftime("%Y", t)
    month = time.strftime("%B", t)
    day = time.strftime("%e", t)
    if day in [" 1", "21", "31"]:
        return "%s %sst, %s" % (month, day, year)
    elif day in [" 2", "22"]:
        return "%s %snd, %s" % (month, day, year)
    elif day in [" 3", "23"]:
        return "%s %srd, %s" % (month, day, year)
    else:
        return "%s %sth, %s" % (month, day, year)
