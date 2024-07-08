from django import forms
from .models import chaiVarity,Reviews,Store

class chaiVarityForm(forms.Form):
    chai_varity = forms.ModelChoiceField(queryset=chaiVarity.objects.all())
