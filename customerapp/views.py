from django.shortcuts import render
from .forms import ContactForm
from django.http.response import HttpResponse
def ContactForm_view(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse('valid form')
        else:
            return HttpResponse('Invalid form')
    else:
        form=ContactForm()
    return render(request,'contact.html',{"abc":form})
