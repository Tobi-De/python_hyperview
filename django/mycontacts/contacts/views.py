from django.contrib import messages
from django.http import FileResponse
from django.http import QueryDict
from django.shortcuts import redirect, get_object_or_404
from django.template.response import TemplateResponse, HttpResponse
from django.views.decorators.http import require_http_methods

from .forms import ContactForm
from .models import Contact
from .utils import Archiver


def index(request):
    # Contact.populate_db()
    search = request.GET.get("q")
    if search is not None and request.headers.get("HX-Trigger") == "search":
        return TemplateResponse(
            request, "rows.html", {"contacts": Contact.search(search)}
        )
    return TemplateResponse(
        request,
        "index.html",
        {"contacts": Contact.objects.all(), "archiver": Archiver.get()},
    )


def archive(request):
    archiver = Archiver.get()
    if request.method == "POST":
        archiver.run()
    return TemplateResponse(request, "archive_ui.html", {"archiver": archiver})


def archive_content(request):
    archiver = Archiver.get()

    response = FileResponse(archiver.archive_content(), content_type="application/json")
    response["Content-Disposition"] = 'attachment; filename="archive.json"'
    return response


@require_http_methods(["DELETE"])
def reset_archive(request):
    archiver = Archiver.get()
    archiver.reset()
    return TemplateResponse(request, "archive_ui.html", {"archiver": archiver})


def contacts_count(request):
    count = Contact.objects.count()
    return HttpResponse(f"({str(count)} total Contacts)")


def new_contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        messages.success(request, "Created New Contact!")
        form.save()
        return redirect("contacts:index")
    return TemplateResponse(request, "new.html", {"form": form})


def details(request, pk):
    contact = Contact.objects.get(pk=pk)
    return TemplateResponse(request, "details.html", {"contact": contact})


def edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=contact)
    if request.method == "POST" and form.is_valid():
        messages.success(request, "Updated Contact!")
        form.save()
        return redirect("contacts:details", pk=pk)
    return TemplateResponse(request, "edit.html", {"form": form, "contact": contact})


def validate_email(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.GET or None, instance=contact)
    if form.is_valid():
        return HttpResponse("")
    return HttpResponse(form.errors["email"][0])


@require_http_methods(["DELETE"])
def delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    if request.headers.get("HX-Trigger") == "delete-btn":
        messages.info(request, "Deleted Contact!")
        return redirect("contacts:index")
    return HttpResponse("")


@require_http_methods(["DELETE"])
def delete_all(request):
    params = QueryDict(request.body)
    contact_ids = list(map(int, params.getlist("selected_contact_ids")))
    Contact.objects.filter(pk__in=contact_ids).delete()
    messages.info(request, "Deleted Contacts!")
    return redirect("contacts:index")
