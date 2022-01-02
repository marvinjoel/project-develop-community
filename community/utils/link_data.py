import requests
from lxml import html


class LinkData():

    def __init__(self, url_group):
        self.url_group = url_group
        self._html_response = self._html_from_url()


    def get_data(self):
        data = {
            'name': self._get_name(),
            'description': self._get_description(),
            'image': self._get_image(),
        }

        return data


    def _html_from_url(self):
        headers = {
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40',
        }
        raw_response = requests.get(self.url_group, headers=headers)

        return html.fromstring(raw_response.text)


    def _get_name(self):
        try:
            name = self._html_response.xpath('//meta[@property="og:title"]/@content')[0]
            if not name:
                print('title name')
                name = self._html_response.xpath('//title/text()')

            return name
        except:
            name = ""
            return name


    def _get_description(self):
        try:
            description = self._html_response.xpath('//meta[@property="og:description"]/@content')
            if not description:
                description = self._html_response.xpath(
                    '(//body/div[contains(@class, "container")]//p/text())[0]')
                if not description:
                    description = self._html_response.xpath(
                        '//div[contains(@class, "container")]//p/text()')
            else:
                description = description[0]

            return description
        except:
            description = ""
            return description


    def _get_image(self):
        try:
            image = self._html_response.xpath('//meta[@property="og:image"]/@content')[0]
            if not image:
                image = self._html_response.xpath(
                    '//img/@src')

            return image
        except:
            image = ""
            return image
