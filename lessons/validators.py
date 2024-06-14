import re
from rest_framework.serializers import ValidationError


class LinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = dict(value).get(self.field)
        if val is None:
            return

        banned_links = r'https?://\S+|www\.\S+'
        correct_link = r'(?:https?://)?(?:www\.)?youtube\.com'

        links = re.findall(banned_links, val)

        for link in links:
            if not bool(re.match(correct_link, link)):
                raise ValidationError(f'ссылка на сторонние образовательные платформы или личные сайты {link}')