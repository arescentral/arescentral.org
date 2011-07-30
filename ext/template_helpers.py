import dateutil.parser

from sphinx.jinja2glue import BuiltinTemplateLoader

def date_html(date_str):
    date_parser = dateutil.parser.parser()
    d = date_parser.parse(date_str)
    month = d.strftime('%B').upper()[:3]
    return (
        "<div class='article-date'>"
            "<span class='month-day'>"
                "<span class='month'>%s</span>"
                "<span class='day'>%s</span>"
            "</span>"
            "<span class='year'>%s</span>"
        "</div>" % (month, d.day, d.year)
    )

class TemplateBridge(BuiltinTemplateLoader):
    def init(self, *args, **kwargs):
        super(TemplateBridge, self).init(*args, **kwargs)
        self.environment.filters['date_html'] = date_html
