from django.template.response import TemplateResponse


def index(request):
    # Contact.populate_db()
    return TemplateResponse(request, "index.html", {})
