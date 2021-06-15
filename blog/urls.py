from django.urls import path

from .views import ProfileView

app_name = 'blog'
urlpatterns = [
    path('', ProfileView.as_view(), name='index'),
]