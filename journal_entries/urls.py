from django.urls import path

from . import views

app_name = 'journal_entries'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # topics page
    path('topics/', views.topics, name='topics')
]
