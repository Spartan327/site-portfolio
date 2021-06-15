from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Profile

class ProfileView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=User.objects.get(username='id54678191'))
        return context
