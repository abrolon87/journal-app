from django.urls import path

from . import views

app_name = 'journal_entries'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # topics page
    path('topics/', views.topics, name='topics'),
    # individual topic page
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # new topic page
    path('new_topic/', views.new_topic, name='new_topic'),
]
