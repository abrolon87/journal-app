from django.shortcuts import render
from .models import Topic

# Create your views here.


def index(request):
    # home page
    return render(request, 'journal_entries/index.html')


def topics(request):
    # all topics
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'journal_entries/topics.html', context)
