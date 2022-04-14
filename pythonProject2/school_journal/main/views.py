from django.shortcuts import render

from .models import Journal
from .forms import Journal_Form


def journal(request):

    school_journal = Journal.objects.all()
    return render(request, "main/Journal.html", {"school_journal": school_journal})


def journal_redection(request):
    if request.method == "POST":
        form = Journal_Form(request.POST)
        form.save()

    form = Journal_Form()

    return render(request, "main/redaction_journal.html", {"form": form})