from django.shortcuts import render
from .models import Resource
from .forms import TeacherSignUpForm
from django.contrib.auth import login
from .models import User
from django.views.generic import CreateView, ListView, UpdateView
from django.shortcuts import get_object_or_404, redirect, render

def viewVideo(request):
    v=Resource.objects.all()
    f=v[0]
    context= {'name' : "test name",
              'file': f,
              'description': "test desription",
              'comment': "test comment",
              }
    
      
    return render(request, 'templates/view_video.html', context)

def viewAllVideos(request):
    f=Resource.objects.all()
    context= {'file': f,
              }
    

    return render(request, 'templates/view_all.html', context)


def homeView(request):
    videos = Resource.objects.all()
    return render(request, 'home.html', {'videos': videos})


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('')