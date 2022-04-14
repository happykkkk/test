from django.forms import *

from .models import Journal


class Journal_Form(ModelForm):
    class Meta:
        model = Journal
        fields = ["grade", "date", "subject", "class_students"]

        widgets = {
            "grade": NumberInput(),
            "date": DateInput(),
            "subject": SelectMultiple(),
            "class_students": SelectMultiple()
        }
