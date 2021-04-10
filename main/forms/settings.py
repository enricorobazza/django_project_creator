from django import forms
from main.models import Settings

class SettingsForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Settings

    def __init__(self, *args, **kwargs):
        super(SettingsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    