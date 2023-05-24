from functools import partial

import requests
from django.db import models

NullBlankCharField = partial(models.CharField, blank=True, null=True, max_length=255)


class Contact(models.Model):
    first_name = NullBlankCharField()
    last_name = NullBlankCharField()
    phone = NullBlankCharField()
    email = models.EmailField(unique=True)

    @classmethod
    def populate_db(cls):
        url = "https://raw.githubusercontent.com/bigskysoftware/contact-app/master/contacts.json"
        r = requests.get(url)
        for c in r.json():
            cls.objects.get_or_create(
                first_name=c["first"],
                last_name=c["last"],
                phone=c["phone"],
                email=c["email"],
            )

    @classmethod
    def search(cls, text):
        return cls.objects.filter(
            models.Q(first_name__icontains=text)
            | models.Q(last_name__icontains=text)
            | models.Q(phone__icontains=text)
            | models.Q(email__icontains=text)
        )
