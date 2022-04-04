from django.shortcuts import render

from .models import Journal


def journal(request):

    school_journal = Journal.objects.all()
    return render(request, "main/Journal.html", {"school_journal": school_journal})