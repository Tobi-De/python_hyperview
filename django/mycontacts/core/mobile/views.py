from functools import partial

from django.template.response import TemplateResponse

HXMLResponse = partial(TemplateResponse, content_type="application/vnd.hyperview+xml")


def index(request):
    return HXMLResponse(request, "mobile/index.xml", {})
