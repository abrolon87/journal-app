from django.shortcuts import render

# Create your views here.


def index(request):
    # home page
    return render(request, 'journal_entries/index.html')
