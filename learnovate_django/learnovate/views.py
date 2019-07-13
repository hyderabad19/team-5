from django.shortcuts import render
from .models import Resource

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
