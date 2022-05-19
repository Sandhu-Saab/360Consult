
from django.forms import ModelForm, forms


class ContectForm(ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    msg = forms.CharField()

    fields = '__all__'
