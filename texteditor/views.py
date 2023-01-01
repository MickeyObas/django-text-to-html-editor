from django.shortcuts import render
from .forms import EditorForm

def index(request):
    form = EditorForm()
    return render(request, 'index.html', {"form": form})


