from django import forms
from .service import currency


class CurrencyForm(forms.Form):
    count = forms.FloatField(label="Количество")
    count_1 = forms.ChoiceField(choices=currency, label="Give")
    count_2 = forms.ChoiceField(choices=currency, label="Get")



