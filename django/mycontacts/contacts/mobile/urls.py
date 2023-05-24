from django.urls import path

from .views import index

app_name = "mobile"
urlpatterns = [path("", index, name="index")]
