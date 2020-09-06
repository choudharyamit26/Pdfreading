from django import forms
from .models import DailyRenewableGenerationReport


class ImportDataForm(forms.ModelForm):
    class Meta:
        model = DailyRenewableGenerationReport
        fields = '__all__'
