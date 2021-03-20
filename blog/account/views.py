from django.shortcuts import render
from .forms import SignupForm
from django.contrib import messages
# Create your views here.


def signup(request):
    if request.method == 'POST':
        fr = SignupForm(request.POST, request.FILES)
        if fr.is_valid():
            messages.success(request, 'Account created successfullly ')
            fr.save()
    else:
        fr = SignupForm()
    return render(request, 'blogreg.html', {'form': fr})
