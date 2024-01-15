from django.urls import path
from . import views

app_name="app"
urlpatterns = [
    path("", views.gadget, name="home"),
    path("before/", views.g_before, name="before"),
    path("after/", views.g_after, name="after"),
]
