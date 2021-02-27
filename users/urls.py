from django.urls import path, include

app_name = 'users'

urlpatterns = [
    # includes default auth urls
    path('', include('django.contrib.auth.urls')),
    # registration page
    path('register/', views.register, name='register'),
]
