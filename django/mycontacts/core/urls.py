from django.urls import path, include

from .views import index

urlpatterns = [
    path("", index, name="home"),
    path("mobile/", include("core.mobile.urls")),
]
