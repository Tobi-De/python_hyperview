from functools import partial

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template.response import TemplateResponse
from render_block import render_block_to_string

from ..models import Contact

HXMLResponse = partial(TemplateResponse, content_type="application/vnd.hyperview+xml")


def index(request):
    search = request.GET.get("q")
    page_number = int(request.GET.get("page", 1))
    rows_only = request.GET.get("rows_only") == "true"
    if search:
        contacts = Contact.search(search)
    else:
        contacts = Contact.objects.order_by("email")

    paginator = Paginator(contacts, 15)
    page = paginator.get_page(page_number)

    template_name = "mobile/rows.xml" if rows_only else "mobile/index.xml"
    # return HXMLResponse(request, template_name, {"page": page})
    template_name = "mobile/index.xml"
    if rows_only:
        data = render_block_to_string(template_name, "rows", {"page": page})
        print(data)
        return HttpResponse(data, content_type="application/vnd.hyperview+xml")
    return HXMLResponse(request, template_name, {"page": page})
