from django.forms import ModelForm
from maps.models import University
from django.forms import ValidationError

# Create the form class.
class UniversityForm(ModelForm):
    class Meta:
        model = University
        fields = ["name", "subject"]

    def clean_subject(self):
        subj = self.cleaned_data.get("subject")
        if len(subj) < 2:
            raise ValidationError("Choose at least 2 subjects for a university.")
        return subj
