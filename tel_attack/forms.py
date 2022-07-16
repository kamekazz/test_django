from django.db.models.base import Model
from django.forms import ModelForm
from .models import TelephoneNumber


class TelephoneForm(ModelForm):
    class Meta:
        model = TelephoneNumber
        fields = [
            'name',
            'target_number',
        ]

    def __init__(self, *args, **kwargs):
        super(TelephoneForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
