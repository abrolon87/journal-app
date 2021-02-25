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


def topic(request, topic_id):
    # like show in rails
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'journal_entries/topic.html', context)
