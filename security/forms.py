from django import forms
from collar.models import Staff
from collar.models import OrderContactPerson

COLLARCHOICE = (
    ('Survey', 'Survey'),
    ('VertexLite', 'VertexLite'),
    ('VertexPlus', 'VertexPlus'),
)


class LinkCreateForm(forms.Form):
    staff = forms.ModelChoiceField(queryset=Staff.objects.all())
    contact_person = forms.ModelChoiceField(queryset=OrderContactPerson.objects.all())
    customerEmail = forms.EmailField()
    collarType = forms.ChoiceField(choices=COLLARCHOICE)


class MyLoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())