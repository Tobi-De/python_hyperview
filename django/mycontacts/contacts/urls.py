from django.urls import path, include

from .views import (
    index,
    archive,
    archive_content,
    reset_archive,
    contacts_count,
    new_contact,
    details,
    edit,
    validate_email,
    delete,
    delete_all,
)

app_name = "contacts"

urlpatterns = [
    path("", index, name="index"),
    path("archive/", archive, name="archive"),
    path("new/", new_contact, name="new"),
    path("archive/content/", archive_content, name="archive_content"),
    path("archive/reset/", reset_archive, name="reset_archive"),
    path("count/", contacts_count, name="count"),
    path("delete-all/", delete_all, name="delete_all"),
    path("mobile/", include("contacts.mobile.urls", namespace="mobile")),
    path("<int:pk>/", details, name="details"),
    path("<int:pk>/edit/", edit, name="edit"),
    path("<int:pk>/delete/", delete, name="delete"),
    path("<int:pk>/validate_email/", validate_email, name="validate_email"),
]
