"""
Reva Agarwal
Sp24 Adv Data Struct/Algorithm Python
parse through HTML code and convert lists into Python lists
"""
from html.parser import HTMLParser


class ListCollector(HTMLParser):
    """
    subclass of HTMLParser from the html.parser library
    """
    def __init__(self):
        """
        initialize lists to store values in
        """
        super().__init__()
        self.lists = []
        self.inner_list = None
        self.list_exists = False

    def handle_starttag(self, tag, attrs):
        """
        creates a list when start tags 'ol' and 'ul' are detected
        :param tag: string value of tag detected
        :param attrs: attribute of tag
        :return: None
        """
        if tag == "ol" or tag == "ul":
            self.inner_list = []
        elif tag == "li":
            self.list_exists = True

    def handle_data(self, data):
        """
        if start tag and 'li' tag were detected then data is added to list
        :param data: text inside list
        :return: None
        """
        if self.list_exists and self.inner_list is not None:
            self.inner_list.append(data.strip())

    def handle_endtag(self, tag):
        """
        adds list to a collection of all lists of the HTML file if
        end tags 'ol' or 'ul' are detected
        :param tag: end tag
        :return: None
        """
        if (tag == "ol" or tag == "ul") and self.inner_list is not None:
            self.lists.append(self.inner_list)
            self.inner_list = None
        elif tag == "li":
            self.list_exists = False

    def getLists(self):
        """
        :return: list with all ordered and unordered lists from the HTML doc
        """
        return self.lists
