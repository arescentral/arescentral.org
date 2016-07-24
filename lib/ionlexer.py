import logging
import pygments.lexers
from pygments.lexer import RegexLexer, include, bygroups
from pygments.token import Error, Keyword, Name, Number, Punctuation, String, Text

logger = logging.getLogger(__name__)

class IonLexer(RegexLexer):
    name = "ion"
    aliases = ["ion"]
    filenames = ["*.ion"]
    mimetypes = ["text/x-ion"]
    tabsize = 0

    tokens = {
        "root": [
            include("line"),
        ],

        "line": [
            ("^(  )*", Text, "content"),
            ("\n", Text),
        ],

        "content": [
            include("extended-value"),
            include("compact-value"),
            (".+", Error, "#pop"),
        ],

        "extended-value": [
            ("(-)( )", bygroups(Punctuation, Text)),
            ("-", Punctuation, "#pop"),
            ("([>|])( )(.*)", bygroups(Punctuation, Text, String.Other), "#pop"),
            ("[>|!]", Punctuation, "#pop"),
            ("([\w./-]+)(:)( +)", bygroups(Name.Tag, Punctuation, Text)),
            ("([\w./-]+)(:)", bygroups(Name.Tag, Punctuation), "#pop"),
        ],

        "compact-value": [
            include("simple-value"),
            ("\{", Punctuation, "mapping-key"),
            ("\[", Punctuation, "sequence-value"),
        ],

        "mapping-key": [
            include("whitespace"),
            ("([\w./-]+)(:)( *)", bygroups(Name.Tag, Punctuation, Text), "mapping-value"),
            ("\}", Punctuation, "#pop"),
        ],

        "mapping-value": [
            include("whitespace"),
            include("compact-value"),
            (",", Punctuation, "#pop"),
            ("\}", Punctuation, "#pop:2"),
        ],

        "sequence-value": [
            include("whitespace"),
            include("compact-value"),
            (",", Punctuation),
            ("\]", Punctuation, "#pop"),
        ],

        "simple-value": [
            (r"(true|false|null|inf|-inf|nan)\b", Keyword.Constant),
            (r"-?(0|[1-9]\d*)\.\d+", Number.Float),
            (r"-?(0|[1-9]\d*)", Number.Integer),
            (r'"([^"\\]|\\.)*"', String.Double),
        ],

        "whitespace": [
            (r"\s+", Text),
        ],
    }

def register():
    pygments.lexers.LEXERS["IonLexer"] = (
        "ionlexer",
        IonLexer.name,
        tuple(IonLexer.aliases),
        tuple(IonLexer.filenames),
        tuple(IonLexer.mimetypes),
    )


__all__ = ["IonLexer"]
