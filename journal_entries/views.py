from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm

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


def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            return redirect('journal_entries:topics')

    context = {'form': form}
    return render(request, 'journal_entries/new_topic.html', context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('journal_entries:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'journal_entries/new_entry.html', context)
