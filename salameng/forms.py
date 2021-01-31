from django.forms import ModelForm
from .models import ClientQuery


class ClientQueryForm(ModelForm):
    class Meta:
        model = ClientQuery
        fields = '__all__'
