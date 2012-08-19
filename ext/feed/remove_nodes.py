# By Gareth Rees
# http://gareth-rees.livejournal.com/27148.html

import html5lib
import html5lib.serializer
import html5lib.treewalkers
import urlparse

def remove_nodes(src, selector):
    """Remove HTML elements in `src` matching `selector`.

    Basic CSS selectors are supported: [element][.class].
    """
    selector = selector.split(".")
    name = selector[0] if selector[0] else "*"
    classes = frozenset(selector[1:])

    # Parse SRC as HTML.
    tree_builder = html5lib.treebuilders.getTreeBuilder('dom')
    parser = html5lib.html5parser.HTMLParser(tree = tree_builder)
    dom = parser.parse(src)

    # Remove non-matching nodes.
    for e in dom.getElementsByTagName(name):
        node_classes = e.getAttribute("class")
        if node_classes:
            node_classes = frozenset(node_classes.split(" "))
        else:
            node_classes = frozenset()

        if classes - node_classes:
            continue
        e.parentNode.removeChild(e)

    # Return the HTML5 serialization of the <BODY> of the result (we don't
    # want the <HEAD>: this breaks feed readers).
    body = dom.getElementsByTagName('body')[0]
    tree_walker = html5lib.treewalkers.getTreeWalker('dom')
    html_serializer = html5lib.serializer.htmlserializer.HTMLSerializer()
    return u''.join(html_serializer.serialize(tree_walker(body)))
