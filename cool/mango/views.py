from django.shortcuts import render
from django.views import View

from .service import *
from .forms import *


class ApiView(View):
    def get(self, request):
        context = {
            'title': 'Currency rate',
            'form': CurrencyForm(),
        }

        return render(request, 'mango/index.html', context)

    def post(self, request):
        form = CurrencyForm(request.POST)
        context = {
            'title': 'Currency rate',
            'form': form,
        }
        if form.is_valid():
            t1 = Translate()
            t1.translate(cleaned_data=form.cleaned_data, context=context)

        return render(request, 'mango/index.html', context)
