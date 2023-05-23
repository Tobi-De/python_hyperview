from functools import partial

import requests
from django.db import models

NullBlankCharField = partial(models.CharField, blank=True, null=True, max_length=255)


class Contact(models.Model):
    first = NullBlankCharField()
    last = NullBlankCharField()
    phone = NullBlankCharField()
    email = models.EmailField()

    @classmethod
    def populate_db(cls):
        url = "https://raw.githubusercontent.com/bigskysoftware/contact-app/master/contacts.json"
        r = requests.get(url)
        for c in r.json():
            cls.objects.create(
                first=c["first"], last=c["last"], phone=c["phone"], email=c["email"]
            )
