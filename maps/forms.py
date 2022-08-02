from django.forms import ModelForm
from maps.models import University

# Create the form class.
class UniversityForm(ModelForm):
    class Meta:
        model = University
        fields = ["name", "subject"]
