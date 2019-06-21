from lxml import etree

class XpathSelector(object):

    def __init__(self, raw_text=None):
        self.html = None
        self._text = raw_text

    def get(self):
        try:
            result = self.html.xpath(self.syntax)[0]
            if isinstance(result, etree._Element):
                result = etree.tostring(result, encoding='utf-8').decode('utf-8')
            return result
        except IndexError:
            return None

    def getall(self):
        return self.html.xpath(self.syntax)

    def __call__(self, syntax):
        self.syntax = syntax
        if self.html is None:
            self.html = etree.HTML(self._text)
        return self