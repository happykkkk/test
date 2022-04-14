from django.urls import path

from . import views

urlpatterns = [
    path("", views.journal, name="journal"),
    path("add-journal/", views.journal_redection, name="journal_add")
]
